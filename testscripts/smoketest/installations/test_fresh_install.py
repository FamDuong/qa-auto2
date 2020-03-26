import platform

import pytest
from pytest_testrail.plugin import pytestrail

import testscripts.smoketest.common as common
from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.version import VersionPageObject
from models.pageobject.settings import SettingsPageObject
from utils_automation.const import Urls
from utils_automation.common import BrowserHandler, FilesHandle
from models.pageobject.installs import verify_installation_complete_popup_appears


class TestFreshInstall:
    coccoc_page_obj = CocCocPageObjects()
    version_page_obj = VersionPageObject()
    settings_page_obj = SettingsPageObject()
    browser_handler_obj = BrowserHandler()
    files_handle_obj = FilesHandle()

    @pytestrail.case('C44777')
    @pytestrail.defect('BR-1071')
    @pytest.mark.coccocdev
    #@pytest.mark.skip(reason="Bug BR-1071 with installer Vietnamese")
    def test_installing_fresh_package_successfully_on_windows(self):
        # Get default download forlder
        browser = common.coccoc_instance()
        download_folder = common.get_default_download_folder(browser)
        languages = ['en', 'vi']
        for language in languages:
            common.delete_installer_download(download_folder, language)
        try:
            for language in languages:
                if language == 'en':
                    browser = self.check_install_coccoc_in_english(browser, download_folder)
                elif language == 'vi':
                    browser = self.check_install_coccoc_in_vietnamese(browser, download_folder)
        finally:
            # Delete downloaded installer
            for language in languages:
                common.delete_installer_download(download_folder, language)

    @pytestrail.case('C44779')
    @pytest.mark.coccocdev
    @pytest.mark.skipif(platform.release() in ["8", "8.1"], reason="BR-810: Windows 8, Windows 8.1 are not show"
                                                                   "'Make Cốc Cốc the default browser'")
    def test_popup_of_installer_confirm_during_the_installation(self):
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
            common.delete_installer_download(download_folder, 'en')

    @pytestrail.case('C44780')
    @pytest.mark.coccocdev
    def test_installation_dialog_after_installing_successfully(self):
        # Get default download forlder
        browser = common.coccoc_instance()
        download_folder = common.get_default_download_folder(browser)
        coccoc_installer = self.coccoc_page_obj.get_path_installer(browser, Urls.COCCOC_DEV_URL, download_folder, "win"
                                                                   , "en")
        try:
            # Install Cốc Cốc
            self.install_coc_coc(coccoc_installer, 'en')
            # Verify "Cốc Cốc installing panel" appears
            verify_installation_complete_popup_appears()
        finally:
            # Delete downloaded installer
            common.delete_installer_download(download_folder, 'en')

    def open_coccoc_installer(self, browser, download_folder, coccoc_installer="Cốc Cốc Installer"):
        # download Cốc Cốc installer from dev
        installer = self.coccoc_page_obj.get_path_installer(browser, Urls.COCCOC_DEV_URL, download_folder, "win"
                                                            , "en")
        # Uninstall Cốc Cốc (if have)
        common.uninstall_old_version_remove_local_app()
        # Open file Cốc Cốc installer
        common.open_coccoc_installer_by_path(installer, coccoc_installer)

    def install_coc_coc(self, coc_coc_installer, language, is_needed_clean_up=True):
        if is_needed_clean_up is True:
            common.cleanup()
        else:
            pass
        common.uninstall_old_version_remove_local_app()
        common.install_coccoc_installer_from_path(coc_coc_installer, language)

    def check_install_coccoc_in_vietnamese(self, browser, download_folder):
        coc_coc_installer = self.coccoc_page_obj.get_path_installer(browser, Urls.COCCOC_DEV_URL, download_folder, "win"
                                                                    , "vi")
        self.install_coc_coc(coc_coc_installer, "vi")
        common.cleanup()
        browser = common.coccoc_instance()
        self.settings_page_obj.verify_menu_base_on_language(browser, "vi")
        return browser

    def check_install_coccoc_in_english(self, browser, download_folder):
        coc_coc_installer = self.coccoc_page_obj.get_path_installer(browser, Urls.COCCOC_DEV_URL, download_folder, "win"
                                                                    , "en")
        self.install_coc_coc(coc_coc_installer, "en")
        common.cleanup()
        browser = common.coccoc_instance()
        self.settings_page_obj.verify_menu_base_on_language(browser, "en")
        self.version_page_obj.verify_installed_coccoc_and_flash_versions(browser)
        return browser