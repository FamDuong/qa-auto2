from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.top_savior_sites.top_savior_sites_social import MessengerLocators


class MessengerElements(BasePageElement):

    def find_login_button_element_by_find_elements(self, driver: webdriver.Chrome):
        return driver.find_elements(By.ID, MessengerLocators.LOGIN_BUTTON_LOCATOR_BY_ID)

    def find_email_text_box(self, driver: webdriver.Chrome):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(MessengerLocators.EMAIL_FIELD_LOCATOR))

    def find_password_text_box(self, driver: webdriver.Chrome):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(MessengerLocators.PASSWORD_FIELD_LOCATOR))

    def find_login_button(self, driver: webdriver.Chrome):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(MessengerLocators.LOGIN_BUTTON_LOCATOR))







