import logging
import time
from models.pageobject.basepage_object import BasePageObject
from datetime import datetime

LOGGER = logging.getLogger(__name__)


class TopSitesSaviorVideoLengthActions(BasePageObject):

    def get_video_length_by_javascript(self, driver, css_locator):
        video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
        LOGGER.info("Expect video length: "+video_length)
        start_time = datetime.now()
        if '0:00' in video_length:
            while '0:00' in video_length:
                time.sleep(2)
                video_length = driver.execute_script("return document.querySelector(\"" + css_locator + "\").textContent")
                LOGGER.info("Try get expect video length: " + video_length)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        return video_length
