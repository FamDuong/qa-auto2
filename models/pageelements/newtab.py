from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.newtab import NewTabSearchLocators


class NewTabSearchElement(BasePageElement):

    def find_search_string_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_STRING))

    def find_search_button_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_BUTTON))















