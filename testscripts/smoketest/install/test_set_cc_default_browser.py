from pytest_testrail.plugin import pytestrail
from testscripts.prepare_new_browser.test_install import TestInstall
from utils_automation.common import WindowsHandler
from utils_automation.const import Urls

windows_handler = WindowsHandler()
test_install = TestInstall()
from models.pageobject.settings import SettingsPageObject
settings_page_object = SettingsPageObject()


@pytestrail.case('C44842')
def test_check_if_user_see_message_default_browser_currently_cc(coccoc_install_instance_on_default_browser):
    coccoc_install_instance_on_default_browser.get(Urls.COCCOC_SETTINGS_DEFAULT)
    assert "Cốc Cốc is your default browser" in settings_page_object.get_text_default_browser_element(
        coccoc_install_instance_on_default_browser)
    try:
        from testscripts.smoketest.install.common import open_link_from_powershell
        open_link_from_powershell()
        from testscripts.smoketest.install.common import get_coccoc_process
        assert 'browser' in get_coccoc_process()
    finally:
        from testscripts.smoketest.install.common import kill_coccoc_process
        kill_coccoc_process()


@pytestrail.case('C44843')
def test_check_if_user_not_set_cc_default_browser_setting_page(coccoc_install_instance_set_not_default_browser):
    coccoc_install_instance_set_not_default_browser.get(Urls.COCCOC_SETTINGS_DEFAULT)
    assert "Cốc Cốc is not currently your default browser" in \
           settings_page_object.get_text_default_browser_element(coccoc_install_instance_set_not_default_browser)


@pytestrail.case('C44845')
def test_set_default_browser_coccoc_then_change_default_browser_to_chrome():
    from testscripts.smoketest.install.conftest import install_coccoc_with_default
    install_coccoc_with_default()
    from testscripts.smoketest.install.common import set_chrome_default_browser
    set_chrome_default_browser()
    from testscripts.smoketest.install.conftest import coccoc_instance
    driver = coccoc_instance()
    try:
        driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
        assert "Make Cốc Cốc the default browser" in settings_page_object.get_text_make_default_browser_element(driver)
    finally:
        driver.quit()


@pytestrail.case('C44846')
def test_check_if_dialog_coccoc_is_not_your_default_after_1_month():
    from testscripts.smoketest.install.common import install_coccoc_not_set_as_default
    from testscripts.smoketest.install.common import check_if_coccoc_is_installed
    if check_if_coccoc_is_installed():
        from testscripts.smoketest.install.common import uninstall_coccoc_silently
        uninstall_coccoc_silently()
    install_coccoc_not_set_as_default()
    from testscripts.smoketest.install.common import set_system_date_to_after_30_days
    from testscripts.smoketest.install.common import set_system_date_to_before_30_days
    from testscripts.smoketest.install.conftest import coccoc_instance
    driver = coccoc_instance()
    try:
        set_system_date_to_after_30_days()
        driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
        assert "Make Cốc Cốc the default browser" in settings_page_object.get_text_make_default_browser_element(driver)
    finally:
        driver.quit()
        set_system_date_to_before_30_days()





