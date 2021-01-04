from selenium.webdriver.common.by import By


class MessengerLocators(object):
    LOGIN_BUTTON_LOCATOR_BY_ID = 'loginbutton'
    LOGIN_BUTTON_LOCATOR = (By.ID, 'loginbutton')
    EMAIL_FIELD_LOCATOR = (By.ID, 'email')
    PASSWORD_FIELD_LOCATOR = (By.ID, 'pass')
    KEEP_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="loginform"]/div/div/label[1]/span')


class FacebookLocators(object):
    HOME_PAGE_FIRST_VIDEO = (By.XPATH,
                             '(//div[@aria-label="Change Position"])[1]//ancestor::div[contains(@data-instancekey,"id-vpuid")]//parent::div//video')
    # VTV_GIAITRI_PAGE_FIRST_VIDEO = (By.XPATH, '(//div[@data-ad-comet-preview="message"]//ancestor::div[@dir="auto" and @class=""]//following-sibling::div//video)[1]')
    VTV_GIAITRI_PAGE_FIRST_VIDEO = (By.XPATH, '(//div[@aria-label="Viết bình luận"]//ancestor::div[@role="article"]//video)[1]')
    # VIDEO_MO_RONG_FIRST_VIDEO = (By.XPATH, '//div[@data-pagelet="TahoeVideo"]')
    VIDEO_MO_RONG_FIRST_VIDEO = (By.CSS_SELECTOR, 'div[data-pagelet="TahoeVideo"] video')
    VTV_GIAITRI_DONG_DOAN_CHAT_BTN = (By.XPATH, '//div[@aria-label="Đóng đoạn chat"]')
    THACHTHUC_DANHHAI_VIDEO = (By.CSS_SELECTOR, '#permalink_video_pagelet video')
    WATCH_FIRST_VIDEO = (By.XPATH, '(//a[@aria-label="Mở rộng"])[1]')


class InstagramLocators(object):
    USER_NAME_LBL = '//a[text()="nganhanguyen0306"]'
    USER_AVATAR_NAV = '//nav//img[@data-testid="user-avatar"]'
    USER_NAME_TXT = '//input[@name="username"]'
    PASSWORD_TXT = '//input[@name="password"]'
    LOGIN_BTN = '//button[@type="submit"]'
    SAVE_INFO_BTN = '//button[text()="Save Info"]'
    LOGOUT_BTN = '//div[text()="Log Out"]'
    EMAIL = 'nganhanguyen0306@gmail.com'
    PASS = 'ha@123456'
    TURN_ON_NOTIFICATIONS_NOT_NOW = '//button[text()="Not Now"]'
    FIRST_VIDEO_HOME_PAGE_CSS = 'article:nth-child(1) video'
    FIRST_VIDEO_HOME_PAGE = (By.CSS_SELECTOR, 'article:nth-child(1) video')
