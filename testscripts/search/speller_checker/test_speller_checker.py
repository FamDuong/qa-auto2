import time

from models.pageactions.coccoc_search.speller_checker_actions import SpellerCheckerActions
from models.pagelocators.coccoc_search.cc_search import CCSpellerCheckerLocators
from testscripts.common_init_driver import init_chrome_driver
from testscripts.search.common import get_worksheet, get_keyword_without_bracket, write_test_result_into_spreadsheet, \
    get_diff_worlds


class TestSpellerChecker:
    speller_checker_action = SpellerCheckerActions()
    cc_speller_checker_locator = CCSpellerCheckerLocators()

    def get_speller_checker_result(self, driver, input_string):

        self.speller_checker_action.enter_string_to_speller_box(driver, input_string)
        self.speller_checker_action.click_kiem_tra_button(driver)
        time.sleep(3)
        error = self.speller_checker_action.get_speller_errors(driver)
        self.speller_checker_action.click_sua_tat_ca_loi_button(driver)
        corrected_string = self.speller_checker_action.get_corrected_speller_string(driver)
        return error, corrected_string

    def get_error_and_actual_string(self, driver, input_speller):
        error, actual_string = self.get_speller_checker_result(driver, input_speller)
        return error, actual_string

    def write_error_and_actual_string(self, error, actual_string, input_speller, worksheet, sheet_range_input,
                                      result_col_error, result_col_actual_string):
        write_test_result_into_spreadsheet(sheet_range_input, worksheet, input_speller,
                                           result_col_error, error)
        write_test_result_into_spreadsheet(sheet_range_input, worksheet, input_speller,
                                           result_col_actual_string, actual_string)

    def write_diff_words(self, i, input_speller, actual_string, worksheet, sheet_range_input, sheet_range_expect,
                         result_col_expect_string_diff, result_col_actual_string_diff):
        expect_list = worksheet.range(sheet_range_expect, returnas='matrix')
        diff_words_expect_string, diff_worlds_corrected_string = get_diff_worlds(
            get_keyword_without_bracket(str(expect_list[i])),
            actual_string)
        i+=1
        write_test_result_into_spreadsheet(sheet_range_input, worksheet, input_speller,
                                           result_col_expect_string_diff,
                                           str(diff_words_expect_string))
        write_test_result_into_spreadsheet(sheet_range_input, worksheet, input_speller,
                                           result_col_actual_string_diff,
                                           str(diff_worlds_corrected_string))

    def test_speller_checker(self, get_spreed_sheet_id, get_sheet_name, get_sheet_range_input,
                              get_sheet_range_expect, get_result_col_error, get_result_col_actual_string,
                              get_result_col_expect_string_diff, get_result_col_actual_string_diff):
        worksheet = get_worksheet(get_spreed_sheet_id, get_sheet_name)
        input_list = worksheet.range(get_sheet_range_input, returnas='matrix')
        expect_list = worksheet.range(get_sheet_range_expect, returnas='matrix')

        driver = init_chrome_driver()
        self.speller_checker_action.open_speller_checker(driver,
                                                         self.cc_speller_checker_locator.SPELLER_CHECKER_DEV_URL)
        actual_list = []
        i = 0
        for input_string in input_list:
            input_speller = get_keyword_without_bracket(str(input_string))
            if len(input_speller) > 0:
                error, actual_string = self.get_speller_checker_result(driver, input_speller)
                actual_list.append(actual_string)
                write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
                                                   get_result_col_error, error)
                write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
                                                   get_result_col_actual_string, actual_string)
                diff_words_expect_string, diff_worlds_corrected_string = get_diff_worlds(
                    get_keyword_without_bracket(str(expect_list[i])),
                    actual_string)
                i = i + 1
                write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
                                                   get_result_col_expect_string_diff,
                                                   str(diff_words_expect_string))
                write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
                                                   get_result_col_actual_string_diff,
                                                   str(diff_worlds_corrected_string))

    # def test_speller_checker(self, get_spreed_sheet_id, get_sheet_name, get_sheet_range_input,
    #                          get_sheet_range_expect, get_result_col_error, get_result_col_actual_string,
    #                          get_result_col_expect_string_diff, get_result_col_actual_string_diff):
    #     worksheet = get_worksheet(get_spreed_sheet_id, get_sheet_name)
    #     input_list = worksheet.range(get_sheet_range_input, returnas='matrix')
    #     expect_list = worksheet.range(get_sheet_range_expect, returnas='matrix')
    #     driver = init_chrome_driver()
    #     self.speller_checker_action.open_speller_checker(driver,
    #                                                      self.cc_speller_checker_locator.SPELLER_CHECKER_DEV_URL)
    #     i = 0
    #     for input_string in input_list:
    #         input_speller = get_keyword_without_bracket(str(input_string))
    #
    #         if len(input_speller) > 0:
    #             error, actual_string = self.get_error_and_actual_string(driver, input_speller)
    #             self.write_error_and_actual_string(error, actual_string, input_speller, worksheet,
    #                                                get_sheet_range_input, get_result_col_error, get_result_col_actual_string)
    #             # self.write_diff_words(i, input_speller, actual_string, worksheet, get_sheet_range_input,
    #             #                       get_sheet_range_expect,
    #             #                       get_result_col_expect_string_diff, get_result_col_actual_string_diff)
    #                 error, actual_string = self.get_speller_checker_result(driver, input_speller)
    #                 write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
    #                                                    get_result_col_error, error)
    #                 write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
    #                                                    get_result_col_corrected_string, actual_string)
    #
    #                 diff_words_expect_string, diff_worlds_corrected_string = get_diff_worlds(
    #                     get_keyword_without_bracket(str(expect_list[i])),
    #                     actual_string)
    #                 i = i + 1
    #                 write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
    #                                                    get_result_col_expect_string_diff,
    #                                                    str(diff_words_expect_string))
    #                 write_test_result_into_spreadsheet(get_sheet_range_input, worksheet, input_speller,
    #                                                    get_result_col_actual_string_diff,
    #                                                    str(diff_worlds_corrected_string))
