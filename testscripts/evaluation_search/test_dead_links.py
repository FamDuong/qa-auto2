from __future__ import print_function
from datetime import datetime
import json
import time
import pygsheets
from google.oauth2 import service_account
from utils_automation.common import FilesHandle
from models.pagelocators.evaluation_search.cc_search import CCSearchPageLocators
from testscripts.smoketest.common import coccoc_instance

file_handle = FilesHandle()


class TestDeadLinks:

    def google_authorize(self):
        credentials_path_file = file_handle.get_absolute_filename("\\qa-auto_service_credentials.json")
        credentials_path_file = credentials_path_file.replace('\\utils_automation', '\\resources')
        SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file')
        with open(credentials_path_file, 'r') as j:
            service_account_info = json.loads(j.read())
        my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
        google_authorize = pygsheets.authorize(custom_credentials=my_credentials)
        return google_authorize

    def get_worksheet(self, spreed_sheet_id, sheet_name):
        google_authorize = self.google_authorize()
        sheet = google_authorize.open_by_key(spreed_sheet_id)
        worksheet = sheet.worksheet('title', sheet_name)
        return worksheet

    def search_by_keyword_and_get_link_list_in_first_page(self, keyword):
        driver = coccoc_instance()
        from utils_automation.const import Urls
        driver.get(Urls.CC_SEARCH_URL)
        driver.find_element_by_xpath(CCSearchPageLocators.SEARCH_TXT_XPATH).send_keys(keyword)
        driver.find_element_by_xpath(CCSearchPageLocators.SEARCH_BTN_XPATH).click()
        links_xpath = driver.find_elements_by_xpath(CCSearchPageLocators.SEARCH_RESULT_LINK_XPATH)
        start_time = datetime.now()
        while len(links_xpath) == 0:
            time.sleep(2)
            links_xpath = driver.find_elements_by_xpath(CCSearchPageLocators.SEARCH_RESULT_LINK_XPATH)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 15:
                break
        search_results = []
        for link_xpath in links_xpath:
            address = link_xpath.get_attribute("href")
            if address.startswith('http'):
                search_results.append(address)
                search_results_without_duplicate = list(dict.fromkeys(search_results))
        return search_results_without_duplicate

    def get_dead_links(self, address):
        import requests
        r = requests.head(address)
        if r.status_code > 400:
            return True
        else:
            return False

    def verify_text_in_body_text(self, driver, address, string):
        driver.get(address)
        html_page_source = driver.page_source
        if string in html_page_source:
            return True
        else:
            return False

    def split_index_from_sheet_range(self, sheet_range):
        index_list = sheet_range.split(":")
        if index_list is None:
            raise Exception
        index_list_int = []
        for index in index_list:
            index_list_int.append(int(index[1:5]))
            index_list_int_without_duplicate = list(dict.fromkeys(index_list_int))
        return index_list_int_without_duplicate

    def split_col_from_sheet_range(self, sheet_range):
        col_list = sheet_range.split(":")
        if col_list is None:
            raise Exception
        for col in col_list:
            col_without_duplicate = list(dict.fromkeys(col[0:1]))
        return col_without_duplicate

    def write_result_into_spreadsheet(self, sheet_range, worksheet, keyword, result_col, content):
        list_index = self.split_index_from_sheet_range(sheet_range)
        col = self.split_col_from_sheet_range(sheet_range)
        for i in list_index:
            for j in col:
                cell = j + str(i)
                cell_actual_keyword = worksheet.get_value(cell)
                if str(cell_actual_keyword) in str(keyword):
                    result_cell = result_col + str(i)
                    worksheet.update_value(result_cell, content)

    def test_search_by_keyword(self, spreed_sheet_id, sheet_name, sheet_range, string_verify, result_col):
        # Get all keywords in "Queries" column => Store to list
        worksheet = self.get_worksheet(spreed_sheet_id, sheet_name)
        list_keywords = worksheet.range(sheet_range, 'matrix')

        for keyword in list_keywords:
            # Get all addresses that returned by coccoc.com/search
            addresses = self.search_by_keyword_and_get_link_list_in_first_page(keyword)
            print("Search by Keyword: " + str(keyword))

            # Check dead link and others invalid links
            dead_links = []
            invalid_links = []
            for address in addresses:
                if self.get_dead_links(address):
                    dead_links.append(address)
                driver = coccoc_instance()
                for string in string_verify:
                    if self.verify_text_in_body_text(driver, address, string):
                        invalid_links.append(address)

            # Write dead link and others invalid links to google spreadsheet
            if dead_links is None:
                dead_links_results = ""
            else:
                dead_links_results = "* Dead link: \n "
                for link in dead_links:
                    link = " -"+link+"\n"
            if invalid_links is None:
                invalid_links_results = ""
            else:
                invalid_links_results = "\n\n* Others Invalid Links: \n"
                for link in invalid_links:
                    link = " -"+link+"\n"

            content = dead_links_results + invalid_links_results
            self.write_result_into_spreadsheet(sheet_range, worksheet, keyword, result_col, content)
