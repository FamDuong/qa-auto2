from models.pageelements.coccoc_music.coccoc_music_cms.dash_board_page import CMSDashBoardPageElements
from models.pageobject.basepage_object import BasePageObject


class CMSDashBoardPageObjects(BasePageObject):

    cms_dash_board_page_elems = CMSDashBoardPageElements()

    def sign_out(self, driver):
        self.cms_dash_board_page_elems.find_more_option_btn(driver).click()
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step()
        self.cms_dash_board_page_elems.find_sign_out_btn(driver).click()
        WaitAfterEach.sleep_timer_after_each_step()

    def mouse_over_music_icon(self, driver):
        from utils_automation.common import WebElements
        WebElements.mouse_over_element(driver, self.cms_dash_board_page_elems.find_music_icon(driver))








