import os

from utils_automation.path import YamlCustom

yaml = YamlCustom()


def get_environment_info():
    return yaml.read_data_from_file(os.getcwd().split('practice')[0] + '/resources/env.yaml')


API_SERVER_URL = get_environment_info()['api_server_url']











