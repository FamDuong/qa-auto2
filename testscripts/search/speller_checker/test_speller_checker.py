import time
import logging

import pandas as pd
from models.pageobject.coccoc_search.speller_checker_objects import SpellerCheckerActions
from models.pagelocators.coccoc_search.cc_search import CCSpellerCheckerLocators
from testscripts.common_init_driver import init_chrome_driver
from testscripts.search.common import get_worksheet, get_diff_worlds

LOGGER = logging.getLogger(__name__)

class TestSpellerChecker:
    speller_checker_action = SpellerCheckerActions()
    cc_speller_checker_locator = CCSpellerCheckerLocators()

    def get_speller_checker_result(self, driver, input_string):

        self.speller_checker_action.enter_string_to_speller_box(driver, input_string)
        self.speller_checker_action.click_kiem_tra_button(driver)
        time.sleep(5)
        error = self.speller_checker_action.get_speller_errors(driver)
        self.speller_checker_action.click_sua_tat_ca_loi_button(driver)
        corrected_string = self.speller_checker_action.get_corrected_speller_string(driver)
        return error, corrected_string

    def get_error_and_actual_string(self, driver, input_speller):
        error, actual_string = self.get_speller_checker_result(driver, input_speller)
        return error, actual_string

    def get_test_status(self, expect_error, actual_error, diff_words_expect_string, diff_worlds_actual_string):
        if expect_error == actual_error:
            if diff_worlds_actual_string == diff_words_expect_string:
                return 'OK'
            else:
                return 'NOK'
        else:
            return 'NOK'

    def get_test_result_list(self, input_list):
        driver = init_chrome_driver()
        self.speller_checker_action.open_speller_checker(driver,
                                                         self.cc_speller_checker_locator.SPELLER_CHECKER_DEV_URL)
        test_result_list = []
        for data in input_list:
            input_string = data[0]
            expect_string = data[1]
            expect_error = data[2]

            if len(input_string) > 0:
                actual_error, actual_string = self.get_speller_checker_result(driver, input_string)
                diff_words_expect_string, diff_worlds_actual_string = get_diff_worlds(expect_string, actual_string)

                test_status = self.get_test_status(expect_error, actual_error, diff_words_expect_string,
                                                   diff_worlds_actual_string)

                temp_list = [input_string, expect_string, expect_error, actual_error, actual_string, test_status,
                             diff_words_expect_string, diff_worlds_actual_string]
                test_result_list.append(list(temp_list))
                temp_list.clear()
        return test_result_list

    def write_test_result_to_google_spreadsheet(self, worksheet, test_result_list):
        df = pd.DataFrame(test_result_list,
                          columns=['Input', 'Expect', 'Number of expect error', 'Number of defect error', 'Actual',
                                   'NOK', 'Diff words expect', 'Diff words actual'])

        # print("\n")
        # print(df)
        worksheet.set_dataframe(df, (1, 1))

    def test_speller_checker(self, get_spreed_sheet_id, get_sheet_name, get_sheet_range_input):
        worksheet = get_worksheet(get_spreed_sheet_id, get_sheet_name)
        input_list = worksheet.range(get_sheet_range_input, returnas='matrix')
        test_result_list = self.get_test_result_list(input_list)
        self.write_test_result_to_google_spreadsheet(worksheet, test_result_list)
