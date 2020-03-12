from selenium.webdriver.common.by import By


class ChromeStorePageLocators:
    SEARCH_THE_STORE_TXT_ID = 'searchbox-input'

    GOOGLE_TRANSLATE_LINK_XPATH = "(//div[contains(text(),'Google Translate')])[1]"
    # Detail page
    ADD_TO_CHROME_BTN_XPATH = "(//div[@aria-label='Add to Chrome'])[1]"
    # EXTESION_NAME_LBL_XPATH = "//h1"
    # VERSION_LBL_XPATH = "//span[text()='Version']//following-sibling::span[1]"
    # ADD_EXTENSION_PANEL = 'Chrome Web Store - flash - Cốc Cốc'
    # ADD_EXTENSION_BTN = 'Add extension'