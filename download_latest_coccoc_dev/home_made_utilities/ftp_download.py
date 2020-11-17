
def get_list_coccoc_installer_dirs(folders_list):
    coccoc_download_folder_list = []
    for each_folder in folders_list:
        import re
        if re.match(r'\b\d+\.+\b\d+\.\b\d+\.+\d*$', each_folder):
            coccoc_download_folder_list.append(each_folder)
    return coccoc_download_folder_list


def sorted_list_directories(folders_list):
    from packaging import version
    list_coccoc_folders = get_list_coccoc_installer_dirs(folders_list)
    sorted_list = sorted(list_coccoc_folders, key=lambda x: version.Version(x))
    return sorted_list


def download_latest_coccoc_dev_installer(needed_download_version=None):
    coccoc_installer_name = "standalone_coccoc_en.exe"
    from ftplib import FTP
    with FTP('browser3v.dev.itim.vn') as ftp:
        ftp.login('anonymous', '')
        ftp.cwd('corom')
        latest_coccoc_download_dir = None
        if needed_download_version is not None:
            latest_coccoc_download_dir = needed_download_version
        else:
            latest_coccoc_download_dir = get_latest_directory_by_set_up_exe_date(ftp)
        from download_latest_coccoc_dev.configs.yaml_configs import CocCocConfigs
        if CocCocConfigs.COCCOC_DEV_VERSION not in latest_coccoc_download_dir:
            ftp.cwd(f"{latest_coccoc_download_dir}/installers")
            try:
                ftp.retrbinary("RETR " + coccoc_installer_name,
                               open(f"C:\\coccoc-dev\\{coccoc_installer_name}", 'wb').write)
            except:
                print(f"Error download coccoc binary for {coccoc_installer_name}")
            return latest_coccoc_download_dir
        else:
            return "Already latest"


def get_latest_coccoc_directory(ftp):
    ftp.cwd('corom')
    folders_list = ftp.nlst()
    coccoc_download_folder_list = get_list_coccoc_installer_dirs(folders_list)
    sorted_list_directory = sorted_list_directories(coccoc_download_folder_list)
    return sorted_list_directory[-1]


def get_latest_coccoc_directories_order_by_version(ftp):
    folders_list = ftp.nlst()
    coccoc_download_folder_list = get_list_coccoc_installer_dirs(folders_list)
    return sorted_list_directories(coccoc_download_folder_list)


def get_modified_time(ftp):
    import sys
    # Store the reference, in case you want to show things again in standard output

    old_stdout = sys.stdout

    # This variable will store everything that is sent to the standard output

    from io import StringIO
    result = StringIO()

    sys.stdout = result

    # Here we can call anything we like, like external modules, and everything that they will send to standard output will be stored on "result"
    ftp.dir()

    # Redirect again the std output to screen

    sys.stdout = old_stdout

    # Then, get the stdout like a string and process it!

    value = result.getvalue()
    # from dateutil import parser
    return value


def get_latest_directory_by_set_up_exe_date(ftp):
    sorted_list_directories = get_latest_coccoc_directories_order_by_version(ftp)
    latest_timestamp = ''
    latest_directory = ''
    for each_directory in sorted_list_directories:
        ftp.cwd(f'{each_directory}')
        timestamp = ftp.voidcmd("MDTM setup.exe")[4:].strip()
        if timestamp > latest_timestamp:
            latest_timestamp = timestamp
            latest_directory = each_directory
        ftp.cwd("../")
    return latest_directory








