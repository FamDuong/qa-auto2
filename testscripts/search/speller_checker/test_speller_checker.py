from testscripts.common_init_driver import init_chrome_driver
from testscripts.search.common import google_authorize, get_worksheet
from models.pageactions.coccoc_search.speller_checker_actions import SpellerCheckerActions

class TestSpellerChecker:
    speller_checker_action = SpellerCheckerActions()

    def get_error_and_data_corrected(self):
        driver = init_chrome_driver()
        driver.get("http://dev4.coccoc.com/search?query=chinh%20ta")
        driver.find_element()

    def test_speller_checker(self):
        google_authorize()
        worksheet = get_worksheet('1n-D7VxSBuV55Ml8JUwTHi0Iczr9yBWy-2wCkyLAoZxU', 'Sheet1')
        list_data_root = worksheet.range('A1:A3', returnas='matrix')
        driver = init_chrome_driver()
        self.speller_checker_action.open_speller_checker(driver)
        corrected_string_outside_list = []
        for list_data in list_data_root:
            print(list_data)

            self.speller_checker_action.enter_string_to_speller_box(driver, list_data)
            self.speller_checker_action.click_kiem_tra_button(driver)
            errors = self.speller_checker_action.get_speller_errors(driver)
            print(errors+"Errors")
            self.speller_checker_action.click_sua_tat_ca_loi_button()
            corrected_string = self.speller_checker_action.get_corrected_speller_string()
            print(corrected_string+"Corrected String")







