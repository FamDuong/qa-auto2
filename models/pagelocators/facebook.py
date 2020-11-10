class FacebookPageLocators:
    EMAIL_TXT_ID = 'email'
    PASS_TXT_ID = 'pass'
    SUBMIT_BTN_XPATH = '//button[@data-testid="royal_login_button"]'
    SHOW_MENU_SETTING_ICON_XPATH = 'userNavigationLabel'
    COCCOC_AT_NAME_XPATH = "//span[text()='Hangnt Cốc Cốc']"
    LOGOUT_BTN_XPATH = "//a[contains(@data-gt,'menu_logout')]"
    EMAIL = 'hangnguyenat123@gmail.com'
    PASS = 'hangnguyenat123123@'

    FACEBOOK_MESSAGE_SMALL_ICON_XPATH = "//a[@name='mercurymessages']"
    USER_NAME_ON_CHAT_TOOL_TIP_XPATH = "//a[@class='messagesContent']//span[text()='Coc Cốc Bảy']"
    NHAN_TIN_BTN_XPATH = "//a[contains(@data-store,'action_bar_message')]"

class FacebookMessagePageLocators:
    CONTINUE_WITH_USER_BTN_XPATH = "//span[text()='Tiếp tục dưới tên ']//ancestor-or-self::button"
    XEM_TAT_CA_TRONG_MESSAGE_BTN_XPATH = "//a[@href='/messages/t/']"
    TUY_CHON_BTN_XPATH = "//div[@class='clearfix titlebar']//a[@aria-label='Tùy chọn']"
    OPEN_MENU_XPATH = "//a[@data-href='https://www.facebook.com/messages/t/100010842734556']/ancestor::li//div[@aria-label='Hành động trong cuộc trò chuyện']"
    XOA_CUOC_TRO_TRUYEN_XPATH = "//span[text()='Xóa']"
    XOA_CUOC_TRO_TRUYEN_CONFIRM_XPATH = "//button[text()='Xóa']"
    SENT_STICKER_IMAGE = "//div[contains(@aria-label,'Nhãn dán')]"
    SENT_STICKER_MOJI = "//span[text()='Coc Coc MojiChat']"
