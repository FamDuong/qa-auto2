import logging
import time

from models.pageelements.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthElements
from models.pageobject.basepage_object import BasePageObject
from datetime import datetime

from testscripts.common_setup import get_sec

LOGGER = logging.getLogger(__name__)


class TopSitesSaviorVideoLengthActions(BasePageObject):
    top_sites_savior_video_length_element = TopSitesSaviorVideoLengthElements()

    def get_video_length_from_html(self, driver, css_locator, element):
        if css_locator == "":
            return self.top_sites_savior_video_length_element.find_video_lengh(driver, element).text
        else:
            return driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")

    def get_video_length(self, driver, css_locator, element=""):
        video_length_root = self.get_video_length_from_html(driver, css_locator, element)
        video_length = self.get_video_length_if_contain_count_down(video_length_root)
        video_length_seconds = get_sec(video_length)
        LOGGER.info("Expect video length: " + video_length)
        LOGGER.info("Expect video length seconds: " + str(video_length_seconds))
        start_time = datetime.now()
        if video_length_seconds < 60:
            while video_length_seconds < 60:
                time.sleep(2)
                video_length_root = self.get_video_length_from_html(driver, css_locator, element)
                video_length = self.get_video_length_if_contain_count_down(video_length_root)
                video_length_seconds = get_sec(video_length)
                LOGGER.info("Retry get expect video length: " + video_length)
                LOGGER.info("Retry get expect video length seconds: " + str(video_length_seconds))
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 25:
                    break
        return video_length

    def get_video_length_if_contain_count_down(self, video_length_root):
        if "/" in video_length_root:
            video_length = video_length_root.split("/")[1]
            LOGGER.info("Video length after split /: "+video_length)
            return video_length
        else:
            return video_length_root

    def get_minutes_and_seconds_video_length(self, video_length_root):
        if video_length_root.count(':') == 2:
            video_length_minutes = video_length_root.split(":")[1]
            video_length_seconds = video_length_root.split(":")[2]
            video_length = video_length_minutes + '.' + video_length_seconds
            LOGGER.info("Video length after get minutes and seconds " + video_length)
            return video_length
        else:
            return video_length_root
