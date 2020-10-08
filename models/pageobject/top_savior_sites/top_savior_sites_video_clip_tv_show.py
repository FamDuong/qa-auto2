from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from models.pageelements.top_savior_sites.top_savior_sites_video_clip_tv_show import \
    TopSaviorSitesVideoClipTvShowElements
from models.pagelocators.top_savior_sites.top_savior_sites_video_clip_tv_show import \
    TopSaviorSitesVideoClipTvShowLocators
from models.pageobject.basepage_object import BasePageObject
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import OtherSiteUrls


class TopSaviorSitesVideoClipTvShowActions(BasePageObject):

    top_savior_sites_video_clip_tv_show_element = TopSaviorSitesVideoClipTvShowElements()

    def login_zalo(self, driver):
        driver.get(TopSaviorSitesVideoClipTvShowLocators.ZALO_WEB_URL)
        zalo_avatar = self.top_savior_sites_video_clip_tv_show_element.find_zalo_avatar_element(driver)
        if zalo_avatar is None:
            user_name = self.top_savior_sites_video_clip_tv_show_element.find_username_label_element(driver)
            if user_name is None:
                username_txt = self.top_savior_sites_video_clip_tv_show_element.find_username_textbox_element(driver)
                self.send_keys_to_element(driver, username_txt, TopSaviorSitesVideoClipTvShowLocators.ZALO_USER_NAME)
            password_txt = self.top_savior_sites_video_clip_tv_show_element.find_password_textbox_element(driver)
            self.send_keys_to_element(driver, password_txt, TopSaviorSitesVideoClipTvShowLocators.ZALO_PASSWORD)
            dang_nhap_btn = self.top_savior_sites_video_clip_tv_show_element.find_dang_nhap_voi_mat_khau_button_element(driver)
            dang_nhap_btn.click()

    def login_tv_zing(self, driver):
        self.login_zalo(driver)
        driver.get(OtherSiteUrls.TV_ZING_VIDEO_URL)
        self.top_savior_sites_video_clip_tv_show_element.find_dang_nhap_bang_zalo_button_element(driver).click()
