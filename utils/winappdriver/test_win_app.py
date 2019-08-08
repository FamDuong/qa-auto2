import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestSimpleCalculator:

    # def getresults(self, driver):
    #     displaytext = driver.find_element_by_accessibility_id("CalculatorResults").text
    #     displaytext = displaytext.strip("Display is " )
    #     displaytext = displaytext.rstrip(' ')
    #     displaytext = displaytext.lstrip(' ')
    #     return displaytext

    def check_savior_icon(self, driver):
        try:
            is_enabled = driver.find_element_by_name('Downloadable media found!')
        # actions = ActionChains(win_app_driver)
        # actions.move_to_element(is_enabled)
        # actions.double_click()
        # actions.perform()
            is_enabled.click()
        except:
            return 'not found'

    def test_initialize(self, win_app_driver):
        time.sleep(10)
        # url_bar = win_app_driver.find_element_by_name('Address and search bar')
        # url_bar.click()
        # url_bar.send_keys('https://git.itim.vn/users/sign_in')
        # url_bar.send_keys(Keys.RETURN)
        value = self.check_savior_icon(win_app_driver)
        assert value == 'not found'



