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
    STICKER_SUGGESTION_INDEX0 = 'div.show-suggestions:nth-child(0)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX1 = 'div.show-suggestions:nth-child(1)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX2 = 'div.show-suggestions:nth-child(2)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX3 = 'div.show-suggestions:nth-child(3)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX4 = 'div.show-suggestions:nth-child(4)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX5 = 'div.show-suggestions:nth-child(5)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX6 = 'div.show-suggestions:nth-child(6)>#sticker-suggestion'
    THANK_YOU_LBL = 'div.onboarding-header-text'
    DA_HIEU_BTN = 'div.onboarding-footer #close'

    # First time open moji on big chat (messenger.com)
    MOJI_SHADOW_PARENT_BIG_CHAT = '#cch_fc08ea6a9ab05 div.moji-icon > div'
    CLICK_VAO_HINH_DE_GUI_NHE_SHADOW_PARENT_BIG_CHAT = "#cch_fc08ea6a9ab05 div[aria-label='Tin nhắn mới'] div:nth-child(1)"
    STICKER_SUGGESTION_PARENT_BIG_CHAT = "#cch_fc08ea6a9ab05 div[aria-label='Tin nhắn mới'] div.chat-suggestion-container"
    STICKER_SUGGESTION_INDEX7 = 'div.show-suggestions:nth-child(7)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX8 = 'div.show-suggestions:nth-child(8)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX9 = 'div.show-suggestions:nth-child(9)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX10 = 'div.show-suggestions:nth-child(10)>#sticker-suggestion'
    STICKER_SUGGESTION_INDEX11 = 'div.show-suggestions:nth-child(11)>#sticker-suggestion'
