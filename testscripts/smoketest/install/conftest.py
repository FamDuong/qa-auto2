import time

import pytest
from selenium import webdriver

from testscripts.smoketest.install.common import check_if_coccoc_is_installed, uninstall_coccoc_silently, \
    install_coccoc_silently, install_coccoc_not_set_as_default
from utils_automation.common import WindowsHandler

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
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument('--disable-application-cache')
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_argument("--disable-features=RendererCodeIntegrity")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    split_after = binary_path.split('\\Local')
    user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
    import subprocess
    prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    prog.communicate()  # Returns (stdoutdata, stderrdata): stdout and stderr are ignored, here
    chrome_options.add_argument('--user-data-dir=' + user_data_path)
    return chrome_options


@pytest.fixture(scope='session')
def coccoc_install_instance_on_default_browser():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_silently()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)
    driver = webdriver.Chrome(options=chrome_options_preset())
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def coccoc_install_instance_set_not_default_browser():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_not_set_as_default()
    driver = webdriver.Chrome(options=chrome_options_preset())
    yield driver
    driver.quit()


