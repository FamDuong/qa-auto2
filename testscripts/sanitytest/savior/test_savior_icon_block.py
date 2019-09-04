import time
import pytest
from pytest_testrail.plugin import pytestrail


class TestSaviorIcon:

    def check_savior_icon(self, driver):
        try:
            is_enabled = driver.find_element_by_name('Downloadable media found!')
            is_enabled.click()
        except:
            return 'not found'

    @pytestrail.case('C54148')
    @pytest.mark.skip(reason='Not able to implement in other machine')
    # @pytest.mark.skipif(platform.release() != "10", reason=" Cannot use win app driver with windows below 10")
    def test_winapp_driver_default_status_savior_icon_new_tab(self, win_app_driver):
        time.sleep(10)
        value = self.check_savior_icon(win_app_driver)
        assert value == 'not found'
