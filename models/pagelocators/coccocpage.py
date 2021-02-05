from selenium.webdriver.common.by import By


class CocCocPageLocators:
    # Element on http://dev.coccoc.com/
    BUTTON_DOWNLOAD = (By.XPATH, '//div[@class="text-center"]')
    BUTTON_PRIVACY = (By.XPATH, '//div[@class="popup-download-bottom"]/a[@class="green-btn"]')

    URL_DOWNLOAD_WIN_EN = (By.XPATH, '//a[@class="btn-download-en download-link" and @data-os="win"]')
    URL_DOWNLOAD_WINXP_VI = (By.XPATH, '//a[@class="btn-download-en download-link" and @data-os="oldwin"]')
    URL_DOWNLOAD_MAC = (By.XPATH, '//a[@class="btn-download-en download-link" and @data-os="mac"]')

    # Element on https://coccoc.com/
    PRO_BUTTON_DOWNLOAD = (By.XPATH, '(//div[ contains(@class,"btn__download__coccoc")])[2]')
    PRO_LANGUAGE_FLAG = (By.XPATH, '//a[@lang="en-US"]')
    PRO_TOI_DA_HIEU_VA_DONG_Y_BTN = (By.XPATH, "//div[contains(@class,'show-modal-download')]//a[contains(@href,'thanks')]")
    PRO_TOI_DA_HIEU_VA_DONG_Y_CSS = 'div[class*="show-modal-download"] a[href*="thanks"]'