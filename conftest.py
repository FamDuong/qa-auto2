from selenium import webdriver
import pytest

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            hasattr(report, 'wasxfail')
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file("screenshots/" + name)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
    return driver
