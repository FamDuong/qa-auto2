from datetime import datetime

from selenium import webdriver
import pytest

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
        driver = webdriver.Chrome()
        driver.maximize_window()
    yield driver
    driver.quit()
    return
