

Feature: Allow regular users to change settings of browser

  Scenario Outline: User choose settings when start up browser is opened a new tab
    Given Navigate to '<url>'
    When Choose open new tab when start up browser
    Examples:
    |url|
    |coccoc://settings|
