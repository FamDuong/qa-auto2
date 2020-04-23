from selenium.webdriver.common.by import By


class MojichatLocators:
    BIG_CHAT = "big_chat"
    SMALL_CHAT = "small chat"

    BIG_CHAT_INPUT = (By.XPATH, '//div[@aria-label="New message"]//*[@data-text="true"]')
    BIG_CHAT_BTN_SEND = (By.XPATH, '//*[text()="Send"]')
    BIG_CHAT_BTN_SEND_A_LIKE = (By.XPATH, '//*[@title="Send a Like"]')

    SMALL_CHAT_INPUT = (By.XPATH, '//div[@data-contents="true"]//*[@data-text="true"]/parent::span')
    SMALL_CHAT_BTN_SEND = (By.XPATH, '//a[@label="send"]')

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

    PANEL_SHADOW_PARENT = '#ChatTabsPagelet div.fbNubFlyoutFooter > div:nth-child(1)'
    GAN_DAY_ICON = '#recent-stickers'
    THINH_HANH_ICON = '#trending-stickers'
    ALBUM_ICON_INDEX = '#album:nth-child({param1})'
    GO_RIGHT_ICON = '#go-right'
    GO_LEFT_ICON = '#go-left'
    SEARCH_TXT = '#search-hashtags'
    TAT_TINH_NANG_GOI_Y_ICON = '#disable-suggestions'
    TRO_GIUP_ICON = '#open-guide-page'

    STICKER_SENT_GANDAY_INDEX = "div[class*='sticker-group recent']:nth-child({param1}) #sticker"
    ALBUM_TOOLTIP_KEYWORD_INDEX = "#album:nth-child({param1}) div[class='tooltip']"
    STICKER_KEYWORD_INDEX = "div[class='sticker-group trending']:nth-child({param1}) #keyword"
    PANEL_SHADOW_PARENT_SMALL_CHAT_BY_FACEBOOK_URL = "#ChatTabsPagelet div.fbNubFlyoutFooter > div:nth-child(3)"
    SHOW_MORE_STICKER = '#show-more'
    STICKER_IN_SHOW_MORE_INDEX1 = 'div.stickers-group #sticker-suggestion:nth-child(1)'
    STICKER_GROUP = '#show-more > div.more-stickers'
