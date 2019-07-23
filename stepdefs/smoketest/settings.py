from pytest_bdd import scenario, given, when, then

from models.pageobject.settings import SettingsPageObject


@scenario('./../../features/smoketest/settings.feature', 'User choose settings when start up browser is opened a new '
                                                         'tab')
def test_setting():
    print("End of settings feature")


@given("Navigate to '<url>'")
def step_impl(url):
    raise NotImplementedError(u'STEP: Given Navigate to \'<url>\'')


@when("Choose '<option>' when start up browser")
def step_impl(option):
    SettingsPageObject.click_continue_where_left_off_button()


@then("Verify start up browser with new tab")
def step_impl():
    raise NotImplementedError(u'STEP: Then Verify start up browser with new tab')


@then("Revert to default settings for start up browser")
def step_impl():
    raise NotImplementedError(u'STEP: Then Revert to default settings for start up browser')
