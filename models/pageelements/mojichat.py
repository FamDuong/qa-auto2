import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import WaitAfterEach


class MojichatElement(BasePageElement):
    global chat_type

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

    def find_sticker_by_index(self, driver, chat_type, index):
        sticker_suggestion_index = 'MojichatLocators.STICKER_SUGGESTION_INDEX' + index
        if chat_type in 'SMALL_CHAT':
            return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
                                            sticker_suggestion_index)
        elif chat_type in 'BIG_CHAT':
            return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT_BIG_CHAT,
                                            sticker_suggestion_index)

    # def find_sticker_index0(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX0)
    #
    # def find_sticker_index1(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX1)
    #
    # def find_sticker_index2(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX2)
    #
    # def find_sticker_index3(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX3)
    #
    # def find_sticker_index4(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX4)
    #
    # def find_sticker_index5(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX5)
    #
    # def find_sticker_index6(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX6)
    #
    # def find_sticker_index7(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX7)
    #
    # def find_sticker_index8(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX8)
    #
    # def find_sticker_index9(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX9)
    #
    # def find_sticker_index10(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX10)
    #
    # def find_sticker_index11(self, driver):
    #     return self.find_shadow_element(driver, MojichatLocators.STICKER_SUGGESTION_PARENT,
    #                                     MojichatLocators.STICKER_SUGGESTION_INDEX11)

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
            return self.find_shadow_element(driver, MojichatLocators.MOJI_SHADOW_PARENT_BIG_CHAT, MojichatLocators.DA_HIEU_BTN)

class ChatElement(BasePageElement):
    def find_chat_input(self, driver, chat_type):
        wait = WebDriverWait(driver, 20)
        chat_box = None
        if self.chat_type in 'BIG_CHAT':
            chat_box = MojichatLocators.BIG_CHAT_INPUT
        elif self.chat_type in 'SMALL_CHAT':
            chat_box = MojichatLocators.SMALL_CHAT_INPUT
        return wait.until(ec.presence_of_element_located(chat_box))
