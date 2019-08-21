import time
from pytest_testrail.plugin import pytestrail
from models.pageobject.mojichat import MojichatObjects
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import Browser
from utils_automation.common import CSVHandle

browser = Browser()
user_chat = "Coc Coc"
mojichat_file = "mojichat_list.csv"

class TestSuggestionPanelBigBoxChat:
    mojichat_object = MojichatObjects()

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


