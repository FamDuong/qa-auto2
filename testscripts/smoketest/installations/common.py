import time
from pywinauto import Desktop
from utils_automation.common import WindowsHandler, WindowsCMD, find_text_in_file

windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()
coccoc_installer_name = "standalone_coccoc_en.exe"


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


def cleanup():
    # Kill all unncessary task
    WindowsCMD.execute_cmd('taskkill /im CocCocUpdate.exe /f')
    WindowsCMD.execute_cmd('taskkill /im browser.exe /f')
    WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')
    WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')


def install_coccoc_not_set_as_default():
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_for_cococ_installer_appear()
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    time.sleep(5)
    coccoc_installer.Make_Cốc_Cốc_your_default_browserCheckBox.click()
    time.sleep(5)
    coccoc_installer.Button.click()
    time.sleep(1)
    while check_if_coccoc_is_installed() is False:
        time.sleep(2)
    cleanup()


def install_coccoc_set_as_default():
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_for_cococ_installer_appear()
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    time.sleep(5)
    coccoc_installer.Button.click()
    time.sleep(1)
    while check_if_coccoc_is_installed() is False:
        time.sleep(2)
    cleanup()


def install_coccoc_set_system_start_up_on():
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_for_cococ_installer_appear()
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    time.sleep(5)
    coccoc_installer.Run_browser_on_system_start.click()
    time.sleep(5)
    coccoc_installer.Button.click()
    time.sleep(1)
    while check_if_coccoc_is_installed() is False:
        time.sleep(2)


def wait_for_cococ_installer_appear():
    index = 0
    while index == 0:
        time.sleep(1)
        all_windows = Desktop(backend='uia').windows()
        for window in all_windows:
            if "Cốc Cốc Installer" in window.window_text():
                index += 1


def open_link_from_powershell():
    import subprocess
    try:
        subprocess.Popen(["powershell.exe",
                          "taskkill /im browser.exe /f; start https://www.google.com;"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(2)
    except:
        print("Ignore error code")


def get_coccoc_process():
    import subprocess
    processes = None
    try:
        processes = subprocess.Popen(["powershell.exe",
                                      "Get-Process browser"],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except:
        print("Ignore error code")
    return str(processes.communicate()[0])


def get_list_start_up_apps():
    import subprocess
    try:
        p = subprocess.Popen(["powershell.exe",
                              "cd C:\\Script; .\\ShowStartUpApps.ps1"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        response = p.communicate()
        return str(response[0])
    except:
        print("Ignore error code")



def kill_coccoc_process():
    import subprocess
    try:
        subprocess.Popen(["powershell.exe",
                          "taskkill /im browser.exe /f"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except:
        print("Ignore error code")


def set_chrome_default_browser():
    import subprocess
    try:
        p = subprocess.Popen(["powershell.exe",
                              "cd C:\\Script; .\\SetDefaultPrograms.ps1"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.communicate()
    except:
        print("Ignore error code")


def set_system_date_to_after_30_days():
    import subprocess
    subprocess.Popen(["powershell.exe",
                      "cd C:\\Script; .\\setSystemDate_more_30.ps1"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def set_system_date_to_before_30_days():
    import subprocess
    subprocess.Popen(["powershell.exe",
                      "cd C:\\Script; .\\setSystemDate_less_30.ps1"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def kill_power_shell_process():
    import subprocess
    time.sleep(3)
    try:
        p = subprocess.Popen(["powershell.exe",
                              "taskkill /im powershell.exe /f"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print("Ignore error code")


def check_if_auto_launch_enabled_is_true():
    time.sleep(2)
    binary_path = f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
    split_after = binary_path.split('\\Local')
    user_data_local_state = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data\\Local State'
    return find_text_in_file(user_data_local_state, '"autolaunch_enabled":true')


def check_if_auto_launch_enabled_is_false():
    time.sleep(2)
    binary_path = f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
    split_after = binary_path.split('\\Local')
    user_data_local_state = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data\\Local State'
    return find_text_in_file(user_data_local_state, '"autolaunch_enabled":true')
