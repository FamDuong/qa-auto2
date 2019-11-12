from selenium.webdriver.common.by import By


class ExtensionsPageLocators:
    EXTENSIONS_MANAGER_TEXT = 'extensions-manager'
    EXTENSIONS_ITEM_LIST = 'extensions-item-list'
    EXTENSIONS_ITEM_CONTAINER_CSS = '[id="content-wrapper"]'
    EXTENSIONS_ITEM = 'extensions-item'
    EXTENSION_ITEM_ID = 'jdfkmiabjpfjacifcmihfdjhpnjpiick'
    EXTENSION_DETAIL_BUTTON = 'detailsButton'

    SAVIOR_EXTENSIONS_WRAPPER_ID = 'jdfkmiabjpfjacifcmihfdjhpnjpiick'
    SAVIOR_EXTENSION_NAME_TEXT = 'Cốc Cốc Savior'

    class UblockPlusPageLocators:
        UBLOCK_PLUS_ID_CSS_LOCATOR = '#oofnbdifeelbaidfgpikinijekkjcicg'
        ENABLE_TOGGER_BTN = '#enable-toggle'
        KNOB_BTN = '#knob'


class SaviorDetailsPageLocators:
    SAVIOR_INCOGNITO_ENABLE_BUTTON_CSS = '[id="crToggle"]'
    SAVIOR_ENABLE_BUTTON_CSS = '#enable-toggle'
    EXTENSION_DETAIL_VIEW = 'extensions-detail-view'
    EXTENSION_TOGGLE_ROW = 'extensions-toggle-row'
    EXTENSION_OPTIONS_DIALOG = 'extensions-options-dialog'
    EXTENSION_OPTIONS = 'extensionoptions'
    CR_ICON_BUTTON = 'cr-icon-button'
    CR_LINK_ROW = 'cr-link-row'
    EXTENSION_OPTIONS_ICON = '[id="icon"]'


class SaviorExtensionOptionsPageLocators:
    SHOW_INSTANT_DOWNLOAD_YOUTUBE = (By.ID, 'instant-button-download')
    SAVE_AND_CLOSE_BTN = (By.ID, 'button')
    SHOW_DOWNLOAD_BTN_NEAR_DOWNLOAD_MEDIA = (By.ID, 'on-page-buttons')

    VIDEO_QUALITY_HIGH_BTN = (By.XPATH, '//input[@name="optionsRadios" and @value="High"]')
    VIDEO_QUALITY_MEDIUM_BTN = (By.XPATH, '//input[@name="optionsRadios" and @value="Medium"]')
    VIDEO_QUALITY_LOW_BTN = (By.XPATH, '//input[@name="optionsRadios" and @value="Low"]')
    REMEMBER_LAST_CHOSEN_OPTION = (By.ID, 'prefer-last-quality')

