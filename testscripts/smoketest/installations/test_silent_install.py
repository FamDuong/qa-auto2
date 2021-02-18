import logging

from pytest_testrail.plugin import pytestrail
from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.settings import SettingsPageObject
from testscripts.smoketest.common import get_browser_and_default_download_folder, delete_installer_download

LOGGER = logging.getLogger(__name__)

class TestSilentInstall:
    settings_page_object = SettingsPageObject()
    coccoc_page_obj = CocCocPageObjects()

    @pytestrail.case('C44785')
    def test_check_with_make_coccoc_default(self, is_active_host, url):
        browser, default_download_folder, is_activated_host = get_browser_and_default_download_folder(is_active_host)
        delete_installer_download(default_download_folder, language='', installer_name='CocCocSetup', extension='.exe')
        coccoc_installer_temp = self.coccoc_page_obj.get_path_installer(browser, url, default_download_folder, os='win',
                                                                        language='en')
        coccoc_installer = coccoc_installer_temp.replace('/CocCocSetup.exe', '\\')
        LOGGER.info("Silent install by installer from "+coccoc_installer)
        from testscripts.smoketest.common import uninstall_then_install_coccoc_silentlty_with_option
        uninstall_then_install_coccoc_silentlty_with_option(installer_path=coccoc_installer,
                                                            coccoc_installer_name='CocCocSetup.exe',
                                                            cmd_options="/forcedcmdline 'make-coccoc-default'")
        from utils_automation.common_browser import coccoc_instance
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
        assert 'AppData\\\\Local\\\\CocCoc\\\\Browser\\\\Application\\\\browser.exe" --auto-launch-at-startup' in get_list_start_up_apps()
        assert 'AppData\\\\Local\\\\CocCoc\\\\Update\\\\CocCocUpdate.exe' in get_list_start_up_apps()

    @pytestrail.case('C44787')
    def test_check_with_do_not_launch_chrome(self):
        from testscripts.smoketest.common import \
            uninstall_then_install_coccoc_silentlty_with_option_without_kill_process
        uninstall_then_install_coccoc_silentlty_with_option_without_kill_process(
            "/forcedcmdline 'do-not-launch-chrome'")
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        from testscripts.smoketest.common import get_application_process
        assert 'browser' not in get_application_process()

    @pytestrail.case('C44788')
    def test_check_combination_some_parameters(self):
        from testscripts.smoketest.common import \
            uninstall_then_install_coccoc_silentlty_with_option_without_kill_process
        uninstall_then_install_coccoc_silentlty_with_option_without_kill_process(
            "/forcedcmdline 'do-not-launch-chrome --make-coccoc-default --auto-launch-coccoc'")
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        from testscripts.smoketest.common import get_application_process
        assert 'browser' not in get_application_process()
        from testscripts.smoketest.common import get_list_start_up_apps
        assert 'browser' in get_list_start_up_apps()
        from utils_automation.common_browser import coccoc_instance
        driver = coccoc_instance()
        try:
            from utils_automation.const import Urls
            driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
            assert "is your default browser. Yay!" in self.settings_page_object.get_text_cococ_is_default_browser_element(
                driver)
        finally:
            driver.quit()
