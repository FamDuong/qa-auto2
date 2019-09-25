
import subprocess
import time
import os

from models.pageobject.coccocpage import CocCocPageObjects
from models.pageobject.downloads import DownloadsPageObject
from os import path
from pywinauto import Desktop, timings
from pywinauto.application import Application
from utils_automation.common import wait_for_stable

from models.pageobject.version import VersionPageObject
from utils_automation.const import Urls
from utils_automation.common import WindowsCMD

class TestWinAuto:
    version_page_object = VersionPageObject()
    coccoc_page_object = CocCocPageObjects()
    download_page_object = DownloadsPageObject()

    def get_dir_data(self, browser):
        browser.get(Urls.COCCOC_VERSION_URL)
        text = self.version_page_object.get_flash_path(browser)
        split1 = text.split('C:\\Users\\')
        split2 = split1[1].split('\\PepperFlash')
        value = u'C:\\Users\\' + split2[0] + u'\\Installer\\setup.exe --uninstall'
        return value

    def test_install_latest_version_from_dev(self, browser, get_current_download_folder, cc_version):
        # Please make sure to add hosts to C:\Windows\System32\drivers\etc\hosts
        # Restriction: Cannot add hosts by script because of administration permission
        # Download latest version
        download_file = self.coccoc_page_object.download_coccoc_from_dev(browser, get_current_download_folder)
        # Uninstall old version
        self.test_uninstall_from_cmd(browser)
        # Install downloaded version
        self.test_install_from_cmd(download_file)
        self.version_page_object.verify_version_is_correct(cc_version)

    def remove_local_app_data(self):
        localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc')
        appdata = path.expandvars(r'%APPDATA%\CocCoc')
        cmdCommand = 'rmdir /q /s ' + localappdata  # specify your cmd command
        WindowsCMD.execute_cmd(cmdCommand)
        cmdCommand = 'rmdir /q /s ' + appdata  # specify your cmd command
        WindowsCMD.execute_cmd(cmdCommand)
        cmdCommand = 'reg delete HKEY_CURRENT_USER\\Software\\CocCoc /f'
        WindowsCMD.execute_cmd(cmdCommand)

    def test_uninstall_from_cmd(self, browser):
        try:
            cmd_text = self.get_dir_data(browser)
            prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            prog.communicate()
            execute = subprocess.Popen(cmd_text, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            coccoc_uninstall = Desktop(backend='uia').Uninstall_Coc_Coc
            coccoc_uninstall.Uninstall.click()
            execute.communicate()
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
            time.sleep(60)
            WindowsCMD.execute_cmd('taskkill /im CocCocUpdate.exe /f')
        finally:
            print("Finish installing!!!")

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
