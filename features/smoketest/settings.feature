
@settings
Feature: Allow regular users to change settings of browser

  Scenario Outline: User choose settings when start up browser is opened a new tab
    Given Navigate to '<url>'
    When Choose '<option>' when start up browser
    Then Verify start up browser with new tab
    Then Revert to default settings for start up browser
    Examples:
    |url|option|
    |coccoc://settings|Open the New Tab page|