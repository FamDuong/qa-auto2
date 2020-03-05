import platform

import pytest
from pytest_testrail.plugin import pytestrail
from utils_automation.common import WindowsHandler
from utils_automation.const import Urls
from models.pageobject.settings import SettingsPageObject


windows_handler = WindowsHandler()
settings_page_object = SettingsPageObject()


class TestCcDefaultBrowser:

    @pytestrail.case('C44842')
    def test_check_if_user_see_message_default_browser_currently_cc(self, coccoc_install_instance_on_default_browser):
        coccoc_install_instance_on_default_browser.get(Urls.COCCOC_SETTINGS_DEFAULT)
        assert "Cốc Cốc is your default browser" in settings_page_object.get_text_default_browser_element(
            coccoc_install_instance_on_default_browser)
        try:
            from testscripts.smoketest.common import open_link_from_powershell
            open_link_from_powershell()
            from testscripts.smoketest.common import get_application_process
            assert 'browser' in get_application_process()
        finally:
            from testscripts.smoketest.common import kill_browser_process
            kill_browser_process()

    @pytestrail.case('C44843')
    @pytestrail.defect('BR-1133')
    @pytest.mark.skip(reason="Due to bug BR-1133")
    def test_check_if_user_can_set_cc_default_browser_setting_page(self, coccoc_install_instance_set_not_default_browser):
        coccoc_install_instance_set_not_default_browser.get(Urls.COCCOC_SETTINGS_DEFAULT)
        assert "Make Cốc Cốc the default browser" in settings_page_object.get_text_make_default_browser_element(
            coccoc_install_instance_set_not_default_browser)
        settings_page_object.click_make_default_browser_button(coccoc_install_instance_set_not_default_browser)
        assert "Cốc Cốc is your default browser" in settings_page_object.get_text_default_browser_element(
            coccoc_install_instance_set_not_default_browser)

    @pytestrail.case('C44845')
    @pytestrail.defect('BR-1133')
    @pytest.mark.skip(reason="Due to bug BR-1133")
    def test_set_default_browser_coccoc_then_change_default_browser_to_chrome(self):
        from testscripts.smoketest.conftest import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default()
        from testscripts.smoketest.common import set_chrome_default_browser
        set_chrome_default_browser()
        from testscripts.smoketest.common import coccoc_instance
        driver = coccoc_instance()
        try:
            driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
            assert "Make Cốc Cốc the default browser" in settings_page_object.get_text_make_default_browser_element(driver)
        finally:
            driver.quit()

    @pytestrail.case('C44846')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7"], reason="Cannot execute in Windows 8, Windows 8.1, 7")
    def test_check_if_dialog_coccoc_is_not_your_default_after_1_month(self):
        from testscripts.smoketest.common import check_if_coccoc_is_installed
        if check_if_coccoc_is_installed():
            from testscripts.smoketest.common import uninstall_coccoc_silently
            uninstall_coccoc_silently()
        from testscripts.smoketest.common import install_coccoc_not_set_as_default
        install_coccoc_not_set_as_default()
        driver = None
        try:
            from testscripts.smoketest.common import set_system_date_to_after_30_days
            set_system_date_to_after_30_days()
            from testscripts.smoketest.common import coccoc_instance
            driver = coccoc_instance()
            driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
            assert "Make Cốc Cốc the default browser" in settings_page_object.get_text_make_default_browser_element(driver)
        finally:
            driver.quit()
            from testscripts.smoketest.common import set_system_date_to_before_30_days
            set_system_date_to_before_30_days()










