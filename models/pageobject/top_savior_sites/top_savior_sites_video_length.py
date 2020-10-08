import logging
import time

from models.pageelements.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthElements
from models.pageobject.basepage_object import BasePageObject
from datetime import datetime

LOGGER = logging.getLogger(__name__)


class TopSitesSaviorVideoLengthActions(BasePageObject):
    top_sites_savior_video_length_element = TopSitesSaviorVideoLengthElements()

    def get_video_length_by_javasript(self, driver, css_locator):
        video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
        length_temp1 = self.get_video_length_if_contain_count_down(video_length)
        length_temp2 = self.get_minutes_and_seconds_video_length(length_temp1)
        if ':' in length_temp2:
            length_temp = length_temp2.replace(':', '.')
        start_time = datetime.now()
        if not (video_length and video_length.strip()) or float(length_temp) < 1:
            while not (video_length and video_length.strip()) or float(length_temp) < 1:
                time.sleep(2)
                video_length = driver.execute_script\
                    ("return document.querySelector(\"" + css_locator + "\").textContent")
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        LOGGER.info("Expect video length: "+video_length)
        return video_length

    def get_video_length_if_contain_count_down(self, video_length_root):
        if "/" in video_length_root:
            video_length = video_length_root.split("/")[1]
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