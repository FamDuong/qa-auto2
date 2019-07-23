

class BasePageObject(object):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)
