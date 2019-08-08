import platform
import time

import pytest

from pytest_testrail.plugin import pytestrail


class TestSaviorIcon:

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

    @pytestrail.case('C54148')
    @pytest.mark.skipif(platform.release() != 10)
    def test_default_status_savior_icon_new_tab(self, win_app_driver):
        time.sleep(10)
        # url_bar = win_app_driver.find_element_by_name('Address and search bar')
        # url_bar.click()
        # url_bar.send_keys('https://git.itim.vn/users/sign_in')
        # url_bar.send_keys(Keys.RETURN)
        value = self.check_savior_icon(win_app_driver)
        assert value == 'not found'
