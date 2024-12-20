import logging
import time
from pytest_testrail.plugin import pytestrail
from models.pageobject.newtab import NewTabLogAdsActions
from testscripts.newtab_page.common import get_browser_log_entries, get_last_info_log, count_log_contain_string, \
    close_the_second_window, scroll_down_to_show_ads, get_news_logs, assert_newsfeed_logs_card_size, \
    assert_newsfeed_logs_reqid, assert_newsfeed_logs_card_click, assert_not_send_logs_after_click_action, \
    get_log_is_ends_with_string
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import NewTabAdsDemoUrls
from models.pageobject.basepage_object import BasePageObject

LOGGER = logging.getLogger(__name__)


class TestLogAdsOnNewTabPage:
    newtab_log_ads_action = NewTabLogAdsActions()
    base_page_object = BasePageObject()

    @pytestrail.case('C329559')
    def test_banner_ads_check_log_events(self, browser):
        try:
            demo_link = NewTabAdsDemoUrls.CENTER_BANNER_ADS_640x360_URL
            browser.get(demo_link)
            LOGGER.info("Open demo link: " + demo_link)

            self.newtab_log_ads_action.switch_to_banner_ads_640x360_iframe(browser)
            self.newtab_log_ads_action.click_on_banner_ads_640x360_ads(browser)
            log_entries = get_browser_log_entries(browser)
            close_the_second_window(browser, demo_link)
            LOGGER.info("Assert after click banner_ads exist console log contains [ntrbClick]")
            assert count_log_contain_string(log_entries, ['ntrbClick']) == 1
        finally:
            close_the_second_window(browser, demo_link)

    @pytestrail.case('C329655')
    def test_magnetic_masthread_ads_check_log_events(self, browser):
        try:
            browser.get(NewTabAdsDemoUrls.MAGNETIC_MASTHREAD_ADS_URL)
            LOGGER.info("Open demo link: " + NewTabAdsDemoUrls.MAGNETIC_MASTHREAD_ADS_URL)
            self.newtab_log_ads_action.click_on_skin_ads(browser)
            close_the_second_window(browser)
            log_entries = get_browser_log_entries(browser)
            LOGGER.info("Assert after click magnetic_masthread_ads exist console log contains [skinClick]")
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
            LOGGER.info("Assert after click video_masthead_ads exist console log contains [skinClick]")
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
                LOGGER.info("Assert after click skin_ads exist console log contains [skinClick]")
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
        LOGGER.info("Assert after scroll down to show floating video shown and click to close floating video_ads "
                    "exist console log contains [feedPinIn, Click]")
        assert count_log_contain_string(log_entries, ['feedPinIn', 'Click']) == 1

        LOGGER.info("================================================================================================")
        LOGGER.info("===============================================================================================\n")
        LOGGER.info("Test log ads wait for floating video completes and auto hides")
        browser.refresh()
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(10)
        log_entries = get_browser_log_entries(browser)
        LOGGER.info("Assert after wait for floating video completes and auto hides exist console log contains ["
                    "feedPipDestroy]")
        assert count_log_contain_string(log_entries, ['feedPipDestroy']) == 1

        LOGGER.info("================================================================================================")
        LOGGER.info("===============================================================================================\n")
        LOGGER.info("Click on video ads to open the landing page of ads")
        browser.refresh()
        self.newtab_log_ads_action.click_on_video_ads(browser)
        log_entries = get_browser_log_entries(browser)
        close_the_second_window(browser)
        LOGGER.info("Assert after click video_ads exist console log contains [ntrbVASTEvent]")
        assert 'ntrbVASTEvent' in get_last_info_log(log_entries)

        LOGGER.info("================================================================================================")
        LOGGER.info("===============================================================================================\n")
        LOGGER.info("Check video playback log")
        browser.refresh()
        time.sleep(15)
        log_entries = get_browser_log_entries(browser)
        assert count_log_contain_string(log_entries, ['Viewability1"']) == 1
        assert count_log_contain_string(log_entries, ['Viewability2']) == 1
        assert count_log_contain_string(log_entries, ['Viewability3']) == 1
        assert count_log_contain_string(log_entries, ['Viewability5']) == 1
        assert count_log_contain_string(log_entries, ['Viewability10']) == 1

    @pytestrail.case('C403341')
    def test_check_card_size_is_shown_in_card_click_log(self, get_newtab_url):
        browser = coccoc_instance()
        if get_newtab_url is not None:
            for url in get_newtab_url:
                browser.get(url)
        assert_newsfeed_logs_card_size(browser, newsfeed_card_type='Small News', card_size='cardSize=small')
        LOGGER.info("===================================================")
        assert_newsfeed_logs_card_size(browser, newsfeed_card_type='Big News', card_size='cardSize=big')
        LOGGER.info("===================================================")
        assert_newsfeed_logs_card_size(browser, newsfeed_card_type='Small Ad', card_size='cardSize=small:ad')
        LOGGER.info("===================================================")
        assert_newsfeed_logs_card_size(browser, newsfeed_card_type='Big Ad', card_size='cardSize=big:ad')

    @pytestrail.case('C410373')
    def test_check_log_when_left_click_a_card(self, get_newtab_url):
        browser = coccoc_instance()
        if get_newtab_url is not None:
            for url in get_newtab_url:
                browser.get(url)
        assert_newsfeed_logs_reqid(browser, newsfeed_card_type='Small News')
        LOGGER.info("===================================================")
        assert_newsfeed_logs_reqid(browser, newsfeed_card_type='Big News')
        LOGGER.info("===================================================")
        assert_newsfeed_logs_reqid(browser, newsfeed_card_type='Small Ad')
        LOGGER.info("===================================================")
        assert_newsfeed_logs_reqid(browser, newsfeed_card_type='Big Ad')

    @pytestrail.case('C403338')
    def test_check_log_when_right_click_a_card(self, get_newtab_url):
        browser = coccoc_instance()
        if get_newtab_url is not None:
            for url in get_newtab_url:
                browser.get(url)
        assert_newsfeed_logs_card_click(browser, newsfeed_card_type='Small News', is_right_click=True)
        LOGGER.info("===================================================")
        assert_newsfeed_logs_card_click(browser, newsfeed_card_type='Big News', is_right_click=True)
        LOGGER.info("===================================================")
        assert_newsfeed_logs_card_click(browser, newsfeed_card_type='Small Ad', is_right_click=True)
        LOGGER.info("===================================================")
        assert_newsfeed_logs_card_click(browser, newsfeed_card_type='Big Ad', is_right_click=True)
        LOGGER.info("===================================================")
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Small News', action='like')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Small News', action='dislike')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Small News', action='hide')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Small News', action='hide source')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Small News', action='report')
        LOGGER.info("===================================================")
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Big News', action='like')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Big News', action='dislike')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Big News', action='hide source')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Big News', action='like')
        assert_not_send_logs_after_click_action(browser, newsfeed_card_type='Big News', action='report')

    @pytestrail.case('C473028')
    def test_check_log_when_first_time_loading_newtab(self, get_newtab_url):
        browser = coccoc_instance()
        if get_newtab_url is not None:
            for url in get_newtab_url:
                browser.get(url)
        browser.refresh()
        new_session_log = get_news_logs(browser, contains_string='nre')
        total_log = get_log_is_ends_with_string(new_session_log, endswith='&newsession=1')
        assert total_log == 1

        scroll_down_to_show_ads(browser, timeout=0, total_news_base=80)
        new_session_log_after_scroll = get_news_logs(browser, contains_string='nre')
        total_log_first = get_log_is_ends_with_string(new_session_log_after_scroll, endswith='&newsession=1')
        total_log_scroll = get_log_is_ends_with_string(new_session_log_after_scroll, endswith='&size=33')
        assert total_log_first == 1
        assert total_log_scroll == len(new_session_log_after_scroll) - 1
