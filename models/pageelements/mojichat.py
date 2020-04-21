import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import WaitAfterEach


class MojichatElement(BasePageElement):
    # global chat_type

    # def __init__(self, type=MojichatLocators.BIG_CHAT):
    #     self.chat_type = type

    def click_on_tooltip_button(self, driver, button):
        element = self.find_tooltip_button(driver, button)
        element.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def find_tooltip_button(self, driver, button):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(button))

    def find_moji_on_suggestion_panel(self, driver, position):
        wait = WebDriverWait(driver, 20)
        # document.querySelector('[class="chat-suggestion-container"]')
        # document.querySelector('[class="chat-suggestion-container"]').shadowRoot
        # document.querySelector('[class="chat-suggestion-container"]').shadowRoot.querySelector('#sticker-suggestion')
        shadow_root = wait.until(ec.presence_of_element_located(MojichatLocators.MOJI_SUGGESTION_PANEL))
        element = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
        return element.find_elements_by_css_selector('#sticker-suggestion')[position]

    def find_small_chat_icon(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(MojichatLocators.MESSAGE_FACEBOOK))

    def find_user_chat(self, driver, user_chat):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located((By.XPATH, '//span[contains(text(),"' + user_chat + '")]')))

    def find_de_xem_nao_btn(self, driver):
        return self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT, MojichatLocators.DE_XEM_NAO_BTN)

    def find_de_go_thu_btn(self, driver, chat_type):
        de_go_thu_btn = None
        if chat_type in 'SMALL_CHAT':
            de_go_thu_btn = self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT,
                                                     MojichatLocators.DE_GO_THU_BTN)
        elif chat_type in 'BIG_CHAT':
            de_go_thu_btn = self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT_BIG_CHAT,
                                                     MojichatLocators.DE_GO_THU_BTN)
        return de_go_thu_btn

    def find_click_vao_hinh_de_gui_nhe_tool_tip(self, driver, chat_type):
        click_vao_hinh_de_gui_nhe_tool_tip = None
        if chat_type in 'SMALL_CHAT':
            click_vao_hinh_de_gui_nhe_tool_tip = self.find_shadow_element(driver,
                                                                          MojichatLocators.CLICK_VAO_HINH_DE_GUI_NHE_SHADOW_PARENT,
                                                                          MojichatLocators.CLICK_VAO_HINH_DE_GUI_NHE_LBL)
        elif chat_type in 'BIG_CHAT':
            click_vao_hinh_de_gui_nhe_tool_tip = self.find_shadow_element(driver,
                                                                          MojichatLocators.CLICK_VAO_HINH_DE_GUI_NHE_SHADOW_PARENT_BIG_CHAT,
                                                                          MojichatLocators.CLICK_VAO_HINH_DE_GUI_NHE_LBL)
        return click_vao_hinh_de_gui_nhe_tool_tip

    def find_sticker_by_index(self, driver, index, parent_shadow=MojichatLocators.STICKER_SUGGESTION_PARENT):
        sticker_suggestion_index = MojichatLocators.STICKER_SUGGESTION_INDEX.replace('{param1}', str(index))
        return self.find_shadow_element(driver, parent_shadow, sticker_suggestion_index)


    def find_thank_you_popup(self, driver, chat_type):
        if chat_type in 'SMALL_CHAT':
            return self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT,
                                            MojichatLocators.THANK_YOU_LBL)
        elif chat_type in 'BIG_CHAT':
            return self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT_BIG_CHAT,
                                            MojichatLocators.THANK_YOU_LBL)

    def find_da_hieu_btn(self, driver, chat_type):
        if chat_type in 'SMALL_CHAT':
            return self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT, MojichatLocators.DA_HIEU_BTN)
        elif chat_type in 'BIG_CHAT':
            return self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT_BIG_CHAT,
                                            MojichatLocators.DA_HIEU_BTN)

    def find_album_by_index(self, driver, index):
        album_suggestion_index = MojichatLocators.ALBUM_ICON_INDEX.replace('{param1}', str(index))
        return self.find_shadow_element(driver, MojichatLocators.PANEL_SHADOW_PARENT, album_suggestion_index)

    def find_pannel_element(self, driver, element):
        return self.find_shadow_element(driver, MojichatLocators.PANEL_SHADOW_PARENT, element)

    def find_sticker_sent_gan_day_by_index(self, driver, index):
        sticker_sent_gan_day_index = MojichatLocators.STICKER_SENT_GANDAY_INDEX.replace('{param1}', str(index))
        return self.find_shadow_element(driver, MojichatLocators.PANEL_SHADOW_PARENT, sticker_sent_gan_day_index)

    def find_album_tooltip_keyword_by_index(self, driver, index):
        album_tooltip_keyword_index = MojichatLocators.ALBUM_TOOLTIP_KEYWORD_INDEX.replace('{param1}', str(index))
        return self.find_shadow_element(driver, MojichatLocators.PANEL_SHADOW_PARENT, album_tooltip_keyword_index)

    def find_sticker_keyword_by_index(self, driver, index):
        sticker_keyword_index = MojichatLocators.STICKER_KEYWORD_INDEX.replace('{param1}', str(index))
        return self.find_shadow_element(driver, MojichatLocators.PANEL_SHADOW_PARENT, sticker_keyword_index)

    def find_show_more_sticker_button(self, driver):
        return self.find_shadow_element(driver, MojichatLocators.STICKER_IN_SHOW_MORE_SHADOW_PARENT, MojichatLocators.SHOW_MORE_STICKER)

    def find_sticker_in_show_more_popup(self, driver):
        return self.find_shadow_element(driver, MojichatLocators.STICKER_IN_SHOW_MORE_SHADOW_PARENT, MojichatLocators.STICKER_IN_SHOW_MORE_INDEX1)

class ChatElement(BasePageElement):
    def find_chat_input(self, driver, chat_type):
        wait = WebDriverWait(driver, 20)
        chat_box = None
        if chat_type in 'BIG_CHAT':
            chat_box = MojichatLocators.BIG_CHAT_INPUT
        elif chat_type in 'SMALL_CHAT':
            chat_box = MojichatLocators.SMALL_CHAT_INPUT
        return wait.until(ec.presence_of_element_located(chat_box))
