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


class SaviorDetailsPageLocators:
    EXTENSION_DETAIL_CR_CHECKBOX = 'cr-checkbox'
    SAVIOR_ENABLE_BUTTON_CSS = '[id="checkbox"]'
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
    REMEMBER_LAST_CHOSEN_OPTION = (By.ID, 'prefer-last-quality')

