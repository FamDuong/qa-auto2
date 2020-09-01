import pytest
from pytest_testrail.plugin import pytestrail

import settings_master as settings
import testscripts.smoketest.common as common
from models.pagelocators.settings import SettingsPageLocators
from models.pageobject.extensions import GoogleExtensionsStorePageObject
from testscripts.download_coc_coc.common import set_driver
from utils_automation.const import Urls
from models.pageobject.settings import SettingsPageObject


class TestExtensionUpdate:
    settings_page_object = SettingsPageObject()
    google_extension_store_object = GoogleExtensionsStorePageObject()

    @pytest.fixture()
    def get_rung_rinh_extension_version_from_google_store(self):
        from selenium import webdriver
        driver = set_driver(driver_choice="CHROME")
        from utils_automation.const import ChromeStoreUrls
        driver.get(ChromeStoreUrls.RUNG_RINH_EXTENSION_URL)
        settings.EXTENSION_VERSION_RUNGRINH = self.google_extension_store_object.get_rung_rinh_extension_version(driver)
        driver.quit()

    # Precondition: Machine is installed Coc Coc
    @pytestrail.case('C44861')
    @pytestrail.defect('BR-1426', 'BR-1438')
    def test_if_coccoc_forced_install_extensions_can_be_updated_or_not(self, get_rung_rinh_extension_version_from_google_store):
        # Deactivate host because currently extension release directly to production
        common.interact_dev_hosts("deactivate")
        common.cleanup()
        driver = common.coccoc_instance()
        try:
            # Open Coc Coc Extension page
            driver.get(Urls.COCCOC_EXTENSIONS)
            # Update extension
            self.settings_page_object.update_extension(driver)
            import time
            time.sleep(10)
            # Verify extension version DICTIONARY/ SAVIOR/ RUNGRINH
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_DICTIONARY_ID,
                                                               settings.EXTENSION_VERSION_DICTIONARY)
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_SAVIOR_ID,
                                                               settings.EXTENSION_VERSION_SAVIOR)
            rung_rinh_extension_version = self.settings_page_object.get_extension_version(driver, SettingsPageLocators.EXTENSION_RUNGRINH_ID)
            from packaging import version
            assert version.parse(rung_rinh_extension_version) == version.parse(settings.EXTENSION_VERSION_RUNGRINH)
        finally:
            driver.quit()
            common.interact_dev_hosts("activate")
