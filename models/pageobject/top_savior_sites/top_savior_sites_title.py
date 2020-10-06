import logging
import time
from datetime import datetime

from models.pageelements.basepage_elements import BasePageElement
from models.pageelements.sites import AnySiteElements
from models.pageelements.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleElements
from models.pagelocators.top_savior_sites.top_savior_sites_title import TopSaviorSitesTitleLocators
from models.pageobject.basepage_object import BasePageObject

LOGGER = logging.getLogger(__name__)


class TopSitesSaviorTitleAction(BasePageObject):
    top_sites_savior_title_elements = TopSitesSaviorTitleElements()
    any_sites_elements = AnySiteElements()
    base_page_element = BasePageElement()

    def replace_special_characters_by_dash_in_string(self, string):
        special_characters = ['|', ':', '/', '?']
        new_string = string
        for character in special_characters:
            if character in new_string:
                new_string = new_string.replace(character, '-')
                LOGGER.info("Video title after replace " + character + " by -: " + new_string)
        return new_string

    def get_first_part_of_video_title(self, video_title):
        title = video_title.split("-")[0]
        LOGGER.info("First part of video title after split by - character: " + title)
        return title

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
        LOGGER.info("Video title: " + youtube_video_title)
        return youtube_video_title

    def get_nhaccuatui_video_title(self, driver):
        nhaccuatui_video_title = self.any_sites_elements.find_nhaccuatui_video_title(driver).text
        LOGGER.info("Get video title: " + nhaccuatui_video_title)
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

    def get_video_title_by_javascript_from_span_tag(self, driver):
        try:
            video_title = self.base_page_element.find_shadow_element(driver,
                                                                     TopSaviorSitesTitleLocators.VIDEO_ROOT_SHADOW_CSS,
                                                                     TopSaviorSitesTitleLocators.VIDEO_TITLE_CSS).text
            # facebook_video_title = driver.execute_script(
            #     " return document.querySelector(\"" + TopSaviorSitesTitleLocators.VIDEO_ROOT_SHADOW_CSS
            #     + "\").shadowRoot.querySelector(\"" + TopSaviorSitesTitleLocators.VIDEO_TITLE_CSS + "\").textContent")
        except:
            video_title = None
            start_time = datetime.now()
            while video_title is None:
                time.sleep(2)
                # facebook_video_title = driver.execute_script(
                #     " return document.querySelector(\"" + TopSaviorSitesTitleLocators.VIDEO_ROOT_SHADOW_CSS
                #     + "\").shadowRoot.querySelector(\"" + TopSaviorSitesTitleLocators.VIDEO_TITLE_CSS + "\").textContent")
                video_title = self.base_page_element.find_shadow_element(driver,
                                                                         TopSaviorSitesTitleLocators.VIDEO_ROOT_SHADOW_CSS,
                                                                         TopSaviorSitesTitleLocators.VIDEO_TITLE_CSS).text
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        return video_title

    def get_fr_pornhub_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_fr_pornhub_video_title_element(driver).get_attribute(
            'data-video-title')

    def get_video_title_from_link(self, driver, title_css_selector, element):
        self.any_sites_elements.find_video_title(driver, element)
        video_title_root = driver.execute_script(
            "return document.querySelector('" + title_css_selector + "').getAttribute('src')")
        temp_list = video_title_root.rsplit('/', 1)
        video_title_list = temp_list[1].rsplit('.', 1)
        LOGGER.info("Get video title: " + video_title_list[0])
        return video_title_list[0]

    def get_video_vnexpress_video_title(self, driver):
        return self.top_sites_savior_title_elements.find_video_vnexpress_video_title_element(driver).text
