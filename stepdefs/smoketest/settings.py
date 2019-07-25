import allure
from pytest_bdd import scenario, given, when, then
from models.pageelements.newtab import NewTabElement
from models.pageobject.settings import SettingsPageObject
import time


@allure.severity(severity_level="CRITICAL")
@scenario('../../features/smoketest/settings.feature', 'User choose settings when start up browser is opened a new '
                                                       'tab')
def test_click_start_up_new_tab():
    print("End of settings feature")


# @scenario('../../features/smoketest/settings.feature', 'Verify browser is opened with new tab')
# def test_browser_is_opened_with_new_tab():
#     print ("Browser is opened with new tab")


settings_page_object = SettingsPageObject()
new_tab_page = NewTabElement()


@given("Navigate to '<url>'")
def navigate_url(url, browser):
    browser.get(url)


@when("Choose open new tab when start up browser")
def choose_open_new_tab_option(browser):
    time.sleep(2)
    settings_page_object.click_open_new_tab(browser)


@then("Verify start up browser with new tab")
@when("Verify start up browser with new tab")
def verify_start_up_browser_new_tab():
    pass
    # global driver
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # url = driver.current_url.__str__()
    # assert url.find("data") > -1


@then("Revert to default settings for start up browser")
def revert_default_settings():
    pass
    # global driver
    # driver.get('coccoc://settings')
    # time.sleep(2)
    # settings_page_object.click_open_new_tab(driver)
    # driver.quit()

    # time.sleep(3)
    # most_visited_element = new_tab_page.find_most_visited_element(browser)
    # most_visited_element.is_displayed()
