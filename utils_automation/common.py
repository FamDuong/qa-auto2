import fileinput
import os
import csv
import shutil
import sys
import time
import subprocess
import psutil
import win32api
import re
from os import path
from selenium import webdriver
from selenium.webdriver import ActionChains


def if_height_frame_so_width_frame(height_frame):
    if int(height_frame) == 4320:
        return 7680
    elif int(height_frame) == 2160:
        return 3840
    elif int(height_frame) == 1440:
        return 2560
    elif int(height_frame) == 1080:
        return 1920
    elif int(height_frame) == 720:
        return 1280


def wait_for_stable(wait_time=3):
    time.sleep(wait_time)


def remove_special_characters(string):
    rm_r = re.sub(r'\\r', ' ', str(string))
    rm_n = re.sub(r'\\n', ' ', str(rm_r))
    rm_t = re.sub(r'\\t', ' ', str(rm_n))
    rm_s = re.sub(' +', ' ', str(rm_t))
    print(rm_s)
    return rm_s


class CSVHandle:
    def get_from_csv(self, filename):
        list_temp = []
        # dirname, runname = os.path.split(os.path.abspath(__file__))
        # filename = dirname + filename
        with open(filename, 'r', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            print("CSV Reader: READING CSV FILE >>", filename)
            try:
                for row in reader:
                    for q in row:
                        if q == None or len(q) == 0:
                            pass
                        else:
                            list_temp.append(q)
                print("CSV Reader: FINISHED READING CSV FILE =>", filename)
                return list_temp
            except csv.Error as i:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, i))
                return None
            except EOFError as e:
                print("Can not read file CSV:", filename)
                print("System error:", e)
                return None


class FilesHandle:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(FilesHandle, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self.appdata = path.expandvars(r'%APPDATA%\CocCoc\\')
        self.localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc\\')

    def get_absolute_filename(self, filename):
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + filename
        return filename

    def find_files_in_folder_by_modified_date(self, mydir, endwith):
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        return filelist

    def delete_files_in_folder(self, mydir, endwith):
        import os
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        for f in filelist:
            os.chmod(os.path.join(mydir, f), 0o777)
            os.remove(os.path.join(mydir, f))

    def delete_all_files_in_folder(self, mydir):
        shutil.rmtree(mydir, ignore_errors=True, onerror=None)

    def clear_downloaded_folder(self, folder):
        self.delete_all_files_in_folder(folder)

    def is_file_exist(self, filepath):
        return str(os.path.isfile(filepath))

    def is_dir_exist(self, directory):
        return str(os.path.isdir(directory))

    def is_file_exist_in_folder(self, filename, folder):
        check = self.is_file_exist(folder + filename)
        if check == "True":
            return True
        else:
            return False

    def is_subfolder_exist_in_folder(self, subfolder, folder):
        check = self.is_dir_exist(folder + subfolder)
        if check == "True":
            return True
        else:
            return False

    def get_file_properties(self, fname):
        """
        Read all properties of the given file return them as a dictionary.
        """
        propNames = ('Comments', 'InternalName', 'ProductName',
                     'CompanyName', 'LegalCopyright', 'ProductVersion',
                     'FileDescription', 'LegalTrademarks', 'PrivateBuild',
                     'FileVersion', 'OriginalFilename', 'SpecialBuild')

        props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

        try:
            # backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
            fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
            props['FixedFileInfo'] = fixedInfo
            props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                                                    fixedInfo['FileVersionMS'] % 65536,
                                                    fixedInfo['FileVersionLS'] / 65536,
                                                    fixedInfo['FileVersionLS'] % 65536)

            # \VarFileInfo\Translation returns list of available (language, codepage)
            # pairs that can be used to retreive string info. We are using only the first pair.
            lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

            # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
            # two are language/codepage pair returned from above

            strInfo = {}
            for propName in propNames:
                strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
                ## print str_info
                strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

            props['StringFileInfo'] = strInfo
        except:
            pass
        return props

    def get_all_files_in_folder(self, folder, filetype):
        # r=root, d=directories, f = files
        list_files = []
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(filetype):
                    list_files.append(os.path.join(r, file))
        return list_files

    def get_signature_of_file(self, filepath):
        dirname, runname = os.path.split(os.path.abspath(__file__))
        print(f"File path is : {filepath}")
        argu = WindowsCMD.execute_cmd(dirname + r"\sigcheck.exe " + filepath)
        # signature = remove_special_characters(argu)
        return str(argu)

    def get_signature_of_files_in_folder(self, filetype, filepath):
        signature_list = []
        # dirname, runname = os.path.split(os.path.abspath(__file__))
        list_files = self.get_all_files_in_folder(filepath, filetype)
        for file in list_files:
            # argu = WindowsCMD.execute_cmd(dirname + r"\sigcheck.exe " + filepath)
            # string = remove_special_characters(argu)
            if 'pepflashplayer' in file:
                pass
            else:
                signature = self.get_signature_of_file(file)
                signature_list.append(signature)
        return signature_list

    def verify_product_version(self, filename, expect_version):
        signature = self.get_signature_of_file(filename)
        pro_version = 'Prod version: ' + expect_version
        assert pro_version in signature

    def copy_file(self, source, destination):
        import shutil
        try:
            shutil.copyfile(source, destination)
            print("File copied successfully.")

            # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

            # If destination is a directory.
        except IsADirectoryError:
            print("Destination is a directory.")

            # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

            # For other errors
        except:
            print("Error occurred while copying file.")


