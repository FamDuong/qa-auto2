import re
import json

from api.coccoc_lucky.coccoc_lucky_api import LuckyAPI;
from api.coccoc_lucky.coccoc_lucky_redis import LuckyRedis;
from databases.sql.coccoc_lucky_db import LuckyDB
from testscripts.api.coccoc_lucky.common import LuckyCommon;

import logging
LOGGER = logging.getLogger(__name__)

class TestLuckyApi:
    result = True
    lucky_api = LuckyAPI()
    lucky_db = LuckyDB()
    lucky_redis = LuckyRedis()
    common = LuckyCommon()

    # csrf_token = 'Ztj3emdX6ImdQZqpK3rzeDlhSSNZnoKDljubttz7'
    # coccoc_lucky_session = 'eyJpdiI6Im5PdUtHVDdOZnVwam9rNHNzY3NLMmc9PSIsInZhbHVlIjoiRzRTem5nZW1XbDJxRG1aeFRKWE1ndFNHR1BKZ3J1YTRRd2hUQUdObVhFb3VETThweGdLTEFUcENwQll0TEdJcmVyOFlldzBhOXdEMS9IT0UvVXRWay9CdTM3RTE5R2xVU0pXbjNGZkpPWDJ6Umo2VGxjMi9rcU4wK2JWSVZLRHAiLCJtYWMiOiJlMDM2YjBlZGQ5OTQ1ZDJjMjU2NWVhMTBhNmQ3MTcwOTdiMmY5OGU1MTU1MmQ3YTIzZGYzZDQ4OWI0YzI2YzA3In0%3D'
    # user_id = '355'

    csrf_token = None
    coccoc_lucky_session = None
    user_id = None
    key = None

    # BRBE-1047: [MKT Lucky 2] [API] Update Get lucky wheel result
    def test_get_lucky_result_format(self):
        schema = {
            "type": "object",
            "properties": {
                "prize_name": {"type": "string"},
                "prize_image_url": {"type": "string"},
                "prize_type": {"type": "string",
                               "enum" : ["good_luck", "reward"],},
                "prize_token": {"type": "string"},
                "order": {"type": "number"},
                "remain_play_times": {"type": "number"},
                "user_collection": {
                    "type": "object",
                    "properties": {
                        "collection_id": {"type": "number"},
                        "name": {"type": "string"},
                        "image_url": {"type": "string"},
                        "description": {"type": "string"},
                    }
                }
            },
            "required": "user_collection",
        }
        for i in range(10):
            response = self.lucky_api.request_post_lucky_result()
            print(response)
            self.common.validate_jsonschema(response, schema)

        self.validate_result()

    # BRBE-1045: [MKT Lucky 2] [API] Update cache
    #   + Mỗi lần user quay sẽ update lại cache cho phần prizes này. (key: USER_COLLECTIONS_PRIZE_STATISTIC_ + user_id)
    #   + Mỗi lần update user_collection sẽ update lại số lượng collection cho user. (KEY: TOTAL_USER_COLLECTIONS_ + user_id)
    def test_get_lucky_result_validate_users(self):
        self.set_variable()
        # Get prizes
        db_prizes = self.lucky_db.get_lucky_db(f'SELECT c.prize_id, c.name, c.image_url, c.prize_type, b.order FROM coccoc_lucky.prize_days a INNER JOIN coccoc_lucky.prize_configs b ON b.prize_config = a.prize_config INNER JOIN coccoc_lucky.prizes c ON c.prize_id = b.prize_id WHERE date(a.value_date) = curdate() ORDER BY b.order  and prize_type != "good_luck";')
        db_prizes_id = self.lucky_db.get_list_db(db_prizes, 0)
        db_prizes_name = self.lucky_db.get_list_db(db_prizes, 1)

        for i in range(10):
            LOGGER.info("Play times: %s" % i)
            response = self.lucky_api.request_post_lucky_result()
            if response["prize_type"] != "good_luck":
                # Check WIn Prizes
                key = self.lucky_redis.get_lucky_today_key("WIN_PRIZES")
                redis_win_prizes = self.lucky_redis.redis_get(key, format_data=None)

                prize_id = self.common.get_reference_data_in_list(db_prizes_id, db_prizes_name, response["prize_name"])
                today_win_number = self.get_today_win_number_from_redis(redis_win_prizes, prize_id)
                LOGGER.info("today_win_number: %s" % today_win_number)

            # If user wins prizes

            # BRBE-1045: Mỗi lần user quay sẽ update lại cache cho phần prizes này. (key: USER_COLLECTIONS_PRIZE_STATISTIC_ + user_id)
            key = self.lucky_redis.get_lucky_key("USER_COLLECTION_PRIZE_STATISTICS_%s" % self.user_id)
            redis_user_collection = self.lucky_redis.redis_get(key, format_data=None)
            self.common.assert_is_not_none(redis_user_collection, "USER_COLLECTIONS_PRIZE_STATISTIC")

            # BRBE-1045: Mỗi lần update user_collection sẽ update lại số lượng collection cho user. (KEY: TOTAL_USER_COLLECTIONS_ + user_id)
            key = self.lucky_redis.get_lucky_key("TOTAL_USER_COLLECTIONS_%s" % self.user_id)
            redis_total_user_collection = self.lucky_redis.redis_get(key, format_data=None)
            self.common.assert_is_not_none(redis_total_user_collection, "TOTAL_USER_COLLECTIONS")

        self.validate_result()

    # BRBE-1045: [MKT Lucky 2] [API] Update cache
    #   Get today user check in from Redis cache => @USER_CHECKIN
    #         Key = USER_CHECKINS_{user_id}_{today}
    def test_get_lucky_result_validate_remain_play_times(self):
        self.set_variable()
        key = self.lucky_redis.get_lucky_today_key("USER_CHECKIN_%s" % self.user_id)
        for i in range(10):
            response = self.lucky_api.request_post_lucky_result()

            redis_user_checkin = self.lucky_redis.redis_get(key, format_data=None)
            redis_user_checkin = self.lucky_redis.convert_redis_data_to_dic(redis_user_checkin, "USER_CHECKIN")
            remain_play_time = redis_user_checkin["totalPlayTimes"] - redis_user_checkin["playedTimes"]
            print(redis_user_checkin)
            self.common.assert_equals(remain_play_time, response["remain_play_times"])
        self.validate_result()

    # BRBE-1045: [MKT Lucky 2] [API] Update cache
    #   Get today user check in from Redis cache => @USER_CHECKIN
    #         Key = USER_CHECKINS_{user_id}_{today}
    #         If not existed then get from DB same above
    #         @remain_play_times = @USER_CHECKIN.total_play_times - played_times
    def test_get_lucky_result_validate_remain_play_times_delete_on_Redis(self):
        self.set_variable()
        key = self.lucky_redis.get_lucky_today_key("USER_CHECKIN_%s" % self.user_id)
        # Delete Redis value
        print("    DELETE KEY: %s" % key)
        self.lucky_redis.redis_delete(key)
        redis_user_checkin = self.lucky_redis.redis_get(key, format_data=None)
        self.common.assert_is_none(redis_user_checkin, key)

        # Call api from home
        print("    Call api again")
        response = self.lucky_api.request_post_lucky_result()

        totalPlayTimes = self.lucky_db.get_list_lucky_db(f'SELECT total_play_times FROM coccoc_lucky.user_checkins where user_id = "{self.user_id}" and checkin_date = curdate();')
        playedTimes = self.lucky_db.get_list_lucky_db(f'SELECT played_times FROM coccoc_lucky.user_checkins where user_id = "{self.user_id}" and checkin_date = curdate();')
        remain_play_time = int(totalPlayTimes[0]) - int(playedTimes[0])
        self.common.assert_equals(remain_play_time, response["remain_play_times"])

        print("    VALIDATE KEY AGAIN")
        redis_user_checkin = self.lucky_redis.redis_get(key, format_data=None)
        redis_user_checkin = self.lucky_redis.convert_redis_data_to_dic(redis_user_checkin, "USER_CHECKIN")
        self.common.assert_is_not_none(redis_user_checkin, key)

        self.validate_result()

    # BRBE-1045: [MKT Lucky 2] [API] Update cache
    #   Else if @remain_play_time > 0 then
    #         Update @USER_CHECKIN in cache
    #             @USER_CHECKIN.played_times = @USER_CHECKIN.played_times + 1
    #         Update played times for today checkin
    #             UPDATE user_checkin
    #             SET
    #                 played_times = played_times + 1
    #             WHERE
    #                 user_id = @user_id AND
    #                 checkin_date = TODAY
    #         SET result.remain_play_times = @remain_play_times  -1;
    # Pass with playTimes = 5, not pass if = 300
    def test_get_lucky_result_validate_played_times(self):
        self.set_variable()
        for i in range(5):
            redis_user_checkin = self.get_redis_user_checkin()
            playedTimes = redis_user_checkin["playedTimes"]

            # Xoay again
            response = self.lucky_api.request_post_lucky_result()
            redis_user_checkin = self.get_redis_user_checkin()
            playedTimes_after = redis_user_checkin["playedTimes"]

            self.common.assert_equals(str(playedTimes + 1), str(playedTimes_after))

            # Check in DB
            playedTimes = self.lucky_db.get_list_lucky_db(f'SELECT played_times FROM coccoc_lucky.user_checkins where user_id = "{self.user_id}" and checkin_date = curdate();')
            self.common.assert_equals(str(playedTimes[0]), str(playedTimes_after))

        self.validate_result()

    # BRBE-1045: [MKT Lucky 2] [API] Update cache
    #   Process get lucky result
    #             Get all prizes of today from Redis
    #                 Key = PRIZES_{TODAY}
    #                 If not existed then get from DB same above
    #                 Extract to 2 lists by prize type
    #                     lstRewardPrize: prizes with type <> good_luck        => order by day limit desc
    #                     lstGoodLuckPrize: prizes with type = good_luck
    def test_get_lucky_result_execute_turns(self):
        self.set_variable()
        for i in range(1000):
            response = self.lucky_api.request_post_lucky_result()
            LOGGER.info(response)


    def validate_result(self):
        result = self.common.get_result()
        assert result == True

    def set_variable(self):
        self.user_id = self.lucky_api.user_id
        self.coccoc_lucky_session = self.lucky_api.coccoc_lucky_session
        self.user_id = self.lucky_api.user_id

    # Get redis user checkin
    def get_redis_user_checkin(self):
        key = self.lucky_redis.get_lucky_today_key("USER_CHECKIN_%s" % self.user_id)
        redis_user_checkin = self.lucky_redis.redis_get(key, format_data=None)
        redis_user_checkin = self.lucky_redis.convert_redis_data_to_dic(redis_user_checkin, "USER_CHECKIN")
        return redis_user_checkin

    # Multi request & check ratio
    def test_get_lucky_result_many_times(self):
        self.set_variable()
        total_play_times = 5000
        probability = 5
        list_prizes = []

        for i in range(total_play_times):
            LOGGER.info("Play times: %s" % i)
            response = self.lucky_api.request_post_lucky_result(time_interval=0)
            list_prizes.append(response["prize_name"])
        ratio = self.common.division(total_play_times, list_prizes.count("Đèn cù "))
        print("Ratio of Đèn cù: %s / %s" % (ratio, probability))
        ratio = self.common.division(total_play_times, list_prizes.count("Đèn con cá"))
        print("Ratio of Đèn con cá: %s / %s" % (ratio, probability))
        ratio = self.common.division(total_play_times, list_prizes.count("Đèn kéo quân"))
        print("Ratio of Đèn kéo quân: %s / %s" % (ratio, probability))
        ratio = self.common.division(total_play_times, list_prizes.count("Đèn ông sao"))
        print("Ratio of Đèn ông sao: %s / %s" % (ratio, probability))
        ratio = self.common.division(total_play_times, list_prizes.count("Voucher brand 1"))
        print("Ratio of Voucher brand 1: %s / %s" % (ratio, probability))
        ratio = self.common.division(total_play_times, list_prizes.count("Voucher brand 2"))
        print("Ratio of Voucher brand 2: %s / %s" % (ratio, probability))


    # Full flow & check functional
    def test_get_lucky_result_validate_result(self):
        self.set_variable()
        # Get prizes
        db_prizes = self.lucky_db.get_lucky_db(f'SELECT c.prize_id, c.name, c.image_url, c.prize_type, b.order FROM coccoc_lucky.prize_days a INNER JOIN coccoc_lucky.prize_configs b ON b.prize_config = a.prize_config INNER JOIN coccoc_lucky.prizes c ON c.prize_id = b.prize_id WHERE date(a.value_date) = curdate() ORDER BY b.order  and prize_type != "good_luck";')
        db_prizes_id = self.lucky_db.get_list_db(db_prizes, 0)
        db_prizes_name = self.lucky_db.get_list_db(db_prizes, 1)

        # Win prizes
        key = self.lucky_redis.get_lucky_today_key("WIN_PRIZES")
        redis_win_prizes_before = self.lucky_redis.redis_get(key, format_data=None)

        for i in range(100):
            LOGGER.info("Play times: %s" % i)
            response = self.lucky_api.request_post_lucky_result(time_interval=0)

            # User win prizes
            prize_type = response["prize_type"]
            if prize_type != "good_luck":
                prize_token = response["prize_token"]
                # Check WIn Prizes
                redis_win_prizes_after= self.lucky_redis.redis_get(key, format_data=None)
                # After
                prize_id = self.common.get_reference_data_in_list(db_prizes_name, db_prizes_id, response["prize_name"])
                prize_id = prize_id[0]
                today_win_number_before = self.get_today_win_number_from_redis(redis_win_prizes_before, prize_id)
                today_win_number_after = self.get_today_win_number_from_redis(redis_win_prizes_after, prize_id)
                LOGGER.info("Check WIN_PRIZES: ")
                LOGGER.info("    prize_id               : %s" % prize_id)
                LOGGER.info("    today_win_number before: %s" % today_win_number_before)
                LOGGER.info("    today_win_number after : %s" % today_win_number_after)
                assert today_win_number_after == today_win_number_before + 1
                redis_win_prizes_before = redis_win_prizes_after

                # INSERT INTO user_plays
                # db_user_plays = self.lucky_db.get_lucky_db(f'select prize_token, prize_id, collection_id, status, prize_type, play_time from coccoc_lucky.user_plays where user_id = "{self.user_id}" and play_date = curdate() order by play_time desc limit 1;')
                db_user_plays = self.lucky_db.get_lucky_db(f'select prize_token, prize_id, collection_id, status, prize_type, play_time from coccoc_lucky.user_plays '
                                                           f'where user_id = "{self.user_id}" and prize_token = "{prize_token}" '
                                                           f'and play_date = curdate() order by play_time desc limit 1;')
                db_prize_token = self.lucky_db.get_list_db(db_user_plays, 0)
                db_prize_id = self.lucky_db.get_list_db(db_user_plays, 1)
                db_collection_id = self.lucky_db.get_list_db(db_user_plays, 2)
                db_status = self.lucky_db.get_list_db(db_user_plays, 3)
                db_prize_type = self.lucky_db.get_list_db(db_user_plays, 4)

                LOGGER.info("INSERT INTO user_plays: ")
                self.common.assert_equals(response["prize_token"], db_prize_token[0], "prize_token")
                self.common.assert_equals(prize_id, db_prize_id[0], "prize_id")
                if prize_type != "voucher":
                    self.common.assert_equals("new", db_status[0], "status")
                else:
                    self.common.assert_equals("done", db_status[0], "status")
                self.common.assert_equals(response["prize_type"], db_prize_type[0], "prize_type")

                # Check if got collection
                # if db_collection_id[0] == "1":
                if prize_type == "collection":
                    # Check if convert data to collection
                    LOGGER.info("CHECK IF USER GOT A COLLECTION: ")
                    db_user_plays_collection = self.lucky_db.get_lucky_db(f'SELECT prize_id, count(prize_id) FROM user_plays WHERE user_id = "{self.user_id}" AND status = "new" AND collection_id = 1 group by prize_id;')
                    db_user_plays_collection_prize_id = self.lucky_db.get_list_db(db_user_plays_collection, 0)
                    db_user_plays_collection_total = self.lucky_db.get_list_db(db_user_plays_collection, 0)
                    # If there is any prize = 0, OK, all <> 0: FAILED
                    self.common.assert_list_contains_item(db_user_plays_collection_total, "0")

                    # If user colect all prize of this collection (isCompledCollection = true) then
                    LOGGER.info("CHECK COLLECTION INFO IN USER_COLLECTIONS: ")
                    db_user_plays_collection = self.lucky_db.get_list_lucky_db(f'SELECT prize_id, count(prize_id) FROM user_plays WHERE user_id = "{self.user_id}" AND status = "done" AND collection_id = 1 group by prize_id;')
                    db_user_collection = self.lucky_db.get_list_lucky_db(f'SELECT * FROM coccoc_lucky.user_collections where user_id = {self.user_id} and created_date = curdate();')
                    if len(db_user_plays_collection) != 0:
                        self.common.assert_is_not_none(db_user_collection, "user_collections")

                # Check if got voucher
                if prize_type == "voucher":
                    LOGGER.info("CHECK IF USER GOT A VOUCHER: ")
                    db_user_vouchers = self.lucky_db.get_list_lucky_db(f'select voucher_code from coccoc_lucky.user_plays where prize_token = "{prize_token}";')
                    voucher_code = db_user_vouchers[0]
                    self.common.assert_is_not_none(voucher_code, "voucher_code")
                    # Check if voucher set to done
                    db_user_vouchers_status = self.lucky_db.get_list_lucky_db(f'SELECT status FROM coccoc_lucky.prize_vouchers where voucher_code = "{voucher_code}" and prize_id = "{prize_id}";')
                    self.common.assert_equals(1, len(db_user_vouchers_status), "Number of voucher in prize_vouchers")
                    voucher_status = db_user_vouchers_status[0]
                    self.common.assert_equals("used", voucher_status, "voucher_code_status")
                    # Check if voucher code is used more than 1 times
                    db_user_vouchers = self.lucky_db.get_list_lucky_db(f'select count(voucher_code) from coccoc_lucky.user_plays where voucher_code = "{voucher_code}";')
                    self.common.assert_equals(db_user_vouchers[0], "1", "Number of voucher in user_plays")
        self.validate_result()

    def get_today_win_number_from_redis(self, redis_data, prize_id):
        today_win_number = None
        # redis_data = '"a:7:{i:0;a:2:{s:8:\"prize_id\";i:15;s:16:\"today_win_number\";i:184;}i:1;a:2:{s:8:\"prize_id\";i:16;s:16:\"today_win_number\";i:119;}i:2;a:2:{s:8:\"prize_id\";i:17;s:16:\"today_win_number\";i:75;}i:3;a:2:{s:8:\"prize_id\";i:18;s:16:\"today_win_number\";i:98;}i:4;a:2:{s:8:\"prize_id\";i:19;s:16:\"today_win_number\";i:85;}i:5;a:2:{s:8:\"prize_id\";i:20;s:16:\"today_win_number\";i:73;}i:6;a:2:{s:8:\"prize_id\";i:21;s:16:\"today_win_number\";i:35;}}"'
        redis_data = redis_data.replace(chr(0), "")
        redis_data = re.sub(";i:", " : ", redis_data)
        redis_data = re.sub("prize_id\";s:[0-9]*:\"", 'prize_id\" : \"', redis_data)
        redis_data = re.sub("i:[0-9]a:2:", ", ", redis_data)
        redis_data = re.sub(";s:[0-9]*:", ' , ', redis_data)
        redis_data = re.sub("s:[0-9]*:", "", redis_data)
        redis_data = re.sub(";", "", redis_data)
        redis_data = re.sub("i:[0-9]a:2:", "; ", redis_data)
        redis_data = re.sub("a:6:{; ", "", redis_data)
        redis_data = re.sub("}}", "}", redis_data)
        # print(redis_data)
        redis_data = redis_data.split(";")
        #print(redis_data)
        for i in range(len(redis_data)):
            sub_data = json.loads(redis_data[i])
            # LOGGER.info("prize_id        : %s" % sub_data["prize_id"])
            # LOGGER.info("today_win_number        : %s" % sub_data["today_win_number"])
            if str(sub_data["prize_id"]) == str(prize_id):
                today_win_number = sub_data["today_win_number"]
                break
        return today_win_number


    # Use to reset data of user if need
    def test_update_user_turn(self):
        email = "coccocbrowser15@gmail.com"
        db_user_checkin = self.lucky_db.get_list_lucky_db(f'SELECT user_id FROM coccoc_lucky.user_checkins where user_id in (select user_id from coccoc_lucky.users where email="{email}") and checkin_date = curdate();')
        user_id = db_user_checkin[0]
        if db_user_checkin == None:
            exit()
        print("FOUND")
        self.lucky_db.update_lucky_db(f'UPDATE coccoc_lucky.user_checkins SET total_play_times = 10000 WHERE (user_id = "{user_id}") and (checkin_date = curdate());')
        # Delete cache
        key = self.lucky_redis.get_lucky_today_key("USER_CHECKIN_%s" % user_id)
        self.lucky_redis.redis_delete(key)