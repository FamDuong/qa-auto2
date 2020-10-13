from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators
from utils_automation.common_browser import coccoc_instance


class TopSitesSaviorVideoLengthElements(BasePageElement):
    def find_video_lengh(self, driver, element):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(element))
