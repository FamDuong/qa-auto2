from pytest_testrail.plugin import pytestrail


class TestDownloadCoccocInstallFile:

    def coccoc_instance(self):
        from testscripts.smoketest.common import chrome_options_preset
        from selenium import webdriver
        driver = webdriver.Chrome(chrome_options=chrome_options_preset())
        return driver

    @pytestrail.case('C10329')
    def test_download_from_thank_you_page(self):
        driver = self.coccoc_instance()
        from utils_automation.const import Urls
        from models.pageobject.coccocpage import sleep_with_timeout
        from testscripts.smoketest.common import get_default_download_folder
        default_download_folder = get_default_download_folder(driver)
        driver.get(Urls.COCCOC_THANK_YOU_URL_EN)
        sleep_with_timeout(default_download_folder, 'en')
        from testscripts.smoketest.common import check_if_installer_is_downloaded
        assert check_if_installer_is_downloaded(default_download_folder, 'en')





