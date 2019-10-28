import os

from utils_automation.path import YamlCustom

yaml = YamlCustom()


def get_path_info():
    return yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/path.yaml')


API_USER_PATH = get_path_info()['api']['user']
API_AUTHENTICATE_PATH = get_path_info()['api']['authenticate']
API_BLOG_PATH = get_path_info()['api']['blog']

API_COCCOC_MUSIC_LISTING = get_path_info()['api']['coccoc_music']['listing']











