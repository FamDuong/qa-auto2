import time
import random
from api.coccoc_lucky.coccoc_lucky_api import LuckyAPI;
from databases.sql.coccoc_lucky_db import LuckyDB
from testscripts.api.coccoc_lucky.common import LuckyCommon;

from config.environment import COCCOC_LUCKY_API_GET_RESULT

class TestLuckyApi:
    lucky_api = LuckyAPI()
    lucky_db = LuckyDB()
    common = LuckyCommon()
    csrf_token = 'l10pWXISNukIVezTiMRI6LLhnkKYNKD9rr4RAugW'
    coccoc_lucky_session = 'eyJpdiI6IkZKelhlQjd1M1FHOVpScTVrWnhSQ0E9PSIsInZhbHVlIjoicTBDV0tITW00Zzg4enhIaXl0L3llR1pTVGhiWGlSejB4OGpDQXVyLy9nM2lsSHY3VlBFcXZnOHJRc2ZJRVNwOCIsIm1hYyI6ImVlMzBlMGZjZTkzZjNkNzI2Y2MyNjU4OGJjMjZlNWFjNWQwNWJlMWFhNmI0YzJiMGNjZThkYWVmM2I5Y2E4OTUifQ%3D%3D'
    user_id = '59'
    unlimited_prize_id = '11'

    def test_get_lucky_result(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_post_lucky_result(COCCOC_LUCKY_API_GET_RESULT, header)
        print(response['prize_name'])

    def test_get_lucky_result_multi_request_daily_round(self):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        turns = 600
        list_prizes = []
        for i in range(turns):
            response = self.lucky_api.request_post_lucky_result(COCCOC_LUCKY_API_GET_RESULT, header, time_interval = 0)
            prize_name = response['prize_name']
            list_prizes.append(prize_name)
            print(i, ": ", prize_name)
        print(list_prizes)

    # Cứ mỗi 500 người chơi sẽ random trao 1 giải limited - 1500 turns
    def test_get_lucky_result_multi_request_special_round(self, coccoc_lucky_db_interact):
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        # turns = 1500
        turns = 100
        number_turns = 30
        list_prizes = []
        for i in range(number_turns):
            for j in range(turns):
                response = self.lucky_api.request_post_lucky_result(COCCOC_LUCKY_API_GET_RESULT, header, time_interval = 0.5)
            total_prizes_db = self.lucky_db.get_lucky_db(coccoc_lucky_db_interact,
                                                      f'SELECT prize_id, count(prize_id) FROM coccoc_lucky.user_plays where play_date = curdate() and prize_id not in (SELECT prize_id from coccoc_lucky.prizes where day_limit != 0) order by prize_id;')
            total_prizes = self.lucky_db.get_list_db(total_prizes_db, 0)
            total_prizes = sum(total_prizes)

            total_turns_db = self.lucky_db.get_lucky_db(coccoc_lucky_db_interact,
                                                      f'select count(prize_token) from coccoc_lucky.user_plays where play_date = curdate();')
            total_turns = self.lucky_db.get_list_db(total_turns_db, 0)
            total_turns = sum(total_turns)

            ratio_1 = total_prizes / total_turns
            ratio_2 = total_turns / total_prizes
            print("total_prizes: %s" % total_prizes)
            print("total_turns : %s" % total_turns)
            print("total_prizes / total_turns : %s" % ratio_1)
            print("total_turns / total_prizes : %s" % ratio_2)
        print(list_prizes)

    # Vòng quay đặc biệt: - Cứ mỗi 500 người chơi sẽ random trao 1 giải limited  : 1500 turns
    def test_check_ratio_get_prizes(self, coccoc_lucky_db_interact):
        total_prizes_db = self.lucky_db.get_lucky_db(coccoc_lucky_db_interact,
                                                     f'SELECT prize_id, count(prize_id) FROM coccoc_lucky.user_plays where play_date = curdate() - interval 1 day and prize_id not in (SELECT prize_id from coccoc_lucky.prizes where day_limit != 0) order by prize_id;')
        total_prizes = self.lucky_db.get_list_db(total_prizes_db, 0)
        total_prizes = sum(total_prizes)

        total_turns_db = self.lucky_db.get_lucky_db(coccoc_lucky_db_interact,
                                                    f'select count(prize_token) from coccoc_lucky.user_plays where play_date = curdate() - interval 1 day;')
        total_turns = self.lucky_db.get_list_db(total_turns_db, 0)
        total_turns = sum(total_turns)

        ratio_1 = total_prizes / total_turns
        ratio_2 = total_turns / total_prizes
        print("total_prizes: %s" % total_prizes)
        print("total_turns : %s" % total_turns)
        print("total_prizes / total_turns : %s" % ratio_1)
        print("total_turns / total_prizes : %s" % ratio_2)