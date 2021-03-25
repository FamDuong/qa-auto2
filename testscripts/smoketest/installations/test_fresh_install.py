import logging

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
    # @pytest.mark.coccocdev
    def test_installing_fresh_package_successfully_on_windows(self, is_active_host, url, coccoc_version):
        browser, download_folder, is_activated_host = self.get_browser_and_download_folder(is_active_host)
        languages = ['en', 'vi']
        try:
            for language in languages:
                if language == 'en':
                    self.check_install_coccoc(browser, download_folder, url, language, coccoc_version=coccoc_version)
                elif language == 'vi':
                    self.check_install_coccoc(browser, download_folder, url, language, coccoc_version=coccoc_version)
        finally:
            self.clearing_cached_data(is_activated_host, browser, download_folder)

    @pytestrail.case('C44779')
    # @pytest.mark.coccocdev
    def test_popup_of_installer_confirm_during_the_installation(self, is_active_host, url):
        browser, download_folder, is_activated_host = self.get_browser_and_download_folder(is_active_host)
        try:
            # Open Cốc Cốc installing panel for
            self.open_coccoc_installer(browser, download_folder, url)
            # Verify Cốc Cốc installing panel appears
            from models.pageobject.installs import verify_installer_popup_appears
            verify_installer_popup_appears()
        finally:
            self.clearing_cached_data(is_activated_host, browser, download_folder)

    @pytestrail.case('C44780')
    @pytest.mark.coccocdev
    @pytest.mark.skip('Outdate when omh 2.7.1.5 releases')
    def test_installation_dialog_after_installing_successfully(self, is_active_host, url):
        browser, download_folder, is_activated_host = self.get_browser_and_download_folder(is_active_host)
        common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup', extension='.exe')
        # download Cốc Cốc installer from url
        coccoc_installer = self.coccoc_page_obj.get_path_installer(browser, url, download_folder, "win", "en")
        try:
            # Install Cốc Cốc
            self.install_coc_coc(coccoc_installer, 'en')
            # Verify "Cốc Cốc installing panel" appears
            verify_installation_complete_popup_appears()
        finally:
            self.clearing_cached_data(is_activated_host, browser, download_folder)

    def open_coccoc_installer(self, browser, download_folder, url, coccoc_installer="Cốc Cốc Installer"):
        common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup', extension='.exe')
        # download Cốc Cốc installer from url
        installer = self.coccoc_page_obj.get_path_installer(browser, url, download_folder, "win", "en")
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

    def check_install_coccoc(self, browser, download_folder, url, language, coccoc_version):
        common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup', extension='.exe')
        coc_coc_installer = self.coccoc_page_obj.get_path_installer(browser, url, download_folder, "win", language)
        self.install_coc_coc(coc_coc_installer, language)
        utils_automation.common_browser.cleanup()
        coccoc_driver = utils_automation.common_browser.coccoc_instance()
        self.settings_page_obj.verify_menu_base_on_language(coccoc_driver, language)
        self.version_page_obj.verify_installed_coccoc_and_flash_versions(coccoc_driver, coccoc_version)
        common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup', extension='.exe')

    def clearing_cached_data(self, is_activated_host, browser, download_folder):
        if is_activated_host:
            LOGGER.info("Deactivate host")
            common.interact_dev_hosts("deactivate")
        browser.quit()
        utils_automation.common_browser.cleanup()
        common.delete_installer_download(download_folder, language='', installer_name='CocCocSetup', extension='.exe')

    def get_browser_and_download_folder(self, is_active_host):
        is_activated_host = False
        if is_active_host:
            LOGGER.info("Activate host: " + str(is_active_host))
            common.interact_dev_hosts("activate")
            is_activated_host = True
        browser = init_chrome_driver()
        download_folder = common.get_default_download_folder(browser, Urls.CHROME_SETTINGS_DOWNLOAD_URL)
        return browser, download_folder, is_activated_host
