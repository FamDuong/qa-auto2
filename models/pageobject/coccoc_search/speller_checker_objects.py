import re

from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.coccoc_search.cc_search import CCSpellerCheckerLocators


class SpellerCheckerActions:
    base_page_element = BasePageElement()
    cc_speller_checker_locator = CCSpellerCheckerLocators()

    def open_speller_checker(self, driver, url):
        driver.get(url)

    def enter_string_to_speller_box(self, driver, string):
        speller_box = self.base_page_element.find_element_if_exist(driver, self.cc_speller_checker_locator.SPELLER_BOX)
        speller_box.clear()
        speller_box.send_keys(string)

    def click_kiem_tra_button(self, driver):
        kiem_tra_button = self.base_page_element.find_element_if_exist(driver,
                                                                       self.cc_speller_checker_locator.KIEM_TRA_BTN)
        kiem_tra_button.click()

    def count_ban_lam_dung_het_roi_nhe_label(self, driver):
        ban_lam_dung_het_roi_nhe_lbl = driver.find_elements_by_xpath \
            (self.cc_speller_checker_locator.BAN_LAM_DUNG_HET_ROI_NHE_LBL_XPATH)
        return len(ban_lam_dung_het_roi_nhe_lbl)

    def get_speller_errors(self, driver):
        if self.count_ban_lam_dung_het_roi_nhe_label(driver) == 0:
            speller_errors_label = self.base_page_element.find_element_if_exist(driver,
                                                                                self.cc_speller_checker_locator.LOI_LBL)
            speller_errors = re.sub('[^0-9]', '', speller_errors_label.text)
            return speller_errors
        else:
            return 0

    def click_sua_tat_ca_loi_button(self, driver):
        if self.count_ban_lam_dung_het_roi_nhe_label(driver) == 0:
            sua_tat_ca_loi_button = self.base_page_element.find_element_if_exist(driver,
                                                                                 self.cc_speller_checker_locator.SUA_TAT_CA_LOI_BTN)
            sua_tat_ca_loi_button.click()

    def count_da_sua_het_loi_label(self, driver):
        da_sua_het_loi_label = driver.find_elements_by_xpath(self.cc_speller_checker_locator.DA_SUA_HET_LOI_LBL_XPATH)
        return len(da_sua_het_loi_label)

    def get_corrected_speller_string(self, driver):
        if self.count_da_sua_het_loi_label(driver) > 0:
            corrected_speller_string = driver.execute_script(
                "return document.querySelector(\"" + self.cc_speller_checker_locator.SPELLER_BOX_CSS + "\").textContent")
            return corrected_speller_string
        else:
            return ""
