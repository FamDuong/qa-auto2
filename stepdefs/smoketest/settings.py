from pytest_bdd import scenario, given, when, then
from models.pageelements.newtab import NewTabElement
from models.pageobject.settings import SettingsPageObject
import time


@scenario('../../features/smoketest/settings.feature', 'User choose settings when start up browser is opened a new '
                                                       'tab')
def test_setting():
    print("End of settings feature")


settings_page_object = SettingsPageObject()
new_tab_page = NewTabElement()


@given("Navigate to '<url>'")
def navigate_url(url, browser):
    browser.get(url)


@when("Choose '<option>' when start up browser")
def choose_open_new_tab_option(option, browser):
    time.sleep(2)
    settings_page_object.click_open_new_tab(browser)


@then("Verify start up browser with new tab")
def verify_start_up_browser_new_tab(browser):
    pass
    # browser.close()
    # browser.get('')


@then("Revert to default settings for start up browser")
def revert_default_settings(browser):
    pass
    # time.sleep(1)
    # most_visited_element = new_tab_page.find_most_visited_element(browser)
    # most_visited_element.is_displayed()
