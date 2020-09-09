import logging
import time

from models.pageobject.extensions import ABPExtensionsDetailPageObject
from models.pageobject.settings import SettingsPageObject
from testscripts.search.ccsearch_with_adblock_plus.common import change_adblock_plus_mode, get_query, \
    verify_ads_is_oppened_in_newtab
from testscripts.search.common import prepare_query
from testscripts.smoketest.common import coccoc_instance
from utils_automation.const import CocCocExtensions, Urls

LOGGER = logging.getLogger(__name__)


class TestCCsearchWithAdblockPlus:
    abp_extension_detail_page_object = ABPExtensionsDetailPageObject()
    settings_page_object = SettingsPageObject()

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
                time.sleep(3)
                verify_ads_is_oppened_in_newtab(driver)
