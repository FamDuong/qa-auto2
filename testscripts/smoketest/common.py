import datetime
import time
from pywinauto import Desktop
from selenium import webdriver

from utils_automation.common import WindowsHandler, WindowsCMD, find_text_in_file, modify_file_as_text, get_current_dir

windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()
powershell_script_path = "\\resources\\powershell_scripts"
ftp_domain = "browser3v.dev.itim.vn"
ftp_username = "anonymous"
ftp_password = ""
ftp_child_folder = "corom"


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
    time.sleep(5)


def uninstall_coccoc_and_delete_user_data():
    import subprocess
    subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application"
                          f"\\{get_coccoc_version_folder_name()}"
                          f"\\Installer; .\\setup.exe --uninstall"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    coccoc_uninstaller = Desktop(backend='uia').Uninstall
    time.sleep(4)
    coccoc_uninstaller.Also_delete_your_browsing_data.click()
    time.sleep(2)
    coccoc_uninstaller.Uninstall.click()
    time.sleep(1)


def get_coccoc_version_folder_name():
    import subprocess
    import re
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application; ls"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    current_dir = str(p.communicate()[0])
    coccoc_version = re.findall(r'\b\d+\.+\b\d+\.\b\d+\.+\d*', current_dir)[0]
    return coccoc_version


def get_list_coccoc_version_folder_name():
    import subprocess
    import re
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application; ls"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    current_dir = str(p.communicate()[0])
    coccoc_version = re.findall(r'\b\d+\.+\b\d+\.\b\d+\.+\d*', current_dir)
    return coccoc_version


def get_list_files_dirs_in_a_folder(application_path=None):
    import subprocess
    print(current_user)
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\{application_path}; ls"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    current_dir = str(p.communicate()[0])
    return current_dir


def move_to_coccoc_installer_dir():
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application"
                          f"\\{get_coccoc_version_folder_name()}"
                          f"\\Installer"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def sorted_list_directories(folders_list):
    from packaging import version
    list_coccoc_folders = get_list_coccoc_installer_dirs(folders_list)
    new_list = []
    for each_folder in list_coccoc_folders:
        import re
        split_item = re.match(rf'\b\d+\.', each_folder)
        integer_split_item = int(str(split_item).split("match='")[1].split('.')[0])
        if integer_split_item not in new_list:
            new_list.append(integer_split_item)
    new_list.sort()
    biggest_number = new_list[-1]
    new_list_2 = []
    new_list_biggest_number = []
    for each_folder in list_coccoc_folders:
        import re
        split_item = re.match(rf'{biggest_number}\.\b\d+\.', each_folder)
        if split_item is not None:
            integer_split_item = int(str(split_item).split("match='")[1].split('.')[1].split('.')[0])
            new_list_biggest_number.append(integer_split_item)
            new_list_2.append(each_folder)
    new_list_biggest_number.sort()
    list_coccoc_folders = new_list_2
    sorted_list = sorted(list_coccoc_folders, key=lambda x: version.Version(x))
    return sorted_list


def get_list_coccoc_installer_dirs(folders_list):
    coccoc_download_folder_list = []
    for each_folder in folders_list:
        import re
        if re.match(r'\b\d+\.+\b\d+\.\b\d+\.+\d*', each_folder):
            coccoc_download_folder_list.append(each_folder)
    return coccoc_download_folder_list


def get_latest_coccoc_dev_installer_version(ftp):
    ftp.cwd(ftp_child_folder)
    folders_list = ftp.nlst()
    coccoc_download_folder_list = get_list_coccoc_installer_dirs(folders_list)
    sorted_list_directory = sorted_list_directories(coccoc_download_folder_list)
    latest_coccoc_download_dir = sorted_list_directory[-1]
    return latest_coccoc_download_dir


def login_then_get_latest_coccoc_dev_installer_version():
    from ftplib import FTP
    latest_coccoc_download_dir = None
    with FTP(ftp_domain) as ftp:
        ftp.login(ftp_username, ftp_password)
        latest_coccoc_download_dir = get_latest_coccoc_dev_installer_version(ftp)
    return latest_coccoc_download_dir


