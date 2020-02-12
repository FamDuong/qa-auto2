from pytest_testrail.plugin import pytestrail

import settings_master as settings
from models.pagelocators.settings import SettingsPageLocators
from utils_automation.const import Urls
from models.pageobject.settings import SettingsPageObject


class TestExtensionUpdate:
    settings_page_object = SettingsPageObject()

    @pytestrail.case('C44861')
    def test_if_coccoc_forced_install_extensions_can_be_updated_or_not(self,
                                                                       activate_then_deactive_hosts_for_coccoc_dev):
        from testscripts.smoketest.common import cleanup
        cleanup()
        from testscripts.smoketest.common import coccoc_instance
        driver = coccoc_instance()
        try:
            driver.get(Urls.COCCOC_EXTENSIONS)
            self.settings_page_object.update_extension(driver)
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_DICTIONARY_ID,
                                                               settings.EXTENSION_VERSION_DICTIONARY)
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_SAVIOR_ID,
                                                               settings.EXTENSION_VERSION_SAVIOR)
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_RUNGRINH_ID,
                                                               settings.EXTENSION_VERSION_RUNGRINH)
        finally:
            driver.quit()
