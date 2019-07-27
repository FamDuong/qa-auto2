from datetime import datetime

from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities

driver = None


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


def _capture_screenshot(filename):
    driver.save_screenshot("screenshots/" + filename)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--proxy-server='direct://'")
        # chrome_options.add_argument("--proxy-bypass-list=*")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument("--allow-insecure-localhost")
        # chrome_options.add_argument("--disable-infobars")
        #
        # capabilities = DesiredCapabilities.CHROME
        # capabilities['acceptSslCerts'] = True
        # capabilities['acceptInsecureCerts'] = True

        driver = webdriver.Chrome()
        driver.maximize_window()
    yield driver
    driver.quit()
    return


@pytest.fixture(scope='session', autouse=True)
def clear_screen_shot_folder():
    from utils.cleanup import Files
    files = Files()
    files.delete_files_in_folder("screenshots", "png")
