from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.sites import YoutubePageLocators, GooglePageLocators


class YoutubePageElements(BasePageElement):

    def find_any_video_item(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(YoutubePageLocators.ANY_VIDEO_ITEM))

    def find_video_player_item(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(YoutubePageLocators.VIDEO_PLAYER_ITEM))


class GooglePageElements(BasePageElement):

    def find_search_field(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(GooglePageLocators.SEARCH_FIELD))

    def find_search_button(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(GooglePageLocators.SEARCH_BUTTON))

    def find_video_search_btn(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.VIDEO_SEARCH_BTN))

    def find_savior_icon(self, driver):
        wait = WebDriverWait(driver, 5)
        shadow_root = wait.until(
            ec.presence_of_element_located(GooglePageLocators.SHADOW_ROOT_CONTENT))
        element = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
        return element.find_element_by_css_selector(GooglePageLocators.SAVIOR_ICON)
