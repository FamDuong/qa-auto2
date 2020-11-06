import logging
import time

from models.pagelocators.newtab import NewTabMostVisitedLocators
from models.pageobject.coccoc_search.coccoc_search_page_objects import CocCocSearchPageObjects
from models.pageobject.newtab import NewTabAdsActions, NewTabLogAdsActions
from testscripts.search.ccsearch_with_adblock_plus.common import verify_ads_is_oppened_in_newtab

coccoc_search_page_object = CocCocSearchPageObjects()
new_tab_ads_action = NewTabAdsActions()

LOGGER = logging.getLogger(__name__)


def scroll_down_to_show_ads(driver, timeout, total_news_base=1200):
    scroll_pause_time = timeout
    last_height = 5000
    while True:
        total_news = new_tab_ads_action.count_all_news(driver)
        driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
        time.sleep(scroll_pause_time)
        last_height += 5000
        if total_news > total_news_base:
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


def count_log_contain_string(log_entries, contains_strings):
    total_contains = 0
    for i in range(len(log_entries)):
        for j in range(len(contains_strings)):
            if contains_strings[j] in str(log_entries[i]):
                LOGGER.info("Log entry is contain [" + contains_strings[j] + "]: " + str(log_entries[i]))
                total_contains += 1
    return total_contains


def close_the_second_window(driver):
    windows_handles = driver.window_handles
    if len(windows_handles) == 2:
        driver.switch_to.window(windows_handles[1])
        driver.close()
        driver.switch_to.window(windows_handles[0])


def get_news_logs(driver, contains_string='coccoc.com/log?'):
    import json
    get_network_log_javascript = "var performance = window.performance || window.mozPerformance || " \
                                 "window.msPerformance || window.webkitPerformance || {}; var network = " \
                                 "performance.getEntries() || {}; return network;";
    log = driver.execute_script(get_network_log_javascript)

    json_formatted_str = json.dumps(log, indent=2)
    network_log_json = json.loads(json_formatted_str)
    news_logs = []
    for network in network_log_json:
        if contains_string in network['name']:
            news_logs.append(network['name'])
    for log in news_logs:
        LOGGER.info(log)
    return news_logs


newtab_log_ads_action = NewTabLogAdsActions()


def click_newsfeed_card(driver, newsfeed_card_type):
    if 'Small News' in newsfeed_card_type:
        newtab_log_ads_action.click_on_news_small_news(driver)
    elif 'Big News' in newsfeed_card_type:
        newtab_log_ads_action.click_on_news_big_news(driver)
    elif 'Small Ad' in newsfeed_card_type:
        newtab_log_ads_action.click_on_news_small_ads(driver)
    else:
        newtab_log_ads_action.click_on_news_big_ads(driver)


def decode_url(log):
    import urllib
    url_decode = urllib.parse.unquote(str(log))
    LOGGER.info(url_decode)
    url_decodes = [url_decode]
    return url_decodes


def get_requid(root_string, start_string, end_string):
    import re
    reqid = re.search('%s(.*)%s' % (start_string, end_string), str(root_string)).group(1)
    LOGGER.info("Reqid = [" + reqid + "] in [" + str(root_string) + "]")
    return reqid


def assert_newsfeed_logs_card_size(driver, newsfeed_card_type, card_size):
    driver.refresh()
    scroll_down_to_show_ads(driver, timeout=0, total_news_base=50)
    LOGGER.info("Get Network log after click " + newsfeed_card_type)
    click_newsfeed_card(driver, newsfeed_card_type)
    close_the_second_window(driver)
    feed_action_card_click_log = get_news_logs(driver, contains_string='coccoc.com/log?feedAction=cardClick')
    webhp_action_card_click_log = get_news_logs(driver, contains_string='coccoc.com/log?webhpAction=Click')
    LOGGER.info(
        "Assert after click " + newsfeed_card_type + " exist network logs: {log?feedAction=cardClick contains [" + card_size + "]} and {log?webhpAction=Click}")
    assert len(webhp_action_card_click_log) == 1
    assert count_log_contain_string(decode_url(feed_action_card_click_log), [card_size]) == 1


def assert_newsfeed_logs_reqid(driver, newsfeed_card_type):
    driver.refresh()
    scroll_down_to_show_ads(driver, timeout=0, total_news_base=50)
    LOGGER.info("Get Network log after click " + newsfeed_card_type)
    click_newsfeed_card(driver, newsfeed_card_type)
    close_the_second_window(driver)
    feed_action_card_click_log = get_news_logs(driver, contains_string='coccoc.com/log?feedAction=cardClick')
    webhp_action_card_click_log = get_news_logs(driver, contains_string='coccoc.com/log?webhpAction=Click')
    reqid_in_feed_action = get_requid(feed_action_card_click_log, start_string='&reqid=', end_string='&type=')
    value_in_webhp_action = get_requid(webhp_action_card_click_log, start_string='&Value=', end_string='&quota=')
    LOGGER.info(
        "Assert after click " + newsfeed_card_type + "requid in feedAction = webhpAction")
    assert reqid_in_feed_action in value_in_webhp_action
