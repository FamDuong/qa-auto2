import time
from pytest_testrail.plugin import pytestrail
from models.pageobject.mojichat import MojichatObjects
from utils_automation.setup import Browser
from utils_automation.common import CSVHandle

browser = Browser()
user_chat = "Coc Coc"
mojichat_file = "mojichat_list.csv"
big_chat = "big_chat"

class TestSuggestionPanelBigBoxChat:
    mojichat_object = MojichatObjects()

    @pytestrail.case('C54462')
    def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
        self.mojichat_object.open_big_chat_browser(browser, big_chat)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.send_text_into_big_chat(browser, "clear cache")

        list_mojichat = CSVHandle().get_from_csv(mojichat_file)
        for i in list_mojichat:
            self.mojichat_object.select_moji_on_suggestion_panel_into_big_chat(browser, i, 0)


class TestSuggestionPanelSmallChat:
    mojichat_object = MojichatObjects()

    @pytestrail.case('C54462')
    def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
        self.mojichat_object.open_small_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.send_text_into_small_chat(browser, "clear cache")

        list_mojichat = CSVHandle().get_from_csv(mojichat_file)
        for i in list_mojichat:
            self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)


