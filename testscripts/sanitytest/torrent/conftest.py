import pytest

from utils_automation.const import Urls


@pytest.fixture(scope='function')
def clear_download_data(browser):
    browser.get(Urls.COCCOC_DOWNLOAD_URL)
    from models.pageobject.downloads import DownloadsPageObject
    download_page_object = DownloadsPageObject()
    download_page_object.cancel_all_current_torrent(browser)
    download_page_object.clear_all_existed_downloads(browser)
