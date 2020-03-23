import time
import pytest
from pytest_testrail.plugin import pytestrail
from selenium import webdriver
from models.pagelocators.extensions import MojiChatLocators
from models.pageobject.mojichat import MojichatObjects
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import Browser
from utils_automation.common import CSVHandle
from utils_automation.const import Urls
from testscripts.smoketest.common import coccoc_instance, chrome_options_preset
from models.pageelements.version import VersionPageElements
from models.pagelocators.flags import FlagsPageLocators

browser = Browser()
user_chat = "Coc Coc"
mojichat_file = "mojichat_list.csv"


# @pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelBigBoxChat:
    mojichat_object = MojichatObjects()
    version_page_element = VersionPageElements()




#Enabled
    def test_change_moji_flag_status(self, status = "Enabled"):
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_FLAGS)
        driver.find_element_by_id(FlagsPageLocators.SEARCH_FLAG_TXT_ID).send_keys('MojiChat Extension')
        from selenium.webdriver.support.select import Select
        status_ddl = Select(driver.find_element_by_xpath(FlagsPageLocators.STATUS_DDL_XPATH))
        if status_ddl.first_selected_option.text not in status:
            status_ddl.select_by_visible_text(status)
            time.sleep(2)
            driver.find_element_by_id(FlagsPageLocators.RELAUNCH_BTN_ID).click()
            time.sleep(3)
            #cleanup()
        import subprocess
        # subprocess.Popen(
        #     r'C:\Users\hangnt2\AppData\Local\CocCoc\Browser\Application\browser.exe --enable-features=CocCocMojichat '
        #     r'--flag-switches-end --synchronization-type --enable-audio-service-sandbox"' + Urls.COCCOC_EXTENSIONS,
        #      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.Popen([
            r'C:\Users\hangnt2\AppData\Local\CocCoc\Browser\Application\browser.exe --enable-features=CocCocMojichat '
            r'--flag-switches-end --synchronization-type --enable-audio-service-sandbox"/new-tab', Urls.COCCOC_EXTENSIONS],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE, shell=True)
        #driver.get(Urls.COCCOC_FLAGS)
        time.sleep(10)
        driver.get(Urls.COCCOC_EXTENSIONS)


    def verify_show_moji_icon(self, action, moji_is_on):
        driver = webdriver.Chrome(options=chrome_options_preset())
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_extension(driver, action)
        self.mojichat_object.login_facebook(driver)
        self.mojichat_object.verify_moji_icon_in_small_chat(driver, moji_is_on)
        self.mojichat_object.verify_moji_icon_in_message_dot_com(driver, moji_is_on)
        self.mojichat_object.verify_moji_icon_in_facebook_message_dot_com(driver, moji_is_on)

    @pytestrail.case('C54439')
    def test_check_status_change_when_user_turn_on_off_moji_feature(self):
        self.change_moji_flag_status()
        self.verify_show_moji_icon(action='ON', moji_is_on=True)
        self.verify_show_moji_icon(action='OFF', moji_is_on=False)

    @pytestrail.case('C147187')
    def test_check_set_mojichat_is_off_at_developer_mode(self):
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_in_detail_extension_page(driver)
        self.mojichat_object.login_facebook(driver)
        self.mojichat_object.verify_moji_icon_in_small_chat(driver, moji_is_on=False)
        self.mojichat_object.verify_moji_icon_in_message_dot_com(driver, moji_is_on=False)
        self.mojichat_object.verify_moji_icon_in_facebook_message_dot_com(driver, moji_is_on=False)


    @pytestrail.case('C54462')
    def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
        self.mojichat_object.open_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.send_text_into_chat(browser, "clear cache")

        list_mojichat = CSVHandle().get_from_csv(mojichat_file)
        for i in list_mojichat:
            self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)
            self.mojichat_object.verify_chat_is_empty(browser)

    @pytestrail.case('C86095')
    def test_check_if_user_can_using_arrow_key_to_navigate_suggestion_stickers(self, browser):
        self.mojichat_object.open_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.select_moji_on_suggestion_panel_by_arrow_key(browser, "hihi")
        time.sleep(10)


@pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelSmallChat:
    mojichat_object = MojichatObjects(MojichatLocators.SMALL_CHAT)

    @pytestrail.case('C54462')
    def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
        self.mojichat_object.open_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.send_text_into_chat(browser, "clear cache")

        list_mojichat = CSVHandle().get_from_csv(mojichat_file)
        for i in list_mojichat:
            self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)
            self.mojichat_object.verify_chat_is_empty(browser)
