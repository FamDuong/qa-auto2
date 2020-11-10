import json
import random
import inspect
import jsonschema
from jsonschema import validate
from databases.sql.coccoc_lucky_db import LuckyDB
from datetime import date

import logging
LOGGER = logging.getLogger(__name__)

class LuckyCommon:
    result = True
    lucky_db = LuckyDB()

    def get_count_number_each_elements_in_list(self, list):
        return None

    # Print list line by line
    def print_list(self, list):
        print(*list, sep='\n')

    def get_total_user_prizes(self, my_list):
        total = 0
        for i in range(my_list):
            total = total + my_list[i][1]
        return total

    def get_ratio_get_prize(self, number_turns, number_prize):
        ratio = number_prize / number_turns
        return ratio

    def print_debug(self, string):
        function_name = inspect.stack()[1].function
        # print("    ", function_name, ": ", string)
        LOGGER.info("    %s : %s" % (function_name, string))

    # Validate json schema
    def validate_jsonschema(self, json_data, schema):
        global result
        try:
            validate(instance=json_data, schema=schema)
        except (jsonschema.exceptions.ValidationError, jsonschema.exceptions.SchemaError) as err:
            self.print_debug("ERROR: %s" % err.message)
            result = False



    # Get DB info
    def get_list_lucky_db(self, sql_query, index = 0, data_query = None):
        db_lucky = self.lucky_db.select_lucky_db(sql_query, data_query)
        list_lucky = self.lucky_db.get_list_db(db_lucky, index)
        return list_lucky;

    # Assert equal
    def assert_equals(self, expect, actual, fail_message = None):
        # global result
        # result = True
        if expect != actual:
            self.print_debug("ERROR: %s are not equal: expect %s != actual %s" % (fail_message, expect, actual))
            self.result = False
        else:
            self.print_debug("PASSED: %s expect %s = actual %s" % (fail_message, expect, actual))
        # return result

    # Assert equal
    def assert_not_equals(self, expect, actual, fail_message = None):
        # global result
        # result = True
        if expect == actual:
            self.print_debug("ERROR: %s are equal: expect %s != actual %s" % (fail_message, expect, actual))
            self.result = False
        else:
            self.print_debug("PASSED: expect %s != actual %s" % (expect, actual))
        # return result

    # Assert element is not none
    def assert_is_not_none(self, data, fail_message = None):
        # global result
        # result = True
        if data == None:
            self.print_debug("ERROR %s: %s is NONE" % (fail_message, data))
            self.result = False
        else:
            self.print_debug(data)
            self.print_debug("PASSED: Data is not NONE")
        # return result

    # Assert element is none
    def assert_is_none(self, data, fail_message = None):
        # global result
        # result = True
        if data != None:
            self.print_debug("ERROR %s: Data is not NONE: %s" % (fail_message, data))
            self.result = False
        else:
            self.print_debug("PASSED: Data is NONE")
        # return result

    # Assert contains sub string
    def assert_contains(self, string, substring, fail_message = None):
        # global result
        result = True
        if str(substring) not in str(string):
            self.print_debug("ERROR: %s: %s is not in %s" % (fail_message, substring, string))
            result = False
        return result

    # Check if list contains items
    def assert_list_contains_item(self, list, element, fail_message=None):
        if element not in list:
            self.print_debug("ERROR %s: Not found %s in list %s" % (fail_message, element, list))
            self.result = False
        else:
            self.print_debug("PASSED: found %s in list" % element)

    def get_result(self):
        # global result
        return self.result

    def convert_list_to_string(self, list, concentrate = ", "):
        convert_string = concentrate.join((map(str, list)))
        self.print_debug(convert_string)
        return convert_string

    def get_substring_between_characters(self, string, start_with, end_with):
        # start = string.find(start_with) + len(start_with)
        start = string.find(start_with)
        end = string.find(end_with)
        substring = string[start:end]
        return substring

    # Get data with reference index is
    def get_reference_data_in_list(self, list_1, list_2, reference):
        list_data = []
        temp = set(list_1)
        index = [i for i, val in enumerate(list_1) if (val in temp and val == reference)]
        for i in index:
            list_data.append(list_2[i])
        return list_data

    def division_percentage(self, x, y):
        try:
            return (x / y) * 100
        except ZeroDivisionError:
            return 0

    def division(self, x, y):
        try:
            return (x / y)
        except ZeroDivisionError:
            return 0