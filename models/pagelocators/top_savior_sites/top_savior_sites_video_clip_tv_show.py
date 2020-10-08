from selenium.webdriver.common.by import By


class TopSaviorSitesVideoClipTvShowLocators:
    ZALO_USER_NAME = '0906215785'
    ZALO_PASSWORD = '123456@A'
    ZALO_USER_NAME_LBL = (By.XPATH, "//p[@class='username' and text()='hangnt2']")
    ZALO_WEB_URL = 'https://chat.zalo.me/'
    ZALO_USER_NAME_TXT = (By.ID, 'input-phone')
    ZALO_PASSWORD_TXT = (By.XPATH, '//input[@type="password"]')
    ZALO_DANG_NHAP_BTN = (By.XPATH, '//a[contains(@class, "block first")]')
    ZALO_AVATAR = (By.ID, 'avatar')
    TV_ZING_VN_DANG_NHAP_BANG_ZALO_BTN = (By.XPATH, '//a[@class="btn-default login-button"]')