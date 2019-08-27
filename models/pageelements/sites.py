from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.sites import YoutubePageLocators, GooglePageLocators, AnySite


class YoutubePageElements(BasePageElement):

    @staticmethod
    def find_any_video_item(driver, text):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.any_video_item(text)))

    @staticmethod
    def find_search_button(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.SEARCH_BTN))

    def search_video(self, driver, text_search):
        wait = WebDriverWait(driver, 20)
        search_field = wait.until(
            ec.presence_of_element_located(YoutubePageLocators.SEARCH_BOX))
        search_field.click()
        search_field.send_keys(text_search)
        self.find_search_button(driver).click()

    @staticmethod
    def find_video_player_item(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.VIDEO_PLAYER_ITEM))


class GooglePageElements(BasePageElement):

    @staticmethod
    def find_search_field(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.SEARCH_FIELD))

    @staticmethod
    def find_search_button(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.SEARCH_BUTTON))

    @staticmethod
    def find_video_search_btn(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.VIDEO_SEARCH_BTN))

    @staticmethod
    def find_savior_icon(driver):
        wait = WebDriverWait(driver, 20)
        shadow_root = wait.until(
            ec.presence_of_element_located(GooglePageLocators.SHADOW_ROOT_CONTENT))
        element = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
        return element.find_element_by_css_selector(GooglePageLocators.SAVIOR_ICON)


class AnySiteElements(BasePageElement):

    @staticmethod
    def click_first_video_element(driver):
        return driver.execute_script('document.getElementsByTagName("video")[0].click()')

    @staticmethod
    def find_first_video_element(driver):
        return driver.execute_script('return document.getElementsByTagName("video")[0]')

    @staticmethod
    def find_video_element_24h(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.TWENTY_FOUR_H_VIDEO_ITEM))

    @staticmethod
    def find_video_element_phimmoi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_VIDEO_ITEM))

    @staticmethod
    def find_close_popup_continue_watching(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_CONTINUE_WATCHING_CLOSE_ELEMENT))

    @staticmethod
    def find_video_item_in_facebook_page(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.FACEBOOK_VIDEO_ITEM))

    @staticmethod
    def find_video_item_in_messenger_chat(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.MESSENGER_CHAT_VIDEO_ITEM))

    @staticmethod
    def click_video_item_in_messenger_chat(driver):
        driver.execute_script('document.querySelector(arguments[0]).click()', AnySite.MESSENGER_CHAT_VIDEO_ITEM_SELECTOR)

    @staticmethod
    def find_video_item_in_instagram(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.INSTAGRAM_VIDEO_ITEM))

    @staticmethod
    def find_video_item_in_kienthuc(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.KIENTHUC_VIDEO_ITEM))

    @staticmethod
    def find_video_item_vietnamnet(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.VIETNAMNET_VIDEO_ITEM))

    @staticmethod
    def find_video_item_eva_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.EVA_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_twitter(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.TWITTER_VIDEO_ITEM))

    @staticmethod
    def find_video_item_soha(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.SOHA_VIDEO_ITEM))



