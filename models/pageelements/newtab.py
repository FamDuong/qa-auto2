from models.pageelements.basepage_elements import BasePageElement


class NewTabElement(BasePageElement):

    def find_most_visited_element(self, driver):
        return driver.find_element_by_id('most-visited')
