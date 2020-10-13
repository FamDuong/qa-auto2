from selenium.webdriver.chrome.webdriver import WebDriver
from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec

from models.pagelocators.top_savior_sites.top_savior_sites_video_clip_tv_show import \
    TopSaviorSitesVideoClipTvShowLocators


class TopSaviorSitesVideoClipTvShowElements(BasePageElement):

    def find_dang_nhap_bang_zalo_button_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
                                                                                  .TV_ZING_VN_DANG_NHAP_BANG_ZALO_BTN))

    def find_username_textbox_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
                                                                                  .ZALO_USER_NAME_TXT))

    def find_username_label_element(self, driver: WebDriver):
        try:
            return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
                                                                                  .ZALO_USER_NAME_LBL))
        except:
            return None

    def find_password_textbox_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
                                                                                  .ZALO_PASSWORD_TXT))

    def find_dang_nhap_voi_mat_khau_button_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
                                                                                  .ZALO_DANG_NHAP_BTN))

    def find_zalo_avatar_element(self, driver: WebDriver):
        try:
            return self.wait_for_element(driver).until(
                ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
                                               .ZALO_AVATAR))
        except:
            return None
