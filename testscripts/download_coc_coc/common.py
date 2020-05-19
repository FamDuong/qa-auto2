from utils_automation.common import FilesHandle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from utils_automation.common import WindowsCMD

file_handle = FilesHandle()


def clean_up_browser(driver_choice):
    if driver_choice in "IE":
        WindowsCMD.execute_cmd('taskkill /im iexplore.exe /f')
    elif driver_choice in "CHROME":
        WindowsCMD.execute_cmd('taskkill /im chrome.exe /f')
    elif driver_choice in "FIREFOX":
        WindowsCMD.execute_cmd('taskkill /im firefox.exe /f')


def set_driver(driver_choice):
    if driver_choice == 'CHROME':
        driver = init_chrome_driver()
    elif driver_choice == 'FIREFOX':
        driver = init_firefox_driver()
    elif driver_choice == 'IE':
        driver = init_ie_driver()
    driver.maximize_window()
    return driver


def get_binary_firefox():
    binary = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    if file_handle.is_file_exist(binary):
        binary = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    elif file_handle.is_file_exist('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'):
        binary = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    return binary


def init_firefox_driver():
    binary = get_binary_firefox()
    options = Options()
    options.binary = binary
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True  # optional
    profile = webdriver.FirefoxProfile()
    # profile.set_preference("browser.download.folderList", 2)
    # profile.set_preference("browser.download.manager.showWhenStarting", False)
    # profile.set_preference("browser.download.dir", download_folder)
    # profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    # profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    # profile.set_preference("browser.download.manager.focusWhenStarting", False)
    # profile.set_preference("browser.download.manager.useWindow", False)
    # profile.set_preference("browser.download.manager.showAlertOnComplete", False)
    # profile.set_preference("browser.download.manager.closeWhenDone", False)
    mime_types = [
        'text/plain',
        'application/vnd.ms-excel',
        'text/csv',
        'application/csv',
        'text/comma-separated-values',
        'application/download',
        'application/octet-stream',
        'binary/octet-stream',
        'application/binary',
        'application/x-unknown'
    ]
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", ",".join(mime_types))
    #
    # profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    binary_path = file_handle.get_absolute_filename("\\webdriver\\geckodriver.exe")
    binary_path = binary_path.replace('\\utils_automation', '\\resources')
    driver = webdriver.Firefox(firefox_profile=profile, options=options, capabilities=cap,
                               executable_path=binary_path)
    return driver


def init_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {'safebrowsing.enabled': 'true'})
    binary_path = file_handle.get_absolute_filename("\\webdriver\\chromedriver.exe")
    binary_path = binary_path.replace('\\utils_automation', '\\resources')
    driver = webdriver.Chrome(options=chrome_options, executable_path=binary_path)
    return driver


def init_ie_driver():
    binary_path = file_handle.get_absolute_filename("\\webdriver\\IEDriverServer.exe")
    binary_path = binary_path.replace('\\utils_automation', '\\resources')
    # cap = DesiredCapabilities().INTERNETEXPLORER
    # cap['ignoreProtectedModeSettings'] = True
    # cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
    # cap['nativeEvents'] = True
    # cap['ignoreZoomSetting'] = True
    # cap['requireWindowFocus'] = False
    # cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
    # driver = webdriver.Ie(desired_capabilities=cap, executable_path=binary_path)
    driver = webdriver.Ie(executable_path=binary_path)
    return driver
