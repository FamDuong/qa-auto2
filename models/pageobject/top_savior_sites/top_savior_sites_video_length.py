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
        video_length_temp = self.get_video_length_if_contain_cound_down(video_length)
        LOGGER.info("Expect video length: " + str(video_length_temp))
        video_length_temp = video_length_temp.replace(':', '.')
        video_length_number = float(video_length_temp)
        start_time = datetime.now()
        i = 0
        if not (video_length_temp and video_length_temp.strip()) or video_length_number < 0.30:
            while not (video_length_temp and video_length_temp.strip()) or video_length_number < 0.30:
                time.sleep(2)
                video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
                video_length_temp = self.get_video_length_if_contain_cound_down(video_length)
                i += 1
                LOGGER.info("Try get Expect video length " + str(i) + ": " + str(video_length_temp))
                video_length_temp = video_length_temp.replace(':', '.')
                video_length_number = float(video_length_temp)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        return video_length_number

    def get_video_length_if_contain_cound_down(self, video_length_root):
        if "/" in video_length_root:
            video_length = video_length_root.split("/")[1]
            return video_length
