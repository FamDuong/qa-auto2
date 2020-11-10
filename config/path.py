import os
import logging

from utils_automation.path import YamlCustom

LOGGER = logging.getLogger(__name__)

yaml = YamlCustom()


def get_path_info():
    LOGGER.info(yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/path.yaml'))
    return yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/path.yaml')


API_PATH = get_path_info()['api']
API_USER_PATH = get_path_info()['api']['user']
API_AUTHENTICATE_PATH = get_path_info()['api']['authenticate']
API_BLOG_PATH = get_path_info()['api']['blog']

API_COCCOC_MUSIC_LISTING = get_path_info()['api']['coccoc_music']['listing']

COCCOC_MUSIC_DATA_API = get_path_info()['coccoc_music_data']['api']
COCCOC_MUSIC_DATA_API_VERSION = get_path_info()['coccoc_music_data']['version']
COCCOC_MUSIC_DATA_API_VERSION_DATA_FEEDS = get_path_info()['coccoc_music_data']['datafeeds_for_crawler']

COCCOC_MUSIC_API_VERSION = get_path_info()['coccoc_music_api']['version']
COCCOC_MUSIC_API_HOME = get_path_info()['coccoc_music_api']['home']
COCCOC_MUSIC_API_CATEGORIES = get_path_info()['coccoc_music_api']['categories']

COCCOC_ATLASSIAN_DOMAIN = get_path_info()['coccoc_atlassian_server']['domain']

COCCOC_GAME_API_HOME = get_path_info()['coccoc_game_api']['home']
COCCOC_GAME_NTP_GAMES = get_path_info()['coccoc_game_api']['ntp-games']
COCCOC_GAME_PUBLIC_EVENTS_ALL_GAMES = get_path_info()['coccoc_game_api']['public-events-all-games']
COCCOC_GAME_GAMES = get_path_info()['coccoc_game_api']['games']
