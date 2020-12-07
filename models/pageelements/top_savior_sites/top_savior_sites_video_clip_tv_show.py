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
            return self.wait_for_element(driver).until(
                ec.presence_of_element_located(TopSaviorSitesVideoClipTvShowLocators
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

    def find_vtc_play_video_button(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.VTC_PLAY_VIDEO_BTN)

    def find_tiktok_avatar_element(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_AVATAR)

    def find_tiktok_logout_button(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_LOGOUT_BTN)

    def count_tiktok_avatar_element(self, driver: WebDriver):
        return len(driver.find_elements_by_css_selector(TopSaviorSitesVideoClipTvShowLocators.TIKTOK_AVATAR_CSS))

    def count_tiktok_profile_lbl(self, driver: WebDriver):
        return len(driver.find_elements_by_xpath(TopSaviorSitesVideoClipTvShowLocators.TIKTOK_PROFILE_LBL_XPATH))

    def find_tiktok_login_by_facebook_option(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_LOGIN_BY_FACEBOOK_OPTION)

    def find_tiktok_facebook_email_textbox(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_EMAIL_TXT)

    def find_tiktok_facebook_password_textbox(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_PASSWORD_TXT)

    def find_tiktok_facebook_submit_button(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_LOGIN_SUBMIT_BTN)

    def find_tiktok_menu(self, driver: WebDriver, menu='For You'):
        if menu == 'For You':
            return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_MENU_FOR_YOU)
        else:
            return self.find_element_if_exist(driver, TopSaviorSitesVideoClipTvShowLocators.TIKTOK_MENU_FOLLOWING)

