import shutil
import subprocess


class Browsers:
    def kill_all_browsers(self):
        prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()
