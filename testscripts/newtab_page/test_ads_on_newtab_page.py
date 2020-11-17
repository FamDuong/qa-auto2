import logging
import time

from models.pagelocators.newtab import NewTabMostVisitedLocators
from models.pageobject.newtab import NewTabAdsActions
from models.pageobject.settings import SettingsPageObject
from testscripts.newtab_page.common import verify_most_visited_ads_in_newtab_page, scroll_down_to_show_ads, \
    check_most_visited_ads_with_url, check_news_ads_with_url
from testscripts.search.ccsearch_with_adblock_plus.common import change_adblock_plus_mode, \
    verify_ads_is_oppened_in_newtab
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import CocCocExtensions

LOGGER = logging.getLogger(__name__)


class TestAdsOnNewTabPage:
    new_tab_ads_action = NewTabAdsActions()
    settings_page_object = SettingsPageObject()

    def test_most_visited_ads(self, get_newtab_url):
        driver = coccoc_instance()
        driver.maximize_window()
        LOGGER.info("Open coccoc://extension")
        self.settings_page_object.open_coc_coc_extension_page(driver)
        ad_block_modes = [CocCocExtensions.AD_BLOCK_STRICT_MODE, CocCocExtensions.AD_BLOCK_STANDARD_MODE]
        for mode in ad_block_modes:
            LOGGER.info("*** Testing in mode: " + mode)
            change_adblock_plus_mode(driver, mode)
            driver = coccoc_instance()
            check_most_visited_ads_with_url(driver, get_newtab_url)

    def test_news_ads(self, get_newtab_url):
        driver = coccoc_instance()
        driver.maximize_window()
        LOGGER.info("Open coccoc://extension")
        self.settings_page_object.open_coc_coc_extension_page(driver)
        ad_block_modes = [CocCocExtensions.AD_BLOCK_STRICT_MODE, CocCocExtensions.AD_BLOCK_STANDARD_MODE]
        for mode in ad_block_modes:
            LOGGER.info("*** Testing in mode: " + mode)
            change_adblock_plus_mode(driver, mode)
            driver = coccoc_instance()
            check_news_ads_with_url(driver, get_newtab_url)