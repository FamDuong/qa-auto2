from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.top_savior_sites.top_savior_sites_social import MessengerLocators, FacebookLocators, \
    InstagramLocators
from utils_automation.const import SocialNetworkUrls


class MessengerElements(BasePageElement):

    def find_login_button_element_by_find_elements(self, driver: webdriver.Chrome):
        return driver.find_elements(By.ID, MessengerLocators.LOGIN_BUTTON_LOCATOR_BY_ID)

    def find_email_text_box(self, driver: webdriver.Chrome):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(MessengerLocators.EMAIL_FIELD_LOCATOR))

    def find_password_text_box(self, driver: webdriver.Chrome):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(MessengerLocators.PASSWORD_FIELD_LOCATOR))

    def find_login_button(self, driver: webdriver.Chrome):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(MessengerLocators.LOGIN_BUTTON_LOCATOR))


class FacebookElements(BasePageElement):
    def find_facebook_first_video(self, driver, url):
        import time
        time.sleep(5)
        try:
            if url == SocialNetworkUrls.FACEBOOK_VTVGIAITRI_PAGE_URL:
                return self.wait_for_element(driver).until(
                    ec.presence_of_element_located(FacebookLocators.VTV_GIAITRI_PAGE_FIRST_VIDEO))
            else:
                return self.wait_for_element(driver).until(ec.presence_of_element_located(FacebookLocators.HOME_PAGE_FIRST_VIDEO))
        except:
            return None

    # def find_dong_doan_chat_button_fanpage(self, driver):
    #     return self.wait_for_element(driver).until(ec.presence_of_element_located(FacebookLocators.VTV_GIAITRI_DONG_DOAN_CHAT_BTN))

    def find_first_video(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(FacebookLocators.WATCH_FIRST_VIDEO))


class InstagramElements(BasePageElement):

    def find_instagram_first_video(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(InstagramLocators.FIRST_VIDEO_HOME_PAGE))
