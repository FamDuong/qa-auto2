import os

from utils_automation.path import YamlCustom

yaml = YamlCustom()


def get_environment_info():
    return yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/env.yaml')


API_SERVER_URL = get_environment_info()['api_server_url']
API_COCCOC_PLAYLIST_URL = get_environment_info()['playlist_api_url']

COCCOC_MUSIC_CRAWLER_DB_SERVER = get_environment_info()['coccoc_music_crawler']['db_info']['server']
COCCOC_MUSIC_CRAWLER_DB_NAME = get_environment_info()['coccoc_music_crawler']['db_info']['database_name']
COCCOC_MUSIC_CRAWLER_DB_USER_NAME = get_environment_info()['coccoc_music_crawler']['db_info']['username']
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


# New feeds
COCCOC_NEW_FEED_DATA_URL = get_environment_info()['coccoc_new_feeds']['data']
COCCOC_NEW_FEED_DATA_DB_SERVER = get_environment_info()['coccoc_new_feeds']['db_info']['server']
COCCOC_NEW_FEED_DATA_DB_NAME = get_environment_info()['coccoc_new_feeds']['db_info']['name']
COCCOC_NEW_FEED_DATA_DB_USERNAME = get_environment_info()['coccoc_new_feeds']['db_info']['username']
COCCOC_NEW_FEED_DATA_DB_PASSWORD = get_environment_info()['coccoc_new_feeds']['db_info']['password']

COCCOC_NEW_FEED_API_CMS = get_environment_info()['coccoc_new_feeds']['domain_cms']
COCCOC_NEW_FEED_API_CMS_RULE = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['rules']
COCCOC_NEW_FEED_API_CMS_INIT_USER = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['users_init']
COCCOC_NEW_FEED_API_CMS_USER_ACTION = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['users_action']
COCCOC_NEW_FEED_API_CMS_WHITELIST_DOMAIN = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['whitelist_domains']
COCCOC_NEW_FEED_API_CMS_BLACKLIST = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['blacklist_keywords']
COCCOC_NEW_FEED_API_CMS_BLOCK_ARTICLE = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['block_articles']
COCCOC_NEW_FEED_API_CMS_PUBLISH_ARTICLE = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['publish_articles']
COCCOC_NEW_FEED_API_CMS_USER_SUBCRIBE_CATEGORIES = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['user_subcribe_categories']
COCCOC_NEW_FEED_API_CMS_USER_BLOCK_ARTICLES = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['user_block_articles']
COCCOC_NEW_FEED_API_CMS_USER_BLOCK_SOURCES = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['user_block_sources']
COCCOC_NEW_FEED_API_CMS_EDITOR_CHOISES_FEED = COCCOC_NEW_FEED_API_CMS + get_environment_info()['coccoc_new_feeds']['editor_choices_feed']
COCCOC_NEW_FEED_BUCKET_URL = get_environment_info()['coccoc_new_feeds']['bucket_url']

COCCOC_NEW_FEED_API_FE = get_environment_info()['coccoc_new_feeds']['domain_frontend']
COCCOC_NEW_FEED_API_FE_CATEGORY = COCCOC_NEW_FEED_API_FE + get_environment_info()['coccoc_new_feeds']['categories']
COCCOC_NEW_FEED_API_FE_USER_SETTING = COCCOC_NEW_FEED_API_FE + get_environment_info()['coccoc_new_feeds']['users_settings']
COCCOC_NEW_FEED_API_FE_USER_FEED = COCCOC_NEW_FEED_API_FE + get_environment_info()['coccoc_new_feeds']['users_feed']
COCCOC_NEW_FEED_API_FE_USER_ACTION = COCCOC_NEW_FEED_API_FE + get_environment_info()['coccoc_new_feeds']['users_action']

COCCOC_NEW_FEED_API_NRE_DEFAULT = get_environment_info()['coccoc_new_feeds']['nre_article_default']
COCCOC_NEW_FEED_API_NRE_ARTICLE_INFOMATION = get_environment_info()['coccoc_new_feeds']['nre_article_information']

COCCOC_NEW_FEED_REDIS_HOST = get_environment_info()['coccoc_new_feeds_redis']['host']
COCCOC_NEW_FEED_REDIS_PORT = get_environment_info()['coccoc_new_feeds_redis']['port']
COCCOC_NEW_FEED_REDIS_PASSWORD = get_environment_info()['coccoc_new_feeds_redis']['password']
COCCOC_NEW_FEED_REDIS_NODES = get_environment_info()['coccoc_new_feeds_redis']['nodes']