def login_then_download_latest_coccoc_dev_installer(coccoc_installer_name='standalone_coccoc_en.exe'):
    from ftplib import FTP
    with FTP(ftp_domain) as ftp:
        ftp.login(ftp_username, ftp_password)
        latest_coccoc_download_dir = get_latest_coccoc_dev_installer_version(ftp)
        ftp.cwd(f"{latest_coccoc_download_dir}/installers")
        try:
            ftp.retrbinary("RETR " + coccoc_installer_name,
                           open(f"C:\\coccoc-dev\\{coccoc_installer_name}", 'wb').write)
        except:
            print(f"Error download coccoc binary for {coccoc_installer_name}")


def install_coccoc_silently(coccoc_installer_name='standalone_coccoc_en.exe'):
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\coccoc-dev; .\\{coccoc_installer_name} /silent /install"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def install_coccoc_silentlty_make_coccoc_default_browser(coccoc_installer_name='standalone_coccoc_en.exe', cmd_options=None):
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\coccoc-dev; .\\{coccoc_installer_name} /silent {cmd_options} /install"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def cleanup(coccoc_update=True):
    # Kill all unncessary task
    if coccoc_update:
        WindowsCMD.execute_cmd('taskkill /im CocCocUpdate.exe /f')
    WindowsCMD.execute_cmd('taskkill /im browser.exe /f')
    WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')
    WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')
    WindowsCMD.execute_cmd('taskkill /im iexplore.exe /f')
    WindowsCMD.execute_cmd('taskkill /im firefox.exe /f')


def wait_for_coccoc_install_finish():
    from datetime import datetime
    start_time = datetime.now()
    while check_if_coccoc_is_installed() is False:
        time.sleep(2)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 120:
            break


def install_coccoc_not_set_as_default(coccoc_installer_name='standalone_coccoc_en.exe'):
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_for_window_appear()
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    time.sleep(5)
    coccoc_installer.Make_Cốc_Cốc_your_default_browserCheckBox.click()
    time.sleep(5)
    coccoc_installer.Button.click()
    time.sleep(1)
    wait_for_coccoc_install_finish()
    cleanup()


def install_coccoc_set_as_default(coccoc_installer_name='standalone_coccoc_en.exe', is_needed_clean_up=True):
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_for_window_appear()
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    time.sleep(5)
    coccoc_installer.Button.click()
    time.sleep(1)
    wait_for_coccoc_install_finish()
    if is_needed_clean_up is True:
        cleanup()
    else:
        pass


def install_coccoc_set_system_start_up_on(coccoc_installer_name='standalone_coccoc_en.exe'):
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"cd C:\\coccoc-dev; .\\{coccoc_installer_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wait_for_window_appear()
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    time.sleep(10)
    coccoc_installer.Run_browser_on_system_start.click()
    time.sleep(5)
    coccoc_installer.Button.click()
    time.sleep(1)
    wait_for_coccoc_install_finish()


