import os
import settings_master as settings
import time
from utils_automation.common import CSVHandle
from pytest_testrail.plugin import pytestrail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils_automation.cleanup import Browsers

startBrowser = 0


class TestPageLoadTime:
    def open_webpage(self, source, binary_file, options_list=None):
        browser = Browsers()
        browser.kill_all_browsers()

        global startBrowser

        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        opts.add_argument('user-data-dir=' + settings.USER_DATA_DIR)
        # opts.add_argument("--headless --disable-gpu")
        if options_list is not None:
            for i in options_list:
                opts.add_argument(i)
        startBrowser = int(round(time.time() * 1000))
        # driver = webdriver.Chrome(executable_path=cc_driver, chrome_options=opts)
        driver = webdriver.Chrome(chrome_options=opts)
        # driver = webdriver.Chrome('/Users/itim/Downloads/python/chromedriver') #Environment: MAC OS

        driver.get(source)
        return driver

    def measureTime(self, driver):
        global browserStartup
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")
        pageComplete = driver.execute_script("return window.performance.timing.loadEventEnd")

        browserStartup = navigationStart - startBrowser
        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        pageloadtime = pageComplete - navigationStart

        print("Browser startup time: %s" % browserStartup)
        print("First frame displayed: %s" % backendPerformance)
        print("DOM Load Event completed: %s" % frontendPerformance)
        print("Total PageLoad Time: %s" % pageloadtime)

        time.sleep(2)
        driver.quit()
        return pageloadtime

    def get_page_load_time(self, filename, file_name_result, binary_file, options_list=None):
        listweb = CSVHandle().get_from_csv(filename)
        loadtimes = []
        for i in listweb:
            loadtime = 0
            looptime = 2   # 10
            for j in range(looptime):
                browser = self.open_webpage(i, binary_file, options_list)
                loadtime = loadtime + self.measureTime(browser)
            loadtimes.append(loadtime / looptime)
        CSVHandle().write_result_data_for_page_load_time(file_name=file_name_result, keyname_list=listweb, value_list=loadtimes,
                                                         result_type='Page load time')

    @pytestrail.case('C82299')
    def test_browser_plt(self, binary_path):
        # Define test filename
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + r"\testbenchmark.csv"
        filename_result = dirname + r"\results_plt.csv"

        self.get_page_load_time(filename, filename_result, binary_path, None)



