from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec

from models.pagelocators.coccoc_music.coccoc_music_cms.login_page import CMSLoginPageLocators


class CMSLoginPageElements(BasePageElement):

    def find_email_field(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(CMSLoginPageLocators.EMAIL_FIELD))

    def find_password_field(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(CMSLoginPageLocators.PASSWORD_FIELD))

    def find_login_dashboard_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(CMSLoginPageLocators.LOGIN_DASH_BOARD_BTN))



