from models.pageelements.extensions import ExtensionsElement
from models.pageelements.settings import SettingsElements
from models.pageobject.extensions import ExtensionsPageObject
from models.pageobject.settings import SettingsPageObject


class TestBrowser:
    settings_cococ_ads_block_page_element = SettingsElements.SettingsAdsBlock()
    settings_coccoc_ads_block_page_object = SettingsPageObject.SettingsAdsBlockPageObject()

    extensions_cococ_page_element = ExtensionsElement.UblockPlusAdblockerElement()
    extensions_cococ_page_object = ExtensionsPageObject.UblockPlusPageObject()

    def test_debug(self):
        string = 'abc'
        print(type(string))
        assert type(string) == str










