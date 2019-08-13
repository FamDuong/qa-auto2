from selenium.webdriver.support.wait import WebDriverWait

from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.version import VersionPageLocators
from selenium.webdriver.support import expected_conditions as ec


class VersionPageElements(BasePageElement):

    def find_profile_path_element(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(VersionPageLocators.PROFILE_PATH_ELEMENT))

    def find_flash_path_element(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(VersionPageLocators.FLASH_PATH_ELEMENT))
