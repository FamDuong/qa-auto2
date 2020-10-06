import pytest
import logging

from models.pageobject.settings import SettingsPageObject
from models.pageobject.downloads import DownloadsPageObject
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import Urls
from utils_automation.setup import WaitAfterEach
from testscripts.common_setup import delete_all_mp4_file_download

LOGGER = logging.getLogger(__name__)

download_folder = None

@pytest.fixture(scope='session')
def browser_top_sites():
    LOGGER.info("Init coc coc browser")
    global download_folder
    driver = coccoc_instance()

    # LOGGER.info("Get default download folder")
    # driver.get(Urls.COCCOC_SETTINGS_URL)
    # WaitAfterEach.sleep_timer_after_each_step()
    # setting_page_object = SettingsPageObject()
    # download_folder = setting_page_object.get_download_folder(driver)
    #
    # LOGGER.info("Delete all mp4 file in "+download_folder)
    # delete_all_mp4_file_download(download_folder, '.mp4')
    #
    # LOGGER.info("Delete all downloaded files in "+Urls.COCCOC_DOWNLOAD_URL)
    # driver.get(Urls.COCCOC_DOWNLOAD_URL)
    # downloads_page_object = DownloadsPageObject()
    # downloads_page_object.clear_all_existed_downloads(driver)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def get_current_download_folder_top_sites():
    return download_folder
# import pytest
# from selenium import webdriver as sele_webdriver
# from selenium.webdriver import DesiredCapabilities
#
# from testscripts.common_setup import clear_data_download
# from utils_automation.setup import WaitAfterEach
#
# driver = None
# username = None
# download_folder = None
# user_data_path = None
# user_data_default = None
#
#
# @pytest.fixture(scope='session')
# def browser_top_sites():
#     global driver
#     global user_data_path
#     from utils_automation.const import Urls
#     from models.pageobject.settings import SettingsPageObject
#     setting_page_object = SettingsPageObject()
#     global download_folder
#     global user_data_default
#     binary_path = f"C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
#     if driver is None:
#         chrome_options = sele_webdriver.ChromeOptions()
#         chrome_options.binary_location = binary_path
#         chrome_options.add_argument("--window-size=1920,1080")
#         chrome_options.add_argument("--proxy-server='direct://'")
#         chrome_options.add_argument("--proxy-bypass-list=*")
#         chrome_options.add_argument("--start-maximized")
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--ignore-certificate-errors')
#         chrome_options.add_argument("--allow-insecure-localhost")
#         chrome_options.add_argument('--disable-application-cache')
#         chrome_options.add_argument("--disable-session-crashed-bubble")
#         chrome_options.add_argument("--disable-features=RendererCodeIntegrity")
#         chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#         split_after = binary_path.split('\\Local')
#         user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
#         import subprocess
#         prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         prog.communicate()  # Returns (stdoutdata, stderrdata): stdout and stderr are ignored, here
#         chrome_options.add_argument('--user-data-dir=' + user_data_path)
#         caps = DesiredCapabilities().CHROME
#         # caps["pageLoadStrategy"] = "normal"  # complete
#         caps["pageLoadStrategy"] = "eager"
#         driver = sele_webdriver.Chrome(options=chrome_options, desired_capabilities=caps)
#         driver.maximize_window()
#         driver.set_page_load_timeout(120)
#         driver.get(Urls.COCCOC_SETTINGS_URL)
#         WaitAfterEach.sleep_timer_after_each_step()
#         download_folder = setting_page_object.get_download_folder(driver)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope='session')
# def get_current_download_folder_top_sites():
#     return download_folder
#
#
# @pytest.fixture(scope='session')
# def get_user_data_path_top_sites():
#     return user_data_path
#
#
# @pytest.fixture()
# def clear_download_page(browser_top_sites, get_current_download_folder_top_sites):
#     yield
#     clear_data_download(browser_top_sites)


# @pytest.fixture(scope='session', autouse=True)
# def get_username():
#     global username
#     username = request.config.getoption("--user")
#     return username
