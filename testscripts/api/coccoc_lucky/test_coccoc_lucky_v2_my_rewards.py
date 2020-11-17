from api.coccoc_lucky.coccoc_lucky_api import LuckyAPI;
from api.coccoc_lucky.coccoc_lucky_redis import LuckyRedis;
from databases.sql.coccoc_lucky_db import LuckyDB
from testscripts.api.coccoc_lucky.common import LuckyCommon;

from config.environment import COCCOC_LUCKY_API_MY_REWARDS

import logging
LOGGER = logging.getLogger(__name__)

class TestLuckyApi:
    result = True
    lucky_api = LuckyAPI()
    lucky_db = LuckyDB()
    lucky_redis = LuckyRedis()
    common = LuckyCommon()

    csrf_token = None
    coccoc_lucky_session = None
    user_id = None
    key = None

    # BRBE-1047: [MKT Lucky 2] [API] Update Get lucky wheel result
    def test_get_lucky_result_format(self):
        self.set_variable()
        data = self.set_my_rewards_data()
        schema = {
            "type": "object",
            "properties": {
                "user_collections": {
                    tu
                },
                "user_prizes": {},
                "prize_name": {"type": "string"},
                "prize_image_url": {"type": "string"},
                "prize_type": {"type": "string",
                               "enum": ["good_luck", "reward"], },
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
        header = self.lucky_api.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.lucky_api.request_get_lucky(COCCOC_LUCKY_API_MY_REWARDS, headers=header, params=data)
        print(response)



    def set_variable(self):
        self.user_id = self.lucky_api.user_id
        self.coccoc_lucky_session = self.lucky_api.coccoc_lucky_session
        self.user_id = self.lucky_api.user_id

    # If vid is empty, set random vid
    def set_my_rewards_data(self):
        import json
        data = {'reward_type': 'all',
                'from_date': '2020-09-10',
                'to_date': '2020-09-10',
                'page': 1,
                'page_size': 20}
        # data = json.loads(data)
        return data