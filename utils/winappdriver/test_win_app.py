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

    def test_initialize(self, win_app_driver):
        time.sleep(1)
        url_bar = win_app_driver.find_element_by_name('Address and search bar')
        url_bar.click()
        url_bar.send_keys('https://www.youtube.com/watch?v=WZDMQOOH_ZE&list=RDWZDMQOOH_ZE&start_radio=1')
        url_bar.send_keys(Keys.RETURN)
        time.sleep(10)
        is_enabled = win_app_driver.find_element_by_class_name('Chrome_WidgetWin_1')
        actions = ActionChains(win_app_driver)
        actions.move_to_element(is_enabled)
        actions.double_click()
        actions.perform()
        time.sleep(3)
        is_enabled.is_selected()
        print('Verify this item:', is_enabled.is_selected())
        time.sleep(2)
        # win_app_driver.find_element_by_name("Clear").click()
        # win_app_driver.find_element_by_name("Seven").click()
        # assert self.getresults(win_app_driver) == "7"
        # win_app_driver.find_element_by_name("Clear").click()

