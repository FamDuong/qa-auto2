import time
import random
import time
from datetime import date
from jsonschema import validate
from api.coccoc_lucky.coccoc_lucky_api import LuckyAPI;
from api.coccoc_lucky.coccoc_lucky_redis import LuckyRedis;
from databases.sql.coccoc_lucky_db import LuckyDB
from testscripts.api.coccoc_lucky.common import LuckyCommon;


from config.environment import COCCOC_LUCKY_API_HOME

class TestLuckyApi:
    result = True
    lucky_api = LuckyAPI()
    lucky_db = LuckyDB()
    lucky_redis = LuckyRedis()
    common = LuckyCommon()
    csrf_token = 'yZnwjzWnJLuNC2iVoVjyC1PtmjvlcUrYKUjcVH6A'
    coccoc_lucky_session = 'eyJpdiI6IndhYkViVDJCV09iUG1mbkZtQmtscEE9PSIsInZhbHVlIjoiRW5kcXZiNTV6RVFrV3AyTXIvTEJQZ1cyWHhudGc1NVpGYzJUVERtYklMVmoyNnV2a0UvVy8rOHJIa1lQUUhpTXBwWTJDOG5BUU5UUzNheHBUZTJaT0lSdWtYQ2QvUW0rcU0vcnlDem9yR2JxeDgrNUUxVkRCcTE2d2d1a2t2OGMiLCJtYWMiOiI0ODZmNWFjNzE2OTJkZTA3YjQxZjJiZjRjYzdlYTgxNTAwNWFlN2VhODZlYTg2ZGU0MjUwYjkwMWQ3MmQxNWM3In0%3D'
    user_id = '192'

    # API Home: BRBE-1041: [MKT Lucky 2] [API] Update Home API
    # if user not logged in
    def test_get_lucky_home_not_logged_in(self):
        apiHomeSchema = {
            "type": "object",
            "properties": {
                "remain_play_times": {"type": "array"},
                "recent_winner": {"type": "array",
                    "avatar_url": {"type": "string"},
                    "email": {"type": "string"},
                    "prize_name": {"type": "string"},
                    "prize_name_url": {"type": "string"},
                    "prize_type": {"type": "string"},},
                "checkin_history": {"type": "array"},
                "prize_day": {"type": "object",
                     "special_day": {"type": "int"},
                     "image_url": {"type": "string"},},
                "campaign": {"type": "object",
                     "start_date": {"type": "date"},
                     "end_date": {"type": "date"},
                     "draw_date": {"type": "date"},} },
            }
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME)
        validate(instance=response, schema=apiHomeSchema)

        assert self.result == True

    # if user not logged in
    def test_get_lucky_home_logged_in(self):
        apiHomeSchema = {
            "type": "object",
            "properties": {
                "remain_play_times": {"type": "number"},
                "recent_winner": {"type": "array",
                    "avatar_url": {"type": "string"},
                    "email": {"type": "string"},
                    "prize_name": {"type": "string"},
                    "prize_name_url": {"type": "string"},
                    "prize_type": {"type": "string"},},
                "checkin_history": {"type": "array"},
                "prize_day": {"type": "object",
                     "special_day": {"type": "int"},
                     "image_url": {"type": "string"},},
                "campaign": {"type": "object",
                     "start_date": {"type": "date"},
                     "end_date": {"type": "date"},
                     "draw_date": {"type": "date"},} },
            }
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)
        validate(instance=response, schema=apiHomeSchema)

        assert self.result == True

    # Check data config
    def test_validate_config_value(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)

        # Get from Redis - Need to ask dev the key
        redis_start_date = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_START_DATE")
        redis_end_date = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_END_DATE")
        redis_draw_date = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_DRAW_DATE")
        redis_total_play = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_TOTAL_PLAY")
        redis_mobile_play = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_ADD_MOBILE_PLAY")

        # Get from DB
        start_date = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="START_DATE";')
        end_date = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="END_DATE";')
        draw_date = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="DRAW_DATE";')
        total_play = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="TOTAL_PLAY";')
        mobile_play = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="ADD_MOBILE_PLAY";')

        self.common.assert_equals(response["campaign"]["start_date"], start_date[0])
        self.common.assert_equals(response["campaign"]["end_date"], end_date[0])
        self.common.assert_equals(response["campaign"]["draw_date"], draw_date[0])

        self.common.assert_contains(redis_start_date, response["campaign"]["start_date"])
        self.common.assert_contains(redis_end_date, response["campaign"]["end_date"])
        self.common.assert_contains(redis_draw_date, response["campaign"]["draw_date"])

        self.common.assert_contains(redis_total_play, total_play[0])
        self.common.assert_contains(redis_mobile_play, mobile_play[0])

        assert self.result == True


    # If user logged in then process to create user checkin if not existed
    def test_validate_checkin_value(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)

        # Get today user check in from Redis cache => @USER_CHECKIN
        key = self.get_user_checkin_key()

        redis_user_checkin = self.lucky_redis.redis_get(key)
        print(redis_user_checkin)
        assert redis_user_checkin != None

    # If user logged in by mobile then process to create user checkin if not existed
    def test_validate_checkin_by_mobile_value(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session, user_agent_type="Mobile")
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)

        # Get today user check in from Redis cache => @USER_CHECKIN
        key = self.get_user_checkin_key()

        redis_user_checkin = self.lucky_redis.redis_get(key)
        print(redis_user_checkin)
        assert redis_user_checkin != None

    # If user logged in by mobile then process to create user checkin if not existed
    def test_validate_prizes(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)

        # Get today user check in from Redis cache => @USER_CHECKIN
        key = self.lucky_redis.get_lucky_today_key("PRIZES")
        redis_prizes = self.lucky_redis.redis_get(key)
        db_prizes = self.lucky_db.get_lucky_db(f'SELECT	c.name,	c.image_url, c.prize_type, b.order FROM coccoc_lucky.prize_days a INNER JOIN coccoc_lucky.prize_configs b ON b.prize_config = a.prize_config INNER JOIN coccoc_lucky.prizes c ON c.prize_id = b.prize_id WHERE date(a.value_date) = curdate() ORDER BY b.order;')
        db_prizes_name = self.lucky_db.get_list_db(db_prizes, 0)
        db_prizes_image_url = self.lucky_db.get_list_db(db_prizes, 1)
        db_prizes_prize_type = self.lucky_db.get_list_db(db_prizes, 2)
        db_prizes_order = self.lucky_db.get_list_db(db_prizes, 3)
        response_prizes = response["prizes"]
        for i in range(len(response_prizes)):
            self.result = self.common.assert_equals(response_prizes[i]["name"], db_prizes_name[i])
            self.result = self.common.assert_equals(response_prizes[i]["image_url"], db_prizes_image_url[i])
            self.result = self.common.assert_equals(response_prizes[i]["prize_type"], db_prizes_prize_type[i])
            self.result = self.common.assert_equals(response_prizes[i]["order"], db_prizes_order[i])
        assert self.result == True

    # If user logged in by mobile then process to create user checkin if not existed
    def test_validate_prize_day(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)

        # Get today user check in from Redis cache => @USER_CHECKIN
        key = self.lucky_redis.get_lucky_today_key("PRIZE_DAYS")
        redis_prizes = self.lucky_redis.redis_get(key)
        db_prizes = self.lucky_db.get_lucky_db(f'SELECT special_day, image_url FROM coccoc_lucky.prize_days WHERE value_date = curdate();')
        db_prizes_special_day = self.lucky_db.get_list_db(db_prizes, 0)
        db_prizes_image_url = self.lucky_db.get_list_db(db_prizes, 1)

        response_prize_day = response["prize_day"]
        self.result = self.common.assert_equals(response_prize_day["special_day"], db_prizes_special_day[0])
        if db_prizes_special_day[0] != 0:
            self.result = self.common.assert_equals(response_prize_day["image_url"], db_prizes_image_url[0])
        assert self.result == True

    # Check data config
    def test_validate_config_value(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header)

        # Get from Redis - Need to ask dev the key
        redis_start_date = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_START_DATE")
        redis_end_date = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_END_DATE")
        redis_draw_date = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_DRAW_DATE")
        redis_total_play = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_TOTAL_PLAY")
        redis_mobile_play = self.lucky_redis.redis_get("coccoc-lucky-local:coccoc_lucky_cache:CONFIGS_ADD_MOBILE_PLAY")

        # Get from DB
        start_date = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="START_DATE";')
        end_date = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="END_DATE";')
        draw_date = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="DRAW_DATE";')
        total_play = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="TOTAL_PLAY";')
        mobile_play = self.common.get_list_lucky_db(f'SELECT value FROM coccoc_lucky.configs where name="ADD_MOBILE_PLAY";')

        self.common.assert_equals(response["campaign"]["start_date"], start_date[0])
        self.common.assert_equals(response["campaign"]["end_date"], end_date[0])
        self.common.assert_equals(response["campaign"]["draw_date"], draw_date[0])

        self.common.assert_contains(redis_start_date, response["campaign"]["start_date"])
        self.common.assert_contains(redis_end_date, response["campaign"]["end_date"])
        self.common.assert_contains(redis_draw_date, response["campaign"]["draw_date"])

        self.common.assert_contains(redis_total_play, total_play[0])
        self.common.assert_contains(redis_mobile_play, mobile_play[0])

        assert self.result == True

    def get_user_checkin_key(self):
        today = date.today()
        today = today.strftime("%Y_%m_%d")
        key = "coccoc-lucky-dev:coccoc_lucky_cache:USER_CHECKIN_" + self.user_id + "_" + today
        print("User checkin key: %s" % key)
        return key

