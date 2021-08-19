import logging
import os
import time

from selenium.webdriver import DesiredCapabilities
from utils_automation.common import get_from_csv, write_result_data_for_page_load_time
from pytest_testrail.plugin import pytestrail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from utils_automation.cleanup import Browsers
from utils_automation.url_utils import URLUtils
from utils_automation.date_time_utils import get_current_timestamp
from selenium.common.exceptions import TimeoutException

start_browser = 0
LOGGER = logging.getLogger(__name__)


class TestPageLoadTime:
    url = URLUtils()
    start_time = 0
    end_time = 0

    def open_webpage(self, source, binary_file, default_dir, get_browser_type, options_list=None):
        browser = Browsers()
        browser.kill_all_browsers(get_browser_type)

        global start_browser

        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        opts.add_argument("enable-automation")
        opts.add_argument('user-data-dir=' + default_dir)
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument("--start-maximized")
        # opts.add_argument('--disable-gpu')
        opts.add_argument('--disable-dev-shm-usage')
        # opts.add_argument('--disable-infobars')
        opts.add_argument('--disable-browser-side-navigation')
        opts.add_argument("--disable-popup-blocking")
        opts.add_argument('--no-sandbox')
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--allow-insecure-localhost")
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_experimental_option("useAutomationExtension", False)
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
        driver.set_page_load_timeout(30)
        try:
            self.start_time = int(round(time.time() * 1000))
            driver.get(source)
            WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            self.end_time = int(round(time.time() * 1000))
        except TimeoutException as e:
            LOGGER.info("Page load Timeout occurred. Quiting !!!")
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
        page_load_time_by_state = self.end_time - self.start_time

        # LOGGER.info("Browser startup time: %s" % browser_startup)
        # LOGGER.info("First frame displayed: %s" % backend_performance)
        # LOGGER.info("DOM Load Event completed: %s" % frontend_performance)
        # LOGGER.info("Total PageLoad Time: %s" % page_load_time)

        time.sleep(2)
        driver.quit()
        return [page_load_time, page_load_time_by_state]

    def get_page_load_time(self, filename, file_name_result, binary_file, default_dir, get_browser_type, options_list=None):
        listweb = get_from_csv(filename)
        loadtimes = []
        loadtimes_by_state = []
        index = 1
        LOGGER.info('%-30s' '%-30s' '%-30s' '%s' % ('No.', 'Url', 'PLT Average', 'PLT by State Average'))
        for i in listweb:
            loadtime = 0
            loadtime_by_state = 0
            looptime = 3
            for j in range(looptime):
                browser = self.open_webpage(i, binary_file, default_dir, get_browser_type, options_list)
                measure_time = self.measureTime(browser)
                page_load_time = measure_time[0]
                page_load_time_by_state = measure_time[1]
                loadtime = loadtime + page_load_time
                loadtime_by_state = loadtime_by_state + page_load_time_by_state
                LOGGER.info('%-30s' '%-30s' '%-30s' '%s' % (str(index) + "." + str(j), i, page_load_time, page_load_time_by_state))
            page_load_time_avg = round(loadtime / looptime, 1)
            page_load_time_by_state_avg = round(loadtime_by_state / looptime, 1)
            loadtimes.append(page_load_time_avg)
            loadtimes_by_state.append(page_load_time_avg)
            LOGGER.info('%-30s' '%-30s' '%-30s' '%s' % ("Average", i, page_load_time_avg, page_load_time_by_state_avg))
            index += 1
            write_result_data_for_page_load_time(file_name=file_name_result, keyname_list=i, value_list=[page_load_time_avg, page_load_time_by_state_avg],
                                                 result_type='Page load time')
        page_load_time_avg = round(sum(loadtimes) / len(listweb), 1)
        write_result_data_for_page_load_time(file_name=file_name_result, keyname_list="Average",
                                             value_list=loadtimes,
                                             result_type='Page load time')

    @pytestrail.case('C82299')
    def test_browser_plt(self, binary_path, default_directory, application_path, get_browser_type):
        LOGGER.info("Run in %s" % get_browser_type)
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + r'\test_data' + r"\testbenchmark.csv"
        file_list_websites_valid = dirname + "\\test_data" + r"\list_websites_valid.csv"
        file_list_websites_invalid = dirname + "\\test_data" + r"\list_websites_invalid.csv"
        filename_result = dirname + r'\test_result' + r"\results_plt_" + get_current_timestamp("%Y%m%d") \
                          + "_" + get_browser_type + ".csv"

        # Validate links before execute
        self.url.get_valid_urls(filename, file_list_websites_valid, file_list_websites_invalid)
        self.get_page_load_time(file_list_websites_valid, filename_result, binary_path, default_directory, get_browser_type, None)
