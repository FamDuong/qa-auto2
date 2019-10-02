from testscripts.prepare_new_browser.test_install import TestInstall
from pytest_testrail.plugin import pytestrail
from utils_automation.const import Urls
from models.pageobject.settings import SettingsPageObject
from models.pageelements.settings import SettingsPageLocators
from utils_automation.common import BrowserHandler, WindowsCMD, wait_for_stable, FilesHandle

class TestFirstRun(TestInstall):
    new_browser = BrowserHandler()
    setting_page_object = SettingsPageObject()
    file = FilesHandle()

    @pytestrail.case('C44830')
    def test_if_widevine_flash_plugin_exist_by_default_right_after_installing_browser(self, browser):
        browser.get(Urls.COCCOC_COMPONENTS)
        self.setting_page_object.verify_text_is_visible_on_page(browser, "Widevine Content Decryption Module")
        self.setting_page_object.verify_text_is_visible_on_page(browser, "Adobe Flash Player")

    @pytestrail.case('C44831')
    def test_task_manager_when_starting_browser(self):
        self.new_browser.browser_cleanup()   # Close all existed browsers
        self.new_browser.browser_init()
        assert WindowsCMD.is_process_exists("browser") is True
        assert WindowsCMD.is_process_exists("CocCocCrashHandler") is True

    @pytestrail.case('C44832')
    def test_extensions_version_after_the_installation(self, browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_DICTIONARY_ID, '1.3.6')
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_SAVIOR_ID, '0.27.3')
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_RUNGRINH_ID, '1.5.0.7', True)
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_MOJICHAT_ID, "0.2.3")

    @pytestrail.case('C44833')
    def test_folders_after_the_installation(self, cc_version):
        assert self.file.is_file_exist_in_app_data('uid') is True
        assert self.file.is_file_exist_in_app_data('hid3') is True
        assert self.file.is_folder_exist_in_local_app_data(r'Browser') is True
        assert self.file.is_folder_exist_in_local_app_data(r'CrashReports') is True
        assert self.file.is_folder_exist_in_local_app_data(r'Update') is True
        assert self.file.is_folder_exist_in_local_app_data(r'Browser\Application') is True
        assert self.file.is_folder_exist_in_local_app_data(r'Browser\User Data') is True
        assert self.file.is_folder_exist_in_local_app_data(r'Browser\Application\\' + cc_version) is True
        assert self.file.is_folder_exist_in_local_app_data(r'Browser\Application\Dictionaries') is True
        assert self.file.is_folder_exist_in_local_app_data(r'Browser\Application\SetupMetrics') is True
        assert self.file.is_file_exist_in_local_app_data(r'Browser\Application\browser.exe') is True
        assert self.file.is_file_exist_in_local_app_data(r'Browser\Application\browser_proxy.exe') is True
        assert self.file.is_file_exist_in_local_app_data(r'Browser\Application\VisualElementsManifest.xml') is True

