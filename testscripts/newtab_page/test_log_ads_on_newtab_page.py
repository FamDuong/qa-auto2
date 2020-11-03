import logging

from pytest_testrail.plugin import pytestrail

from models.pageobject.newtab import NewTabLogAdsActions
from testscripts.newtab_page.common import get_browser_log_entries, get_last_info_log
from utils_automation.const import NewTabAdsDemoUrls
from models.pageobject.basepage_object import BasePageObject

LOGGER = logging.getLogger(__name__)


class TestLogAdsOnNewTabPage:
    newtab_log_ads_action = NewTabLogAdsActions()
    base_page_object = BasePageObject()
    @pytestrail.case('C329559')
    def test_banner_ads_check_log_events(self, browser):
        browser.get(NewTabAdsDemoUrls.CENTER_BANNER_ADS_640x360_URL)
        LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.CENTER_BANNER_ADS_640x360_URL)
        self.newtab_log_ads_action.switch_to_banner_ads_640x360_iframe(browser)
        self.newtab_log_ads_action.click_on_banner_ads_640x360_ads(browser)
        log_entries = get_browser_log_entries(browser)
        last_log = get_last_info_log(log_entries)
        assert 'ntrbClick' in last_log

    @pytestrail.case('C329655')
    def test_magnetic_masthread_ads_check_log_events(self, browser):
        browser.get(NewTabAdsDemoUrls.MAGNETIC_MASTHREAD_ADS_URL)
        LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.MAGNETIC_MASTHREAD_ADS_URL)
        self.newtab_log_ads_action.click_on_skin_ads(browser)
        log_entries = get_browser_log_entries(browser)
        last_log = get_last_info_log(log_entries)
        assert 'skinClick' in last_log

    @pytestrail.case('C329664')
    def test_video_masthead_ads_check_log_events(self, browser):
        browser.get(NewTabAdsDemoUrls.VIDEO_MASTHREAD_ADS_URL)
        LOGGER.info("Open demo link: "+NewTabAdsDemoUrls.VIDEO_MASTHREAD_ADS_URL)
        self.newtab_log_ads_action.click_on_skin_ads(browser)
        log_entries = get_browser_log_entries(browser)
        last_log = get_last_info_log(log_entries)
        assert 'skinClick' in last_log

    @pytestrail.case('C329613')
    def test_skin_ads_check_log_events(self, browser):
        urls = [NewTabAdsDemoUrls.SKIN_ADS_URL1, NewTabAdsDemoUrls.SKIN_ADS_URL2]
        for url in urls:
            browser.get(url)
            LOGGER.info("Open demo link: " + url)
            self.newtab_log_ads_action.click_on_skin_ads(browser)
            log_entries = get_browser_log_entries(browser)
            last_log = get_last_info_log(log_entries)
            assert 'skinClick' in last_log

    @pytestrail.case('C329505')
    def test_video_ads_check_log_events(self, browser):
        browser.get(NewTabAdsDemoUrls.VIDEO_ADS_URL)
        LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.VIDEO_ADS_URL)

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        log_entries = get_browser_log_entries(browser)
        last_log = get_last_info_log(log_entries)
        import time
        time.sleep(10)
        # assert 'skinClick' in last_log


