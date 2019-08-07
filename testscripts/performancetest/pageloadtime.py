import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from io import open
from pytest_testrail.plugin import pytestrail
import time
import sys
import settings_master as settings

# start = 0

def openWebpage(source, binary_file, options_list=None):
    global startBrowser

    opts = Options()
    opts.binary_location = binary_file
    opts.add_argument("start-maximized")
    if options_list is not None:
        for i in options_list:
            opts.add_argument(i)
    startBrowser = int(round(time.time() * 1000))
    # driver = webdriver.Chrome(executable_path=cc_driver, chrome_options=opts)
    driver = webdriver.Chrome(chrome_options=opts)
    # driver = webdriver.Chrome('/Users/itim/Downloads/python/chromedriver') #Environment: MAC OS

    driver.get(source);
    return driver


def getFromCSV(filename):
    list = []
    with open(filename, 'r', newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        print("CSV Reader: READING CSV FILE >>", filename)
        try:
            for row in reader:
                for q in row:
                    if q == None or len(q) == 0:
                        pass
                    else:
                        list.append(q)
            print("CSV Reader: FINISHED READING CSV FILE =>", filename)
            return list
        except csv.Error as i:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, i))
            return None
        except EOFError as e:
            print("Can not read file CSV:", filename)
            print("System error:", e)
            return None


def measureTime(driver):
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

def get_page_load_time(binary_file, options_list=None):
    listweb = getFromCSV('testbenchmark.csv')
    loadtimes = {}
    startuptimes = {}
    for i in listweb:
        loadtime = 0
        startuptime = 0
        looptime = 2
        for j in range(looptime):
            print("Run time: %s" % j)
            browser = openWebpage(i, binary_file, options_list)
            loadtime = loadtime + measureTime(browser)
            startuptime = startuptime + browserStartup
        loadtimes[i] = loadtime / looptime
        startuptimes[i] = startuptime / looptime
    for i in listweb:
        print("Average load time of %s is %s" % (i, loadtimes.get(i)))
        print("Average browser startup time of %s is %s" % (i, startuptimes.get(i)))

@pytestrail.case('C82299')
def main():
    options_list = {"--enable-features=NetworkService"}
    get_page_load_time(settings.COCCOC_PATH, None)
    get_page_load_time(settings.COCCOC_PATH, options_list)
    get_page_load_time(settings.CHROME_PATH, None)


if __name__ == "__main__":
    main()