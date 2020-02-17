from pytest_testrail.plugin import pytestrail
import testscripts.smoketest.common as common
from models.pageobject.version import VersionPageObject
import settings_master as settings


class TestFreshInstall:
    version_page_object = VersionPageObject()

    @pytestrail.case('C44777')
    def test_install_latest_version_from_dev(self):
        try:
            # Uninstall old version
            if common.check_if_coccoc_is_installed():
                common.uninstall_coccoc_silently()
            # Install downloaded version
            common.install_coccoc_set_as_default()
            # Verify Cốc Cốc version
            cc_version = common.login_then_get_latest_coccoc_dev_installer_version()
            self.version_page_object.verify_version_is_correct(cc_version)
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup()
            common.uninstall_coccoc_silently()

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