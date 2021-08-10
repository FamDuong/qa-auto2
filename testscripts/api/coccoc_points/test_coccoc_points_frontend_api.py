import time
import random
import json
import logging
LOGGER = logging.getLogger(__name__)

from testscripts.api.coccoc_points.common import CocCocPointsCommon;
from databases.sql.coccoc_point_db import CocCocPointsDB;
from api.coccoc_points.coccoc_points_api import CocCocPointsAPI;

from config.environment import COCCOC_POINTS_API_LUCKY_PRIZES
from config.environment import COCCOC_POINTS_API_RECENT_WINNER
from config.environment import COCCOC_POINTS_API_LUCKY_RESULT

class TestCocCocPointFrontendAPI:
    points_db = CocCocPointsDB()
    points_api = CocCocPointsAPI()
    points_common = CocCocPointsCommon()
    result = True
    access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvZGV2LXBvaW50cy1mcm9udGVuZC1hcGkuY29jY29jLmNvbVwvYXBpXC92MVwvYXV0aFwvbG9naW4iLCJpYXQiOjE2MTU0NjAyNjgsImV4cCI6MTYxNTUwMzQ2OCwibmJmIjoxNjE1NDYwMjY4LCJqdGkiOiJTUEd5cGloM2tZYk14U1RMIiwic3ViIjo0NiwicHJ2IjoiM2Q4ZTkxM2FiZWM5M2JlMGQzYTA1NzQwZjQ2ZmM4Y2YyZWM4M2E0NCJ9.BpAKHB_p_icxaHRWNrdciVjoYixAGJmChu6gBIYyNDw'
    email = "coccocbrowser07@gmail.com"
    password = "@Pass01234567"

    # Get list prizes for Lucky wheel
    def test_get_lucky_prizes(self):
        header = self.points_api.set_header(self.access_token)
        response = self.points_api.request_get_coccoc_points(COCCOC_POINTS_API_LUCKY_PRIZES, headers=header)
        prizes = response['data']['prizes']
        print(prizes)

        list_prize_id_db = self.points_db.get_list_point_db(f'SELECT b.list_prize_id FROM points.prize_days a INNER JOIN points.prize_configs b ON b.prize_config = a.prize_config WHERE value_date = curdate();')
        # print(list_prize_id_db[0])

        sql_query = f'SELECT prize_id, name, image_url, prize_type, probability FROM points.prizes WHERE prize_id IN ("{list_prize_id_db[0]}")' \
                    f'ORDER BY FIELD(prize_id, "{list_prize_id_db[0]}");'
        sql_query = sql_query.replace('"', '')
        list_prizes = self.points_db.select_point_db(sql_query)
        # print(list_prizes[0])

        # Assert name / image_url / prize_type
        for i in range(len(list_prizes)):
            self.assert_equal(response['data']['prizes'][i]['name'], list_prizes[i][1], "Invalid name")
            self.assert_equal(response['data']['prizes'][i]['image_url'], list_prizes[i][2], "Invalid image_url")
            self.assert_equal(response['data']['prizes'][i]['prize_type'], list_prizes[i][3], "Invalid prize_type")
        assert self.result == True

    # Get recent winner
    # Note: Keep 2 first & 2 last characters, replace middle characters of email with *
    def test_get_recent_winner(self):
        header = self.points_api.set_header(self.access_token)
        response = self.points_api.request_get_coccoc_points(COCCOC_POINTS_API_RECENT_WINNER, headers=header)
        print(response)

        list_winner_db = self.points_db.select_point_db(f'SELECT b.user_avatar, b.email, c.name as prize_name, c.small_image_url as prize_image_url, c.prize_type '
                                                        f'FROM points.user_plays a INNER JOIN points.user_points b ON b.user_id = a.user_id INNER JOIN points.prizes c ON c.prize_id = a.prize_id '
                                                        f'WHERE a.prize_type <> "good_luck" AND a.play_type = "lucky" ORDER BY a.create_time DESC LIMIT 20;')
        for i in range(len(list_winner_db)):
            self.assert_equal(response['data'][i]['avatar_url'], list_winner_db[i][0], "Invalid avatar_url")
            self.assert_equal(response['data'][i]['email'], list_winner_db[i][1], "Invalid email")
            self.assert_equal(response['data'][i]['prize_name'], list_winner_db[i][2], "Invalid prize_name")
            self.assert_equal(response['data'][i]['prize_image_url'], list_winner_db[i][3], "Invalid prize_image_url")
            self.assert_equal(response['data'][i]['prize_type'], list_winner_db[i][4], "Invalid prize_type")
        assert self.result == True

    # Get lucky wheel result
    def test_post_lucky_wheel_result(self):
        header = self.points_api.set_header(self.access_token)
        for i in range(200):
            response = self.points_api.request_post_coccoc_points(COCCOC_POINTS_API_LUCKY_RESULT, headers=header)
            response_data = json.loads(response.content)
            LOGGER.info(response_data)

    # Assert value
    def assert_equal(self, value_1, value_2, message_fail):
        if (value_1 != value_2):
            print("ERROR: ", message_fail, ": ", value_1, " != ", value_2)
            self.result = False

    # Try to get DEVID
    def test_get_lucky_prizes(self):
        response = self.points_api.request_post_login(self.email, self.password)
        header = self.points_api.set_cookies()
        for i in range(5):
            # response = self.points_api.request_get_coccoc_points(COCCOC_POINTS_API_LUCKY_RESULT, headers=header)
            response = self.points_api.request_post_coccoc_points(COCCOC_POINTS_API_LUCKY_RESULT)
            LOGGER.info(response)