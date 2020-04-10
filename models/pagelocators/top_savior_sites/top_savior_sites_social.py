from selenium.webdriver.common.by import By


class MessengerLocators(object):
    LOGIN_BUTTON_LOCATOR_BY_ID = 'loginbutton'
    LOGIN_BUTTON_LOCATOR = (By.ID, 'loginbutton')
    EMAIL_FIELD_LOCATOR = (By.ID, 'email')
    PASSWORD_FIELD_LOCATOR = (By.ID, 'pass')
    KEEP_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="loginform"]/div/div/label[1]/span')












