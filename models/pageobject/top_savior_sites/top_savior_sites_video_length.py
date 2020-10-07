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
        start_time = datetime.now()
        if not (video_length and video_length.strip()):
            while not (video_length and video_length.strip()):
                time.sleep(2)
                video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        LOGGER.info("Expect video length: "+video_length)
        return video_length

    def get_video_length_if_contain_count_down(self, video_length_root):
        if "/" in video_length_root:
            video_length = video_length_root.split("/")[1]
            return video_length
