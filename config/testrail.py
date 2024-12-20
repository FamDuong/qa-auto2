import os

from utils_automation.cfgparse import CfgParse

cfg_parse = CfgParse(file_name=os.getcwd().split('testscripts')[0] + '/testrail.cfg')
testrail_config = cfg_parse.read_testrail_config()

TESTRAIL_DOMAIN_URL = testrail_config['API']['url']
TESTRAIL_USERNAME = testrail_config['API']['email']
TESTRAIL_PASSWORD = testrail_config['API']['password']
TESTRAIL_DOMAIN_URL_TEST_PLAN = testrail_config['DOMAIN']['test_plan']
TESTRAIL_DOMAIN_URL_TEST_RUN = testrail_config['DOMAIN']['test_run']








