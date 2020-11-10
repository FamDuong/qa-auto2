import requests
import json
import uuid
import time

import logging
LOGGER = logging.getLogger(__name__)

from config.environment import COCCOC_LUCKY_API_GET_RESULT
from config.environment import COCCOC_LUCKY_API_RECENT_WINNERS

class LuckyAPI:
    csrf_token = '67Aw3x8nWqYbtI6W5vHI1kYD0Usi7uVNtWct0iwY'
    coccoc_lucky_session = 'eyJpdiI6IkN3T2E4SDVIblJ2ZzBYREY2RDAwZGc9PSIsInZhbHVlIjoiY1ZUbEtwNVNBSjcxak9xZ1lPeXE0VjdJYitiY2xIUUlSbmZVUmg3Q1RiMmI2YW53cHUvdWR3OXBkSkpMQTdiQk02V3ZxYzlVMFcwYUozYnVtNEV1QkZUdVZkczIrYWYvbkpTRFZac2hwNnBZSU9VbjQvVGI4eFNPMHU4bk5FTDYiLCJtYWMiOiI4OGE3MWZjNzg0MmFhZmU4NTI2OGVlZmM3MTFmMWJhN2ZmNjEyNTgxMmQwZGYxMDExYWZiYjM4NzhjM2U5ZWJiIn0%3D'
    user_id = '389'

    def set_user_info(self, csrf_token, cookie_session, user_agent_type="Desktop"):
        user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/87.0.148 Chrome/81.0.4044.148 Safari/537.36'
        user_agent_mobile = 'Mozilla/5.0 (Linux; Android 10; RMX1801) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/87.0.195 Mobile Chrome/81.0.4044.195 Mobile Safari/537.36'
        if user_agent_type == "Desktop":
            user_agent = user_agent_desktop
        elif user_agent_type == "Mobile":
            user_agent = user_agent_mobile
        session = 'coccoc_lucky_session=' + cookie_session
        data = {'X-CSRF-TOKEN': csrf_token,
                'Cookie': session,
                'User-Agent': user_agent,
                'X-Requested-With': 'XMLHttpRequest'}

        #data = json.dumps(data)
        # print(data)
        return data

    def request_get_lucky(self, api_url, headers=None, params=None, format='json'):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.get(api_url, headers=headers, params=None)
            # print(response.status_code)
        if format == "json":
            api_data = json.loads(response.content)
        elif format == "text":
            api_data = response.text
        else:
            api_data = response
        print(api_data)
        return api_data

    # Commond methods
    def request_post_lucky(self, api_url, headers, time_interval = 1):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.post(api_url, headers=headers)
            time.sleep(time_interval)
            LOGGER.info("Resonse status  : %s" % response.status_code)
        return json.loads(response.content)


    # Get result
    def request_post_lucky_result(self, header=None, time_interval=0):
        if header == None:
            header = self.set_user_info(self.csrf_token, self.coccoc_lucky_session)
        response = self.request_post_lucky(COCCOC_LUCKY_API_GET_RESULT, headers=header, time_interval=time_interval)
        LOGGER.info(response)
        return response


    # Get recent winner
    def request_get_recent_winner(self):
        header = {'X-Requested-With': 'XMLHttpRequest'}
        response = self.request_get_lucky(COCCOC_LUCKY_API_RECENT_WINNERS, headers=header)
        LOGGER.info(response)
        return response