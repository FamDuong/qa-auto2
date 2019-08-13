
import subprocess
import sys
import time

from pywinauto import Desktop, timings
from pywinauto.application import Application

from models.pageobject.version import VersionPageObject
from utils_automation.const import Urls


class TestWinAuto:
    version_page_object = VersionPageObject()

    def get_dir_data(self, browser):
        browser.get(Urls.COCCOC_VERSION_URL)
        text = self.version_page_object.get_flash_path(browser)
        split1 = text.split('C:\\Users\\')
        split2 = split1[1].split('\\PepperFlash')
        value = u'C:\\Users\\' + split2[0] + u'\\Installer\\setup.exe --uninstall'
        return value

    def test_uninstall_from_cmd(self, browser):
        try:
            cmd_text = self.get_dir_data(browser)
            prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            prog.communicate()
            execute = subprocess.Popen(cmd_text, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            coccoc_uninstall = Desktop(backend='uia').Uninstall_Coc_Coc
            coccoc_uninstall.Uninstall.click()
            execute.communicate()
        except:
            pass

    def test_install_from_cmd(self):
        subprocess.Popen('C:\\CoccocInstaller\\coccoc-en.exe')
        time.sleep(14)
        coccoc_install = Desktop(backend='uia').Cốc_Cốc_Installer
        coccoc_install.Button1.click()
        time.sleep(44)
        prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()


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
