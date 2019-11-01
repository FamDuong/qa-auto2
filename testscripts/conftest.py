import pytest

from models.pageobject.settings import SettingsPageObject
from testscripts.common_setup import clear_data_download, delete_all_mp4_file_download
from utils_automation.const import Urls
from utils_automation.setup import WaitAfterEach


@pytest.fixture()
def clear_download_page_and_download_folder(browser, get_current_download_folder):
    yield
    clear_data_download(browser)
    delete_all_mp4_file_download(get_current_download_folder, '.mp4')


settings_page_object = SettingsPageObject()


@pytest.fixture()
def disable_coccoc_block_ads(browser):
    browser.get(Urls.COCCOC_ADS_BLOCK_URL)
    WaitAfterEach.sleep_timer_after_each_step()
    settings_page_object.interact_ads_block(browser, 'disable')
    yield
    browser.get(Urls.COCCOC_ADS_BLOCK_URL)
    WaitAfterEach.sleep_timer_after_each_step()
    settings_page_object.interact_ads_block(browser, 'enable')






