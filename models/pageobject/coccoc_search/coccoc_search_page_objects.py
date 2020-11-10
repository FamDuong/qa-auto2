from models.pageelements.basepage_elements import BasePageElement
from models.pageelements.coccoc_search.coccoc_search_elements import CocCocSearchElements
from models.pagelocators.coccoc_search.cc_search import CCSearchPageLocators
from models.pageobject.basepage_object import BasePageObject


class CocCocSearchPageObjects(BasePageObject):
    coccoc_search_element = CocCocSearchElements()
    base_page_element = BasePageElement()

    def count_total_ads_on_ccsearch_page(self, driver):
        self.base_page_element.find_element_if_exist(driver, CCSearchPageLocators.AD_LINK)
        ad_link = driver.find_elements_by_xpath(CCSearchPageLocators.AD_LINK_XPATH)
        return len(ad_link)

    def click_on_ad(self, driver, index, locator_xpath):
        ad_by_index = self.coccoc_search_element.find_ad_by_index(driver, index, locator_xpath)
        self.click_on_element_if_exist(ad_by_index)
