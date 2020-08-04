

def get_current_login_user():
    import subprocess
    import re
    p1 = subprocess.Popen(["powershell.exe", "whoami"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    who_am_i = p1.communicate()[0]
    user_name = re.split(r'\\r', (re.split(r'.\\\\', str(who_am_i))[1]))[0]
    return user_name


current_user = get_current_login_user()
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


def get_coccoc_version_folder_name():
    import subprocess
    import re
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application; ls"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    current_dir = str(p.communicate()[0])
    coccoc_version = re.findall(r'\b\d+\.+\b\d+\.\b\d+\.+\d*', current_dir)[0]
    return coccoc_version


def uninstall_coccoc_silently():
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application"
                          f"\\{get_coccoc_version_folder_name()}"
                          f"\\Installer; .\\setup.exe --uninstall --force-uninstall"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def install_coccoc_silently():
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"cd C:\\coccoc-dev; .\\{coccoc_installer_name} /silent /install"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()


def main():
    if check_if_coccoc_is_installed():
        coccoc_version = get_coccoc_version_folder_name()
        from configs.yaml_configs import CocCocConfigs
        if coccoc_version in CocCocConfigs.COCCOC_DEV_VERSION:
            pass
        else:
            uninstall_coccoc_silently()
            import time
            time.sleep(5)
            install_coccoc_silently()
    else:
        install_coccoc_silently()


if __name__ == "__main__":
    main()






