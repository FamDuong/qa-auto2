from pytest_testrail.plugin import pytestrail
from testscripts.smoketest.common import coccoc_instance, get_default_download_folder, delete_installer_download
from utils_automation.const import Urls
from models.pageobject.coccocpage import sleep_with_timeout


class TestDownloadCoccocInstallFile:

    @pytestrail.case('C10329')
    def test_download_from_thank_you_page(self):
        driver = coccoc_instance()
        default_download_folder = get_default_download_folder(driver)
        try:
            delete_installer_download(default_download_folder, 'en')
            delete_installer_download(default_download_folder, 'vn')
            # Assert download coccoc_en installer
            driver.get(Urls.COCCOC_THANK_YOU_URL_EN)
            sleep_with_timeout(default_download_folder, 'en')
            from testscripts.smoketest.common import check_if_installer_is_downloaded
            assert check_if_installer_is_downloaded(default_download_folder, 'en')
            # Assert download coccoc_vi installer
            driver.get(Urls.COCCOC_THANK_YOU_URL_VI)
            sleep_with_timeout(default_download_folder, 'vi')
            from testscripts.smoketest.common import check_if_installer_is_downloaded
            assert check_if_installer_is_downloaded(default_download_folder, 'vi')
        finally:
            delete_installer_download(default_download_folder, 'en')
            delete_installer_download(default_download_folder, 'vi')

