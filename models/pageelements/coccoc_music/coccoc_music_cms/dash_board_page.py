from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec

from models.pagelocators.coccoc_music.coccoc_music_cms.dash_board_page import CMSDashBoardPageLocators


class CMSDashBoardPageElements(BasePageElement):

    def find_more_option_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(CMSDashBoardPageLocators
                                                                                  .MORE_DROP_DOWN_TOGGLE))

    def find_sign_out_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(CMSDashBoardPageLocators
                                                                                  .SIGN_OUT_BTN))

    def find_music_icon(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(CMSDashBoardPageLocators
                                                                                  .MUSIC_ICON))
