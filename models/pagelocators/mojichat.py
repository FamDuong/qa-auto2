from selenium.webdriver.common.by import By

class MojichatLocators:

    BIG_CHAT = "big_chat"

    BIG_CHAT_INPUT = (By.XPATH, '//div[@aria-label="New message"]//*[@data-text="true"]')
    BIG_CHAT_BTN_SEND = (By.XPATH, '//*[text()="Send"]')
    BIG_CHAT_BTN_SEND_A_LIKE = (By.XPATH, '//*[@title="Send a Like"]')

    # MOJI_SUGGESTION_PANEL = '[class="chat-suggestion-container"]'
    MOJI_SUGGESTION_PANEL = (By.XPATH, '//div[@class="chat-suggestion-container"]')


    MESSAGE_FACEBOOK = (By.XPATH, '//*[@name="mercurymessages"]')
    SMALL_CHAT_INPUT = (By.XPATH, '//*[@data-text="true"]')
    SMALL_CHAT_BTN_SEND = (By.XPATH, '//*[@data-tooltip-content="Press Enter to send"]')