from appium import webdriver


class TestAccess:

    def test_access_coccoc_browser(self, appium_android_driver):
        appium_android_driver.get('https://www.google.com')




