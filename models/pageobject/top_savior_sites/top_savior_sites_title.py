import logging

from models.pageelements.sites import AnySiteElements
from models.pageelements.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleElements
from models.pageobject.basepage_object import BasePageObject

LOGGER = logging.getLogger(__name__)


class TopSitesSaviorTitleAction(BasePageObject):
    top_sites_savior_title_elements = TopSitesSaviorTitleElements()
    any_sites_elements = AnySiteElements()

    def get_website_title_by_javascript(self, driver):
        video_title = driver.execute_script("return document.title")
        LOGGER.info("Get video title: " + video_title)
        return video_title

    def get_x_videos_title_video(self, driver):
        return self.top_sites_savior_title_elements.find_x_videos_title_video_element(driver).text

    def get_xnxx_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_xnxx_video_title_element(driver).text

    def get_tv_zing_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_tv_zing_video_title_element(driver).text

    def get_youtube_video_title(self, driver):
        youtube_video_title = self.top_sites_savior_title_elements.find_youtube_video_title_element(driver).text
        LOGGER.info("Video title: "+youtube_video_title)
        return youtube_video_title

    def get_nhaccuatui_video_title(self, driver):
        nhaccuatui_video_title = self.any_sites_elements.find_nhaccuatui_video_title(driver).text
        LOGGER.info("Get video title: "+nhaccuatui_video_title)
        return nhaccuatui_video_title


    def get_instagram_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_video_instagram_title_element(driver).get_attribute('content')

    def get_messenger_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_video_messenger_title_element(driver).text

    def get_mot_phim_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_mot_phim_video_title_element(driver).get_attribute('content')

    def get_phimmoi_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_video_phimmoi_title_element(driver).get_attribute('content')

    def get_ok_ru_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_ok_ru_video_title_element(driver).text

    def get_facebook_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_facebook_video_title_element(driver).text

    def get_fr_pornhub_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_fr_pornhub_video_title_element(driver).get_attribute('data-video-title')




