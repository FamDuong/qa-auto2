from selenium.webdriver.common.by import By

class MojichatLocators:

    BIG_CHAT = "big_chat"
    SMALL_CHAT = "small chat"

    BIG_CHAT_INPUT = (By.XPATH, '//*[@data-text="true"]')
    BIG_CHAT_BTN_SEND = (By.XPATH, '//*[text()="Send"]')
    BIG_CHAT_BTN_SEND_A_LIKE = (By.XPATH, '//*[@title="Send a Like"]')

    SMALL_CHAT_INPUT = (By.XPATH, '//div[@data-contents="true"]//*[@data-text="true"]')
    SMALL_CHAT_BTN_SEND = (By.XPATH, '//*[@data-tooltip-content="Press Enter to send"]')

    # MOJI_SUGGESTION_PANEL = '[class="chat-suggestion-container"]'
    MOJI_SUGGESTION_PANEL = (By.XPATH, '//div[@class="chat-suggestion-container"]')
    MESSAGE_FACEBOOK = (By.XPATH, '//*[@name="mercurymessages"]')
    MOJI_ICON = '//div[@class="moji-icon"]'

    # First time open moji on small chat
    MOJI_SHADOW_PARENT = '#ChatTabsPagelet div.moji-icon>div'
    DE_XEM_NAO_BTN = '#next-state'
    DE_GO_THU_BTN = '#focus-input'
    CLICK_VAO_HINH_DE_GUI_NHE_SHADOW_PARENT = '#ChatTabsPagelet div.fbNubFlyoutFooter > div:nth-child(1)'
    CLICK_VAO_HINH_DE_GUI_NHE_LBL = 'div.onboarding-tooltip'
    # Sticker suggestion by index
    STICKER_SUGGESTION_PARENT = 'div.chat-suggestion-container'
    STICKER_SUGGESTION_INDEX = 'div.show-suggestions:nth-child({param1})>#sticker-suggestion'
    THANK_YOU_LBL = 'div.onboarding-header-text'
    DA_HIEU_BTN = 'div.onboarding-footer #close'

    # First time open moji on big chat (messenger.com)
    CLICK_VAO_HINH_DE_GUI_NHE_SHADOW_PARENT_BIG_CHAT = "div[aria-label='Tin nhắn mới'] div:nth-child(1)"
    MOJI_SHADOW_PARENT_BIG_CHAT = 'div.moji-icon > div'

    GAN_DAY_ICON = '#recent-stickers'
