import  json
import string
import re
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import DatafeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedsDB;

class TestDataRules:
    new_feed_data_api = DatafeedAPI()
    new_feed_data_db = NewFeedsDB()

    # Test rule is not null
    def test_check_if_rules_is_null(self):
        result = True
        api_rules = self.new_feed_data_api.get_rules_crawler()
        api_number_of_rules = len(api_rules)
        print(api_number_of_rules)

        for i in range(api_number_of_rules):
            api_hostname = api_rules[i]['host']
            api_number_of_rules_hostname = len(api_rules[i]['rules'])
            if api_number_of_rules_hostname == 0:
                print(api_hostname, ": ", api_number_of_rules_hostname)
                result = False
        assert result == True

    # Check if action is remove or keep
    def test_check_if_action_is_correct(self):
        result = True
        api_rules = self.new_feed_data_api.get_rules_crawler()
        api_number_of_rules = len(api_rules)
        print(api_number_of_rules)

        for i in range(api_number_of_rules):
            api_hostname = api_rules[i]['host']
            api_number_of_rules_hostname = len(api_rules[i]['rules'])
            for j in range(api_number_of_rules_hostname):
                api_hostname_action = api_rules[i]['rules'][j]['action']
                if api_hostname_action != 'remove' and api_hostname_action != 'keep':
                    print(api_hostname_action)
                    result = False
        assert result == True

    # Get rules is regrex
    def test_check_if_rules_is_correct(self):
        result = True
        api_rules = self.new_feed_data_api.get_rules_crawler()
        api_number_of_rules = len(api_rules)
        print(api_number_of_rules)

        for i in range(api_number_of_rules):
            api_hostname = api_rules[i]['host']
            api_number_of_rules_hostname = len(api_rules[i]['rules'])
            for j in range(api_number_of_rules_hostname):
                api_hostname_rules_action = api_rules[i]['rules'][j]['action']
                api_hostname_rules_r = api_rules[i]['rules'][j]['r']
                # Ignore default rules
                if api_hostname_rules_r != '*':
                    try:
                        re.compile(api_hostname_rules_r)
                    except re.error:
                        print(api_hostname, ": ", api_hostname_rules_r)
                        result = False
        assert result == True

    # Test rule is not null
    def test_check_if_last_default_rules(self):
        result = True
        api_rules = self.new_feed_data_api.get_rules_crawler()
        api_number_of_rules = len(api_rules)
        print(api_number_of_rules)

        for i in range(api_number_of_rules):
            api_hostname = api_rules[i]['host']
            api_number_of_rules_hostname = len(api_rules[i]['rules'])
            print(api_hostname)
            for j in range(api_number_of_rules_hostname):
                api_hostname_rules = api_rules[i]['rules'][j]
                print("    ", api_hostname_rules)
        assert result == True

    # Check assessment in DB
    def test_check_assessment_in_db(self, coccoc_new_feeds_db_interact):
        result = True
        api_rules = self.new_feed_data_api.get_rules_crawler()
        api_number_of_rules = len(api_rules)
        print(api_number_of_rules)

        for i in range(api_number_of_rules):
            api_hostname = api_rules[i]['host']
            api_hostname_rules = api_rules[i]['rules']
            api_hostname_rules = str(api_hostname_rules)
            api_hostname_rules = api_hostname_rules.replace(' ', '').replace('\'','"')

            db_hostname_rule = self.new_feed_data_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select rules from assessments where host_id in (select id from hosts where hostname = "{api_hostname}");')
            db_hostname_rule = str(db_hostname_rule)
            db_hostname_rule = db_hostname_rule.replace('\\\\', '\\')
            if api_hostname_rules not in db_hostname_rule:
                print(api_hostname)
                print("    api rule:", api_hostname_rules)
                print("    db rule :", db_hostname_rule)
                result = False
        assert result == True

