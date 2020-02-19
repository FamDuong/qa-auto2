from pytest_testrail.plugin import pytestrail
import testscripts.smoketest.common as common
from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.version import VersionPageObject
import settings_master as settings
from utils_automation.const import Urls
from utils_automation.common import BrowserHandler, FilesHandle


def install_coccoc(coccoc_installer):
    #common.uninstall_old_version_remove_local_app()
    common.open_coccoc_installer_from_path(coccoc_installer)


class TestFreshInstall:
    version_page_obj = VersionPageObject()
    coccoc_page_obj = CocCocPageObjects()
    browser_handler_obj = BrowserHandler()
    files_handle_obj = FilesHandle()

    # Precondition: Machine is installed Coc Coc
    @pytestrail.case('C44777')
    def test_installing_fresh_package_successfully_on_windows(self, activate_then_deactive_hosts_for_coccoc_dev,
                                                              language="en"):
        common.cleanup()
        driver = common.coccoc_instance()
        try:
            install_coccoc(self.get_installer(driver))
            self.verify_installed_coccoc_version()
        finally:
            self.files_handle_obj.delete_files_in_folder(common.get_default_download_folder(driver),
                                                         'coccoc_' + language + '.exe')

    @pytestrail.case('C44779')
    def test_popup_of_installer_confirm_during_the_installation(self):
        common.uninstall_old_version_remove_local_app()
        try:
            # Open file Cốc Cốc installer
            common.open_coccoc_installer_by_name(settings.COCCOC_INSTALLER_NAME)
            # Verify popup appears
            from models.pageobject.installs import verify_installer_popup_appears
            verify_installer_popup_appears()
        finally:
            common.cleanup()

    def test_popup_of_installer_confirm_during_the_installation(self):
        common.cleanup()
        # Uninstall old version
        if common.check_if_coccoc_is_installed():
            common.uninstall_coccoc_silently()
        try:
            # Open file Cốc Cốc installer
            common.open_coccoc_installer_by_name(settings.COCCOC_INSTALLER_NAME)
            # Verify popup appears
            from models.pageobject.installs import verify_installer_popup_appears
            verify_installer_popup_appears()
        finally:
            common.cleanup()

    def get_installer(self, driver):
        default_download_folder = common.get_default_download_folder(driver)
        coccoc_installer = self.coccoc_page_obj.get_path_installer_that_download_from_dev(driver,
                                                                                          default_download_folder)
        return coccoc_installer

    def verify_installed_coccoc_version(self):
        # Verify in folder: %LOCALAPPDATA%\CocCoc\Browser\Application\\
        cc_expect_version = "79.0.3945.134"
        # common.login_then_get_latest_coccoc_dev_installer_version()
        assert common.get_coccoc_version_folder_name() in cc_expect_version

        # Verify in coccoc://version
        driver = common.coccoc_instance()
        driver.get(Urls.COCCOC_VERSION_URL)
        assert cc_expect_version in self.version_page_obj.get_flash_path(driver)
        assert cc_expect_version in self.version_page_obj.get_user_agent(driver)
