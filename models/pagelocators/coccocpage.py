from selenium.webdriver.common.by import By


class CocCocPageLocators:

    BUTTON_DOWNLOAD = (By.XPATH, '//div[@class="text-center"]')
    BUTTON_PRIVACY = (By.XPATH, '//div[@class="popup-download-bottom"]/a[@class="green-btn"]')

    URL_DOWNLOAD_WIN_EN = (By.XPATH, '//a[@class="btn-download-en download-link" and @data-os="win"]')
    URL_DOWNLOAD_WINXP_VI = (By.XPATH, '//a[@class="btn-download-en download-link" and @data-os="oldwin"]')
    URL_DOWNLOAD_MAC = (By.XPATH, '//a[@class="btn-download-en download-link" and @data-os="mac"]')