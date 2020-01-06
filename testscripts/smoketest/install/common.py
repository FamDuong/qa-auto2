import time

from pywinauto import Desktop

from testscripts.prepare_new_browser.test_install import TestInstall
from utils_automation.common import WindowsHandler


windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()
coccoc_installer_name = "standalone_coccoc_en.exe"
test_install = TestInstall()


def check_if_coccoc_is_installed():
    file_name = 'browser.exe'

    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"Get-ChildItem -Path C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application -Filter {file_name} -Recurse " + "| %{$_.FullName}"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.communicate()[0]
    if file_name in str(result):
        return True
    else:
        return False


def uninstall_coccoc_silently():
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application"
                          f"\\{get_coccoc_version_folder_name()}"
                          f"\\Installer; .\\setup.exe --uninstall --force-uninstall"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def get_coccoc_version_folder_name():
    import subprocess
    import re
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application; ls"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    current_dir = str(p.communicate()[0])
    coccoc_version = re.findall(r'\b\d+\.+\b\d+\.\b\d+\.+\d*', current_dir)[0]
    return coccoc_version


def move_to_coccoc_installer_dir():
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application"
                          f"\\{get_coccoc_version_folder_name()}"
                          f"\\Installer; ls"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def get_list_coccoc_installer_dirs(folders_list):
    coccoc_download_folder_list = []
    for each_folder in folders_list:
        import re
        if re.match(r'\b\d+\.+\b\d+\.\b\d+\.+\d*', each_folder):
            coccoc_download_folder_list.append(each_folder)
    return coccoc_download_folder_list


def download_latest_coccoc_dev_installer():
    from ftplib import FTP
    with FTP('browser3v.dev.itim.vn') as ftp:
        ftp.login('anonymous', '')
        ftp.cwd('corom')
        folders_list = ftp.nlst()
        coccoc_download_folder_list = get_list_coccoc_installer_dirs(folders_list)
        latest_coccoc_download_dir = coccoc_download_folder_list[-1]
        ftp.cwd(f"{latest_coccoc_download_dir}/installers")
        try:
            ftp.retrbinary("RETR " + coccoc_installer_name,
                           open(f"C:\\coccoc-dev\\{coccoc_installer_name}", 'wb').write)
        except:
            print(f"Error download coccoc binary for {coccoc_installer_name}")


def install_coccoc_silently():
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\coccoc-dev; .\\{coccoc_installer_name} /silent /install"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def install_coccoc_not_set_as_default():
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    index = 0
    while index == 0:
        time.sleep(1)
        all_windows = Desktop(backend='uia').windows()
        for window in all_windows:
            if "Cốc Cốc Installer" in window.window_text():
                index += 1
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    print(coccoc_installer)
    time.sleep(1)
    coccoc_installer.Make_Cốc_Cốc_your_default_browserCheckBox.click()
    time.sleep(1)
    coccoc_installer.Button.click()
    time.sleep(1)
    while check_if_coccoc_is_installed() is False:
        time.sleep(2)
    test_install.cleanup()




