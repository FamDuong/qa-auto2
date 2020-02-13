from selenium.webdriver.common.by import By


class SettingsPageLocators(object):
    SETTINGS_UI_TEXT = 'settings-ui'
    SETTINGS_MAIN_TEXT = 'settings-main'
    SETTINGS_BASIC_PAGE_TEXT = 'settings-basic-page'
    SETTINGS_ABOUT_TEXT = 'settings-about-page'
    SETTINGS_ON_START_UP_PAGE_TEXT = 'settings-on-startup-page'
    SETTINGS_LANGUAGES_PAGE_TEXT = 'settings-languages-page'
    SETTINGS_START_UP_URLS_PAGE_TEXT = 'settings-startup-urls-page'
    SETTINGS_DEFAULT_BROWSER_PAGE_TEXT = 'settings-default-browser-page'
    SETTINGS_COCCOC_SECTION_PAGE_TEXT = 'settings-section'
    SETTINGS_COCCOC_TORRENTS_PAGE_TEXT = 'settings-coccoc-torrents-page'
    SETTINGS_DEFAULT_BROWSER_SECONDARY_TEXT = 'div.secondary'
    SETTINGS_DEFAULT_BROWSER_BUTTON_TEXT = 'cr-button'
    SETTINGS_TOGGLE_BUTTON_TEXT = 'settings-toggle-button'
    SETTINGS_SYSTEM_START_UP_CONTROL_TEXT = '#control'
    SETTINGS_ABOUT_RELAUNCH_BROWSER_TEXT = '#relaunch'

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

    EXTENSION_MAIN = 'extensions-manager'
    EXTENSION_TOOLBAR = 'extensions-toolbar'
    EXTENSION_LIST = '#items-list'
    EXTENSION_NAME = '#name'
    EXTENSION_VERSION = '#version'
    EXTENSION_BTN_UPDATE = '#updateNow'
    EXTENSION_NOTIFY_PARENT = 'cr-toast-manager'
    EXTENSION_NOTIFY = '#toast[open]'
    EXTENSION_TOGGLE = '#enable-toggle'
    EXTENSION_TOGGLE_DEV_MODE = '#devMode'
    EXTENSION_DICTIONARY_ID = '#gfgbmghkdjckppeomloefmbphdfmokgd'
    EXTENSION_SAVIOR_ID = '#jdfkmiabjpfjacifcmihfdjhpnjpiick'
    EXTENSION_RUNGRINH_ID = '#paenbjlckelooppiepeiechkeehogoha'
    EXTENSION_MOJICHAT_ID = '#paenbjlckelooppiepeiechkeehogoha'

    ABOUT_MESSAGE = '#updateStatusMessage > div'

    class SettingsAdsBlockPageLocators(object):
        SUB_RESOURCE_FILTER_PAGE = 'settings-coccoc-subresource-filter-page'
        CURRENT_BLOCK_MOD = '#subLabel'
        SETTINGS_DROP_DOWN_MENU = 'settings-dropdown-menu'
        DROP_DOWN_MENU = '#dropdownMenu'


class SettingsDownloadPageLocators(object):

    AUTOMATIC_STOP_SEEDING_TORRENTS_CHECK_BOX = '[id="checkbox"]'

