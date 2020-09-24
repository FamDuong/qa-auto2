from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec

from models.pagelocators.chrome_store_page import ChromeStorePageLocators


class ChromeStorePageElements(BasePageElement):
    def find_add_to_chrome_button(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(ChromeStorePageLocators.ADD_TO_CHROME_BTN_XPATH))
