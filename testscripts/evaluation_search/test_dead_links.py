import json
import pygsheets
from google.oauth2 import service_account
from models.pagelocators.evaluation_search.cc_search import CCSearchPageLocators
from utils_automation.common import FilesHandle
import requests

file_handle = FilesHandle()
headers = {
<<<<<<< HEAD
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

=======
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
>>>>>>> 1f07c44bd3ee761b51ca8c1b56ea8709a93d6691

def google_authorize():
    credentials_path_file = file_handle.get_absolute_filename("\\qa-auto_service_credentials.json")
    credentials_path_file = credentials_path_file.replace('\\utils_automation', '\\resources')
    SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file')
    with open(credentials_path_file, 'r') as j:
        service_account_info = json.loads(j.read())
    my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    authorize = pygsheets.authorize(custom_credentials=my_credentials)
    return authorize


def get_worksheet(spreed_sheet_id, sheet_name):
    sheet = google_authorize().open_by_key(spreed_sheet_id)
    worksheet = sheet.worksheet('title', sheet_name)
    return worksheet


def split_index_from_sheet_range(sheet_range):
    index_list = sheet_range.split(":")
    if index_list is None:
        raise Exception
    index_list_int = []
    for index in index_list:
        index_list_int.append(int(index[1:5]))
        index_list_int_without_duplicate = list(dict.fromkeys(index_list_int))
    return index_list_int_without_duplicate


def split_col_from_sheet_range(sheet_range):
    col_list = sheet_range.split(":")
    if col_list is None:
        raise Exception
    for col in col_list:
        col_without_duplicate = list(dict.fromkeys(col[0:1]))
    return col_without_duplicate


def create_content_to_update_into_spreadsheet(links_list, title):
    if len(links_list) == 0:
        links_results = ""
    else:
        links_results = "*** " + title + ": \n"
        for link in links_list:
            links_results += link + "\n"
    return links_results


def write_result_into_spreadsheet(sheet_range, worksheet, keyword, result_col, dead_links, invalid_links, prefix):
    dead_links_result = create_content_to_update_into_spreadsheet(dead_links,
                                                                  prefix + " Dead links (" + str(len(dead_links)) + ")")
    invalid_links_result = create_content_to_update_into_spreadsheet(invalid_links,
                                                                     prefix + " Others Invalid Links (" + str(
                                                                         len(invalid_links)) + ")")
    content = dead_links_result + invalid_links_result
    list_index = split_index_from_sheet_range(sheet_range)
    col = split_col_from_sheet_range(sheet_range)
    for i in list_index:
        for j in col:
            cell = j + str(i)
            cell_actual_keyword = worksheet.get_value(cell)
            if str(cell_actual_keyword) in str(keyword):
                result_cell = result_col + str(i)
                worksheet.update_value(result_cell, content)


def get_keyword_without_bracket(keyword):
    start = keyword.find("['") + len("['")
    end = keyword.find("']")
    keyword_without_bracket = keyword[start:end]
    return keyword_without_bracket


def prepare_query(url, keyword):
    import urllib.parse
    keyword_encode_uri = urllib.parse.quote(keyword)
    query = url + keyword_encode_uri
    return query

<<<<<<< HEAD

=======
>>>>>>> 1f07c44bd3ee761b51ca8c1b56ea8709a93d6691
def get_search_results_for_google(query_url):
    request = request_url(query_url)
    from lxml import html
    web_page = html.fromstring(request.content)
    search_results = web_page.xpath(CCSearchPageLocators.GOOGLE_SEARCH_RESULTS_XPATH)
    print("\t" + str(search_results))
    return search_results


def get_search_results_for_coccoc(query_url):
    # request to query_url
    request = request_url(query_url)

    # get data in <Script> tag contain search results
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(request.content, 'html.parser')
    script = soup.find('script')
    label = str(script).replace('<script type="text/javascript">window.composerResponse = ', "")
    label = label.replace(';</script>', "")
    import json
    json_contain_search_results = json.loads(label)
    import re

    # get address in <Script> tag and store into list
    search_result_list = []
    for sub_json in json_contain_search_results['search']['search_results']:
        if 'content' in sub_json:
            addresses = re.findall(r"(?<='url': ').+?(?=')", str(sub_json))
            for address in addresses:
                # print('\t Link content: ' + str(address))
                search_result_list.append(str(address))
        else:
            addresses_page_url = re.findall(r"(?<='page_url': ').+?(?=', 'preview_height)", str(sub_json))
            addresses_url = re.findall(r"(?<='url': ').+?(?=')", str(sub_json))
            for address_page_url in addresses_page_url:
                # print('\t Link page_url: ' + str(address_page_url))
                search_result_list.append(str(address_page_url))
            for address_url in addresses_url:
                # print('\t Link url: ' + str(address_url))
                search_result_list.append(str(address_url))
    search_results_without_duplicate = list(dict.fromkeys(search_result_list))
    print("\t" + str(search_results_without_duplicate))
    return search_results_without_duplicate


def request_url(query_url):
    request = requests.get(url=query_url, headers=headers)
    return request

<<<<<<< HEAD

=======
>>>>>>> 1f07c44bd3ee761b51ca8c1b56ea8709a93d6691
def get_dead_links(address):
    try:
        r = requests.get(address, timeout=45, headers=headers)
        if r.status_code > 400:
            return True, r.status_code
        else:
            return False, r.status_code
    except requests.exceptions.RequestException as e:
        return True, e


def verify_text_in_html(address, string):
    request = request_url(address)
    html_page_source = request.text
    if string in html_page_source:
        return True
    else:
        return False


def evaluation_search(url, keyword, string_verify):
    # Create query url
    query_url = prepare_query(url=url, keyword=keyword)
    print("\n- Query:\n" + query_url)

    # Get all search results and store into list
    if 'coccoc.com/search' in url:
        addresses = get_search_results_for_coccoc(query_url=query_url)
    else:
        addresses = get_search_results_for_google(query_url=query_url)
    # Check dead links/ invalid links
    dead_links = []
    invalid_links = []
    for address in addresses:
        # Check dead links
        status, code = get_dead_links(address)
        if status:
            dead_links.append(address + "\n[Error]:" + str(code) + "\n")
        # Check html of link contains some strings
        else:
            for string in string_verify:
                string_is_exist = verify_text_in_html(address, string)
                if string_is_exist:
                    invalid_links.append(address + "\n[Reason]:" + string + "\n")
    return dead_links, invalid_links


class TestDeadLinks:

    def test_search_by_keyword(self, spreed_sheet_id, sheet_name, sheet_range, string_verify, result_col):
        result_col_cc, result_col_gg = result_col
        # Get all keywords in "Queries" column => Store to list
        worksheet = get_worksheet(spreed_sheet_id, sheet_name)
        list_keywords = worksheet.range(sheet_range, returnas='matrix')
        for keyword in list_keywords:
            keyword = get_keyword_without_bracket(str(keyword))
            dead_links_cc, invalid_links_cc = evaluation_search(url='https://coccoc.com/search?query=', keyword=keyword,
                                                                string_verify=string_verify)

            write_result_into_spreadsheet(sheet_range, worksheet, keyword, result_col_cc, dead_links_cc,
                                          invalid_links_cc,
                                          prefix="Coc Coc")

            dead_links_gg, invalid_links_gg = evaluation_search(url='https://www.google.com.vn/search?q=',
                                                                keyword=keyword, string_verify=string_verify)
            # Write result to google spread sheet
            write_result_into_spreadsheet(sheet_range, worksheet, keyword, result_col_gg, dead_links_gg,
                                          invalid_links_gg,
                                          prefix="Google")

        #Send skype notify
        from testscripts.jobs.noti_test_result_change import send_message_skype
        send_message_skype("(porg)(porg)(porg) Evaluation Search - Finished get broken links (porg)(porg)(porg)"
                           "\nPlease check result for Coc Coc in col [" + result_col_cc + "]/ Google in col ["
                           + result_col_gg + "] of sheet [" + sheet_name
                           + "] in bellow link:\nhttps://docs.google.com/spreadsheets/d/" + spreed_sheet_id)
