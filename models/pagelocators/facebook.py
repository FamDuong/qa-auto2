class FacebookPageLocators:
    EMAIL_TXT_ID = 'email'
    PASS_TXT_ID = 'pass'
    SUBMIT_BTN_XPATH = '//input[@data-testid="royal_login_button"]'
    SHOW_MENU_SETTING_ICON_XPATH = 'userNavigationLabel'
    COCCOC_AT_NAME_XPATH = "//div[text()='Cốc Cốc AT']"
    LOGOUT_BTN_XPATH = "//a[contains(@data-gt,'menu_logout')]"
    EMAIL = 'hangnth123456@gmail.com'
    PASS = 'hangnth123456@@@'

    FACEBOOK_MESSAGE_SMALL_ICON_XPATH = "//a[@name='mercurymessages']"
    USER_NAME_ON_CHAT_TOOL_TIP_XPATH = "//a[@class='messagesContent']//span[text()='Coc Cốc Bảy']"


class FacebookMessagePageLocators:
    CONTINUE_WITH_USER_BTN_XPATH = "//span[text()='Tiếp tục dưới tên ']//ancestor-or-self::button"
