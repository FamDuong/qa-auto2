import platform

import pytest
from pytest_testrail.plugin import pytestrail
from models.pageobject.settings import SettingsPageObject


settings_page_object = SettingsPageObject()


class TestCocCocAutomaticallySystemStartup:

    @pytestrail.case('C44850')
    @pytest.mark.skipif(platform.release() in ["7"], reason="Cannot execute in Win7 cuz does not have Get-Cim command in powershell")
    def test_check_autorun_with_system_option_set_off_installer_dialog(self, install_default_coccoc_unsilently):
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        try:
            from testscripts.smoketest.common import get_list_start_up_apps
            assert 'browser.exe' not in get_list_start_up_apps()
        finally:
            from testscripts.smoketest.common import kill_browser_process
            kill_browser_process()

    @pytestrail.case('C44851')
    @pytest.mark.skipif(platform.release() in ["7"], reason="Cannot execute in Win7 cuz does not have Get-Cim command in powershell")
    def test_check_autorun_with_system_option_set_on_installer_dialog(self, install_set_system_option_on):
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        try:
            from testscripts.smoketest.common import get_list_start_up_apps
            assert 'browser' in get_list_start_up_apps()
        finally:
            from testscripts.smoketest.common import kill_browser_process
            kill_browser_process()






















