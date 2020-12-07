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
    VTC_PLAY_VIDEO_BTN = (By.CSS_SELECTOR, 'div[class*="display"] div[aria-label="Play"]')

    # TIKTOK_FIRST_VIDEO = 'div[class*="video-feed-item"]:nth-child(1) a'
    TIKTOK_FIRST_VIDEO = 'div[class*="video-feed-item"]:nth-child(1) a'
    # TIKTOK_LOGIN_BTN = (By.CSS_SELECTOR, 'div[class*="menu-right"] button[class*="login-button"]')
    TIKTOK_LOGIN_BY_FACEBOOK_OPTION = (By.XPATH, '//div[text()="Log in with Facebook"]')
    TIKTOK_EMAIL_TXT = (By.ID, 'email')
    TIKTOK_PASSWORD_TXT = (By.ID, 'pass')
    TIKTOK_LOGIN_SUBMIT_BTN= (By.XPATH, '//input[@type="submit"]')
    TIKTOK_AVATAR = (By.CSS_SELECTOR, 'div[class*="profile"] img')
    TIKTOK_AVATAR_CSS = 'div[class*="profile"] img'
    TIKTOK_LOGOUT_BTN = (By.XPATH, '//a[text()="Log out"]')
    TIKTOK_PROFILE_LBL_XPATH = '//p[text()="This user has not published any videos."]'
    TIKTOK_MENU_FOLLOWING = (By.XPATH, "//div[contains(@class,'nav-wrapper')]//span[contains(text(),'Following')]")
    TIKTOK_MENU_FOR_YOU = (By.XPATH, "//div[contains(@class,'nav-wrapper')]//span[contains(text(),'For You')]")


