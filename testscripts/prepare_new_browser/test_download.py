from testscripts.prepare_new_browser.test_install import TestInstall
from pytest_testrail.plugin import pytestrail

class TestDownload(TestInstall):

    @pytestrail.case('C10328')
    def test_download_from_homepage_of_2_domains(self, browser, get_current_download_folder):
        # Download latest version
        download_file = self.coccoc_page_object.get_path_of_downloaded_coccoc_installer_from_dev(browser, get_current_download_folder)
        download_file = self.coccoc_page_object.download_coccoc_from_production(browser, get_current_download_folder)

