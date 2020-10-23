from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.top_savior_sites.top_savior_sites_online_music import TopSaviorSitesOnlineMusicLocators


class TopSaviorSitesOnlineMusicElements(BasePageElement):
    def find_nhac_cua_tui_close_popup_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesOnlineMusicLocators.NHACCUATUI_MARKETING_POPUP))

    def find_number_nhac_cua_tui_popup_btn(self, driver):
        return driver.find_elements_by_xpath(TopSaviorSitesOnlineMusicLocators.NHACCUATUI_MARKETING_POPUP_XPATH)
