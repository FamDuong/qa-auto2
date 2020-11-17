import time

from api.coccoc_lucky.coccoc_lucky_api import LuckyAPI;
from api.coccoc_lucky.coccoc_lucky_redis import LuckyRedis;
from databases.sql.coccoc_lucky_db import LuckyDB
from testscripts.api.coccoc_lucky.common import LuckyCommon;

import logging
LOGGER = logging.getLogger(__name__)

from config.environment import COCCOC_LUCKY_API_HOME

class TestLuckyApi:
    # result = True
    lucky_api = LuckyAPI()
    lucky_db = LuckyDB()
    lucky_redis = LuckyRedis()
    common = LuckyCommon()

    csrf_token = 'zCwtK4w4bfUYKm12JFzN9g8a8fsP6xaLwreE4aLv'
    coccoc_lucky_session = 'eyJpdiI6Ing5SUZBNkx0TFNQakNQbEFvdmFMenc9PSIsInZhbHVlIjoiQTUxWFdnSHMvYVl6S1BIYzJUYkJuWkpxUmZTZ2YyUytVVWFXeC9tWkVtdnNySVZURVBzSVhuNi9OcGJ4MXh6OFBFZnljaWNwSXhpaWJwVHZaRUZlemRWMk80eDJGbndLU2ZsaW5PbG5jWVJPbnFMNnpndVdiVUdTT0J2NDFyZDkiLCJtYWMiOiIwMWE1ZGEyYjVkYTVlMGNkNDA0ZWMxYzk2MjU3M2Q3MjZhYjQ0M2U4ZWIwNGIyNWVmMTNmMzY0MTZhZWNiN2EyIn0%3D'
    user_id = '383'

    # BRBE-1045
    # Configs key: //expired time: never expired : Update by reset cache
    def test_redis_config(self):
        # Get config name
        db_config = self.lucky_db.get_lucky_db(f'SELECT name, value FROM coccoc_lucky.configs;')
        db_config_name = self.lucky_db.get_list_db(db_config, 0)
        db_config_value = self.lucky_db.get_list_db(db_config, 1)
        for i in range(len(db_config_name)):
            key = self.lucky_redis.get_lucky_key("CONFIGS_" + db_config_name[i])
            redis_config = self.lucky_redis.redis_get(key)
            redis_config = self.lucky_redis.convert_redis_data_to_dic(redis_config, "CONFIGS")
            # print(redis_config)
            # Check key is available on Redis
            self.common.assert_is_not_none(redis_config)
            # Check key contains correct data
            self.common.assert_equals(redis_config["value"], db_config_value[i])
        self.validate_result()

    # Configs key: //If not existed then get from DB
    def test_redis_config_not_in_redis(self):
        # Get config name
        db_config = self.lucky_db.get_lucky_db(f'SELECT name, value FROM coccoc_lucky.configs;')
        db_config_name = self.lucky_db.get_list_db(db_config, 0)
        db_config_value = self.lucky_db.get_list_db(db_config, 1)
        for i in range(len(db_config_name)):
            key = self.lucky_redis.get_lucky_key("CONFIGS_" + db_config_name[i])

            # Check delete successfully
            print("    DELETE KEY: %s" % key)
            self.lucky_redis.redis_delete(key)
            redis_config = self.lucky_redis.redis_get(key, format_data=None)
            self.common.assert_is_none(redis_config)

            # Call api from home
            print("    Call api from home")
            header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
            response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

            print("    VALIDATE KEY AGAIN")
            redis_config = self.lucky_redis.redis_get(key, format_data=None)
            redis_config = self.lucky_redis.convert_redis_data_to_dic(redis_config, "CONFIGS")
            # Check key is available on Redis again
            self.common.assert_is_not_none(redis_config)
            # Check key contains correct data
            self.common.assert_equals(redis_config["value"], db_config_value[i])
        self.validate_result()

    # Collections key: //expired time: never expired : Update by reset cache
    def test_redis_collections(self):
        db_collection = self.lucky_db.get_list_lucky_db(f'SELECT collection_id FROM coccoc_lucky.collections where collection_id in (select collection_id from coccoc_lucky.prizes);')
        for collection_id in db_collection:
            db_collection_prize = self.lucky_db.get_lucky_db(f'SELECT a.collection_id, a.name, a.image_url, a.description, b.prize_id FROM coccoc_lucky.collections a inner join coccoc_lucky.prizes b on a.collection_id = b.collection_id where a.collection_id = "{collection_id}";')
            db_collection_prize_id = self.lucky_db.get_list_db(db_collection_prize, 0)
            db_collection_prize_name = self.lucky_db.get_list_db(db_collection_prize, 1)
            db_collection_prize_image_url = self.lucky_db.get_list_db(db_collection_prize, 2)
            db_collection_prize_description = self.lucky_db.get_list_db(db_collection_prize, 3)
            db_collection_prize_prize_id = self.lucky_db.get_list_db(db_collection_prize, 4)

            key = self.lucky_redis.get_lucky_key("COLLECTIONS_" + str(collection_id))
            redis_collection = self.lucky_redis.redis_get(key, format_data=None)

            # print(redis_collection)
            # Check key is available on Redis
            self.common.assert_is_not_none(redis_collection, key)
            # Check key contains correct data
            if self.common.result:
                redis_collection = self.lucky_redis.convert_redis_data_to_dic(redis_collection, "COLLECTIONS")
                self.common.assert_equals(redis_collection["collectionId"], db_collection_prize_id[0])
                self.common.assert_equals(redis_collection["name"], db_collection_prize_name[0])
                self.common.assert_equals(redis_collection["imageUrl"], db_collection_prize_image_url[0])
                self.common.assert_equals(redis_collection["description"], db_collection_prize_description[0])
                # self.common.assert_equals(redis_collection["prizeIdArray"], db_collection_prize_prize_id[0])
        self.validate_result()

    # Collections key: //If not existed then get from DB
    def test_redis_collections_not_in_redis(self):
        # Get config name
        db_collection = self.lucky_db.get_list_lucky_db(f'SELECT collection_id FROM coccoc_lucky.collections where collection_id in (select collection_id from coccoc_lucky.prizes);')
        # db_config_name = self.lucky_db.get_list_db(db_config, 0)
        # db_config_value = self.lucky_db.get_list_db(db_config, 1)
        for collection_id in db_collection:
            db_collection_prize = self.lucky_db.get_lucky_db(
                f'SELECT a.collection_id, a.name, a.image_url, a.description, b.prize_id FROM coccoc_lucky.collections a inner join coccoc_lucky.prizes b on a.collection_id = b.collection_id where a.collection_id = "{collection_id}";')
            db_collection_prize_id = self.lucky_db.get_list_db(db_collection_prize, 0)
            db_collection_prize_name = self.lucky_db.get_list_db(db_collection_prize, 1)
            db_collection_prize_image_url = self.lucky_db.get_list_db(db_collection_prize, 2)
            db_collection_prize_description = self.lucky_db.get_list_db(db_collection_prize, 3)
            db_collection_prize_prize_id = self.lucky_db.get_list_db(db_collection_prize, 4)
            key = self.lucky_redis.get_lucky_key("COLLECTIONS_" + str(collection_id))

            # Check delete successfully
            print("    DELETE KEY: %s" % key)
            self.lucky_redis.redis_delete(key)
            redis_collection = self.lucky_redis.redis_get(key, format_data=None)
            self.common.assert_is_none(redis_collection, key)

            # Call api from home
            print("    Call api from home")
            header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
            response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

            print("    VALIDATE KEY AGAIN")
            redis_collection = self.lucky_redis.redis_get(key, format_data=None)

            # Check key contains correct data
            self.common.assert_is_not_none(redis_collection, key)
            # Check key contains correct data
            if self.common.result:
                redis_collection = self.lucky_redis.convert_redis_data_to_dic(redis_collection, "COLLECTIONS")
                self.common.assert_equals(redis_collection["collectionId"], str(db_collection_prize_id[0]))
                self.common.assert_equals(redis_collection["name"], db_collection_prize_name[0])
                self.common.assert_equals(redis_collection["imageUrl"], db_collection_prize_image_url[0])
                self.common.assert_equals(redis_collection["description"], db_collection_prize_description[0])
                # self.common.assert_equals(redis_collection["prizeIdArray"], db_collection_prize_prize_id[0])
        self.validate_result()

    # Prize days : Update cache when change value from CMS //expired time: 1 day
    def test_redis_prize_day(self):
        db_prize_day = self.lucky_db.get_list_lucky_db(f'SELECT prize_config, special_day, image_url FROM coccoc_lucky.prize_days WHERE value_date = curdate();')
        # db_value_date = self.lucky_db.get_list_db(db_prize_day, 0)
        db_prize_config = self.lucky_db.get_list_db(db_prize_day, 0)
        db_special_day = self.lucky_db.get_list_db(db_prize_day, 1)
        db_image_url = self.lucky_db.get_list_db(db_prize_day, 2)

        # Validate Redis
        key = self.lucky_redis.get_lucky_today_key("PRIZE_DAYS")
        redis_prize_day = self.lucky_redis.redis_get(key)

        # Check key is available on Redis
        print("    VALIDATE KEY ON REDIS")
        self.common.assert_is_not_none(redis_prize_day)
        # Check key contains correct data
        self.common.assert_contains(redis_prize_day, db_prize_config[0])
        self.common.assert_contains(redis_prize_day, db_special_day[0])
        self.common.assert_contains(redis_prize_day, db_image_url[0])

        # Check delete successfully
        print("    DELETE KEY: %s" % key)
        self.lucky_redis.redis_delete(key)
        redis_prize_day = self.lucky_redis.redis_get(key, format_data=None)
        self.common.assert_is_none(redis_prize_day, key)

        # Call api from home
        print("    Call api from home")
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

        print("    VALIDATE KEY AGAIN")
        redis_prize_day = self.lucky_redis.redis_get(key, format_data=None)

        # Check key contains correct data
        self.common.assert_is_not_none(redis_prize_day, key)

        # Check key contains correct data
        if self.common.result:
            self.common.assert_contains(redis_prize_day, db_prize_config[0])
            self.common.assert_contains(redis_prize_day, db_special_day[0])
            self.common.assert_contains(redis_prize_day, db_image_url[0])

        self.validate_result()

    # Prize days : List prizes today => on CMS if change value then need to remove this cache //expired time: 1 day
    def test_redis_prizes(self):
        # Get today user check in from Redis cache => @USER_CHECKIN
        db_prizes = self.lucky_db.get_lucky_db(f'SELECT	c.name,	c.image_url, c.prize_type, b.order FROM coccoc_lucky.prize_days a INNER JOIN coccoc_lucky.prize_configs b ON b.prize_config = a.prize_config INNER JOIN coccoc_lucky.prizes c ON c.prize_id = b.prize_id WHERE date(a.value_date) = curdate() ORDER BY b.order;')
        db_prizes_name = self.lucky_db.get_list_db(db_prizes, 0)
        db_prizes_image_url = self.lucky_db.get_list_db(db_prizes, 1)
        db_prizes_prize_type = self.lucky_db.get_list_db(db_prizes, 2)
        db_prizes_order = self.lucky_db.get_list_db(db_prizes, 3)

        key = self.lucky_redis.get_lucky_today_key("PRIZES")
        redis_prizes = self.lucky_redis.redis_get(key)

        # Check key is available on Redis
        print("    VALIDATE KEY ON REDIS")
        self.common.assert_is_not_none(redis_prizes)
        # Check key contains correct data
        for i in range(len(db_prizes_name)):
            self.common.assert_contains(redis_prizes, db_prizes_name[i])
            self.common.assert_contains(redis_prizes, db_prizes_image_url[i])
            self.common.assert_contains(redis_prizes, db_prizes_prize_type[i])
            self.common.assert_contains(redis_prizes, db_prizes_order[i])

        # Check delete successfully
        print("    DELETE KEY: %s" % key)
        self.lucky_redis.redis_delete(key)
        redis_prizes = self.lucky_redis.redis_get(key, format_data=None)
        self.common.assert_is_none(redis_prizes, key)

        # Call api from home
        print("    Call api from home")
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

        print("    VALIDATE KEY AGAIN")
        redis_prizes = self.lucky_redis.redis_get(key, format_data=None)

        # Check key contains correct data
        self.common.assert_is_not_none(redis_prizes, key)

        # Check key contains correct data
        if self.common.result:
            for i in range(len(db_prizes_name)):
                self.common.assert_contains(redis_prizes, db_prizes_name[i])
                self.common.assert_contains(redis_prizes, db_prizes_image_url[i])
                self.common.assert_contains(redis_prizes, db_prizes_prize_type[i])
                self.common.assert_contains(redis_prizes, db_prizes_order[i])

        self.validate_result()

    # Recent winners: //expired time: 5 minutes
    def test_redis_recent_winners(self):
        for i in range(10):
            reccent_winners = self.lucky_db.get_lucky_db(f'SELECT b.user_avatar, b.email, c.name as prize_name, c.small_image_url as prize_image_url, c.prize_type FROM coccoc_lucky.user_plays a INNER JOIN coccoc_lucky.users b ON b.user_id = a.user_id INNER JOIN coccoc_lucky.prizes c ON c.prize_id = a.prize_id WHERE c.prize_type != "good_luck" ORDER BY a.created_at DESC LIMIT 20;')
            db_user_avatar = self.lucky_db.get_list_db(reccent_winners, 0)
            db_email = self.lucky_db.get_list_db(reccent_winners, 1)
            db_prize_name = self.lucky_db.get_list_db(reccent_winners, 2)
            db_prize_image_url = self.lucky_db.get_list_db(reccent_winners, 3)
            db_prize_type = self.lucky_db.get_list_db(reccent_winners, 4)

            # Get from api
            api_recent_winner = self.lucky_api.request_get_recent_winner()

            key = self.lucky_redis.get_lucky_today_key("RECENT_WINNERS")
            redis_reccent_winners = self.lucky_redis.redis_get(key, format_data=None)

            # Check key is available on Redis
            self.common.assert_is_not_none(redis_reccent_winners)
            # Check key contains correct data
            if self.common.get_result():
                for i in range(len(db_user_avatar)):
                    # Compare with Redis
                    self.common.assert_contains(redis_reccent_winners, db_user_avatar[i], "redis: user_avatar")
                    #self.common.assert_contains(redis_reccent_winners, db_email[i])
                    self.common.assert_contains(redis_reccent_winners, db_prize_name[i], "redis: prize_name")
                    self.common.assert_contains(redis_reccent_winners, db_prize_image_url[i], "redis: prize_image_url")
                    self.common.assert_contains(redis_reccent_winners, db_prize_type[i], "redis: prize_type")

                    # Compare with response
                    self.common.assert_contains(api_recent_winner[i]["user_avatar"], db_user_avatar[i], "api: user_avatar")
                    self.common.assert_contains(api_recent_winner[i]["prize_name"], db_prize_name[i], "api: prize_name")
                    self.common.assert_contains(api_recent_winner[i]["prize_image_url"], db_prize_image_url[i], "api: prize_image_url")
                    self.common.assert_contains(api_recent_winner[i]["prize_type"], db_prize_type[i], "api: prize_type")

                #  (we need to update it in each 2 minutes).
                # time.sleep(120)
                time.sleep(120)

        self.validate_result()

    # User checkin //expired time: 1 day
    def test_redis_user_checkins(self):
        # Get users checkin to day
        db_user_checkins = self.lucky_db.get_list_lucky_db(f'SELECT * FROM coccoc_lucky.user_checkins where user_id = "{self.user_id}" and date(updated_at) = curdate() limit 10;')
        for user_id in db_user_checkins:
            db_user_value = self.lucky_db.get_lucky_db(f'SELECT user_id, checkin_date, total_play_times, played_times, is_mobile FROM coccoc_lucky.user_checkins WHERE user_id = "{user_id}" AND checkin_date = curdate();')
            db_user_id = self.lucky_db.get_list_db(db_user_value, 0)
            db_checkin_date = self.lucky_db.get_list_db(db_user_value, 1)
            db_total_play_times = self.lucky_db.get_list_db(db_user_value, 2)
            db_is_mobile = self.lucky_db.get_list_db(db_user_value, 2)

            # Check in Redis
            print("    VALIDATE KEY ON REDIS")
            key = self.lucky_redis.get_lucky_today_key("USER_CHECKIN_%s" % user_id)
            redis_user_checkins = self.lucky_redis.redis_get(key, format_data=None)
            # print(redis_user_checkins)

            # Check key is available on Redis
            self.common.assert_is_not_none(redis_user_checkins)
            # Check key contains correct data
            if self.common.result:
                self.common.assert_contains(redis_user_checkins, db_user_id[0])
                self.common.assert_contains(redis_user_checkins, db_checkin_date[0])
                self.common.assert_contains(redis_user_checkins, db_total_play_times[0])
                self.common.assert_contains(redis_user_checkins, db_is_mobile[0])

            # Check delete successfully
            print("    DELETE KEY: %s" % key)
            self.lucky_redis.redis_delete(key)
            redis_user_checkins = self.lucky_redis.redis_get(key, format_data=None)
            self.common.assert_is_none(redis_user_checkins, key)

            # Call api from home
            print("    Call api from home")
            header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
            response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

            print("    VALIDATE KEY AGAIN")
            redis_user_checkins = self.lucky_redis.redis_get(key, format_data=None)
            # Check key contains correct data
            self.common.assert_is_not_none(redis_user_checkins, key)
            # Check key contains correct data
            if self.common.result:
                self.common.assert_contains(redis_user_checkins, db_user_id[0])
                self.common.assert_contains(redis_user_checkins, db_checkin_date[0])
                self.common.assert_contains(redis_user_checkins, db_total_play_times[0])
                self.common.assert_contains(redis_user_checkins, db_is_mobile[0])
        self.validate_result()

    # Checkin_history //expired time: 1 day
    # I added a note to skip checking this logic in ticket description (In the document of Thang, it has this logic and Cuong implemented it.
    # Last week, after design phase, we saw that UI doesn’t show this info, so we decided to skip this logic in this version to reduce workload).
    def test_redis_checkins_history(self):
        # Get users checkin to day
        # db_user_checkins = self.lucky_db.get_list_lucky_db(f'SELECT user_id FROM coccoc_lucky.user_checkins WHERE date(checkin_date) >= (select date(value) from coccoc_lucky.configs where name="START_DATE") AND date(checkin_date) <= (select date(value) from coccoc_lucky.configs where name="END_DATE") group by user_id order by checkin_date limit 10;')
        db_user_checkins = self.lucky_db.get_list_lucky_db(f'SELECT user_id FROM coccoc_lucky.user_checkins WHERE user_id = "{self.user_id}" and date(checkin_date) >= (select date(value) from coccoc_lucky.configs where name="START_DATE") AND date(checkin_date) <= (select date(value) from coccoc_lucky.configs where name="END_DATE") group by user_id order by checkin_date limit 10;')
        for user_id in db_user_checkins:
            db_checkin_date = self.lucky_db.get_list_lucky_db(f'SELECT checkin_date FROM coccoc_lucky.user_checkins WHERE date(checkin_date) >= (select date(value) from coccoc_lucky.configs where name="START_DATE") AND date(checkin_date) <= (select date(value) from coccoc_lucky.configs where name="END_DATE") and user_id = "{user_id}";')
            # Check key is available on Redis
            print("    VALIDATE KEY ON REDIS")
            key = self.lucky_redis.get_lucky_today_key("CHECKIN_HISTORY_%s" % user_id)
            redis_checkins_history = self.lucky_redis.redis_get(key, format_data=None)

            # Check key is available on Redis
            self.common.assert_is_not_none(redis_checkins_history)
            # Check key contains correct data
            if self.common.result:
                checkin_date = self.common.convert_list_to_string(db_checkin_date, "checkin_date on Redis")
                self.common.assert_contains(redis_checkins_history, checkin_date)

            # Check delete successfully
            print("    DELETE KEY: %s" % key)
            self.lucky_redis.redis_delete(key)
            redis_checkins_history = self.lucky_redis.redis_get(key, format_data=None)
            self.common.assert_is_none(redis_checkins_history, key)

            # Call api from home
            print("    Call api from home")
            header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
            response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

            print("    VALIDATE KEY AGAIN")
            redis_checkins_history = self.lucky_redis.redis_get(key, format_data=None)
            # Check key contains correct data
            self.common.assert_is_not_none(redis_checkins_history, key)

            # Check key contains correct data
            if self.common.result:
                checkin_date = self.common.convert_list_to_string(db_checkin_date, "checkin_date on Redis")
                self.common.assert_contains(redis_checkins_history, checkin_date)

            # If not existed, then calculate and push to Redis
            # (T.B.D) Will delete and check again ??
        self.validate_result()

    # Today win prizes: //expired time: 1 day
    def test_redis_win_prizes(self):
        db_win_prizes = self.lucky_db.get_list_lucky_db(f'SELECT prize_id, count(*) as today_win_number FROM coccoc_lucky.user_plays WHERE play_date = curdate() and prize_type <> "good_luck" GROUP BY prize_id;')
        db_prize_id = self.lucky_db.get_list_db(db_win_prizes, 0)
        db_number = self.lucky_db.get_list_db(db_win_prizes, 1)

        # Check key is available on Redis
        print("    VALIDATE KEY ON REDIS")
        key = self.lucky_redis.get_lucky_today_key("WIN_PRIZES")
        redis_win_prizes = self.lucky_redis.redis_get(key, format_data=None)
        self.common.assert_is_not_none(redis_win_prizes, key)
        # Check key contains correct data
        if self.common.result:
            for i in range(len(db_prize_id)):
                self.common.assert_contains(redis_win_prizes, db_prize_id[i])
                self.common.assert_contains(redis_win_prizes, db_number[i])

        # Check delete successfully
        print("    DELETE KEY: %s" % key)
        self.lucky_redis.redis_delete(key)
        redis_win_prizes = self.lucky_redis.redis_get(key, format_data=None)
        self.common.assert_is_none(redis_win_prizes, key)

        # Call api from home
        print("    Call api from home")
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_HOME, headers=header, format=None)

        print("    VALIDATE KEY AGAIN")
        redis_win_prizes = self.lucky_redis.redis_get(key, format_data=None)
        # Check key contains correct data
        self.common.assert_is_not_none(redis_win_prizes, key)

        # Check key contains correct data
        if self.common.result:
            for i in range(len(db_prize_id)):
                self.common.assert_contains(redis_win_prizes, db_prize_id[i])
                self.common.assert_contains(redis_win_prizes, db_number[i])

        self.validate_result()

    def validate_result(self):
        # global result
        result = self.common.get_result()
        assert result == True

    # Convert lucky redis data to dic
    def test_convert_redis_data_to_dic(self):
        import re
        type = "WIN_PRIZES"
        data = '"a:7:{i:0;a:2:{s:8:\"prize_id\";i:15;s:16:\"today_win_number\";i:184;}i:1;a:2:{s:8:\"prize_id\";i:16;s:16:\"today_win_number\";i:119;}i:2;a:2:{s:8:\"prize_id\";i:17;s:16:\"today_win_number\";i:75;}i:3;a:2:{s:8:\"prize_id\";i:18;s:16:\"today_win_number\";i:98;}i:4;a:2:{s:8:\"prize_id\";i:19;s:16:\"today_win_number\";i:85;}i:5;a:2:{s:8:\"prize_id\";i:20;s:16:\"today_win_number\";i:73;}i:6;a:2:{s:8:\"prize_id\";i:21;s:16:\"today_win_number\";i:35;}}"'
        # data = 'O:25:"App\Entities\ConfigEntity":4:{s:31:" App\Entities\ConfigEntity name";s:8:"END_DATE";s:32:" App\Entities\ConfigEntity value";s:10:"2020-09-20";s:33:" App\Entities\ConfigEntity status";i:1;s:38:" App\Entities\ConfigEntity description";s:12:"end campaign";}'
        # data = data.replace(r" App\Entities\ConfigEntity ", "")
        # data = data.replace(r"App\Entities\ConfigEntity", "")
        data = data.replace(chr(0), "")
        data = re.sub(";i:", " : ", data)
        print("test_convert_redis_data_to_dic")
        if type == "USER_CHECKIN":
            data = data.replace(r"App\Entities\UserCheckInEntity", "")
            data = re.sub("ip\";s:[0-9]*:\"", 'ip\" : \"', data)
            data = re.sub("userAgent\";s:[0-9]*:\"", 'userAgent\" : \"', data)
            data = re.sub("checkInDate\";s:[0-9]*:\"", 'checkInDate\" : \"', data)
        elif type == "WIN_PRIZES":
            data = re.sub("prize_id\";s:[0-9]*:\"", 'prize_id\" : \"', data)
            print(data)
            data = re.sub("i:[0-9]a:2:", ", ", data)
        elif type == "PRIZES":
            data = data.replace(r"Illuminate\Database\Eloquent\Collection", "")
            data = re.sub("name\";s:[0-9]*:\"", 'name\" : \"', data)
            data = re.sub("image_url\";s:[0-9]*:\"", 'image_url\" : \"', data)
            data = re.sub("prize_type\";s:[0-9]*:\"", 'prize_type\" : \"', data)
            print(data)
        elif type == "CONFIGS":
            data = data.replace(r"App\Entities\ConfigEntity", "")
            data = re.sub("name\";s:[0-9]*:\"", 'name\" : \"', data)
            data = re.sub("value\";s:[0-9]*:\"", 'value\" : \"', data)
            data = re.sub("description\";s:[0-9]*:\"", 'description\" : \"', data)
        elif type == "COLLECTIONS":
            data = data.replace(r" App\Entities\CollectionEntity ", "")
            data = re.sub("name\";s:[0-9]*:\"", 'name\" : \"', data)
            data = re.sub("imageUrl\";s:[0-9]*:\"", 'imageUrl\" : \"', data)
            data = re.sub("description\";s:[0-9]*:\"", 'description\" : \"', data)
            print(data)
            start = data.find("\"prizeIdArray") + len("{") - 1
            end = data.find("}}") + 1
            substring = data[start:end]
            data = data.replace(substring, '')
            print(data)
        elif type == "USER_COLLECTIONS_PRIZE_STATISTIC":
            data = re.sub("name\";s:[0-9]*:\"", 'name\" : \"', data)
            data = re.sub("imageUrl\";s:[0-9]*:\"", 'imageUrl\" : \"', data)
            data = re.sub("description\";s:[0-9]*:\"", 'description\" : \"', data)
            print(data)

        data = re.sub(";s:[0-9]*:", ' , ', data)
        data = re.sub("s:[0-9]*:", "", data)
        data = re.sub(";", "", data)
        data = re.sub("i:[0-9]a:2:", ", ", data)

        #start = data.find("{") + len("{") - 1
        # end = data.find("}") + 1
        # substring = data[start:end]
        #data = substring
        print(data)
        # Convert to dic
        # data_dict = eval(data)
        # return data_dict