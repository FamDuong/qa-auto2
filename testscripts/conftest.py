import pytest
import subprocess
import time
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

from models.pageelements.settings import SettingsElements
from models.pageobject.extensions import ExtensionsPageObject
from models.pageobject.settings import SettingsPageObject
from testscripts.common_setup import clear_data_download, delete_all_mp4_file_download
from utils_automation.const import Urls, ExtensionIds
from utils_automation.setup import WaitAfterEach

settings_page_object = SettingsPageObject()
settings_cococ_ads_block_page_element = SettingsElements.SettingsAdsBlock()
settings_coccoc_ads_block_page_object = SettingsPageObject.SettingsAdsBlockPageObject()
extensions_cococ_page_object = ExtensionsPageObject.UblockPlusPageObject()
username = None

@pytest.fixture(scope='session', autouse=True)
def get_username(request):
    global username
    username = request.config.getoption("--user")
    return username


@pytest.fixture(scope='session')
def binary_path():
    return f"C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"


@pytest.fixture(scope='session')
def default_directory():
    return f'C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\User Data'


@pytest.fixture(scope='session')
def application_path():
    return f"C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application"

def interact_ad(browser, url, script_get_attribute_aria_pressed, script_click_ads_block, action):
    browser.get(url)
    WaitAfterEach.sleep_timer_after_each_step()
    settings_page_object.interact_ads_block(browser, action, script_get_attribute_aria_pressed, script_click_ads_block)


@pytest.fixture()
def disable_coccoc_block_ads(browser):
    script_get_attribute_aria_pressed = 'return document.querySelector("body > settings-ui")' \
                                        '.shadowRoot.querySelector("#main")' \
                                        '.shadowRoot.querySelector("settings-basic-page")' \
                                        '.shadowRoot.querySelector("#advancedPage ' \
                                        '> settings-section:nth-child(5) ' \
                                        '> settings-coccoc-subresource-filter-page")' \
                                        '.shadowRoot.querySelector("settings-toggle-button")' \
                                        '.shadowRoot.querySelector("#control").getAttribute("aria-pressed")'

    script_click_ads_block = 'document.querySelector("body > settings-ui").shadowRoot.querySelector("#main")' \
                             '.shadowRoot.querySelector("settings-basic-page")' \
                             '.shadowRoot.querySelector("#advancedPage > settings-section:nth-child(5) ' \
                             '> settings-coccoc-subresource-filter-page")' \
                             '.shadowRoot.querySelector("settings-toggle-button")' \
                             '.shadowRoot.querySelector("#control").click()'

    interact_ad(browser, Urls.COCCOC_ADS_BLOCK_URL, script_get_attribute_aria_pressed, script_click_ads_block,
                'disable')
    yield
    interact_ad(browser, Urls.COCCOC_ADS_BLOCK_URL, script_get_attribute_aria_pressed, script_click_ads_block, 'enable')


@pytest.fixture()
def disable_fair_adblocker(browser):
    script_get_attribute_aria_pressed = 'return document.querySelector("body > extensions-manager")' \
                                        '.shadowRoot.querySelector("#items-list")' \
                                        '.shadowRoot.querySelector("#cfhdojbkjhnklbpkdaibdccddilifddb")' \
                                        '.shadowRoot.querySelector("#enableToggle").getAttribute("aria-pressed")'

    script_click_ads_block = 'document.querySelector("body > extensions-manager")' \
                             '.shadowRoot.querySelector("#items-list").shadowRoot' \
                             '.querySelector("#cfhdojbkjhnklbpkdaibdccddilifddb")' \
                             '.shadowRoot.querySelector("#enableToggle").click()'

    interact_ad(browser, Urls.COCCOC_EXTENSIONS, script_get_attribute_aria_pressed, script_click_ads_block, 'disable')
    yield
    interact_ad(browser, Urls.COCCOC_EXTENSIONS, script_get_attribute_aria_pressed, script_click_ads_block, 'enable')
    WaitAfterEach.sleep_timer_after_each_step()


