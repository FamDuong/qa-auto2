from selenium.webdriver.common.by import By


class SettingsPageLocators(object):

    SETTINGS_MAIN_TEXT = 'settings-main'
    SETTINGS_BASIC_PAGE_TEXT = 'settings-basic-page'
    SETTINGS_ON_START_UP_PAGE_TEXT = 'settings-on-startup-page'
    SETTINGS_LANGUAGES_PAGE_TEXT = 'settings-languages-page'
    OPEN_SPECIFIC_PAGE_OR_SET_OF_PAGES_TEXT = 'Open a specific page or set of pages'
    CONTINUE_WHERE_LEFT_OFF_TEXT = 'Continue where you left off'
    SHOW_LANGUAGE_OPTIONS_TEXT = 'Show language options'

    SETTINGS_UI = (By.TAG_NAME, 'settings-ui')
    SETTINGS_MAIN = (By.CSS_SELECTOR, 'settings-main')
    SETTINGS_BASIC_PAGE = (By.CSS_SELECTOR, 'settings-basic-page')
    SETTINGS_ON_START_UP_PAGE = (By.CSS_SELECTOR, 'settings-on-startup-page')
    SETTINGS_LANGUAGES_PAGE = (By.CSS_SELECTOR, 'settings-languages-page')
    OPEN_SPECIFIC_PAGE_OR_SET_OF_PAGES = (By.CSS_SELECTOR, 'Open a specific page or set of pages')
    CONTINUE_WHERE_LEFT_OFF = (By.CSS_SELECTOR, 'Continue where you left off')
    SHOW_LANGUAGE_OPTIONS = (By.CSS_SELECTOR, 'Show language options')
