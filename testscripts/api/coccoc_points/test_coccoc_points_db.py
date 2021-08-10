import time
import random
# from api.coccoc_lucky.coccoc_lucky_api import LuckyAPI;
from testscripts.api.coccoc_points.common import CocCocPointsCommon;
from databases.sql.coccoc_point_db import CocCocPointsDB;

class TestCocCocPointDB:
    point_db = CocCocPointsDB()
    point_common = CocCocPointsCommon()


    # Insert user to user_plays table
    def test_insert_user_plays(self):
        time.sleep(4)
        # Get user id list
        user_id_list = self.point_db.get_list_point_db(f'SELECT user_id FROM coccoc_point.user_points where status = "active" order by create_time desc limit 30;')
        # Get prize id, prize type
        prizes = self.point_db.get_point_db(f'SELECT prize_id, prize_type FROM coccoc_point.prizes where status = "active";')
        prize_id_list = self.point_db.get_list_db(prizes, 0)
        prize_type_list = self.point_db.get_list_db(prizes, 1)

        # Others fixed information
        status = "new"
        notes = "import automatically"
        ip = self.point_common.get_ip()
        user_agents = "Chrome"

        number_of_users = 200
        for i in range(number_of_users):
            # Set information
            prize_token = self.point_common.get_random_string(10)
            user_id = random.choice(user_id_list)
            # prize_id = random.choice(prize_id_list)
            prize_id = "17"
            prize_type = "voucher"
            # prize_type = self.points_common.get_reference_data_in_list(prize_id_list, prize_type_list, prize_id)
            # prize_type = prize_type[0]
            play_type = random.choice(["lucky", "redeem"])

            # print(prize_token)
            # print(user_id)
            # print(prize_id)
            # print(prize_type)
            # print(play_type)
            # print(notes)
            # print(ip)
            # print(user_agents)
            users = self.point_db.update_point_db(f'insert into coccoc_point.user_plays values("{prize_token}", "{user_id}", NOW(), NOW(), '
                                              f'"{prize_id}", "{prize_type}", NULL, "new", "{play_type}", "{notes}", "{ip}", "{user_agents}", NOW(), NOW());')

    # Insert into event_logs
    def test_insert_event_logs(self):
        list_event = self.point_db.select_point_db(f'SELECT event_code, event_type FROM points.event_types;')
        list_event_codes = self.point_db.get_list_db(list_event, 0)
        list_event_types = self.point_db.get_list_db(list_event, 1)
        user_id = '46'
        vid = 'ury33SQ31bT6V1o6S31urrb1b6VGoQ9Gug9bWqb2.3w1Kz-LgS_YNogpdyOWW'
        status = 'new'
        default_browser_status = (0, 1)
        earn_points_max = 100
        event_date = self.point_common.get_curdate()

        for i in range(10):
            event_id = self.point_common.get_random_string(36)
            event_code = self.point_common.get_random_element_in_list(list_event_codes)
            event_type = self.point_common.get_reference_data(list_event_codes, list_event_types, event_code)
            earn_points = self.point_common.get_random_integer(earn_points_max)
            default_browser = self.point_common.get_random_element_in_list(default_browser_status)

            print("%s : %s : %s : %s : %s : %s : %s : %s" % (event_id, user_id, vid, event_code, event_type, status, default_browser, earn_points))
            users = self.point_db.update_point_db(f'insert into points.event_logs values("{event_id}", "{user_id}", "{vid}", "{event_code}", "{event_type}", "{event_date}", NOW(),  "{status}", '
                                                  f'"{default_browser}", "{earn_points}", NOW(), NOW(), "");')



