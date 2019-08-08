import os
from datetime import datetime
from appium import webdriver
from selenium import  webdriver as sele_webdriver
import pytest
from simple_settings import settings


driver = None
user_data_path = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report right before close webdriver.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        hasattr(report, 'wasxfail')
        # file_name = report.nodeid.replace("::", "_") + ".png"
        timestamp = datetime.now().strftime('%H-%M-%S.%f')[:-3]
        filename = timestamp + ".png"
        _capture_screenshot(filename)
        # if file_name:
        html = '<div><img src="screenshots/%s" style="width:600px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % filename
        extra.append(pytest_html.extras.html(html))
    report.extra = extra


def get_current_dir():
    before_split = os.getcwd()
    return before_split.split('\\testscripts\\')


def _capture_screenshot(filename):
    current_dir = get_current_dir()[0]
    driver.save_screenshot(current_dir + "/screenshots/" + filename)


@pytest.fixture(scope='session')
def browser():
    import subprocess
    import os
    prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    prog.communicate()  # Returns (stdoutdata, stderrdata): stdout and stderr are ignored, here
    global driver
    global user_data_path
    if driver is None:
        chrome_options = sele_webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.add_argument("--disable-infobars")
        # chrome_options.add_argument('--user-data-dir=' + os.environ['user-dir-path'])
        chrome_options.add_argument('--user-data-dir=' + user_data_path)

        driver = sele_webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
    yield driver
    driver.quit()
    return


@pytest.fixture(scope='session')
def win_app_driver():
    global driver
    if driver is None:
        desired_caps = {}
        desired_caps["app"] = "Browser"
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)
    yield driver
    driver.quit()
    return


@pytest.fixture(scope='session', autouse=True)
def get_user_data_path():
    from models.pageobject.version import VersionPageObject
    from utils_automation.const import Urls
    global user_data_path, local_driver
    version_page_object = VersionPageObject()
    try:
        local_driver = sele_webdriver.Chrome()
        local_driver.maximize_window()
        local_driver.get(Urls.COCCOC_VERSION_URL)
        path_full = version_page_object.get_profile_path(local_driver)
        split_after = path_full.split('\\Local')
        user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
    finally:
        local_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def clear_screen_shot_folder():
    from utils_automation.cleanup import Files
    current_dir = get_current_dir()[0]
    files = Files()
    files.delete_files_in_folder(current_dir+"/screenshots", "png")


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')
