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

    def test_string_date(self):
        from utils_automation.date_time_utils import how_many_days_til_now
        import re
        string_date_time = 'Wed, 27/11/2019 | 19:10 GMT+7'
        check_if_found_regex = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}', string_date_time)
        if check_if_found_regex is not []:
            date_found = re.search('[0-9]{2}/[0-9]{2}/[0-9]{4}', string_date_time).group(0)
            print(date_found)
            print(how_many_days_til_now(date_found))
        else:
            print("Not found that regex")










