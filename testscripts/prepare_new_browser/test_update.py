from testscripts.prepare_new_browser.test_install import TestInstall
from pytest_testrail.plugin import pytestrail
from utils_automation.const import Urls
from models.pageelements.settings import SettingsPageLocators
import settings_master as settings


class TestUpdate(TestInstall):

    @pytestrail.case('C44861')
    def test_if_coccoc_forced_install_extensions_can_be_updated_or_not(self, browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.setting_page_object.update_extension(browser)
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_DICTIONARY_ID, settings.EXTENSION_VERSION_DICTIONARY)
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_SAVIOR_ID, settings.EXTENSION_VERSION_SAVIOR)
        self.setting_page_object.verify_extension_version(browser, SettingsPageLocators.EXTENSION_RUNGRINH_ID, settings.EXTENSION_VERSION_RUNGRINH)

    @pytestrail.case('C44862')
    def test_that_Rung_Rinh_extension_which_has_been_disabled_on_old_version_can_NOT_be_enabled_after_updating_browser(self, browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.setting_page_object.disable_extension(browser, SettingsPageLocators.EXTENSION_RUNGRINH_ID)
        browser.get(Urls.COCCOC_ABOUT)
        self.setting_page_object.update_cc_version(browser)
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.setting_page_object.verify_extension_status(browser, SettingsPageLocators.EXTENSION_RUNGRINH_ID, "True")

