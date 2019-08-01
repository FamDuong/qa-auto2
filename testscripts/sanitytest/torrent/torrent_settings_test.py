
import pytest
from pytest_testrail.plugin import pytestrail
from models.pageobject.settings import SettingsPageObject
from utils.const import Urls


class TestTorrentSettings:
    settings_page_object = SettingsPageObject()

    @pytestrail.case('C54205')
    def test_coccoc_as_torrent_client(self, browser):
        # Go to CocCoc Settings page

        browser.get(Urls.COCCOC_SETTINGS_URL)

        # Check for default torrent_settings
        value = self.settings_page_object.get_default_torrent_value(browser)
        assert value == 'The default torrent client is currently Cốc Cốc.'

    @pytest.mark.skip
    def test_default_torrent_settings(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)