def change_default_browser(browser_name):
    import subprocess
    subprocess.Popen(["powershell.exe",
                      r"Start-Process $env:windir\system32\control.exe -LoadUserProfile -Wait -ArgumentList '/name Microsoft.DefaultPrograms /page pageDefaultProgram'"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)
    default_apps = Desktop(backend='uia').SettingsDialog
    time.sleep(2)
    default_apps.child_window(auto_id='TextBox').click_input()
    from pywinauto import keyboard
    time.sleep(2)
    keyboard.SendKeys('browser')
    time.sleep(2)
    default_apps.Choose_a_default_web_browser.click_input()
    time.sleep(2)
    try:
        default_apps.child_window(auto_id='SystemSettings_DefaultApps_BrowserDefaultAssociation_TitleTextBlock').click_input()
    except:
        default_apps.child_window(
            auto_id='SystemSettings_DefaultApps_Browser_Button').click_input()
    time.sleep(2)
    default_apps = Desktop(backend='uia').Dialog0
    if browser_name in 'Firefox':
        default_apps.Firefox.click()
    elif browser_name in 'Google Chrome':
        default_apps.Google_Chrome.click()
    elif browser_name in 'Microsoft Edge':
        default_apps.Microsoft_Edge.click()
    elif browser_name in 'Internet Explorer':
        default_apps.Internet_Explorer.click()
    else:
        default_apps.Cốc_Cốc.click()
    time.sleep(2)
    subprocess.Popen(["powershell.exe",
                      r"Stop-Process -Name 'SystemSettings'"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def choose_import_browser_settings(action='Continue', browser_name='Chrome'):
    default_apps = None
    if browser_name in 'Chrome':
        default_apps = Desktop(backend='uia').Import_Google_Chrome_Settings
    elif browser_name in 'Firefox':
        default_apps = Desktop(backend='uia').Import_Mozilla_Firefox_Settings
    elif browser_name in 'Internet Explorer':
        default_apps = Desktop(backend='uia').Import_Microsoft_Internet_Explorer_Settings
    elif browser_name in 'Microsoft Edge':
        default_apps = Desktop(backend='uia').Import_Microsoft_Edge_Settings
    if action == 'Continue':
        default_apps.Continue.click()
    elif action == 'Cancel':
        default_apps.Cancel.click()


def is_popup_import_browser_settings_displayed(browser_import_name='Import Google Chrome Settings'):
    time.sleep(5)
    from pywinauto import Desktop
    windows = Desktop(backend="uia").windows()
    list_windows = []
    for w in windows:
        list_windows.append(w.window_text())
    print(f"List windows are : {list_windows}")
    return browser_import_name in list_windows


def wait_for_window_appear(window_name='Cốc Cốc Installer'):
    from datetime import datetime
    index = 0
    start_time = datetime.now()
    while index == 0:
        time.sleep(1)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 120:
            break
        all_windows = Desktop(backend='uia').windows()
        for window in all_windows:
            if window_name in window.window_text():
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


def kill_browser_process(browser_name='browser.exe'):
    import subprocess
    try:
        subprocess.Popen(["powershell.exe",
                          f"taskkill /im {browser_name} /f"],
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


def coccoc_instance():
    return webdriver.Chrome(options=chrome_options_preset())


def chrome_options_preset():
    binary_path = f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = binary_path
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    split_after = binary_path.split('\\Local')
    user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
    chrome_options.add_argument('--user-data-dir=' + user_data_path)
    modify_file_as_text(user_data_path + '\\Default\\Preferences', 'Crashed', 'none')
    return chrome_options


def uninstall_then_install_coccoc_with_default(is_needed_clean_up=True, is_needed_clear_user_data=False):
    if check_if_coccoc_is_installed():
        if is_needed_clear_user_data is False:
            uninstall_coccoc_silently()
        else:
            uninstall_coccoc_and_delete_user_data()
    install_coccoc_set_as_default(is_needed_clean_up=is_needed_clean_up)


def uninstall_then_install_coccoc_silentlty_with_option(cmd_options):
    from datetime import datetime
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_silentlty_make_coccoc_default_browser(cmd_options=cmd_options)
    start_time = datetime.now()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 300:
            break
    kill_browser_process()
    time.sleep(2)


def uninstall_then_install_coccoc_silentlty_with_option_without_kill_process(cmd_options):
    from datetime import datetime
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_silentlty_make_coccoc_default_browser(cmd_options=cmd_options)
    start_time = datetime.now()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 300:
            break


def interact_dev_hosts(action="activate"):
    import subprocess
    current_dir = get_current_dir()[0] + powershell_script_path
    subprocess.Popen(["powershell.exe",
                      f"cd {current_dir}; .\\interactDevHost.ps1 -action {action}"],
                     stdin=subprocess.PIPE, stderr=subprocess.PIPE)


def install_old_coccoc_version():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_set_as_default(coccoc_installer_name='coccoc_en_old_version.exe')
