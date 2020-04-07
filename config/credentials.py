import os

from utils_automation.path import YamlCustom

yaml = YamlCustom()


def get_credentials_info():
    return yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/credentials.yaml')


SKYPE_BOT_ACCOUNT_NAME = get_credentials_info()['skype']['bot']['accountname']
SKYPE_BOT_PASSWORD = get_credentials_info()['skype']['bot']['password']
SKYPE_GROUP_AUTOMATION_ID = get_credentials_info()['skype']['group']['qa_automation_id']

ATLASSIAN_BOT_ACCOUNT_NAME = get_credentials_info()['atlassian']['bot']['accountname']
ATLASSIAN_BOT_PASSWORD = get_credentials_info()['atlassian']['bot']['password']

















