import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from models.pageelements.top_savior_sites.top_savior_sites_video_clip_tv_show import \
    TopSaviorSitesVideoClipTvShowElements
from models.pagelocators.facebook import FacebookPageLocators
from models.pagelocators.top_savior_sites.top_savior_sites_video_clip_tv_show import \
    TopSaviorSitesVideoClipTvShowLocators
from models.pageobject.basepage_object import BasePageObject
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import OtherSiteUrls, VideoClipTVShowUrls


class TopSaviorSitesVideoClipTvShowActions(BasePageObject):
    top_savior_sites_video_clip_tv_show_element = TopSaviorSitesVideoClipTvShowElements()

    def login_zalo(self, driver):
        # driver.get(TopSaviorSitesVideoClipTvShowLocators.ZALO_WEB_URL)
        zalo_avatar = self.top_savior_sites_video_clip_tv_show_element.find_zalo_avatar_element(driver)
        if zalo_avatar is None:
            user_name = self.top_savior_sites_video_clip_tv_show_element.find_username_label_element(driver)
            if user_name is None:
                username_txt = self.top_savior_sites_video_clip_tv_show_element.find_username_textbox_element(driver)
                self.clear_text_to_element(driver, username_txt)
                self.send_keys_to_element(driver, username_txt, TopSaviorSitesVideoClipTvShowLocators.ZALO_USER_NAME)
            password_txt = self.top_savior_sites_video_clip_tv_show_element.find_password_textbox_element(driver)
            self.clear_text_to_element(driver, password_txt)
            self.send_keys_to_element(driver, password_txt, TopSaviorSitesVideoClipTvShowLocators.ZALO_PASSWORD)
            dang_nhap_btn = self.top_savior_sites_video_clip_tv_show_element.find_dang_nhap_voi_mat_khau_button_element(driver)
            dang_nhap_btn.click()

    def login_tv_zing(self, driver):
        # self.login_zalo(driver)
        driver.get(OtherSiteUrls.TV_ZING_VIDEO_URL)

        self.top_savior_sites_video_clip_tv_show_element.find_dang_nhap_bang_zalo_button_element(driver).click()
        windows_handles = driver.window_handles
        if len(windows_handles) == 2:
            driver.switch_to.window(windows_handles[1])
            self.login_zalo(driver)

        import time
        time.sleep(10)
        driver.close()
        driver.switch_to.window(windows_handles[0])

    def click_vtc_play_video_button(self, driver: WebDriver):
        element = self.top_savior_sites_video_clip_tv_show_element.find_vtc_play_video_button(driver)
        element.click()

    def logout_tiktok(self, driver: WebDriver):
        self.top_savior_sites_video_clip_tv_show_element.find_tiktok_avatar_element(driver).click()

        # logout_btn_count = driver.find_elements_by_xpath(InstagramLocators.LOGOUT_BTN)
        # start_time = datetime.now()
        # while len(logout_btn_count) == 0:
        #     time.sleep(2)
        #     logout_btn_count = driver.find_elements_by_xpath(InstagramLocators.LOGOUT_BTN)
        #     time_delta = datetime.now() - start_time
        #     if time_delta.total_seconds() >= 15:
        #         break
        self.top_savior_sites_video_clip_tv_show_element.find_tiktok_logout_button(driver).click()

    def login_tiktok(self, driver: WebDriver):
        driver.get(VideoClipTVShowUrls.TIKTOK_VIEW_PROFILE_URL)
        user_avatar = self.top_savior_sites_video_clip_tv_show_element.count_tiktok_avatar_element(driver)
        user_profile_lbl = self.top_savior_sites_video_clip_tv_show_element.count_tiktok_profile_lbl(driver)
        if user_profile_lbl == 1 and user_avatar > 0:
            self.logout_tiktok(driver)
        else:
            driver.get(VideoClipTVShowUrls.TIKTOK_LOGIN_URL)
            time.sleep(3)
            self.top_savior_sites_video_clip_tv_show_element.find_tiktok_login_by_facebook_option(driver).click()
            windows_handles = driver.window_handles
            if len(windows_handles) == 2:
                driver.switch_to.window(windows_handles[1])
                email_txt = self.top_savior_sites_video_clip_tv_show_element.find_tiktok_facebook_email_textbox(driver)
                self.clear_text_to_element(driver, email_txt)
                self.send_keys_to_element(driver, email_txt, FacebookPageLocators.EMAIL)
                pass_txt = self.top_savior_sites_video_clip_tv_show_element.find_tiktok_facebook_password_textbox(driver)
                self.clear_text_to_element(driver, pass_txt)
                self.send_keys_to_element(driver, pass_txt, FacebookPageLocators.PASS)
                self.top_savior_sites_video_clip_tv_show_element.find_tiktok_facebook_submit_button(driver).click()
                # driver.switch_to.window(windows_handles[0])