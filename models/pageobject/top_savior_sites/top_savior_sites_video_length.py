import logging
import time

from models.pageelements.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthElements
from models.pageobject.basepage_object import BasePageObject
from datetime import datetime

LOGGER = logging.getLogger(__name__)


class TopSitesSaviorVideoLengthActions(BasePageObject):
    top_sites_sav_ior_video_length_element = TopSitesSaviorVideoLengthElements()
    def get_video_length(self, driver, element):
        # video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
        video_length = self.top_sites_savior_video_length_element.find_video_lengh(driver, element).text
        LOGGER.info("Expect video length: "+video_length)
        video_length_number = float(video_length.replace(':', '.'))
        start_time = datetime.now()
        if not (video_length and video_length.strip()) or '0:00' in video_length or video_length_number < 0.30:
            while not (video_length and video_length.strip()) or '0:00' in video_length or video_length_number < 0.30:
                time.sleep(2)
                # video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
                video_length = self.top_sites_savior_video_length_element.find_video_lengh(driver, element).text
                video_length_number = float(video_length.replace(':', '.'))
                LOGGER.info("Try get expect video length: " + video_length)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        return video_length

    def get_ok_ru_video_length(self, video_length_root):
        video_length = video_length_root.split("/")[1]
        return video_length

