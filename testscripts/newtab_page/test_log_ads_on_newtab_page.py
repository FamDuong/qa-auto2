import logging
import time

from pytest_testrail.plugin import pytestrail

from models.pageobject.newtab import NewTabLogAdsActions
from testscripts.newtab_page.common import get_browser_log_entries, get_last_info_log, count_log_contain_string, \
    close_the_second_window
from utils_automation.const import NewTabAdsDemoUrls
from models.pageobject.basepage_object import BasePageObject

LOGGER = logging.getLogger(__name__)


class TestLogAdsOnNewTabPage:
    newtab_log_ads_action = NewTabLogAdsActions()
    base_page_object = BasePageObject()

    @pytestrail.case('C329559')
    def test_banner_ads_check_log_events(self, browser):
        try:
            browser.get(NewTabAdsDemoUrls.CENTER_BANNER_ADS_640x360_URL)
            LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.CENTER_BANNER_ADS_640x360_URL)
            self.newtab_log_ads_action.switch_to_banner_ads_640x360_iframe(browser)
            self.newtab_log_ads_action.click_on_banner_ads_640x360_ads(browser)
            close_the_second_window(browser)
            log_entries = get_browser_log_entries(browser)
            last_log = get_last_info_log(log_entries)
            assert 'ntrbClick' in last_log
        finally:
            close_the_second_window(browser)

    @pytestrail.case('C329655')
    def test_magnetic_masthread_ads_check_log_events(self, browser):
        try:
            browser.get(NewTabAdsDemoUrls.MAGNETIC_MASTHREAD_ADS_URL)
            LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.MAGNETIC_MASTHREAD_ADS_URL)
            self.newtab_log_ads_action.click_on_skin_ads(browser)
            close_the_second_window(browser)
            log_entries = get_browser_log_entries(browser)
            assert count_log_contain_string(log_entries, ['skinClick']) == 1
        finally:
            close_the_second_window(browser)

    @pytestrail.case('C329664')
    def test_video_masthead_ads_check_log_events(self, browser):
        try:
            browser.get(NewTabAdsDemoUrls.VIDEO_MASTHREAD_ADS_URL)
            LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.VIDEO_MASTHREAD_ADS_URL)
            self.newtab_log_ads_action.click_on_skin_ads(browser)
            close_the_second_window(browser)
            log_entries = get_browser_log_entries(browser)
            assert count_log_contain_string(log_entries, ['skinClick']) == 1
        finally:
            close_the_second_window(browser)

    @pytestrail.case('C329613')
    def test_skin_ads_check_log_events(self, browser):
        try:
            urls = [NewTabAdsDemoUrls.SKIN_ADS_URL1, NewTabAdsDemoUrls.SKIN_ADS_URL2]
            for i in range(len(urls)):
                browser.get(urls[i])
                LOGGER.info("Open demo link: " + urls[i])
                self.newtab_log_ads_action.click_on_skin_ads(browser)
                close_the_second_window(browser)
                log_entries = get_browser_log_entries(browser)
                assert count_log_contain_string(log_entries, ['skinClick']) == 1
        finally:
            close_the_second_window(browser)

    @pytestrail.case('C329505')
    def test_video_ads_check_log_events(self, browser):
        LOGGER.info("Scroll down to show floating video shown and click to close floating video")
        import time
        browser.get(NewTabAdsDemoUrls.VIDEO_ADS_URL)
        LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.VIDEO_ADS_URL)
        self.newtab_log_ads_action.click_on_video_ads_close_float_button(browser)
        log_entries = get_browser_log_entries(browser)
        assert count_log_contain_string(log_entries, ['feedPinIn', 'Click']) == 1

        LOGGER.info("===================================================")
        LOGGER.info("Test log ads wait for floating video completes and auto hides")
        browser.refresh()
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(10)
        log_entries = get_browser_log_entries(browser)
        assert count_log_contain_string(log_entries, ['feedPipDestroy']) == 1

        LOGGER.info("===================================================")
        LOGGER.info("Click on video ads to open the landing page of ads")
        browser.refresh()
        self.newtab_log_ads_action.click_on_video_ads(browser)
        close_the_second_window(browser)
        log_entries = get_browser_log_entries(browser)
        last_log = get_last_info_log(log_entries)
        assert 'ntrbVASTEvent' in last_log
