from pytest_testrail.plugin import pytestrail
from models.pageelements.mojichat import ChatElement
from models.pageobject.mojichat import MojichatObjects
from utils_automation.setup import Browser
from utils_automation.const import Urls
from testscripts.smoketest.common import coccoc_instance
from models.pageelements.version import VersionPageElements

#browser = Browser()
#mojichat_file = "mojichat_list.csv"


# @pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelBigBoxChat():
    mojichat_object = MojichatObjects()
    version_page_element = VersionPageElements()
    chat_elements = ChatElement()

    def change_moji_extension_status_and_login_facebook(self, driver, action="ON"):
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_extension(driver, action)
        self.mojichat_object.login_facebook(driver)

    def verify_show_moji_icon(self, driver, action, moji_is_on=True):
        self.change_moji_extension_status_and_login_facebook(driver, action)
        self.mojichat_object.delete_message_then_send_text_message(driver)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'SMALL_CHAT', moji_is_on)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT', moji_is_on)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT_FACEBOOK_MESSENDER', moji_is_on)

    @pytestrail.case('C86109')
    def test_check_if_user_send_first_sticker_successfully_follow_tooltips(self, browser_moji):
        self.change_moji_extension_status_and_login_facebook(browser_moji, action='ON')
        self.mojichat_object.verify_send_first_sticker(browser_moji, chat_type='SMALL_CHAT')

    @pytestrail.case('C54439')
    def test_check_status_change_when_user_turn_on_off_moji_feature(self, browser_moji):
        driver = coccoc_instance()
        self.verify_show_moji_icon(driver, action='OFF', moji_is_on=False)
        self.verify_show_moji_icon(driver, action='ON', moji_is_on=True)

    @pytestrail.case('C147187')
    def test_check_set_mojichat_is_off_at_developer_mode(self, browser_moji):
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_EXTENSIONS)
        self.mojichat_object.on_off_moji_in_detail_extension_page(driver)
        self.mojichat_object.login_facebook(driver)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'SMALL_CHAT', moji_is_on=False)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT', moji_is_on=False)
        self.mojichat_object.verify_moji_icon_is_on(driver, 'BIG_CHAT_FACEBOOK_MESSENDER', moji_is_on=False)

    @pytestrail.case('C54450')
    def test_check_the_mojichat_panel(self, browser_moji):
        driver = coccoc_instance()
        self.change_moji_extension_status_and_login_facebook(driver, action='ON')
        self.mojichat_object.verify_mojichat_panel(driver, chat_type='SMALL_CHAT')

    @pytestrail.case('C54451')
    def test_check_if_an_emoji_is_added_into_recent_stickers(self, browser_moji):
        driver = coccoc_instance()
        self.change_moji_extension_status_and_login_facebook(driver, action='ON')
        self.mojichat_object.delete_message_then_send_text_message(driver)
        self.mojichat_object.verify_emoji_is_added_into_recent_stickers(driver, chat_type='SMALL_CHAT')

    @pytestrail.case('C81579')
    def test_check_most_popular_stickers_by_package_album_collection(self, browser_moji):
        driver = coccoc_instance()
        self.change_moji_extension_status_and_login_facebook(driver, action='ON')
        self.mojichat_object.verify_most_popular_stickers_by_package_album_collection(driver,
                                                                                      chat_type='SMALL_CHAT')

    @pytestrail.case('C86105')
    def test_check_most_popular_stickers_when_user_type_related_keywords_again(self, browser_moji):
        driver = coccoc_instance()
        self.change_moji_extension_status_and_login_facebook(driver, action='ON')
        self.mojichat_object.verify_most_popular_stickers_when_user_type_related_keywords_again(driver,
                                                                                                chat_type='SMALL_CHAT')

    # @pytestrail.case('C54462')
    # def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser_moji):
    #     driver = coccoc_instance()
    #     self.change_moji_extension_status_and_login_facebook(driver, action='ON')
    #     self.mojichat_object.verify_suggestion_is_shown_when_entering_the_supported_keyword(driver,
    #                                                                                         chat_type='SMALL_CHAT',
    #                                                                                         mojichat_file=mojichat_file)

    @pytestrail.case('C54464')
    def test_check_that_keyword_is_auto_deleted_after_user_sends_the_sticker(self, browser_moji):
        driver = coccoc_instance()
        self.change_moji_extension_status_and_login_facebook(driver, action='ON')
        self.mojichat_object.verify_keyword_is_auto_deleted_after_user_sends_the_sticker(driver,
                                                                                         chat_type='SMALL_CHAT')

    @pytestrail.case('C86098')
    def test_check_that_keyword_is_auto_deleted_after_user_sends_the_sticker_in_show_more(self, browser_moji):
        driver = coccoc_instance()
        self.change_moji_extension_status_and_login_facebook(driver, action='ON')
        self.mojichat_object.verify_keyword_is_auto_deleted_after_user_sends_the_sticker(driver,
                                                                                         chat_type='SMALL_CHAT',
                                                                                         sticker_in_show_more=True)
