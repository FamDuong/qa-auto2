import os
from datetime import datetime
from appium import webdriver
from selenium import  webdriver as sele_webdriver
import pytest
from utils_automation.setup import WaitAfterEach

driver = None
user_data_path = None
winappdriver = None
download_folder = None
block_origin_extension_path = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report right before close webdriver.
        :param request:
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
        if driver is not None and ('winapp' not in item.name):
            _capture_screenshot(filename)

        elif win_app_driver is not None:
            _capture_screenshot_win_app(filename)
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


def _capture_screenshot_win_app(filename):
    current_dir = get_current_dir()[0]
    winappdriver.save_screenshot(current_dir + "/screenshots/" + filename)


@pytest.fixture(scope='session')
def browser():
    import subprocess
    prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    prog.communicate()  # Returns (stdoutdata, stderrdata): stdout and stderr are ignored, here
    global driver
    global user_data_path
    global skip_ad_extension_path
    global block_origin_extension_path
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
        # chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('load-extension=' + skip_ad_extension_path)
        driver = sele_webdriver.Chrome(options=chrome_options)
        driver.create_options()
        driver.maximize_window()
        driver.set_page_load_timeout(40)
    yield driver
    driver.quit()
    return


@pytest.fixture(scope='session')
def win_app_driver():
    global winappdriver
    if winappdriver is None:
        desired_caps = {"app": "browser"}
        winappdriver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)
    yield winappdriver
    winappdriver.quit()
    return


@pytest.fixture(scope='session', autouse=True)
def set_up_before_run_user_browser():
    from models.pageobject.version import VersionPageObject
    from utils_automation.const import Urls
    global user_data_path, local_driver
    version_page_object = VersionPageObject()
    from models.pageobject.settings import SettingsPageObject
    setting_page_object = SettingsPageObject()
    global download_folder
    global skip_ad_extension_path
    global block_origin_extension_path
    try:
        local_driver = sele_webdriver.Chrome()
        local_driver.maximize_window()
        local_driver.get(Urls.COCCOC_VERSION_URL)
        path_full = version_page_object.get_profile_path(local_driver)
        local_driver.get(Urls.COCCOC_SETTINGS_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        download_folder = setting_page_object.get_download_folder(local_driver)
        split_after = path_full.split('\\Local')
        user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
        clear_downloaded_folder(download_folder)
        skip_ad_extension_path = user_data_path + u'\\Default\\Extensions\\lgblnfidahcdcjddiepkckcfdhpknnjh\\1.511_0'
        print(skip_ad_extension_path)
    finally:
        local_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def clear_screen_shot_folder():
    from utils_automation.cleanup import Files
    current_dir = get_current_dir()[0]
    files = Files()
    files.delete_files_in_folder(current_dir+"/screenshots", "png")


def clear_downloaded_folder(folder):
    from utils_automation.cleanup import Files
    files = Files()
    files.delete_all_files_in_folder(folder)


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')


@pytest.fixture(scope='session')
def get_current_download_folder():
    return download_folder

