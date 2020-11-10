from models.pageobject.basepage_object import BasePageObject
from models.pageelements.chrome_store_page import ChromeStorePageElements


class ChromeStorePageObjects(BasePageObject):
    chrome_store_page_element = ChromeStorePageElements()

    def click_on_add_to_chrome_button(self, driver):
        self.chrome_store_page_element.find_add_to_chrome_button(driver).click()
