import logging
import os
import subprocess
import time

from selenium.webdriver import DesiredCapabilities
from utils_automation.common import get_from_csv, write_result_data_for_page_load_time
from pytest_testrail.plugin import pytestrail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils_automation.cleanup import Browsers
from utils_automation.url_utils import URLUtils
from utils_automation.date_time_utils import get_current_timestamp

start_browser = 0
LOGGER = logging.getLogger(__name__)


class TestPageLoadTime:
    def open_webpage(self, source, binary_file, default_dir, options_list=None):
        browser = Browsers()
        url_utils = URLUtils()
        browser.kill_all_browsers()

        global start_browser

        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        opts.add_argument("enable-automation")
        opts.add_argument('user-data-dir=' + default_dir)
        #if enabled_ads_block == "True":
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument("--start-maximized")
        opts.add_argument('--disable-gpu')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument('--disable-infobars')
        opts.add_argument('--disable-browser-side-navigation')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--allow-insecure-localhost")
        # opts.add_argument("--headless")  # Not use headless due to need to check UI as same as end user
        # opts.add_argument("--enable-features=CocCocBlockAdByExtension")
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"  # complete
        # caps["pageLoadStrategy"] = "eager"
        if options_list is not None:
            for i in options_list:
                opts.add_argument(i)
        start_browser = int(round(time.time() * 1000))
        driver = webdriver.Chrome(options=opts, desired_capabilities=caps)
        # driver = webdriver.Chrome('/Users/itim/Downloads/python/chromedriver') #Environment: MAC OS
        if url_utils.is_url_exits(source):
            driver.get(source)
        return driver


    def measureTime(self, driver):
        global browser_startup
        navigation_start = driver.execute_script("return window.performance.timing.navigationStart")
        response_start = driver.execute_script("return window.performance.timing.responseStart")
        dom_complete = driver.execute_script("return window.performance.timing.domComplete")
        page_complete = driver.execute_script("return window.performance.timing.loadEventEnd")

        browser_startup = navigation_start - start_browser
        backend_performance = response_start - navigation_start
        frontend_performance = dom_complete - response_start
        page_load_time = page_complete - navigation_start

        # LOGGER.info("Browser startup time: %s" % browser_startup)
        # LOGGER.info("First frame displayed: %s" % backend_performance)
        # LOGGER.info("DOM Load Event completed: %s" % frontend_performance)
        # LOGGER.info("Total PageLoad Time: %s" % page_load_time)

        time.sleep(2)
        driver.quit()
        return page_load_time

    def get_page_load_time(self, filename, file_name_result, binary_file, default_dir, options_list=None):
        listweb = get_from_csv(filename)
        loadtimes = []
        index = 1
        LOGGER.info('%-25s' '%-60s' '%s' % ('No.', 'Url', 'Page load time Average'))
        for i in listweb:
            loadtime = 0
            looptime = 3
            for j in range(looptime):
                browser = self.open_webpage(i, binary_file, default_dir, options_list)
                loadtime = loadtime + self.measureTime(browser)
                page_load_time_avg = round(loadtime / looptime, 1)
            loadtimes.append(page_load_time_avg)
            LOGGER.info('%-25s' '%-60s' '%s' % (index, i, page_load_time_avg))
            index += 1
            write_result_data_for_page_load_time(file_name=file_name_result, keyname_list=i, value_list=page_load_time_avg,
                                                 result_type='Page load time')
        #write_result_data_for_page_load_time(file_name=file_name_result, keyname_list=listweb,
        #                                     value_list=loadtimes,
        #                                     result_type='Page load time')

    @pytestrail.case('C82299')
    # def test_browser_plt(self, binary_path, default_directory, application_path, get_enabled_adblock_extension):
    def test_browser_plt(self, binary_path, default_directory, application_path):
        # Define test filename
        # enabled_adblock_extension = get_enabled_adblock_extension
        # if enabled_adblock_extension == "True":
        #    subprocess.Popen(["powershell.exe",
        #                      f"cd {application_path}; .\\browser.exe --enable-features=CocCocBlockAdByExtension"],
        #                     stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        #    time.sleep(10)
        #    subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + r'\test_data' + r"\testbenchmark.csv"
        filename_result = dirname + r'\test_result' + r"\results_plt_" + get_current_timestamp("%Y%m%d%H%M") + ".csv"
        # self.get_page_load_time(filename, filename_result, binary_path, default_directory, None,
        #                        enabled_ads_block=enabled_adblock_extension)
        self.get_page_load_time(filename, filename_result, binary_path, default_directory, None)
