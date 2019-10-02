
import os
import csv
import sys
import time
import subprocess
import psutil
from selenium import webdriver
from os import path
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

def wait_for_stable(wait_time = 3):
    time.sleep(wait_time)

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
    def get_absolute_filename(self, filename):
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + filename
        return filename

    def find_files_in_folder_by_modified_date(self, mydir, endwith):
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        return filelist

    @staticmethod
    def clear_downloaded_folder(folder):
        from utils_automation.cleanup import Files
        files = Files()
        files.delete_all_files_in_folder(folder)

    def is_file_exist(self, filepath):
        return str(os.path.isfile(filepath))

    def is_dir_exist(self, directory):
        return str(os.path.isdir(directory))

    def is_file_exist_in_app_data(self, filename):
        appdata = path.expandvars(r'%APPDATA%\CocCoc\\')
        check = self.is_file_exist(appdata + filename)
        if check == "True":
            return True
        else:
            return False

    def is_file_exist_in_local_app_data(self, filename):
        appdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc\\')
        check = self.is_file_exist(appdata + filename)
        if check == "True":
            return True
        else:
            return False

    def is_dir_exist_in_app_data(self, filename):
        localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc\\')
        check = self.is_dir_exist(localappdata + filename)
        if check == "True":
            return True
        else:
            return False

    def is_folder_exist_in_local_app_data(self, filename):
        localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc\\')
        check = self.is_dir_exist(localappdata + filename)
        if check == "True":
            return True
        else:
            return False



class WebElements:

    @staticmethod
    def mouse_over_element(driver, element):
            hov = ActionChains(driver).move_to_element(element)
            hov.perform()

class WindowsCMD:
    @staticmethod
    def execute_cmd(cmd_text):
        try:
            wait_for_stable()
            process = subprocess.Popen(cmd_text.split(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            print(output)
        finally:
            print("Cannot execute command!")

    def is_process_exists(process_name):
        wait_for_stable()
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;

class BrowserHandler:
    def browser_init(self):
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
        # chrome_options.add_argument('--user-data-dir=' + os.environ['user-dir-path'])
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
