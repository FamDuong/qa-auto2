from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.coccocpage import CocCocPageLocators


class CocCocPageElement(BasePageElement):

    def find_download_button(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(CocCocPageLocators.BUTTON_DOWNLOAD))

    def find_privacy_button(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(CocCocPageLocators.BUTTON_PRIVACY))

    def find_download_element(self, driver, os, language):
        wait = WebDriverWait(driver, 20)
        if os is "win" and language is "en":
            return wait.until(ec.presence_of_element_located(CocCocPageLocators.URL_DOWNLOAD_WIN_EN))
        elif os is "winxp":
            return wait.until(ec.presence_of_element_located(CocCocPageLocators.URL_DOWNLOAD_WINXP_VI))
        elif os is "mac":
            return wait.until(ec.presence_of_element_located(CocCocPageLocators.URL_DOWNLOAD_WINXP_VI))
        else:
            return wait.until(ec.presence_of_element_located(CocCocPageLocators.BUTTON_DOWNLOAD))

    def find_privacy_button_production(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(CocCocPageLocators.PRO_TOI_DA_HIEU_VA_DONG_Y_BTN))

    def find_language_flag_production(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(CocCocPageLocators.PRO_LANGUAGE_FLAG))

    def find_download_element_production(self, driver, language):
        wait = WebDriverWait(driver, 20)
        if language is "en":
            self.find_language_flag_production(driver).click()
        return wait.until(ec.presence_of_element_located(CocCocPageLocators.PRO_BUTTON_DOWNLOAD))