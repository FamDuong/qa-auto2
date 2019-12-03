from models.pageelements.coccoc_music.coccoc_music_cms.login_page import CMSLoginPageElements
from models.pageobject.basepage_object import BasePageObject


class CMSLoginPagePageObject(BasePageObject):
    cms_login_page_elems = CMSLoginPageElements()

    def input_text_to_email_field(self, driver, email_input):
        email_field = self.cms_login_page_elems.find_email_field(driver)
        email_field.clear()
        email_field.send_keys(email_input)

    def input_text_to_password_field(self, driver, password_input):
        password_field = self.cms_login_page_elems.find_password_field(driver)
        password_field.clear()
        password_field.send_keys(password_input)

    def click_log_in_dashboard_btn(self, driver,):
        self.cms_login_page_elems.find_login_dashboard_btn(driver).click()

    def login(self, driver, email_input, password_input):
        self.input_text_to_email_field(driver, email_input)
        self.input_text_to_password_field(driver, password_input)
        self.click_log_in_dashboard_btn(driver)




