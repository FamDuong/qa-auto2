import logging
import time

from models.pagelocators.coccoc_search.cc_search import CCSearchPageLocators
from models.pageobject.extensions import ABPExtensionsDetailPageObject
from models.pageobject.settings import SettingsPageObject
from testscripts.search.ccsearch_with_adblock_plus.common import change_adblock_plus_mode, get_query, \
    verify_ads_is_oppened_in_newtab
from testscripts.search.common import prepare_query
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import CocCocExtensions, Urls
from models.pageobject.coccoc_search.coccoc_search_page_objects import CocCocSearchPageObjects

LOGGER = logging.getLogger(__name__)


class TestCCsearchWithAdblockPlus:
    abp_extension_detail_page_object = ABPExtensionsDetailPageObject()
    settings_page_object = SettingsPageObject()
    coccoc_search_page_object = CocCocSearchPageObjects()

    def test_ccsearch_with_adblock_plus(self):
        driver = coccoc_instance()
        driver.maximize_window()
        LOGGER.info("Open coccoc://extension")
        self.settings_page_object.open_coc_coc_extension_page(driver)
        ad_block_modes = [CocCocExtensions.AD_BLOCK_STRICT_MODE, CocCocExtensions.AD_BLOCK_STANDARD_MODE]
        for mode in ad_block_modes:
            LOGGER.info("*** Testing in mode: " + mode)
            change_adblock_plus_mode(driver, mode)

            queries = get_query()
            for query in queries:
                url = prepare_query(Urls.CC_SEARCH_QUERY, query)
                driver.get(url)
                total_ads = self.coccoc_search_page_object.count_total_ads_on_ccsearch_page(driver)
                verify_ads_is_oppened_in_newtab(driver, total_ads, CCSearchPageLocators.AD_LINK_BY_INDEX_XPATH)
