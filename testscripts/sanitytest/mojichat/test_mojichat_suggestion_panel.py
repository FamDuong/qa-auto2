from pytest_testrail.plugin import pytestrail
from selenium import webdriver

from models.pageelements.mojichat import ChatElement
from models.pageobject.mojichat import MojichatObjects

from utils_automation.setup import Browser
from utils_automation.const import Urls
from testscripts.smoketest.common import coccoc_instance, chrome_options_preset
from models.pageelements.version import VersionPageElements

browser = Browser()
user_chat = "Coc Coc"
mojichat_file = "mojichat_list.csv"


# @pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelBigBoxChat:
    mojichat_object = MojichatObjects()
    version_page_element = VersionPageElements()
    chat_elements = ChatElement()

    def verify_show_moji_icon(self, action='ON', moji_is_on=True):
        driver = webdriver.Chrome(options=chrome_options_preset())
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_extension(driver, action)
        self.mojichat_object.login_facebook(driver)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'SMALL_CHAT', moji_is_on)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT', moji_is_on)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT_FACEBOOK_MESSENDER', moji_is_on)

    @pytestrail.case('C54439')
    def test_check_status_change_when_user_turn_on_off_moji_feature(self):
        # self.mojichat_object.enable_moji()
        # Enable moji flag notyet stable
        self.verify_show_moji_icon(action='ON', moji_is_on=True)
        self.verify_show_moji_icon(action='OFF', moji_is_on=False)

    @pytestrail.case('C147187')
    def test_check_set_mojichat_is_off_at_developer_mode(self):
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_in_detail_extension_page(driver)
        self.mojichat_object.login_facebook(driver)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'SMALL_CHAT', moji_is_on=False)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT', moji_is_on=False)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT_FACEBOOK_MESSENDER', moji_is_on=False)

    @pytestrail.case('C86109')
    # Need install coccoc, enable flag (but enable flag still not stabled when using in function)
    def test_check_if_user_send_first_sticker_successfully_follow_tooltips(self):
        # from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        # uninstall_then_install_coccoc_with_default(is_needed_clear_user_data=True, is_needed_clean_up=True)
        driver = coccoc_instance()
        driver.maximize_window()
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_extension(driver, action="ON")
        self.mojichat_object.login_facebook(driver)
        #self.mojichat_object.verify_send_first_sticker(driver, chat_type='SMALL_CHAT')
        self.mojichat_object.verify_send_first_sticker(driver, chat_type='BIG_CHAT')

#     @pytestrail.case('C54462')
#     def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
#         self.mojichat_object.open_chat_browser(browser)
#         self.mojichat_object.select_user_chat(browser, user_chat)
#         self.mojichat_object.send_text_into_chat(browser, "clear cache")
#
#         list_mojichat = CSVHandle().get_from_csv(mojichat_file)
#         for i in list_mojichat:
#             self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)
#             self.mojichat_object.verify_chat_is_empty(browser)
#
#     @pytestrail.case('C86095')
#     def test_check_if_user_can_using_arrow_key_to_navigate_suggestion_stickers(self, browser):
#         self.mojichat_object.open_chat_browser(browser)
#         self.mojichat_object.select_user_chat(browser, user_chat)
#         self.mojichat_object.select_moji_on_suggestion_panel_by_arrow_key(browser, "hihi")
#         time.sleep(10)
#
#
# @pytest.mark.skip(reason='Skip mojchat')
# class TestSuggestionPanelSmallChat:
#     mojichat_object = MojichatObjects(MojichatLocators.SMALL_CHAT)
#
#     @pytestrail.case('C54462')
#     def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
#         self.mojichat_object.open_chat_browser(browser)
#         self.mojichat_object.select_user_chat(browser, user_chat)
#         self.mojichat_object.send_text_into_chat(browser, "clear cache")
#
#         list_mojichat = CSVHandle().get_from_csv(mojichat_file)
#         for i in list_mojichat:
#             self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)
#             self.mojichat_object.verify_chat_is_empty(browser)
