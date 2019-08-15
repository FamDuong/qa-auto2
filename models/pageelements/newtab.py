from models.pageelements.basepage_elements import BasePageElement
import time

from utils_automation.setup import WaitAfterEach


class NewTabElement(BasePageElement):

    WaitAfterEach.sleep_timer_after_each_step()

    def find_most_visited_element(self, driver):
        return driver.find_element_by_id('search-string')
