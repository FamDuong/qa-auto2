from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec

from models.pagelocators.top_savior_sites.top_savior_sites_title import TopSaviorSitesTitleLocators


class TopSitesSaviorTitleElements(BasePageElement):

    def find_x_videos_title_video_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators
                                                                                  .X_VIDEOS_VIDEO_TITLE))

    def find_xnxx_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators
                                                                                  .XNXX_VIDEO_TITLE))

    def find_tv_zing_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.TV_ZING_VIDEO_TITLE))

    def find_youtube_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.YOUTUBE_VIDEO_TITLE))

    def find_video_instagram_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.INSTAGRAM_VIDEO_TITLE))

    def find_video_messenger_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.MESSENGER_VIDEO_TITLE))

    def find_mot_phim_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.MOT_PHIM_VIDEO_TITLE))

    def find_video_phimmoi_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.PHIMMOI_VIDEO_TITLE))

    def find_ok_ru_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.OK_RU_VIDEO_TITLE))

    def find_facebook_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.FACEBOOK_VIDEO_TITLE))

    def find_fr_pornhub_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesTitleLocators.FR_PORNHUB_VIDEO_TITLE))

    def find_video_vnexpress_video_title_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(
            TopSaviorSitesTitleLocators.VIDEO_VNEXPRESS_VIDEO_TITLE))





