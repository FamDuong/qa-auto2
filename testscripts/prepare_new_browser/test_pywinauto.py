
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
        cmd_text = self.get_dir_data(browser)
        prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()
        execute = subprocess.Popen(cmd_text, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        coccoc_uninstall = Desktop(backend='uia').Uninstall_Coc_Coc
        coccoc_uninstall.Uninstall.click()
        execute.communicate()

    def test_install_from_cmd(self):
        subprocess.Popen('C:\\CoccocInstaller\\coccoc-en.exe')
        time.sleep(14)
        coccoc_install = Desktop(backend='uia').Cốc_Cốc_Installer
        coccoc_install.Button1.click()
        time.sleep(44)
        prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()

    # # Go to "Programs"
    # app.window(title='Control Panel').ProgramsHyperlink.invoke()
    # app.wait_cpu_usage_lower(threshold=0.5, timeout=30, usage_interval=1.0)
    #
    # # Go to "Uninstall a program"
    # app.window(title='Programs').child_window(title='Uninstall a program', control_type='Hyperlink').invoke()
    # app.wait_cpu_usage_lower(threshold=0.5, timeout=30, usage_interval=1.0)
    # # # this dialog is open in another process (Desktop object doesn't rely on any process id)
    # Properties = Desktop(backend='uia').Programs_and_Features
    # coccoc = Properties.FolderView.get_item('Cốc Cốc')
    # coccoc.click_input(button='right')
    # app.PopupMenu.menu_item('Uninstall').click()
    # Properties.Cancel.click()
    # Properties.wait_not('visible')  # make sure the dialog is closed

    # programs_and_features = app.window(top_level_only=True, active_only=True,
    #                                       title='Programs and Features')
    #
    # app.wait_cpu_usage_lower(threshold=5)

    # item_7z = programs_and_features.FolderView.get_item('Cốc Cốc')
    # item_7z.click_input(button='right', where='icon')
    # app.PopupMenu.menu_item('Uninstall').click()
    #
    # confirmation = app.window(title='Programs and Features', class_name='#32770', active_only=True)
    # if confirmation.Exists():
    #     confirmation.Yes.click_input()
    #     confirmation.wait_not('visible')




    # connect to another process spawned by explorer.exe
    # Note: make sure the script is running as Administrator!


    # app.ProgramFiles.set_focus()
    # common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
    # common_files.right_click_input()
    # app.ContextMenu.Properties.invoke()
    #
    # # this dialog is open in another process (Desktop object doesn't rely on any process id)
    # Properties = Desktop(backend='uia').Common_Files_Properties
    # Properties.print_control_identifiers()
    # Properties.Cancel.click()
    # Properties.wait_not('visible')  # make sure the dialog is closed
    # NewWindow.close()


# def test_uninstall():
#     Application().Start('explorer.exe')
#     explorer = Application().Connect(path='explorer.exe', title='Quick access')
#
#     # Go to "Control Panel -> Programs and Features"
#     NewWindow = explorer.window(top_level_only=True, active_only=True, class_name='CabinetWClass')
#     try:
#         NewWindow.AddressBandRoot.click_input()
#         NewWindow.type_keys(r'Control Panel\Programs\Programs and Features{ENTER}',
#                             with_spaces=True, set_foreground=False)
#         ProgramsAndFeatures = explorer.window(top_level_only=True, active_only=True,
#                                               title='Programs and Features', class_name='CabinetWClass')
#
#         # wait while the list of programs is loading
#         explorer.wait_cpu_usage_lower(threshold=5)
#
#         item_7z = ProgramsAndFeatures.FolderView.get_item('Cốc Cốc')
#         item_7z.ensure_visible()
#         item_7z.click_input(button='right', where='icon')
#         explorer.PopupMenu.menu_item('Uninstall').click()
#
#         Confirmation = explorer.window(title='Programs and Features', class_name='#32770', active_only=True)
#         if Confirmation.Exists():
#             Confirmation.Yes.click_input()
#             Confirmation.wait_not('visible')
#
#         WindowsInstaller = explorer.window(title='Windows Installer', class_name='#32770', active_only=True)
#         if WindowsInstaller.Exists():
#             WindowsInstaller.wait_not('visible', timeout=20)
#
#         SevenZipInstaller = explorer.window(title='Cốc Cốc', class_name='#32770', active_only=True)
#         if SevenZipInstaller.Exists():
#             SevenZipInstaller.wait_not('visible', timeout=20)
#
#         if 'Cốc Cốc' not in ProgramsAndFeatures.FolderView.texts():
#             print('OK')
#     finally:
#         NewWindow.close()
