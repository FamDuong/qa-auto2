import os

from utils_automation.path import YamlCustom

yaml = YamlCustom()


def get_environment_info():
    return yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/env.yaml')


API_SERVER_URL = get_environment_info()['api_server_url']
API_COCCOC_PLAYLIST_URL = get_environment_info()['playlist_api_url']

COCOC_MUSIC_CRAWLER_DB_SERVER = get_environment_info()['coccoc_music_crawler']['db_info']['server']
COCCOC_MUSIC_CRAWLER_DB_NAME = get_environment_info()['coccoc_music_crawler']['db_info']['database_name']
COCOC_MUSIC_CRAWLER_DB_USER_NAME = get_environment_info()['coccoc_music_crawler']['db_info']['username']
COCCOC_MUSIC_CRAWLER_DB_PASS_WORD = get_environment_info()['coccoc_music_crawler']['db_info']['password']

COCCOC_MUSIC_DATA_DOMAIN_URL = get_environment_info()['cocccoc_music_data']['domain_url']
COCCOC_MUSIC_DATA_REGULAR_USER = get_environment_info()['cocccoc_music_data']['regular_user']
COCCOC_MUSIC_DATA_REGULAR_PASSWORD = get_environment_info()['cocccoc_music_data']['regular_password']

COCCOC_MUSIC_CMS_DOMAIN_URL = get_environment_info()['coccoc_music_cms']['domain_url']
COCCOC_MUSIC_CMS_ADMIN_EMAIL = get_environment_info()['coccoc_music_cms']['admin_email']
COCCOC_MUSIC_CMS_ADMIN_PASSWORD = get_environment_info()['coccoc_music_cms']['admin_password']

COCCOC_MUSIC_API_DOMAIN_URL = get_environment_info()['coccoc_music_api']['domain_url']
COCCOC_MUSIC_API_USERNAME = get_environment_info()['coccoc_music_api']['username']
COCCOC_MUSIC_API_PASSWORD = get_environment_info()['coccoc_music_api']['password']

COCCOC_GAME_CRAWLER_DB_SERVER = get_environment_info()['coccoc_game_crawler']['db_info']['server']
COCCOC_GAME_CRAWLER_DB_NAME = get_environment_info()['coccoc_game_crawler']['db_info']['database_name']
COCCOC_GAME_CRAWLER_DB_USER_NAME = get_environment_info()['coccoc_game_crawler']['db_info']['username']
COCCOC_GAME_CRAWLER_DB_PASSWORD = get_environment_info()['coccoc_game_crawler']['db_info']['password']

COCCOC_GAME_API_DB_SERVER = get_environment_info()['coccoc_game_api']['db_info']['server']
COCCOC_GAME_API_DB_NAME = get_environment_info()['coccoc_game_api']['db_info']['database_name']
COCCOC_GAME_API_DB_USER_NAME = get_environment_info()['coccoc_game_api']['db_info']['username']
COCCOC_GAME_API_DB_PASSWORD = get_environment_info()['coccoc_game_api']['db_info']['password']

COCCOC_GAME_API_DOMAIN_URL = get_environment_info()['coccoc_game_api']['api']['domain']

COCCOC_NEW_FEED_DATA_URL = get_environment_info()['coccoc_new_feeds']['data']
COCCOC_NEW_FEED_DATA_DB_SERVER = get_environment_info()['coccoc_new_feeds']['db_info']['server']
COCCOC_NEW_FEED_DATA_DB_NAME = get_environment_info()['coccoc_new_feeds']['db_info']['name']
COCCOC_NEW_FEED_DATA_DB_USERNAME = get_environment_info()['coccoc_new_feeds']['db_info']['username']
COCCOC_NEW_FEED_DATA_DB_PASSWORD = get_environment_info()['coccoc_new_feeds']['db_info']['password']

COCCOC_NEW_FEED_API_CMS = get_environment_info()['coccoc_new_feeds']['domain']
COCCOC_NEW_FEED_API_CMS_RULE = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['rules']
COCCOC_NEW_FEED_API_CMS_INIT_USER = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['users_init']
COCCOC_NEW_FEED_API_CMS_USER_ACTION = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['users_action']
COCCOC_NEW_FEED_API_CMS_WHITELIST_DOMAIN = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['whitelist_domains']
COCCOC_NEW_FEED_API_CMS_BLACKLIST = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['blacklist_keywords']

COCCOC_NEW_FEED_API_FE = get_environment_info()['coccoc_new_feeds']['domain_frontend']
COCCOC_NEW_FEED_API_FE_CATEGORY = COCCOC_NEW_FEED_API_FE + get_environment_info()['coccoc_new_feeds']['categories']
COCCOC_NEW_FEED_API_FE_USER_SETTING = COCCOC_NEW_FEED_API_FE + get_environment_info()['coccoc_new_feeds']['users_settings']







