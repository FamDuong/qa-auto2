from models.pageelements.extensions import ExtensionsElement
from models.pageelements.settings import SettingsElements
from models.pageobject.extensions import ExtensionsPageObject
from models.pageobject.settings import SettingsPageObject
from utils_automation.const import Urls
from utils_automation.setup import WaitAfterEach


class TestBrowser:
    settings_cococ_ads_block_page_element = SettingsElements.SettingsAdsBlock()
    settings_coccoc_ads_block_page_object = SettingsPageObject.SettingsAdsBlockPageObject()

    extensions_cococ_page_element = ExtensionsElement.UblockPlusAdblockerElement()
    extensions_cococ_page_object = ExtensionsPageObject.UblockPlusPageObject()

    def test_debug(self, browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        WaitAfterEach.sleep_timer_after_each_step()
        self.extensions_cococ_page_object.interact_with_ublock_knob_btn(browser, action='enable')