@pytest.fixture()
def enable_fair_adblocker(browser):
    script_get_attribute_aria_pressed = 'return document.querySelector("body > extensions-manager")' \
                                        '.shadowRoot.querySelector("#items-list")' \
                                        '.shadowRoot.querySelector("#cfhdojbkjhnklbpkdaibdccddilifddb")' \
                                        '.shadowRoot.querySelector("#enableToggle").getAttribute("aria-pressed")'

    script_click_ads_block = 'document.querySelector("body > extensions-manager")' \
                             '.shadowRoot.querySelector("#items-list").shadowRoot' \
                             '.querySelector("#cfhdojbkjhnklbpkdaibdccddilifddb")' \
                             '.shadowRoot.querySelector("#enableToggle").click()'

    interact_ad(browser, Urls.COCCOC_EXTENSIONS, script_get_attribute_aria_pressed, script_click_ads_block, 'enable')
    yield
    interact_ad(browser, Urls.COCCOC_EXTENSIONS, script_get_attribute_aria_pressed, script_click_ads_block, 'disable')
    WaitAfterEach.sleep_timer_after_each_step()


def change_mod_disable_cococ_ads(browser, block_mode):
    browser.get(Urls.COCCOC_ADS_BLOCK_URL)
    WaitAfterEach.sleep_timer_after_each_step()
    current_ads_block_mode = settings_cococ_ads_block_page_element.find_current_block_mod(browser).text
    print(f"Current ad block mode is : {current_ads_block_mode}")
    settings_coccoc_ads_block_page_object.change_ads_block_mode(browser, block_mode=block_mode)
    WaitAfterEach.sleep_timer_after_each_step()


@pytest.fixture()
def change_disable_coccoc_ads_mode_strict(browser):
    change_mod_disable_cococ_ads(browser, block_mode='Strict')
    yield
    change_mod_disable_cococ_ads(browser, block_mode='Standard')


def interact_ublock_extension(browser, action='enable'):
    browser.get(Urls.COCCOC_EXTENSIONS)
    WaitAfterEach.sleep_timer_after_each_step()
    extensions_cococ_page_object.interact_with_ublock_knob_btn(browser, action=action)
    WaitAfterEach.sleep_timer_after_each_step()


@pytest.fixture()
def enable_ublock_plus_extension(browser):
    interact_ublock_extension(browser, action='enable')
    yield
    interact_ublock_extension(browser, action='disable')


@pytest.fixture()
def revert_high_quality_default_option(browser):
    yield
    from models.pageobject.extensions import SaviorExtensionOptionsPageObject
    savior_extension = SaviorExtensionOptionsPageObject()
    browser.get(u'chrome-extension://' + ExtensionIds.SAVIOR_EXTENSION_ID + u'/options.html')
    savior_extension.choose_video_quality_high(browser)
    WaitAfterEach.sleep_timer_after_each_step()


@pytest.fixture()
def choose_low_quality_option(browser):
    from models.pageobject.extensions import SaviorExtensionOptionsPageObject
    savior_extension = SaviorExtensionOptionsPageObject()
    browser.get(u'chrome-extension://' + ExtensionIds.SAVIOR_EXTENSION_ID + u'/options.html')
    savior_extension.choose_video_quality_low(browser)
    WaitAfterEach.sleep_timer_after_each_step()
    yield


@pytest.fixture()
def get_disabled_dark_mode(browser):
    # kill_all_processes
    # change_disable_coccoc_ads_mode_strict(browser)
    WaitAfterEach.sleep_timer_after_each_step()
    return browser

@pytest.fixture()
def get_enabled_dark_mode(browser_enabled_dark_mode):
    WaitAfterEach.sleep_timer_after_each_step()
    return browser_enabled_dark_mode

# Kill all unnecessary process if any
def kill_all_processes():
    prog = subprocess.Popen("taskkill /im chromedriver.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    prog.communicate()
