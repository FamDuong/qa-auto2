import pytest

from testscripts.smoketest.common import coccoc_instance
from utils_automation.common import WindowsHandler
from models.pagelocators.flags import FlagsPageLocators
from selenium import webdriver as sele_webdriver
from utils_automation.common import modify_file_as_text
from utils_automation.setup import WaitAfterEach

windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()
driver = None

@pytest.fixture(scope='class')
def uninstall_coccoc():
    from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
    uninstall_then_install_coccoc_with_default(is_needed_clear_user_data=True, is_needed_clean_up=True)


@pytest.fixture(scope='class')
def enable_moji_flag(uninstall_coccoc):
    driver = coccoc_instance()
    from utils_automation.const import Urls
    driver.get(Urls.COCCOC_FLAGS)
    search_bar = driver.find_element_by_id(FlagsPageLocators.SEARCH_FLAG_TXT_ID)
    search_bar.click()
    search_bar.send_keys('Moji')
    from selenium.webdriver.support.select import Select
    select = Select(driver.find_element_by_xpath(FlagsPageLocators.STATUS_DDL_XPATH))
    select.select_by_visible_text('Enabled')
    import time
    time.sleep(3)
    from testscripts.smoketest.common import cleanup
    cleanup()


@pytest.fixture(scope='class')
def open_coccoc_by_terminal(enable_moji_flag):
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe", ],
                     shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    import time
    time.sleep(10)
    from testscripts.smoketest.common import cleanup
    cleanup()


@pytest.fixture(scope='class')
def browser_moji(open_coccoc_by_terminal):
    driver = coccoc_instance()
    driver.maximize_window()
    from utils_automation.const import Urls
    driver.get(Urls.COCCOC_EXTENSIONS)
    yield driver
    driver.quit()