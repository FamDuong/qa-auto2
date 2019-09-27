from selenium.webdriver.common.by import By


class SettingsPageLocators(object):
    SETTINGS_UI_TEXT = 'settings-ui'
    SETTINGS_MAIN_TEXT = 'settings-main'
    SETTINGS_BASIC_PAGE_TEXT = 'settings-basic-page'
    SETTINGS_ON_START_UP_PAGE_TEXT = 'settings-on-startup-page'
    SETTINGS_LANGUAGES_PAGE_TEXT = 'settings-languages-page'
    SETTINGS_START_UP_URLS_PAGE_TEXT = 'settings-startup-urls-page'
    SETTINGS_DEFAULT_BROWSER_PAGE_TEXT = 'settings-default-browser-page'
    SETTINGS_COCCOC_SECTION_PAGE_TEXT = 'settings-section'
    SETTINGS_COCCOC_TORRENTS_PAGE_TEXT = 'settings-coccoc-torrents-page'

    SETTINGS_DOWNLOAD_PAGE_TEXT = 'settings-downloads-page'

    OPEN_SPECIFIC_PAGE_OR_SET_OF_PAGES_TEXT = '[label="Open a specific page or set of pages"]'
    CONTINUE_WHERE_LEFT_OFF_TEXT = '[label="Continue where you left off"]'
    SHOW_LANGUAGE_OPTIONS_TEXT = '[label="Show language options"]'
    OPEN_NEW_TAB_PAGE_TEXT = '[label="Open the New Tab page"]'
    ADD_A_NEW_PAGE_TEXT = '[id="addPage"]'

    DEFAULT_BROWSER_RUN_AUTO_ONSTARTUP = '[label="Run automatically on system startup"]'
    DEFAULT_BROWSER_RUN_AUTO_ONSTARTUP_CHECKBOX = '[aria-label="Run automatically on system startup"]'

    DEFAULT_TORRENT_CLIENT_TEXT = '[class="settings-box two-line"]'

    SETTINGS_MAX_NUMBER_OF_CONNECTION_TORRENT = '[size="6"]'

    DEFAULT_DOWNLOAD_PATH_TEXT = '#defaultDownloadPath'


class SettingsDownloadPageLocators(object):

    AUTOMATIC_STOP_SEEDING_TORRENTS_CHECK_BOX = '[id="checkbox"]'

