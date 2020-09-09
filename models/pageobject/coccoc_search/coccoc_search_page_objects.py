from models.pageelements.coccoc_search.coccoc_search_elements import CocCocSearchElements
from models.pagelocators.coccoc_search.cc_search import CCSearchPageLocators
from models.pageobject.basepage_object import BasePageObject


class CocCocSearchPageObjects(BasePageObject):
    coccoc_search_element = CocCocSearchElements()
    def count_total_ads_on_ccsearch_page(self, driver):
        ad_link = driver.find_elements_by_xpath(CCSearchPageLocators.AD_LINK)
        return len(ad_link)

    def click_on_ad(self, driver, index):
        ad_by_index = self.coccoc_search_element.find_ad_by_index(driver, index)
        self.click_on_element_if_exist(ad_by_index)
