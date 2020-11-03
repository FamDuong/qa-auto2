import logging
import time

from models.pagelocators.newtab import NewTabMostVisitedLocators
from models.pageobject.coccoc_search.coccoc_search_page_objects import CocCocSearchPageObjects
from models.pageobject.newtab import NewTabAdsActions
from testscripts.search.ccsearch_with_adblock_plus.common import verify_ads_is_oppened_in_newtab

coccoc_search_page_object = CocCocSearchPageObjects()
new_tab_ads_action = NewTabAdsActions()

LOGGER = logging.getLogger(__name__)


def scroll_down_to_show_ads(driver, timeout):
    scroll_pause_time = timeout
    last_height = 5000
    while True:
        total_news = new_tab_ads_action.count_all_news(driver)
        driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
        time.sleep(scroll_pause_time)
        last_height += 5000
        if total_news > 1200:
            LOGGER.info("Total news:" + str(total_news))
            break


def verify_most_visited_ads_in_newtab_page(driver, total_ads, ads_locator_xpath_by_index):
    root_url = driver.current_url
    LOGGER.info("===============================================")
    LOGGER.info("Root url " + root_url)
    LOGGER.info("Total ads: " + str(total_ads))
    if total_ads > 0:
        for i in range(total_ads):
            coccoc_search_page_object.click_on_ad(driver, i + 1, ads_locator_xpath_by_index)
            ad_url = driver.current_url
            if root_url not in ad_url:
                LOGGER.info("Ad " + str(i + 1) + ": " + ad_url)
            from datetime import datetime
            start_time = datetime.now()
            if root_url in ad_url:
                while root_url in ad_url:
                    time.sleep(1)
                    ad_url = driver.current_url
                    LOGGER.info("Ad " + str(i + 1) + ": " + ad_url)
                    time_delta = datetime.now() - start_time
                    if time_delta.total_seconds() >= 15:
                        break
            assert root_url not in ad_url
            driver.execute_script("window.history.go(-1)")


def verify_most_visited_ads_steps(driver):
    total_ads = new_tab_ads_action.count_all_most_visited_ads(driver)
    verify_most_visited_ads_in_newtab_page(driver, total_ads,
                                           NewTabMostVisitedLocators.MOST_VISITED_QC_BY_INDEX_XPATH)


def verify_news_ads_steps(driver):
    scroll_down_to_show_ads(driver, 0)
    total_news_ads = new_tab_ads_action.count_all_news_ads(driver)
    verify_ads_is_oppened_in_newtab(driver, total_news_ads, NewTabMostVisitedLocators.NEWS_ADS_BY_INDEX_XPATH)


def check_most_visited_ads_with_url(driver, url_list):
    if url_list is not None:
        for url in url_list:
            driver.get(url)
            verify_most_visited_ads_steps(driver)
    else:
        verify_most_visited_ads_steps(driver)


def check_news_ads_with_url(driver, url_list):
    if url_list is not None:
        for url in url_list:
            driver.get(url)
            verify_news_ads_steps(driver)
    else:
        verify_news_ads_steps(driver)


def get_browser_log_entries(driver):
    """Get the browser console log"""
    try:
        slurped_logs = driver.get_log('browser')
        for log in slurped_logs:
            LOGGER.info(log)
        return slurped_logs
    except Exception as e:
        LOGGER.info("Exception when reading Browser Console log")
        LOGGER.info(str(e))


def get_last_info_log(log_entries):
    new_log_entries = []
    for i in range(len(log_entries)):
        if "'level': 'INFO'" in str(log_entries[i]):
            new_log_entries.append(log_entries[i])
        else:
            new_log_entries = log_entries
    new_log_entries.reverse()
    last_log = str(new_log_entries[0])
    import json
    LOGGER.info("Last log: " + json.dumps(last_log, indent=4))
    return last_log
