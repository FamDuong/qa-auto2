import os
import settings_master as settings
import time
from utils_automation.common import CSVHandle
from utils_automation.setup import Browser
from pytest_testrail.plugin import pytestrail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils_automation.cleanup import Browsers
# start = 0

class TestPageLoadTime:
    def open_webpage(self, source, binary_file, options_list=None):
        browser = Browsers();
        browser.kill_all_browsers()

        global startBrowser

        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        opts.add_argument('--user-data-dir=' + settings.USER_DATA_DIR)
        if options_list is not None:
            for i in options_list:
                opts.add_argument(i)
        startBrowser = int(round(time.time() * 1000))
        # driver = webdriver.Chrome(executable_path=cc_driver, chrome_options=opts)
        driver = webdriver.Chrome(chrome_options=opts)
        # driver = webdriver.Chrome('/Users/itim/Downloads/python/chromedriver') #Environment: MAC OS

        driver.get(source);
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

        driver.quit()
        return pageloadtime

    def get_page_load_time(self, filename, binary_file, options_list=None):
        listweb = CSVHandle().get_from_csv(filename)
        loadtimes = {}
        startuptimes = {}
        for i in listweb:
            loadtime = 0
            startuptime = 0
            looptime = 2   # 10
            for j in range(looptime):
                print("Run time: %s" % j)
                browser = self.open_webpage(i, binary_file, options_list)
                loadtime = loadtime + self.measureTime(browser)
                startuptime = startuptime + browserStartup
            loadtimes[i] = loadtime / looptime
            startuptimes[i] = startuptime / looptime
        for i in listweb:
            print("Average load time of %s is %s" % (i, loadtimes.get(i)))
            print("Average browser startup time of %s is %s" % (i, startuptimes.get(i)))

    def test_browser_plt(self):
        # Define test filename
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + r"\ads_block_standard.csv"
        # filename = dirname + r"\ads_block_strict.csv"

        # Test for NetworkService
        # options_list = {"--enable-features=NetworkService"}
        # Test for ads block
        options_list = {"--component-updater=url-source=http://dev-update.coccoc.com/service/update2/json"}
        self.get_page_load_time(filename, settings.COCCOC_PATH, None)


