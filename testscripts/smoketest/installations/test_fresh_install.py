import logging
import platform

import pytest
from pytest_testrail.plugin import pytestrail

import testscripts.smoketest.common as common
import utils_automation.common
import utils_automation.common_browser
from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.version import VersionPageObject
from models.pageobject.settings import SettingsPageObject
from testscripts.common_init_driver import init_chrome_driver
from utils_automation.const import Urls
from utils_automation.common import FilesHandle
from models.pageobject.installs import verify_installation_complete_popup_appears

LOGGER = logging.getLogger(__name__)


class TestFreshInstall:
    coccoc_page_obj = CocCocPageObjects()
    version_page_obj = VersionPageObject()
    settings_page_obj = SettingsPageObject()
    files_handle_obj = FilesHandle()

    @pytestrail.case('C44777')
    # @pytestrail.defect('BR-1071')
    # @pytest.mark.coccocdev
    # @pytest.mark.skip(reason="Bug BR-1071 with installer Vietnamese")
    def test_installing_fresh_package_successfully_on_windows(self, is_active_host, url, coccoc_version):
        # Get default download forlder
        is_activated_host = False
        if is_active_host:
            LOGGER.info("Activate host: " + str(is_active_host))
            common.interact_dev_hosts("activate")
            is_activated_host = True
        browser = init_chrome_driver()
        download_folder = common.get_default_download_folder(browser, Urls.CHROME_SETTINGS_DOWNLOAD_URL)
        common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup', extension='.exe')
        # browser = utils_automation.common_browser.coccoc_instance()
        # download_folder = common.get_default_download_folder(browser)
        languages = ['en', 'vn']
        try:
            for language in languages:
                if language == 'en':
                    LOGGER.info("Install in english")
                    browser = self.check_install_coccoc_in_english(browser, download_folder, url, language,
                                                                   coccoc_version)
                elif language == 'vi':
                    LOGGER("Install in vietnamese")
                    browser = self.check_install_coccoc_in_english(browser, download_folder, url, language,
                                                                   coccoc_version)
        finally:
            if is_activated_host:
                LOGGER.info("Deactivate host")
                common.interact_dev_hosts("deactivate")
            browser.quit()
            # Delete downloaded installer
            common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup',
                                             extension='.exe')

    @pytestrail.case('C44779')
    # @pytest.mark.coccocdev
    def test_popup_of_installer_confirm_during_the_installation(self):
        # Get download folder
        browser = utils_automation.common_browser.coccoc_instance()
        download_folder = common.get_default_download_folder(browser)
        try:
            # Open Cốc Cốc installing panel for
            self.open_coccoc_installer(browser, download_folder)
            # Verify Cốc Cốc installing panel appears
            from models.pageobject.installs import verify_installer_popup_appears
            verify_installer_popup_appears()
        finally:
            # Install Cốc Cốc again (for run other cases)
            utils_automation.common_browser.cleanup()
            common.install_coccoc_set_as_default()
            # Delete downloaded installer
            common.delete_installer_download(download_folder, 'en')

    @pytestrail.case('C44780')
    # @pytest.mark.coccocdev
    def test_installation_dialog_after_installing_successfully(self):
        # Get default download forlder
        browser = utils_automation.common_browser.coccoc_instance()
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
            utils_automation.common_browser.cleanup()
        else:
            pass
        common.uninstall_old_version_remove_local_app()
        common.install_coccoc_installer_from_path(coc_coc_installer, language)

    def check_install_coccoc_in_vietnamese(self, browser, download_folder, url, coccoc_version):
        coc_coc_installer = self.coccoc_page_obj.get_path_installer(browser, url, download_folder, "win", "vi")
        self.install_coc_coc(coc_coc_installer, "vi")
        utils_automation.common_browser.cleanup()
        browser = utils_automation.common_browser.coccoc_instance()
        self.settings_page_obj.verify_menu_base_on_language(browser, "vi")
        self.version_page_obj.verify_installed_coccoc_and_flash_versions(browser)
        return browser

    def check_install_coccoc_in_english(self, browser, download_folder, url, language, coccoc_version):
        coc_coc_installer = self.coccoc_page_obj.get_path_installer(browser, url, download_folder, "win", "en")
        self.install_coc_coc(coc_coc_installer, "en")
        utils_automation.common_browser.cleanup()
        browser = utils_automation.common_browser.coccoc_instance()
        self.settings_page_obj.verify_menu_base_on_language(browser, "en")
        self.version_page_obj.verify_installed_coccoc_and_flash_versions(browser, coccoc_version)
        return browser
