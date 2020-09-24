from testscripts.prepare_new_browser.test_install import TestInstall
from pytest_testrail.plugin import pytestrail
from utils_automation.const import Urls
from models.pageobject.settings import SettingsPageObject
from models.pageelements.settings import SettingsPageLocators
from utils_automation.common import BrowserHandler, WindowsCMD, wait_for_stable, FilesHandle, WindowsHandler
from utils_automation.common_browser import cleanup, coccoc_instance


class TestFirstRun(TestInstall):

    new_browser = BrowserHandler()
    setting_page_object = SettingsPageObject()
    windows = WindowsHandler()
    file = FilesHandle()

    @pytestrail.case('C44830')
    def test_if_widevine_flash_plugin_exist_by_default_right_after_installing_browser(self, browser):
        browser.get(Urls.COCCOC_COMPONENTS)
        self.setting_page_object.verify_text_is_visible_on_page(browser, "Widevine Content Decryption Module")
        self.setting_page_object.verify_text_is_visible_on_page(browser, "Adobe Flash Player")

    @pytestrail.case('C44831')
    def test_task_manager_when_starting_browser(self):
        cleanup()   # Close all existed browsers
        coccoc_instance()
        assert WindowsCMD.is_process_exists("browser") is True
        assert WindowsCMD.is_process_exists("CocCocCrashHandler") is True

    @pytestrail.case('C44832')
    def test_extensions_version_after_the_installation(self, browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_DICTIONARY_ID, '1.3.6')
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_SAVIOR_ID, '0.27.3')
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_RUNGRINH_ID, '1.5.0.8', True)
        # self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_MOJICHAT_ID, "0.2.3")

    @pytestrail.case('C44833')
    def test_folders_after_the_installation(self, cc_version):
        assert self.file.is_file_exist_in_folder('uid', self.file.appdata) is True
        assert self.file.is_file_exist_in_folder('hid3', self.file.appdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser', self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'CrashReports', self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Update', self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application', self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\User Data', self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\\' + cc_version, self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\Dictionaries', self.file.localappdata) is True
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\SetupMetrics', self.file.localappdata) is True
        assert self.file.is_file_exist_in_folder(r'Browser\Application\browser.exe', self.file.localappdata) is True
        assert self.file.is_file_exist_in_folder(r'Browser\Application\browser_proxy.exe', self.file.localappdata) is True
        assert self.file.is_file_exist_in_folder(r'Browser\Application\VisualElementsManifest.xml', self.file.localappdata) is True

    @pytestrail.case('C44834')
    def test_where_data_file_of_dictionaries_extension_is_saved(self, cc_version):
        assert self.file.is_subfolder_exist_in_folder(r'Browser\Application\\' + cc_version + r'\Dictionaries', self.file.localappdata) is True

    @pytestrail.case('C44837')
    def test_browser_version_and_omaha_client_version_after_the_installation(self, ohama_version, cc_version):
        self.file.verify_product_version(self.file.localappdata + r'Browser\Application\browser.exe', cc_version)
        self.file.verify_product_version(self.file.localappdata + r'Update\\' + ohama_version + r'\CocCocUpdate.exe', ohama_version)

    @pytestrail.case('C44838')
    def test_the_company_signature_in_file_exe_and_dll(self):
        # signatures = self.file.get_signature_of_files_in_folder('.exe', self.file.localappdata)
        # for signature in signatures:
        #     assert "COC COC COMPANY LIMITED" in signature
        signatures = self.file.get_signature_of_files_in_folder('.dll', self.file.localappdata)
        index = 0
        for signature in signatures:
            index += 1
            print(f" {index} Signature is : {signature} \n")
        #     assert "COC COC COMPANY LIMITED" in signature

    @pytestrail.case('C44840')
    def test__rule_in_firewall_of_windows_if_user_selects_allow_access_btn(self):
        # Note: Default when setting, user always select "Allow access" button
        # Inbound
        self.windows.verify_netfirewall_rule('Cốc Cốc (mDNS-In)', 'Inbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc (TCP-In)', 'Inbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc (UDP-In)', 'Inbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (TCP-In)', 'Inbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (UDP-In)', 'Inbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc (TCP-Out)', 'Outbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc (UDP-Out)', 'Outbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (TCP-Out)', 'Outbound', 'Allow')
        self.windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (UDP-Out)', 'Outbound', 'Allow')
