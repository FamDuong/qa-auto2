import time

import pytest
from selenium import webdriver

from testscripts.smoketest.installations.common import check_if_coccoc_is_installed, uninstall_coccoc_silently, \
    install_coccoc_silently, kill_coccoc_process, install_coccoc_not_set_as_default, \
    install_coccoc_set_system_start_up_on, install_coccoc_set_as_default
from utils_automation.common import WindowsHandler, modify_file_as_text

windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()


def chrome_options_preset():
    binary_path = f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = binary_path
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    split_after = binary_path.split('\\Local')
    user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
    chrome_options.add_argument('--user-data-dir=' + user_data_path)
    modify_file_as_text(user_data_path + '\\Default\\Preferences', 'Crashed', 'none')
    return chrome_options


def install_coccoc_with_default():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_set_as_default()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)
    kill_coccoc_process()
    time.sleep(2)


@pytest.fixture(scope='function')
def coccoc_install_instance_on_default_browser():
    install_coccoc_with_default()
    driver = webdriver.Chrome(options=chrome_options_preset())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def install_default_coccoc():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_silently()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)


@pytest.fixture(scope='function')
def install_default_coccoc_unsilently():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_set_as_default()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)


@pytest.fixture(scope='function')
def coccoc_install_instance_set_not_default_browser():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_not_set_as_default()
    driver = webdriver.Chrome(options=chrome_options_preset())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def install_set_system_option_on():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_set_system_start_up_on()


def coccoc_instance():
    return webdriver.Chrome(options=chrome_options_preset())



