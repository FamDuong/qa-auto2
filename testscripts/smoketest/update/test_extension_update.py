from pytest_testrail.plugin import pytestrail

import settings_master as settings
import testscripts.smoketest.common as common
from models.pagelocators.settings import SettingsPageLocators
from utils_automation.const import Urls
from models.pageobject.settings import SettingsPageObject


class TestExtensionUpdate:
    settings_page_object = SettingsPageObject()

    # Precondition: Machine is installed Coc Coc
    @pytestrail.case('C44861')
    def test_if_coccoc_forced_install_extensions_can_be_updated_or_not(self):
        # Deactivate host because currently extension release directly to production
        common.interact_dev_hosts("deactivate")
        common.cleanup()
        driver = common.coccoc_instance()
        try:
            # Open Coc Coc Extension page
            driver.get(Urls.COCCOC_EXTENSIONS)
            # Update extension
            self.settings_page_object.update_extension(driver)
            # Verify extension version DICTIONARY/ SAVIOR/ RUNGRINH
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_DICTIONARY_ID,
                                                               settings.EXTENSION_VERSION_DICTIONARY)
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_SAVIOR_ID,
                                                               settings.EXTENSION_VERSION_SAVIOR)
            self.settings_page_object.verify_extension_version(driver, SettingsPageLocators.EXTENSION_RUNGRINH_ID,
                                                               settings.EXTENSION_VERSION_RUNGRINH)
        finally:
            driver.quit()
