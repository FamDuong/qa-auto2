import math, datetime
import calendar
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import time

class TestDemo:

    def test_calculate_date(self):
        year = 2019
        month = 3
        day_to_count = calendar.MONDAY
        matrix = calendar.monthcalendar(year, month)
        num_days = sum(1 for x in matrix if x[day_to_count] != 0)
        print(num_days)

    def test_check_empty_fields(self, binary_path, default_directory):
        url = "https://dev-accounts.coccoc.com/"
        driver = self.start_browser(binary_path, default_directory)
        driver.get(url)
        time.sleep(3)
        value = driver.execute_script('document.querySelector("input[name=\'email\']").value')
        assert value == None
        value = driver.execute_script('document.querySelector("input[name=\'password\']").value')
        assert value == None
        driver.close()


    def start_browser(self, binary_path, default_directory):
        prog = subprocess.Popen("taskkill /im chromedriver.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()

        global startBrowser

        opts = Options()
        opts.binary_location = binary_path
        opts.add_argument("start-maximized")
        opts.add_argument('user-data-dir=' + default_directory)
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--allow-insecure-localhost")

        caps = DesiredCapabilities().CHROME
        driver = webdriver.Chrome(chrome_options=opts, desired_capabilities=caps)
        return driver