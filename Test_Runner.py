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
        current_url = 'http://game.kul.vn/cuuthien3250/landing-page12.html?utm_source=1&utm_medium=CPC&utm_campaign=C%E1%BB%ADu%20Thi%C3%AAn%20Phong%20Th%E1%BA%A7n%203%5FIcon&utm_term=*&utm_content=25344477'
        for utm_type in ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term']:
            import re
            assert re.search(rf'{utm_type}=[a-zA-Z0-9*]', current_url) is not None

    def test_singleton(self):
        from utils_automation.common import FilesHandle
        instance_1 = FilesHandle()
        instance_2 = FilesHandle()
        print(f"Instance 1 is : {instance_1} \n")
        print(f"Instance 2 is : {instance_2} \n")










