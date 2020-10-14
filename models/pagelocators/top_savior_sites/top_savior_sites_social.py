from selenium.webdriver.common.by import By


class MessengerLocators(object):
    LOGIN_BUTTON_LOCATOR_BY_ID = 'loginbutton'
    LOGIN_BUTTON_LOCATOR = (By.ID, 'loginbutton')
    EMAIL_FIELD_LOCATOR = (By.ID, 'email')
    PASSWORD_FIELD_LOCATOR = (By.ID, 'pass')
    KEEP_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="loginform"]/div/div/label[1]/span')

class FacebookLocators(object):
    HOME_PAGE_FIRST_VIDEO = (By.XPATH, '(//div[@aria-label="Change Position"])[1]//ancestor::div[contains(@data-instancekey,"id-vpuid")]//parent::div//video')
    # VTV_GIAITRI_PAGE_FIRST_VIDEO = (By.XPATH, '(//div[@data-ad-comet-preview="message"]//ancestor::div[@dir="auto" and @class=""]//following-sibling::div//video)[1]')
    VTV_GIAITRI_PAGE_FIRST_VIDEO = (By.XPATH, '(//div[@aria-label="Viết bình luận"]//ancestor::div[@data-testid="Keycommand_wrapper"]//video)[1]')
    VTV_GIAITRI_DONG_DOAN_CHAT_BTN = (By.XPATH, '//div[@aria-label="Đóng đoạn chat"]')










