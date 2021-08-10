import json
import random
import string
import inspect
import socket
import jsonschema
from time import sleep
from functools import reduce
from datetime import datetime
from jsonschema import validate
from databases.sql.coccoc_point_db import CocCocPointsDB
from datetime import date

import logging
LOGGER = logging.getLogger(__name__)

class CocCocPointsCommon:
    result = True
    point_db = CocCocPointsDB()

    # Get random string with length
    def get_random_string(self, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    # Get random element in list
    def get_random_element_in_list(self, list):
        # choose from all lowercase letter
        return random.choice(list)

    # Get random integer in range
    def get_random_integer(self, number):
        # choose from all lowercase letter
        return random.randrange(number)

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    # Get data with reference index , and return list value
    def get_reference_data_in_list(self, list_1, list_2, reference):
        list_data = []
        temp = set(list_1)
        index = [i for i, val in enumerate(list_1) if (val in temp and val == reference)]
        for i in index:
            list_data.append(list_2[i])
        return list_data

    # Get data with reference index , and return only one value
    def get_reference_data(self, list_1, list_2, reference):
        list_data = []
        temp = set(list_1)
        index = [i for i, val in enumerate(list_1) if (val in temp and val == reference)]
        for i in index:
            list_data.append(list_2[i])
        return list_data[0]

    def get_curdate(self):
        return datetime.today()

    def get_previousdate(self, day=1):
        import datetime
        date = datetime.datetime.today() - datetime.timedelta(days=day)
        # date = date.strftime(format)
        return date

    def get_nextdate(self, day=1):
        import datetime
        date = datetime.datetime.today() + datetime.timedelta(days=day)
        # date = date.strftime(format)
        return date

    def convert_date(self, date, format='%Y-%m-%d'):
        return date.strftime(format)

    # Old from coccoc lucky, will remove if stable

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

    # Convert string to list by delimiter
    def convert_string_to_list(self, string, delimiter = ','):
        return list(string.split(delimiter))

    def get_substring_between_characters(self, string, start_with, end_with):
        # start = string.find(start_with) + len(start_with)
        start = string.find(start_with)
        end = string.find(end_with)
        substring = string[start:end]
        return substring



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

    def get_list_json_level_1(self, data, key):
        list_groups = []
        for i in range(len(data)):
            group = data[i][key]
            list_groups.append(group)
        return list_groups

    def get_list_json_level_2(self, data, key_1, value_1, key_2):
        list_groups = []
        for i in range(len(data)):
            value = data[i][key_1]
            if value == value_1:
                for j in range(len(data[i][key_2])):
                    value_2 = data[i][key_2][j]
                    list_groups.append(value_2)
                    # print(value_2)
        return list_groups

    def get_list_json_level_2(self, data, key_1, value_1, key_2):
        list_groups = []
        for i in range(len(data)):
            value = data[i][key_1]
            if value == value_1:
                for j in range(len(data[i][key_2])):
                    value_2 = data[i][key_2][j]
                    list_groups.append(value_2)
                    # print(value_2)
        return list_groups

    # Multiple all operator in list
    def multiplication(self, list):
        return reduce((lambda x, y: int(x) * int(y)), list)

    # Database
    # Insert into event log
    def insert_into_event_logs(self, user_id, vid, event_code="default", event_type="default", event_date="default", status="default", default_browser="1", number_events=1):
        if event_type == "default":
            list_event = self.point_db.select_point_db(f'SELECT event_code, event_type FROM points.event_types;')
            list_event_codes = self.point_db.get_list_db(list_event, 0)
            list_event_types = self.point_db.get_list_db(list_event, 1)
            event_code = self.point_common.get_random_element_in_list(list_event_codes)
            event_type = self.point_common.get_reference_data(list_event_codes, list_event_types, event_code)
        if status == "default":
            status = 'new'
        # if default_browser == "default":
        #    default_browser_status = (0, 1)
        if event_date == "default":
            event_date = self.get_curdate()
        event_time = self.convert_date(event_date, '%Y-%m-%d %H:%M:%S')
        event_date = self.convert_date(event_date, '%Y-%m-%d')

        # create_time = event_time
        # update_time = event_time

        for i in range(number_events):
            event_id = self.get_random_string(36)
            # event_code = self.point_common.get_random_element_in_list(list_event_codes)
            # event_type = self.point_common.get_reference_data(list_event_codes, list_event_types, event_code)
            # earn_points = self.get_random_integer(earn_points_max)
            # default_browser = self.get_random_element_in_list(default_browser_status)

            LOGGER.info("%s : %s : %s : %s : %s : %s : %s " % (event_id, user_id, vid, event_code, event_type, status, default_browser))
            users = self.point_db.update_point_db(f'insert into points.event_logs values("{event_id}", "{user_id}", "{vid}", "{event_code}", "{event_type}", "{event_date}", "{event_time}",  "{status}", '
                                                  f'"{default_browser}", "0", "{event_time}", "{event_time}", "");')