class WebElements:

    @staticmethod
    def mouse_over_element(driver, element):
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()


class WindowsCMD:
    @staticmethod
    def execute_cmd(cmd_text):
        wait_for_stable()
        process = subprocess.Popen(cmd_text.split(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
        return output

    def is_process_exists(process_name):
        wait_for_stable()
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False


class WindowsHandler:

    def get_netfirewall_rule(self, display_name):
        rule = WindowsCMD.execute_cmd("powershell get-netfirewallrule -DisplayName '" + display_name + "'")
        string = remove_special_characters(rule)
        return string

    def verify_netfirewall_rule(self, display_name, direction, action):
        rule = self.get_netfirewall_rule(display_name)
        assert "Direction : " + direction in rule
        assert "Action : " + action in rule

    def get_current_login_user(self):
        import subprocess, re
        p1 = subprocess.Popen(["powershell.exe", "whoami"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        who_am_i = p1.communicate()[0]
        user_name = re.split(r'\\r', (re.split(r'.\\\\', str(who_am_i))[1]))[0]
        return user_name


class BrowserHandler:
    def browser_init(self, user_data_path):
        # browser = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--allow-insecure-localhost")
        # chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument('--user-data-dir=' + user_data_path)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        browser = webdriver.Chrome(options=chrome_options)
        browser.create_options()
        browser.maximize_window()
        browser.set_page_load_timeout(40)
        return browser

    def browser_cleanup(self):
        WindowsCMD.execute_cmd('taskkill /im CocCocUpdate.exe /f')
        WindowsCMD.execute_cmd('taskkill /im CocCocCrashHandler.exe /f')
        WindowsCMD.execute_cmd('taskkill /im browser.exe /f')


def modify_file_as_text(text_file_path, text_to_search, replacement_text):
    try:
        with fileinput.FileInput(text_file_path, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(text_to_search, replacement_text), end='')
    except:
        print("Preferences file is not existed")


def find_text_in_file(text_file_path, text_to_search):
    found = 0
    with fileinput.FileInput(text_file_path, inplace=True) as file:
        for line in file:
            if text_to_search in line:
                found += 1
                break
    return found


def check_if_duplicates_list(list_of_elems):
    """ Check if given list contains any duplicates """
    set_of_elems = set()
    for elem in list_of_elems:
        if elem in set_of_elems:
            return True
        else:
            set_of_elems.add(elem)
    return False


def get_current_dir():
    before_split = os.getcwd()
    return before_split.split('\\testscripts\\')

