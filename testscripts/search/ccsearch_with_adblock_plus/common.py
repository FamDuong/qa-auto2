import logging
import time

from models.pageobject.coccoc_home_page_objects import CocCocHomePageActions
from models.pageobject.coccoc_search.coccoc_search_page_objects import CocCocSearchPageObjects
from models.pageobject.extensions import ExtensionsDetailsPageObject, ABPExtensionsDetailPageObject
from models.pageobject.settings import SettingsPageObject
from utils_automation.common import WindowsHandler, FilesHandle, CSVHandle
import testscripts.smoketest.common as common

LOGGER = logging.getLogger(__name__)

windows_handler = WindowsHandler()
coccoc_home_page_action = CocCocHomePageActions()
settings_page_object = SettingsPageObject()
extension_detail_page_object = ExtensionsDetailsPageObject()
abp_extension_detail_page_object = ABPExtensionsDetailPageObject()
file_handle = FilesHandle()
coccoc_search_page_object = CocCocSearchPageObjects()


def get_resource_path():
    resource_path_temp = file_handle.get_absolute_filename("\\resources\\")
    resource_path = resource_path_temp.replace('\\utils_automation', '')
    return resource_path


def update_extension(driver):
    driver.maximize_window()
    settings_page_object.open_coc_coc_extension_page(driver)
    settings_page_object.update_extension(driver)
    abp_extension_detail_page_object.wait_until_finish_update_abp_to_latest(driver)


def change_host_file(test_environment):
    LOGGER.info("Test environment" + test_environment)
    if test_environment in 'dev':
        LOGGER.info("Activate host")
        common.interact_dev_hosts("activate")
    else:

        LOGGER.info("Deactivate host")
        common.interact_dev_hosts("deactivate")


def change_adblock_plus_mode(driver, ads_block_mode):
    settings_page_object.open_coc_coc_extension_page(driver)
    extension_detail_page_object.click_coc_coc_ad_block_extension_details_button(driver)
    abp_extension_detail_page_object.click_extension_options(driver)
    windows_handles = driver.window_handles
    if len(windows_handles) == 2:
        driver.switch_to.window(windows_handles[1])
    abp_extension_detail_page_object.select_abp_mode(driver, ads_block_mode)
    time.sleep(5)
    driver.close()
    driver.switch_to.window(windows_handles[0])


def get_query():
    test_data = get_resource_path() + "test_data\\test_data_adblock_for_search.csv"
    query = CSVHandle().get_from_csv(test_data)
    return query


def verify_ads_is_oppened_in_newtab(driver, total_ads, ads_locator_xpath_by_index):
    time.sleep(2)
    root_url = driver.current_url
    LOGGER.info("===============================================")
    LOGGER.info("Root url " + root_url)
    LOGGER.info("Total ads: " + str(total_ads))
    if total_ads > 0:
        for i in range(total_ads):
            coccoc_search_page_object.click_on_ad(driver, i + 1, ads_locator_xpath_by_index)
            windows_handles = driver.window_handles
            assert len(windows_handles) == 2

            driver.switch_to.window(windows_handles[1])
            ad_url = driver.current_url
            LOGGER.info("Ad " + str(i) + ": " + ad_url)
            from datetime import datetime
            start_time = datetime.now()
            while root_url in ad_url:
                time.sleep(1)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 10:
                    break
            assert root_url not in ad_url

            driver.close()
            driver.switch_to.window(windows_handles[0])
        driver.execute_script("window.history.go(-1)")
