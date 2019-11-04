import pytest

from models.pageobject.settings import SettingsPageObject
from testscripts.common_setup import clear_data_download, delete_all_mp4_file_download
from utils_automation.const import Urls
from utils_automation.setup import WaitAfterEach


@pytest.fixture()
def clear_download_page_and_download_folder(browser, get_current_download_folder):
    yield
    clear_data_download(browser)
    delete_all_mp4_file_download(get_current_download_folder, '.mp4')


settings_page_object = SettingsPageObject()


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




