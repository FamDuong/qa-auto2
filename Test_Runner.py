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

    def test_debug(self):
        current_url = 'http://game.kul.vn/cuuthien3250/landing-page12.html?utm_source=%&utm_medium=CPC&utm_campaign=C%E1%BB%ADu%20Thi%C3%AAn%20Phong%20Th%E1%BA%A7n%203%5FIcon&utm_term=Entertainment&utm_content=25344477'
        for utm_type in ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term']:
            import re
            assert re.search(rf'\b(\w*{utm_type}=\w*)\b(?!\s*$).+', current_url) is not None










