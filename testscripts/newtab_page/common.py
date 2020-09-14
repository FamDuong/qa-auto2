import logging
import time

from models.pageobject.coccoc_search.coccoc_search_page_objects import CocCocSearchPageObjects
from models.pageobject.newtab import NewTabAdsActions

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
            LOGGER.info("Ad " + str(i) + ": " + ad_url)
            from datetime import datetime
            start_time = datetime.now()
            while root_url in ad_url:
                time.sleep(1)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
            assert root_url not in ad_url
            driver.execute_script("window.history.go(-1)")