COCCOC_NEW_FEED_KAFKA_SERVERS = get_environment_info()['coccoc_new_feeds_kafka']['bootstrap_servers']
COCCOC_NEW_FEED_KAFKA_SASL_MECHANISM = get_environment_info()['coccoc_new_feeds_kafka']['sasl_mechanism']
COCCOC_NEW_FEED_KAFKA_SASL_PLAIN_USERNAME = get_environment_info()['coccoc_new_feeds_kafka']['sasl_plain_username']
COCCOC_NEW_FEED_KAFKA_SASL_PLAIN_PASSWORD = get_environment_info()['coccoc_new_feeds_kafka']['sasl_plain_password']
COCCOC_NEW_FEED_KAFKA_SERCURITY_PROTOCOL = get_environment_info()['coccoc_new_feeds_kafka']['security_protocol']
COCCOC_NEW_FEED_KAFKA_TOPIC_USERS = get_environment_info()['coccoc_new_feeds_kafka']['topic_users']
COCCOC_NEW_FEED_KAFKA_TOPIC_CMS = get_environment_info()['coccoc_new_feeds_kafka']['topic_cms']
COCCOC_NEW_FEED_KAFKA_TOPIC_NRE = get_environment_info()['coccoc_new_feeds_kafka']['topic_nre']

# Lucky
COCCOC_LUCKY_API_URL = get_environment_info()['coccoc_lucky']['domain']
COCCOC_LUCKY_API_HOME = COCCOC_LUCKY_API_URL + get_environment_info()['coccoc_lucky']['home']
COCCOC_LUCKY_API_GET_RESULT = COCCOC_LUCKY_API_URL + get_environment_info()['coccoc_lucky']['lucky_result']
COCCOC_LUCKY_API_MY_REWARDS = COCCOC_LUCKY_API_URL + get_environment_info()['coccoc_lucky']['my_rewards']
COCCOC_LUCKY_API_RECENT_WINNERS = COCCOC_LUCKY_API_URL + get_environment_info()['coccoc_lucky']['recent_winner']
COCCOC_LUCKY_DB_SERVER = get_environment_info()['coccoc_lucky']['db_info']['server']
COCCOC_LUCKY_DB_NAME = get_environment_info()['coccoc_lucky']['db_info']['name']
COCCOC_LUCKY_DB_USERNAME = get_environment_info()['coccoc_lucky']['db_info']['username']
COCCOC_LUCKY_DB_PASSWORD = get_environment_info()['coccoc_lucky']['db_info']['password']

COCCOC_LUCKY_REDIS_HOST = get_environment_info()['coccoc_lucky_redis']['host']
COCCOC_LUCKY_REDIS_POST = get_environment_info()['coccoc_lucky_redis']['port']
COCCOC_LUCKY_REDIS_PASSWORD = get_environment_info()['coccoc_lucky_redis']['password']

# CocCoc Edu
COCCOC_EDU_API_GIFT = get_environment_info()['coccoc_edu_quiz']['domain']

# CocCoc Account
COCCOC_ACCOUNTS_HOME_URL = get_environment_info()['coccoc_accounts']['url']['home_url']
COCCOC_ACCOUNTS_API_LOGIN = COCCOC_ACCOUNTS_HOME_URL + get_environment_info()['coccoc_accounts']['api']['login']

# CocCoc Point
COCCOC_POINTS_DB_SERVER = get_environment_info()['coccoc_points']['db_info']['server']
COCCOC_POINTS_DB_NAME = get_environment_info()['coccoc_points']['db_info']['database_name']
COCCOC_POINTS_DB_USERNAME = get_environment_info()['coccoc_points']['db_info']['username']
COCCOC_POINTS_DB_PASSWORD = get_environment_info()['coccoc_points']['db_info']['password']

COCCOC_POINTS_HOME_URL = get_environment_info()['coccoc_points']['url']['home_url']
COCCOC_POINTS_SERVICE_LOGIN = COCCOC_ACCOUNTS_HOME_URL + "/ServiceLogin?continue=https%3A%2F%2F" + get_environment_info()['coccoc_points']['url']['home_url'] + "&passive=true&service=points"

COCCOC_POINTS_API_URL = get_environment_info()['coccoc_points']['api']['domain']
COCCOC_POINTS_API_LUCKY_PRIZES = COCCOC_POINTS_API_URL + get_environment_info()['coccoc_points']['api']['lucky_prizes']
COCCOC_POINTS_API_RECENT_WINNER = COCCOC_POINTS_API_URL + get_environment_info()['coccoc_points']['api']['recent_winners']
COCCOC_POINTS_API_LUCKY_RESULT = COCCOC_POINTS_API_URL + get_environment_info()['coccoc_points']['api']['lucky_result']

COCCOC_POINTS_REDIS_HOST = get_environment_info()['coccoc_points']['redis']['host']
COCCOC_POINTS_REDIS_PORT = get_environment_info()['coccoc_points']['redis']['port']
COCCOC_POINTS_REDIS_PASSWORD = get_environment_info()['coccoc_points']['redis']['password']
