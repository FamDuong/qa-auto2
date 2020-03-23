from models.pageelements.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleElements
from models.pageobject.basepage_object import BasePageObject


class TopSitesSaviorTitleAction(BasePageObject):
    top_sites_savior_title_elements = TopSitesSaviorTitleElements()

    def get_x_videos_title_video(self, driver):
        return self.top_sites_savior_title_elements.find_x_videos_title_video_element(driver).text

    def get_xnxx_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_xnxx_video_title_element(driver).text

    def get_tv_zing_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_tv_zing_video_title_element(driver).text

    def get_youtube_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_youtube_video_title_element(driver).text

    def get_instagram_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_video_instagram_title_element(driver).text

    def get_messenger_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_video_messenger_title_element(driver).text




