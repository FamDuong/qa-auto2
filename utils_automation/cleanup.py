import shutil
import subprocess


class Browsers:
    def kill_all_browsers(self, get_browser_type):
        if get_browser_type == "CocCoc":
            prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            prog = subprocess.Popen("taskkill /im CocCocCrashHandler.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            prog = subprocess.Popen("taskkill /im CocCocCrashHandler64.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif get_browser_type == "Chrome":
            prog = subprocess.Popen("taskkill /im chrome.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #prog = subprocess.Popen("taskkill /im CocCocCrashHandler.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #prog = subprocess.Popen("taskkill /im CocCocCrashHandler64.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog = subprocess.Popen("taskkill /im chromedriver.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()
