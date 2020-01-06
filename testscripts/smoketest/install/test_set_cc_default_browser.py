import time

from pytest_testrail.plugin import pytestrail
from pywinauto import Desktop

from testscripts.prepare_new_browser.test_install import TestInstall
from utils_automation.common import WindowsHandler
from utils_automation.const import Urls

windows_handler = WindowsHandler()
test_install = TestInstall()


@pytestrail.case('C44842')
def test_check_if_user_see_message_default_browser_currently_cc(coccoc_install_instance_on_default_browser):
    coccoc_install_instance_on_default_browser.get(Urls.COCCOC_SETTINGS_DEFAULT)
    from models.pageobject.settings import SettingsPageObject
    settings_page_object = SettingsPageObject()
    assert "Cốc Cốc is your default browser" in settings_page_object.get_text_default_browser_element(
        coccoc_install_instance_on_default_browser)


@pytestrail.case('C44843')
def test_check_if_user_set_cc_default_browser_setting_page(coccoc_install_instance_set_not_default_browser):
    coccoc_install_instance_set_not_default_browser.get(Urls.COCCOC_SETTINGS_DEFAULT)
    from models.pageobject.settings import SettingsPageObject
    settings_page_object = SettingsPageObject()
    assert "Cốc Cốc is not currently your default browser" in \
           settings_page_object.get_text_default_browser_element(coccoc_install_instance_set_not_default_browser)



