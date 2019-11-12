import pytest

from models.pageelements.settings import SettingsElements
from models.pageobject.extensions import ExtensionsPageObject
from models.pageobject.settings import SettingsPageObject
from testscripts.common_setup import clear_data_download, delete_all_mp4_file_download
from utils_automation.const import Urls, ExtensionIds
from utils_automation.setup import WaitAfterEach


@pytest.fixture()
def clear_download_page_and_download_folder(browser, get_current_download_folder):
    yield
    clear_data_download(browser)
    delete_all_mp4_file_download(get_current_download_folder, '.mp4')


settings_page_object = SettingsPageObject()
settings_cococ_ads_block_page_element = SettingsElements.SettingsAdsBlock()
settings_coccoc_ads_block_page_object = SettingsPageObject.SettingsAdsBlockPageObject()
extensions_cococ_page_object = ExtensionsPageObject.UblockPlusPageObject()

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

    interact_ad(browser, Urls.COCCOC_ADS_BLOCK_URL, script_get_attribute_aria_pressed, script_click_ads_block, 'disable')
    yield
    interact_ad(browser, Urls.COCCOC_ADS_BLOCK_URL, script_get_attribute_aria_pressed, script_click_ads_block, 'enable')


@pytest.fixture()
def disable_fair_adblocker(browser):
    script_get_attribute_aria_pressed = 'return document.querySelector("body > extensions-manager")' \
                                        '.shadowRoot.querySelector("#items-list")' \
                                        '.shadowRoot.querySelector("#lgblnfidahcdcjddiepkckcfdhpknnjh")' \
                                        '.shadowRoot.querySelector("#enable-toggle").getAttribute("aria-pressed")'

    script_click_ads_block = 'document.querySelector("body > extensions-manager")' \
                             '.shadowRoot.querySelector("#items-list").shadowRoot' \
                             '.querySelector("#lgblnfidahcdcjddiepkckcfdhpknnjh")' \
                             '.shadowRoot.querySelector("#enable-toggle").click()'

    interact_ad(browser, Urls.COCCOC_EXTENSIONS, script_get_attribute_aria_pressed, script_click_ads_block, 'disable')
    yield
    interact_ad(browser, Urls.COCCOC_EXTENSIONS, script_get_attribute_aria_pressed, script_click_ads_block, 'enable')
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

