from selenium.webdriver.common.by import By


class SettingsPageLocators(object):
    SETTINGS_UI_TEXT = 'settings-ui'
    SETTINGS_MENU_TEXT = 'settings-menu'
    SETTINGS_MENU_PEOPLE_LBL = '#people'
    SETTINGS_MENU_AUTO_FILL_LBL = '#autofill'
    SETTINGS_MENU_DEFAULT_BROWSER_LBL = '#defaultBrowser'
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
    SETTINGS_DEFAULT_BROWSER_IS_DEFAULT_TEXT = '#isDefault'
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
    EXTENSION_AD_BLOCK_PLUS = '#jeoooddfnfogpngdoijplcijdcoeckgm'
    EXTENSIONS_ITEM_LIST = '#items-list'
    EXTENSIONS_CONTENT_WRAPPER = '#content-wrapper > div:nth-child(5)'
    EXTENSIONS_DETAIL_BUTTON = '#detailsButton'

    ABOUT_MESSAGE = '#updateStatusMessage > div'

    class SettingsAdsBlockPageLocators(object):
        SUB_RESOURCE_FILTER_PAGE = 'settings-coccoc-subresource-filter-page'
        CURRENT_BLOCK_MOD = '#subLabel'
        SETTINGS_DROP_DOWN_MENU = 'settings-dropdown-menu'
        DROP_DOWN_MENU = '#dropdownMenu'


class SettingsDownloadPageLocators(object):
    AUTOMATIC_STOP_SEEDING_TORRENTS_CHECK_BOX = '[id="checkbox"]'


class SettingsComponentsPageLocators(object):
    CHECK_FOR_UPDATE_BUTTON = '//button[@class="button-check-update"]'
    COMPONENT_VERSION_ELEMENT = '//span[@jscontent="version"]'


class SettingsClearBrowserDataLocators(object):
    SETTINGS_MAIN = '#main'
    SETTINGS_PRIVACY_PAGE = 'settings-privacy-page'
    SETTINGS_CLEAR_BROWSING_DATA_DIALOG = 'settings-clear-browsing-data-dialog'
    SETTINGS_CLEAR_FROM_BASIC = '#clearFromBasic'
    SETTINGS_CLEAR_DATA_BUTTON = 'cr-button#clearBrowsingDataConfirm'

    SETTINGS_TIME_RANGE_DROPDOWN_MENU = '#dropdownMenu'
    SETTINGS_BROWSING_HISTORY_CHECKBOX_BASIC = '#browsingCheckboxBasic'
    SETTINGS_BROWSING_COOKIES_CHECKBOX_BASIC = '#cookiesCheckboxBasic'
    SETTINGS_BROWSING_CACHED_CHECKBOX_BASIC = '#cacheCheckboxBasic'
    SETTINGS_BROWSING_CHECKBOX = 'cr-checkbox#checkbox'
    SETTINGS_BROWSING_CHILD_CHECKBOX = 'div#checkbox'


class SettingsDarkmodeLocators(object):
    SETTINGS_ANIMATED_PAGE = 'settings-animated-pages'
    SETTINGS_SUB_PAGE = 'settings-subpage'
    SETTINGS_CATEGORY_DEFAULT_SETTING = 'category-default-setting'
    SETTINGS_RADIO_GROUP = 'settings-radio-group'
    SETTINGS_CONTROLLED_RADIO_BUTTON = 'controlled-radio-button'
    SETTINGS_DARKMODE_LABEL = 'span#label'
    # SETTINGS_DARKMODE_ICON_FOR_SITE = "//*[@ControlType='ControlType.Button' and @Name='Enable/Disable Coc Coc Dark Mode on this site']"
    # SETTINGS_DARKMODE_ICON_FOR_SITE = "//*[contains(@ControlType,'ControlType.Button') and contains(@name,'Enable/Disable Coc Coc Dark Mode on this site')]"
    SETTINGS_DARKMODE_ICON_FOR_SITE = "//*[contains(name(), 'Dark Mode')]"
    COMPONENT_DARKMODE_BUTTON = '//*[@id="hlihchmekigeljcmpkkkhlojcmhjgjpa"]'
    # Big monitors
    # SETTINGS_DARKMODE_TOGGLE_COORDINATES = (1010, -754)
    # ICON_DARKMODE_COORDINATES = (1945, -1027)
    # ICON_DARKMODE_SWITCH_COORDINATES = (1921, -894)
    # Small monitors
    SETTINGS_DARKMODE_TOGGLE_COORDINATES = (498, 280)
    SETTINGS_DARKMODE_OPTION_COORDINATES = (571, 329)
    ICON_DARKMODE_COORDINATES = (1144, 53)
    ICON_DARKMODE_SWITCH_COORDINATES = (1118, 224)
    ICON_DARKMODE_SWITCH_COORDINATES_IS_EXCEPTION = (1118, 188)
    SETTINGS_DARK_MODE_CATEGORY_DEFAULT_SETTING = 'category-default-setting'
    SETTINGS_DARK_MODE_CONTROLLED_RADIO_BUTTON1 = 'controlled-radio-button:nth-child(1)'
    SETTINGS_DARK_MODE_RADIO_BOX = '#button'
    SETTINGS_COCCOC_DARK_MODE_PAGE = 'settings-coccoc-dark-mode-page'
    SETTINGS_COCCOC_DARK_MODE_PAGE_BAR = '#bar'
