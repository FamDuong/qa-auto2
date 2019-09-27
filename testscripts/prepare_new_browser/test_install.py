
import subprocess
import time
from models.pagelocators.settings import SettingsPageLocators
from pytest_testrail.plugin import pytestrail
from utils_automation.common import BrowserHandler

from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.settings import SettingsPageObject
from os import path
from pywinauto import Desktop, timings
from pywinauto.application import Application
from utils_automation.common import wait_for_stable

from models.pageobject.version import VersionPageObject
from utils_automation.const import Urls
from utils_automation.common import WindowsCMD

class TestInstall:
    version_page_object = VersionPageObject()
    coccoc_page_object = CocCocPageObjects()
    download_page_object = DownloadsPageObject()
    setting_page_object = SettingsPageObject()

    def get_dir_data(self, browser):
        browser.get(Urls.COCCOC_VERSION_URL)
        text = self.version_page_object.get_flash_path(browser)
        split1 = text.split('C:\\Users\\')
        split2 = split1[1].split('\\PepperFlash')
        value = u'C:\\Users\\' + split2[0] + u'\\Installer\\setup.exe --uninstall'
        return value

    def remove_local_app_data(self):
        localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc')
        appdata = path.expandvars(r'%APPDATA%\CocCoc')
        # Temporary do not download delete
        cmdCommand = 'rmdir /q /s ' + localappdata  # specify your cmd command
        WindowsCMD.execute_cmd(cmdCommand)
        cmdCommand = 'rmdir /q /s ' + appdata  # specify your cmd command
        WindowsCMD.execute_cmd(cmdCommand)
        cmdCommand = 'reg delete HKEY_CURRENT_USER\\Software\\CocCoc /f'
        WindowsCMD.execute_cmd(cmdCommand)

    def cleanup(self):
        # Kill all unncessary task
        WindowsCMD.execute_cmd('taskkill /im CocCocUpdate.exe /f')
        WindowsCMD.execute_cmd('taskkill /im browser.exe /f')
        WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')
        WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')

    def test_uninstall_from_cmd(self, browser, rm_user_data):
        try:
            cmd_text = self.get_dir_data(browser)
            prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            prog.communicate()
            execute = subprocess.Popen(cmd_text, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            coccoc_uninstall = Desktop(backend='uia').Uninstall_Coc_Coc
            coccoc_uninstall.Uninstall.click()
            execute.communicate()
            if rm_user_data is not None:
                self.remove_local_app_data()
        except:
            print("Uninstall not success!!!")

    def test_install_from_cmd(self, install_file):
        try:
            wait_for_stable
            subprocess.Popen(install_file)
            time.sleep(14)
            coccoc_install = Desktop(backend='uia').Cốc_Cốc_Installer
            coccoc_install.Button1.click()
            time.sleep(40)
            self.cleanup()
        except:
            print("Install unsuccessfully!!!")

    def test_silent_install_from_cmd(self, install_file, option = None):
        try:
            wait_for_stable
            subprocess.Popen(install_file + ' /silent /forcedcmdline "' + option + '" /install')
            time.sleep(40)
            self.cleanup()
        except:
            print("Install unsuccessfully!!!")

    @pytestrail.case('C44777')
    def test_install_latest_version_from_dev(self, browser, get_current_download_folder, cc_version, rm_user_data):
        # Please make sure to add hosts to C:\Windows\System32\drivers\etc\hosts
        # Restriction: Cannot add hosts by script because of administration permission
        # Download latest version
        download_file = self.coccoc_page_object.download_coccoc_from_dev(browser, get_current_download_folder)
        # Uninstall old version
        self.test_uninstall_from_cmd(browser, rm_user_data)
        # Install downloaded version
        self.test_install_from_cmd(download_file)
        self.version_page_object.verify_version_is_correct(cc_version)

class TestOverrideInstall(TestInstall):
    @pytestrail.case('C44773')
    def test_check_install_new_version_above_old_version(self, browser, get_current_download_folder, cc_version,
                                                         rm_user_data = "Yes"):
        # Precondition: Download latest file
        # Download latest version
        download_file = self.coccoc_page_object.download_coccoc_from_dev(browser, get_current_download_folder)
        # Uninstall old version
        self.test_uninstall_from_cmd(browser, rm_user_data)
        # Install old version version
        self.test_install_from_cmd("C:\CoccocInstaller\coccoc-en.exe")
        self.version_page_object.verify_version_is_correct("75.0.3770.152")
        # Install latest version version
        self.test_install_from_cmd(download_file)
        self.version_page_object.verify_version_is_correct(cc_version)

    @pytestrail.case('C44777')
    def test_check_installing_fresh_package_successfully_on_windows(self, browser, get_current_download_folder, cc_version, rm_user_data = "Yes"):
        # Please make sure to add hosts to C:\Windows\System32\drivers\etc\hosts
        # Restriction: Cannot add hosts by script because of administration permission
        # Download latest version
        download_file = self.coccoc_page_object.download_coccoc_from_dev(browser, get_current_download_folder)
        # Uninstall old version
        self.test_uninstall_from_cmd(browser, rm_user_data)
        # Install downloaded version
        self.test_install_from_cmd(download_file)
        self.version_page_object.verify_version_is_correct(cc_version)

class TestSilentInstall(TestInstall):
    new_browser = BrowserHandler()

    @pytestrail.case('C44785')
    def test_check_with_make_coccoc_default(self, browser, get_current_download_folder, cc_version, rm_user_data):
        download_file = self.coccoc_page_object.download_coccoc_from_dev(browser, get_current_download_folder)  # Download latest version
        self.test_uninstall_from_cmd(browser, rm_user_data)   # Uninstall old version
        self.test_silent_install_from_cmd(download_file, 'make-coccoc-default')  # Install downloaded version
        self.version_page_object.verify_version_is_correct(cc_version)
        browser = self.new_browser.browser_init()
        self.setting_page_object.verify_setting_on_startup(browser, SettingsPageLocators.OPEN_NEW_TAB_PAGE_TEXT)

    @pytestrail.case('C44786')
    def test_check_with_auto_launch_coccoc(self, browser, get_current_download_folder, cc_version, rm_user_data):
        download_file = self.coccoc_page_object.download_coccoc_from_dev(browser, get_current_download_folder)  # Download latest version
        self.test_uninstall_from_cmd(browser, rm_user_data)  # Uninstall old version
        self.test_silent_install_from_cmd(download_file, 'auto-launch-coccoc')  # Install downloaded version
        self.version_page_object.verify_version_is_correct(cc_version)
        browser = self.new_browser.browser_init()
        self.setting_page_object.verify_setting_default_browser(browser, SettingsPageLocators.DEFAULT_BROWSER_RUN_AUTO_ONSTARTUP_CHECKBOX)




def test_uninstall():
    Application().start('control.exe')
    app = Application(backend='uia').connect(path='explorer.exe', title='Control Panel')

    # Go to "Programs"
    app.window(title='Control Panel').ProgramsHyperlink.invoke()
    app.wait_cpu_usage_lower(threshold=0.5, timeout=30, usage_interval=1.0)

    # Go to "Uninstall a program"
    app.window(title='Programs').child_window(title='Uninstall a program', control_type='Hyperlink').invoke()
    app.wait_cpu_usage_lower(threshold=0.5, timeout=30, usage_interval=1.0)
    # # this dialog is open in another process (Desktop object doesn't rely on any process id)
    Properties = Desktop(backend='uia').Programs_and_Features
    coccoc = Properties.FolderView.get_item('Cốc Cốc')
    coccoc.click_input(button='right')
    app.top_window().Menu.item_by_path('Uninstall')[0].click_input()  # This one caused the error
