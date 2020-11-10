from selenium.webdriver.common.by import By

from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.coccoc_search.cc_search import CCSearchPageLocators


class CocCocSearchElements(BasePageElement):
    def find_ad_by_index(self, driver, index, locator_xpath):
        ad_by_index_xpath = locator_xpath.replace('{param1}', str(index))
        ad_by_index_element = self.find_element_if_exist(driver, (By.XPATH, ad_by_index_xpath))
        return ad_by_index_element

