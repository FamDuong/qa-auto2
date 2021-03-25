from pytest_testrail.plugin import pytestrail

from testscripts.common_init_driver import init_chrome_driver
from testscripts.smoketest.common import get_default_download_folder, delete_installer_download
from utils_automation.const import Urls
from models.pageobject.coccocpage import sleep_with_timeout
import logging

LOGGER = logging.getLogger(__name__)


class TestDownloadCoccocInstallFile:

    @pytestrail.case('C10329')
    def test_download_from_thank_you_page(self):
        driver = init_chrome_driver()
        default_download_folder = get_default_download_folder(driver, Urls.CHROME_SETTINGS_DOWNLOAD_URL)
        try:
            urls = [Urls.COCCOC_THANK_YOU_URL_EN, Urls.COCCOC_THANK_YOU_URL_VI, Urls.COCCOC_THANK_YOU_URL_EN_PRO, Urls.COCCOC_THANK_YOU_URL_VI_PRO]

            for i in range(len(urls)):
                child_url = str(urls[i])
                #delete_installer_download(default_download_folder, language='', installer_name='CocCocSetup', extension='.exe')
                LOGGER.info("Download from " + child_url)
                driver.get(child_url)
                sleep_with_timeout(default_download_folder, language='', installer_name='CocCocSetup', extension='.exe')
                from testscripts.smoketest.common import check_if_installer_is_downloaded
                assert check_if_installer_is_downloaded(default_download_folder, language='', installer_name='CocCocSetup', extension='.exe')
                #delete_installer_download(default_download_folder, language='', installer_name='CocCocSetup',extension='.exe')
        finally:
            delete_installer_download(default_download_folder, language='', installer_name='CocCocSetup', extension='.exe')
            driver.quit()