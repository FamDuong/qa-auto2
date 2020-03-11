from pytest_testrail.plugin import pytestrail
from selenium import webdriver
from models.pageobject.settings import SettingsPageObject


class TestBrowserUpdate:
    settings_page_object = SettingsPageObject()

    def coccoc_instance(self):
        from utils_automation.common import WindowsHandler
        windows_handler = WindowsHandler()
        current_user = windows_handler.get_current_login_user()
        binary_path = f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = binary_path
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    @pytestrail.case('C44855')
    def test_check_update_browser_via_about_us_windows(self, activate_then_deactive_hosts_for_coccoc_dev):
        from testscripts.smoketest.common import install_old_coccoc_version
        import time
        install_old_coccoc_version()
        from utils_automation.const import Urls
        from testscripts.smoketest.common import get_list_coccoc_version_folder_name
        driver = self.coccoc_instance()
        driver.get(Urls.COCCOC_ABOUT)
        element = self.settings_page_object.check_if_relaunch_browser_displayed(driver)
        # Wait for creating new folder for new coccoc version
        time.sleep(5)
        list_coccoc_version = get_list_coccoc_version_folder_name()
        assert len(list_coccoc_version) == 2
        element.click()
        # Wait for relaunching coccoc and delete old coccoc version
        time.sleep(5)
        from testscripts.smoketest.common import cleanup
        cleanup()
        # Wait for browser_cleanup
        time.sleep(5)
        list_coccoc_version = get_list_coccoc_version_folder_name()
        from testscripts.smoketest.common import get_list_files_dirs_in_a_folder
        list_files_folders = get_list_files_dirs_in_a_folder(application_path=
                                                             "\"AppData/Local/CocCoc/Browser/Application\"")
        assert len(list_coccoc_version) == 1
        assert 'browser.exe' in list_files_folders
        assert 'Dictionaries' in list_files_folders
        assert 'SetupMetrics' in list_files_folders
        assert 'VisualElementsManifest' in list_files_folders
        from testscripts.smoketest.common import login_then_get_latest_coccoc_dev_installer_version
        assert list_coccoc_version[0] == login_then_get_latest_coccoc_dev_installer_version()
