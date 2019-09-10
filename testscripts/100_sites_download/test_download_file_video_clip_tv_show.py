from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

savior_page_object = SaviorPageObject()
any_site_page_object = AnySitePageObject()


class TestFptPlay:

    @staticmethod
    def prepare_savior_option_display(browser):
        browser.get(OtherSiteUrls.FPT_PLAY_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        list_windows = browser.window_handles
        if len(list_windows) >= 2:
            browser.switch_to.window(list_windows[0])
        any_site_page_object.choose_watch_from_beginning_fpt_play(browser)
        any_site_page_object.mouse_over_video_item_fpt_play(browser)

    @pytestrail.case('C98727')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_option_display(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')



