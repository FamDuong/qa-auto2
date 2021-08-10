import time
import random
import json
import logging

LOGGER = logging.getLogger(__name__)

from testscripts.api.coccoc_points.common import CocCocPointsCommon;
from databases.sql.coccoc_point_db import CocCocPointsDB;
from api.coccoc_points.coccoc_points_api import CocCocPointsAPI;
from api.coccoc_points.coccoc_points_redis import CocCocPointsRedis;

from config.environment import COCCOC_POINTS_API_LUCKY_PRIZES
from config.environment import COCCOC_POINTS_API_RECENT_WINNER
from config.environment import COCCOC_POINTS_API_LUCKY_RESULT

class TestCocCocPointServices:
    points_db = CocCocPointsDB()
    points_api = CocCocPointsAPI()
    points_common = CocCocPointsCommon()
    points_redis = CocCocPointsRedis()

    result = True

    user_id = '124'
    vid = 'ury33SQ31bT6V1o6S31urrb1b6VGoQ9Gug9bWqb2.3w1Kz-LgS_YNogpdyOWW'

    # Check exist @event.event_code in @ALL_EVENT_TYPES
    # If @event.event_code does not exist in list event type  @ALL_EVENT_TYPES  then update event log status to 'done'
    def test_event_code_not_in_event_types(self):
        self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="new_event", event_type="new_type", status="new", number_events=10)
        list_event_code = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code not in (SELECT event_code FROM points.event_types) and status <> "done";')
        assert len(list_event_code) != 0
        self.wait_point_services()
        list_event_code = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code not in (SELECT event_code FROM points.event_types) and status <> "done";')
        assert len(list_event_code) == 0

    # Check for create event desktop_one_house_use: check by manual on Redis
    # There is an issue when cannot read from edit to console
    def test_event_code_is_desktop_one_house_use(self):
        # If @event.event_date > @last_day + 1 day then reset @ndays = 1 in cache
        event_date = self.points_common.get_curdate()
        self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="desktop_one_hour_use", event_type="daily", event_date=event_date, status="new")
        key = "NDAYS_USE_DESKTOP_" + self.user_id
        redis = self.points_redis.redis_get("NDAYS_USE_DESKTOP_" + self.user_id)
        redis = self.points_redis.redis_get("NDAYS_USE_DESKTOP_" + self.user_id)
        print(redis["ndays"])

    # Check to insert new event for desktop_open_3_days, desktop_open_5_days, desktop_open_7_days
    def test_event_code_is_desktop_open_n_days(self):
        # Clear all data
        key = "NDAYS_USE_DESKTOP_" + self.user_id
        default_browser = 0
        self.points_redis.redis_del(key)
        self.points_db.delete_point_db(f'Delete FROM points.event_logs where user_id = "{self.user_id}";')
        # If @ndays >= 3 then process add event desktop_open_3_days
        day = 0
        for i in range(3):
            event_date = self.points_common.get_nextdate(i)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="desktop_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_DESKTOP_"{self.user_id}"', format_data="None")
            day = i + 1
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_3_days" and user_id = "{self.user_id}";')
        assert len(event_logs) == 1

        # If @ndays >= 5 then process add event desktop_open_5_days
        for i in range(day, day + 2):
            event_date = self.points_common.get_nextdate(i)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="desktop_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_DESKTOP_"{self.user_id}"', format_data="None")
            day = i + 1
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_5_days" and user_id = "{self.user_id}";')
        assert len(event_logs) == 1

        # If @ndays >= 7 then process add event desktop_open_7_days
        for i in range(day, day + 3):
            event_date = self.points_common.get_nextdate(i)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="desktop_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_DESKTOP_"{self.user_id}"', format_data="None")
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_7_days" and user_id = "{self.user_id}";')
        assert len(event_logs) == 1

        # Check all data
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_3_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_3_days = 1")
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_5_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_5_days = 1")
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_7_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_7_days = 1")
        assert self.result == True

    # Check to insert new event for desktop_open_3_days, desktop_open_5_days, desktop_open_7_days
    # With different vid
    def test_event_code_is_desktop_open_n_days_different_vid(self):
        # Clear all data
        key = "NDAYS_USE_DESKTOP_" + self.user_id
        default_browser = 0
        self.points_redis.redis_del(key)
        self.points_db.delete_point_db(f'Delete FROM points.event_logs where user_id = "{self.user_id}";')
        # get diff vid
        vid_1 = self.points_common.get_random_string(61)
        vid_2 = self.points_common.get_random_string(61)

        # If @ndays >= 3 then process add event desktop_open_3_days
        day = 0
        for i in range(3):
            event_date = self.points_common.get_nextdate(i)
            self.vid = self.points_common.get_random_element_in_list((vid_1, vid_2))
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="desktop_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_DESKTOP_"{self.user_id}"', format_data="None")
            day = i + 1
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "desktop_open_3_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_3_days = 1")
        assert self.result == True

    # Check to insert new event for mobile_open_3_days, mobile_open_5_days, mobile_open_7_days
    def test_event_code_is_mobile_open_n_days(self):
        # Clear all data
        key = "NDAYS_USE_MOBILE_" + self.user_id
        default_browser = 1
        self.points_redis.redis_del(key)
        self.points_db.delete_point_db(f'Delete FROM points.event_logs where user_id = "{self.user_id}";')
        # If @ndays >= 3 then process add event desktop_open_3_days
        day = 0
        for i in range(3):
            event_date = self.points_common.get_nextdate(i)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="mobile_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_MOBILE_"{self.user_id}"', format_data="None")
            day = i + 1
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "mobile_open_3_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of mobile_open_3_days = 1")

        # If @ndays >= 5 then process add event desktop_open_5_days
        for i in range(day, day + 2):
            event_date = self.points_common.get_nextdate(i)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="mobile_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_DESKTOP_"{self.user_id}"', format_data="None")
            day = i + 1
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "mobile_open_5_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of mobile_open_5_days = 1")

        # If @ndays >= 7 then process add event desktop_open_7_days
        for i in range(day, day + 3):
            event_date = self.points_common.get_nextdate(i)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code="mobile_one_hour_use", event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            redis = self.points_redis.redis_get(f'NDAYS_USE_DESKTOP_"{self.user_id}"', format_data="None")
        self.wait_point_services()
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "mobile_open_7_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of mobile_open_7_days = 1")

        # Check all data
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "mobile_open_3_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_3_days != 1")
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "mobile_open_5_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_5_days != 1")
        event_logs = self.points_db.get_list_point_db(f'SELECT * from points.event_logs where event_code = "mobile_open_7_days" and user_id = "{self.user_id}";')
        self.assert_equal(len(event_logs), 1, "Number of desktop_open_7_days != 1")
        assert self.result == True

    # If @event.event_type = 'one_time' then
    def test_event_type_is_one_time(self):
        list_events = self.points_db.get_point_db(f'SELECT event_code, earn_point FROM points.event_types where event_type = "one_time";')
        list_event_code = self.points_db.get_list_db(list_events, 0)
        list_earn_point = self.points_db.get_list_db(list_events, 1)
        default_browser = 0
        DEFAULT_BROWSER_POINT = 2

        # Clear all data
        self.points_db.delete_point_db(f'Delete FROM points.event_logs where user_id = "{self.user_id}";')
        for i in list_event_code:
            event_key = "EVENT_" + i + "_" + self.user_id
            self.points_redis.redis_del(event_key)

        event_date = self.points_common.get_curdate()
        pos_earn_points = 0
        for i in range(5):
            pre_earn_points = pos_earn_points
            event_code = self.points_common.get_random_element_in_list(list_event_code)
            earn_points = self.points_common.get_reference_data(list_event_code, list_earn_point, event_code)
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code=event_code, event_type="one_time", event_date=event_date, default_browser=default_browser, status="new")

            self.wait_point_services()
            # If count > 0 then do nothing
            # Else if count = 0 then update count in cache = 1
            event_key = "EVENT_" + event_code + "_" + self.user_id
            redis = self.points_redis.redis_get(event_key)
            self.assert_equal(redis["count"], 1, "Number of count != 1")
            # @earnPoint =  @event.earn_points * IF(@event.default_browser = 1 ? DEFAULT_BROWSER_POINTS : 1))
            # Only add points for the 1st time use

            if i == 0:
                if default_browser == 1:
                    pos_earn_points = pre_earn_points + int(earn_points) * DEFAULT_BROWSER_POINT
                else:
                    pos_earn_points = pre_earn_points + int(earn_points)
            LOGGER.info("default_browser: " + str(default_browser))
            LOGGER.info("pre_earn_points: " + str(pre_earn_points))
            LOGGER.info("earn_points: " + str(earn_points))
            LOGGER.info("pos_earn_points: " + str(pos_earn_points))
            self.assert_equal(pos_earn_points, redis["earnPoint"], "Number of earnpoints: pos_earn_points != Redis")
        assert self.result == True

    # If @event.event_type = 'daily' then
    def test_event_type_is_daily(self):
        list_events = self.points_db.get_point_db(f'SELECT event_code, earn_point, max_event_per_day FROM points.event_types where event_type = "daily";')
        list_event_code = self.points_db.get_list_db(list_events, 0)
        list_earn_point = self.points_db.get_list_db(list_events, 1)
        list_max_events = self.points_db.get_list_db(list_events, 2)

        # Clear all data
        self.points_db.delete_point_db(f'Delete FROM points.event_logs where user_id = "{self.user_id}";')
        for i in list_event_code:
            event_key = "EVENT_" + i + "_" + self.user_id
            self.points_redis.redis_del(event_key)


        # event_date = self.points_common.get_curdate()
        vid_1 = self.points_common.get_random_string(61)
        vid_2 = self.points_common.get_random_string(61)
        # event_code = self.points_common.get_random_element_in_list(list_event_code)
        # event_code = 'desktop_new_tab'
        # event_code = 'desktop_one_hour_use'
        # event_code = 'desktop_open_3_days'
        # event_code = 'desktop_open_5_days'
        # event_code = 'desktop_open_7_days'
        # event_code = 'desktop_search'
        # event_code = 'mobile_new_tab'
        event_code = 'mobile_one_hour_use'
        # event_code = 'mobile_open_3_days'
        # event_code = 'mobile_open_5_days'
        # event_code = 'mobile_open_7_days'
        event_code = 'mobile_search'
        earn_points = self.points_common.get_reference_data(list_event_code, list_earn_point, event_code)
        max_event_per_day = self.points_common.get_reference_data(list_event_code, list_max_events, event_code)

        # Clear data
        event_date = self.points_common.get_curdate()
        event_key = "EVENT_" + event_code + "_" + self.user_id + "_" + self.points_common.convert_date(event_date, '%Y-%m-%d')
        self.clear_event_logs(list_event_code, event_date, self.user_id)

        times = 20
        total_earn_points = 0
        for i in range(1, times + 1):
            time.sleep(5)
            event_date = self.points_common.get_curdate()
            default_browser = self.points_common.get_random_element_in_list((0, 1))
            self.vid = self.points_common.get_random_element_in_list((vid_1, vid_2))
            self.points_common.insert_into_event_logs(self.user_id, self.vid, event_code=event_code, event_type="daily", event_date=event_date, default_browser=default_browser, status="new")
            if i <= int(max_event_per_day):
                total_earn_points = total_earn_points + self.points_common.multiplication((earn_points, default_browser + 1))
            LOGGER.info("max_event_per_day  : " + str(max_event_per_day))
            LOGGER.info("times              : " + str(i))
            LOGGER.info("default_browser    : " + str(default_browser))
            LOGGER.info("total_earn_points  : " + str(total_earn_points))
        self.wait_point_services()

        redis = self.points_redis.redis_get(event_key)
        LOGGER.info("event_code           : " + event_code)
        LOGGER.info("max_event_per_day    : " + max_event_per_day)
        LOGGER.info("earn_points          : " + str(earn_points))
        self.assert_equal(redis["count"], min((times, int(max_event_per_day))), "Number of count")
        self.assert_equal(redis["earnPoint"], total_earn_points, "Number of earnPoint")
        assert self.result == True

    # Assert value
    def assert_equal(self, value_1, value_2, message_fail):
        if (value_1 != value_2):
            LOGGER.info("ERROR: " + message_fail + ": " + str(value_1) + " != " + str(value_2))
            self.result = False
        else:
            LOGGER.info("ERROR: " + message_fail + ": " + str(value_1) + " == " + str(value_2))

    # Wait for job execute
    def wait_point_services(self):
        LOGGER.info("Start Waiting 60s for Points Service")
        time.sleep(60)
        LOGGER.info("Stop Waiting 60s for Points Service")

    def clear_event_logs(self, list_event_code, event_date, user_id):
        for event_code in list_event_code:
            event_key = "EVENT_" + event_code + "_" + self.user_id + "_" + self.points_common.convert_date(event_date, '%Y-%m-%d')
            self.points_redis.redis_del(event_key)
        self.points_db.delete_point_db(f'Delete FROM points.event_logs where user_id = "{self.user_id}";')

