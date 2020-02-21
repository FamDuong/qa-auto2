from pytest_testrail.plugin import pytestrail

import testscripts.smoketest.common as common
from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.version import VersionPageObject
from utils_automation.const import Urls
from utils_automation.common import BrowserHandler, FilesHandle
from models.pageobject.installs import verify_installation_complete_popup_appears


def install_coc_coc(coc_coc_installer, is_needed_clean_up=True):
    common.uninstall_old_version_remove_local_app()
    common.install_coccoc_installer_from_path(coc_coc_installer, is_needed_clean_up)


class TestFreshInstall:
    version_page_obj = VersionPageObject()
    coccoc_page_obj = CocCocPageObjects()
    browser_handler_obj = BrowserHandler()
    files_handle_obj = FilesHandle()

    # Precondition: Machine is installed Coc Coc
    @pytestrail.case('C44777')
    def test_installing_fresh_package_successfully_on_windows(self, language="en"):
        # Get default download forlder
        browser = common.coccoc_instance()
        download_folder = common.get_default_download_folder(browser)
        try:
            # Install Cốc Cốc
            install_coc_coc(self.get_installer_path(browser, download_folder))
            # Verify version
            self.verify_installed_coccoc_version(browser)
        finally:
            # Delete downloaded installer
            self.files_handle_obj.delete_files_in_folder(download_folder, 'coccoc_' + language + '.exe')

    @pytestrail.case('C44779')
    def test_popup_of_installer_confirm_during_the_installation(self, language="en"):
        # Get download folder
        browser = common.coccoc_instance()
        download_folder = common.get_default_download_folder(browser)
        try:
            # Open Cốc Cốc installing panel for
            self.open_coccoc_installer(browser, download_folder)
            # Verify Cốc Cốc installing panel appears
            from models.pageobject.installs import verify_installer_popup_appears
            verify_installer_popup_appears()
        finally:
            # Install Cốc Cốc again (for run other cases)
            common.cleanup()
            common.install_coccoc_set_as_default()
            # Delete downloaded installer
            self.files_handle_obj.delete_files_in_folder(download_folder, 'coccoc_' + language + '.exe')

    @pytestrail.case('C44780')
    def test_installation_dialog_after_installing_successfully(self, language="en"):
        # Get default download forlder
        browser = common.coccoc_instance()
        download_folder = common.get_default_download_folder(browser)
        try:
            # Install Cốc Cốc
            install_coc_coc(self.get_installer_path(browser, download_folder), False)
            # Verify "Cốc Cốc installing panel" appears
            verify_installation_complete_popup_appears()
        finally:
            # Delete downloaded installer
            self.files_handle_obj.delete_files_in_folder(download_folder, 'coccoc_' + language + '.exe')

    def get_installer_path(self, browser, download_folder, os="win", language="en"):
        coc_coc_installer = self.coccoc_page_obj.get_path_installer(browser, Urls.COCCOC_DEV_URL, download_folder, os, language)
        return coc_coc_installer

    def verify_installed_coccoc_version(self, browser):
        # Verify in folder: %LOCALAPPDATA%\CocCoc\Browser\Application\\
        cc_expect_version = common.login_then_get_latest_coccoc_dev_installer_version()
        assert common.get_coccoc_version_folder_name() in cc_expect_version
        # Verify in coccoc://version
        browser.get(Urls.COCCOC_VERSION_URL)
        assert cc_expect_version in self.version_page_obj.get_flash_path(browser)
        assert cc_expect_version in self.version_page_obj.get_user_agent(browser)

    def open_coccoc_installer(self, browser, download_folder):
        # download Cốc Cốc installer from dev
        installer = self.get_installer_path(browser, download_folder)
        # Uninstall Cốc Cốc (if have)
        common.uninstall_old_version_remove_local_app()
        # Open file Cốc Cốc installer
        print("open installer...")
        common.open_coccoc_installer_by_path(installer)

    def verify_installed_coccoc_version(self, browser):
        # Verify in folder: %LOCALAPPDATA%\CocCoc\Browser\Application\\
        cc_expect_version = "79.0.3945.134"
        common.login_then_get_latest_coccoc_dev_installer_version()
        assert common.get_coccoc_version_folder_name() in cc_expect_version
        # Verify in coccoc://version
        browser.get(Urls.COCCOC_VERSION_URL)
        assert cc_expect_version in self.version_page_obj.get_flash_path(browser)
        assert cc_expect_version in self.version_page_obj.get_user_agent(browser)
