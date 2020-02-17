from pytest_testrail.plugin import pytestrail

from models.pageobject.settings import SettingsPageObject


class TestSilentInstall:
    settings_page_object = SettingsPageObject()

    @pytestrail.case('C44785')
    def test_check_with_make_coccoc_default(self):
        from testscripts.smoketest.common import uninstall_then_install_coccoc_silentlty_with_option
        uninstall_then_install_coccoc_silentlty_with_option("/forcedcmdline 'make-coccoc-default'")
        from testscripts.smoketest.common import coccoc_instance
        driver = coccoc_instance()
        try:
            from utils_automation.const import Urls
            driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
            assert "is your default browser. Yay!" in self.settings_page_object.get_text_cococ_is_default_browser_element(
                driver)
        finally:
            driver.quit()

    @pytestrail.case('C44786')
    def test_check_with_auto_launch_coccoc(self):
        from testscripts.smoketest.common import uninstall_then_install_coccoc_silentlty_with_option
        uninstall_then_install_coccoc_silentlty_with_option("/forcedcmdline 'auto-launch-coccoc'")
        from testscripts.smoketest.common import get_list_start_up_apps
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        assert 'browser.exe' in get_list_start_up_apps()

    @pytestrail.case('C44787')
    def test_check_with_do_not_launch_chrome(self):
        from testscripts.smoketest.common import \
            uninstall_then_install_coccoc_silentlty_with_option_without_kill_process
        uninstall_then_install_coccoc_silentlty_with_option_without_kill_process("/forcedcmdline 'do-not-launch-chrome'")
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        from testscripts.smoketest.common import get_coccoc_process
        assert 'browser' not in get_coccoc_process()

    @pytestrail.case('C44788')
    def test_check_combination_some_parameters(self):
        from testscripts.smoketest.common import \
            uninstall_then_install_coccoc_silentlty_with_option_without_kill_process
        uninstall_then_install_coccoc_silentlty_with_option_without_kill_process(
            "/forcedcmdline 'do-not-launch-chrome --make-coccoc-default --auto-launch-coccoc'")
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        from testscripts.smoketest.common import get_coccoc_process
        assert 'browser' not in get_coccoc_process()
        from testscripts.smoketest.common import get_list_start_up_apps
        assert 'browser.exe' in get_list_start_up_apps()
        from testscripts.smoketest.common import coccoc_instance
        driver = coccoc_instance()
        try:
            from utils_automation.const import Urls
            driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
            assert "is your default browser. Yay!" in self.settings_page_object.get_text_cococ_is_default_browser_element(
                driver)
        finally:
            driver.quit()











