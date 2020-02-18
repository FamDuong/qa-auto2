from pytest_testrail.plugin import pytestrail
import testscripts.smoketest.common as common
from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.version import VersionPageObject
import settings_master as settings
from utils_automation.const import Urls


class TestFreshInstall:
    version_page_object = VersionPageObject()
    coccoc_page_object = CocCocPageObjects()

    # Precondition: Machine is installed Coc Coc
    @pytestrail.case('C44777')
    def test_install_latest_version_from_dev(self, activate_then_deactive_hosts_for_coccoc_dev):
        download_file_path = self.get_downloaded_coccoc_installer_path()
        self.uninstall_old_version_and_remove_local_app_data()
        common.open_coccoc_installer_from_path(download_file_path)
        self.verify_installed_coccoc_version()

    @pytestrail.case('C44779')
    def test_popup_of_installer_confirm_during_the_installation(self):
        common.cleanup()
        # Uninstall old version
        if common.check_if_coccoc_is_installed():
            common.uninstall_coccoc_silently()
        try:
            # Open file Cốc Cốc installer
            common.open_coccoc_installer(settings.COCCOC_INSTALLER_NAME)
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
            common.open_coccoc_installer(settings.COCCOC_INSTALLER_NAME)
            # Verify popup appears
            from models.pageobject.installs import verify_installer_popup_appears
            verify_installer_popup_appears()
        finally:
            common.cleanup()

    def get_downloaded_coccoc_installer_path(self):
        common.cleanup()
        # Download latest version on https://dev.coccoc.com/
        driver = common.coccoc_instance()
        current_download_folder = common.get_current_download_folder(driver)
        download_file = self.coccoc_page_object.get_path_of_downloaded_coccoc_installer_from_dev(driver,
                                                                                                 current_download_folder)
        return download_file

    def uninstall_old_version_and_remove_local_app_data(self):
        common.uninstall_coccoc_silently()
        common.remove_local_app_data()

    def verify_installed_coccoc_version(self):
        # Verify in folder: %LOCALAPPDATA%\CocCoc\Browser\Application\\
        cc_expect_version = common.login_then_get_latest_coccoc_dev_installer_version()
        assert common.get_coccoc_version_folder_name() in cc_expect_version

        # Verify in coccoc://version
        driver = common.coccoc_instance()
        driver.get(Urls.COCCOC_VERSION_URL)
        assert cc_expect_version in self.version_page_object.get_flash_path(driver)
        assert cc_expect_version in self.version_page_object.get_user_agent(driver)
