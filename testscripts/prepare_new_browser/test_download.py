from testscripts.prepare_new_browser.test_install import TestInstall
from pytest_testrail.plugin import pytestrail

from utils_automation.const import Urls


class TestDownload(TestInstall):

    @pytestrail.case('C10328')
    def test_download_from_homepage_of_2_domains(self, browser, get_current_download_folder):
        # Download latest version
        download_file = self.coccoc_page_object.get_path_installer(browser, Urls.COCCOC_DEV_URL,
                                                                   get_current_download_folder)
        download_file = self.coccoc_page_object.get_path_installer(browser, Urls.COCCOC_URL,
                                                                   get_current_download_folder)