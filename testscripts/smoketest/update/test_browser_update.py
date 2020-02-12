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
    def test_check_update_browser_via_about_us_windows(self):
        from testscripts.smoketest.common import install_old_coccoc_version
        install_old_coccoc_version()
        from utils_automation.const import Urls
        from testscripts.smoketest.common import get_list_coccoc_version_folder_name
        driver = self.coccoc_instance()
        driver.get(Urls.COCCOC_ABOUT)
        element = self.settings_page_object.check_if_relaunch_browser_displayed(driver)
        list_coccoc_version = get_list_coccoc_version_folder_name()
        assert len(list_coccoc_version) == 2
        element.click()
        import time
        time.sleep(5)
        from testscripts.smoketest.common import cleanup
        cleanup()
        time.sleep(5)
        list_coccoc_version = get_list_coccoc_version_folder_name()
        from testscripts.smoketest.common import get_list_files_dirs_in_coccoc_application_folder
        list_files_folders = get_list_files_dirs_in_coccoc_application_folder()
        assert len(list_coccoc_version) == 1
        assert 'browser.exe' in list_files_folders
        assert 'Dictionaries' in list_files_folders
        assert 'SetupMetrics' in list_files_folders
        assert 'VisualElementsManifest' in list_files_folders
