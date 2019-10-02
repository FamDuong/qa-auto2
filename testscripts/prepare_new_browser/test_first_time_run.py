from os import path
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
        appdata = path.expandvars(r'%APPDATA%\CocCoc\\')
        localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc\\')
        assert self.file.is_file_exist_in_folder('uid', appdata) is True
        assert self.file.is_file_exist_in_folder('hid3', appdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser', localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'CrashReports', localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Update', localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application', localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\User Data', localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\\' + cc_version, localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\Dictionaries', localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\SetupMetrics', localappdata) is True
        assert self.file.is_file_exist_in_folder(r'Browser\Application\browser.exe', localappdata) is True
        assert self.file.is_file_exist_in_folder(r'Browser\Application\browser_proxy.exe', localappdata) is True
        assert self.file.is_file_exist_in_folder(r'Browser\Application\VisualElementsManifest.xml', localappdata) is True

    @pytestrail.case('C44834')
    def test_where_data_file_of_dictionaries_extension_is_saved(self, cc_version):
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\\' + cc_version + r'\Dictionaries', path.expandvars(r'%LOCALAPPDATA%\CocCoc\\')) is True

    @pytestrail.case('C44838')
    def test_the_company_signature_in_file_exe_and_dll(self):
        signatures = self.file.get_signature_of_files_in_folder('.exe', path.expandvars(r'%LOCALAPPDATA%\CocCoc\\'))
        for i in range(len(signatures)):
            print(signatures[i])
            assert "COC COC COMPANY LIMITED" in str(signatures[i])
        signatures = self.file.get_signature_of_files_in_folder('.dll', path.expandvars(r'%LOCALAPPDATA%\CocCoc\\'))
        for i in range(len(signatures)):
            print(signatures[i])
            assert "COC COC COMPANY LIMITED" in str(signatures[i])

