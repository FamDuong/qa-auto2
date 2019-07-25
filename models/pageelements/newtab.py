from models.pageelements.basepage_elements import BasePageElement
import time


class NewTabElement(BasePageElement):

    time.sleep(2)

    def find_most_visited_element(self, driver):
        return driver.find_element_by_id('search-string')
