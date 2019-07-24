

class BasePageObject(object):
    print "abc"
    # def find_element(self, *locator):
    #     if locator.__len__() == 2:
    #         return self.driver.find_element(*locator)
    #     return self.driver.find_element(*(locator[1], locator[2] % locator[0]))
    #
    # def find_elements(self, *locator):
    #     if locator.__len__() == 2:
    #         return self.driver.find_elements(*locator)
    #     return self.driver.find_elements(*(locator[1], locator[2] % locator[0]))
