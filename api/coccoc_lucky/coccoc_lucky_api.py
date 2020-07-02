import requests
import json
import uuid
import time

from config.environment import COCCOC_LUCKY_API_GET_RESULT

class LuckyAPI:

    def set_user_info(self, csrf_token, cookie_session):
        session = 'coccoc_lucky_session=' + cookie_session
        data = {'X-CSRF-TOKEN': csrf_token,
                'Cookie': session}
        #data = json.dumps(data)
        print(data)
        return data

    def request_get_lucky(self, api_url, format='json'):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.get(api_url)
            # print(response.status_code)
        if format == "json":
            api_data = json.loads(response.content)
        elif format == "text":
            api_data = response.text
        return api_data

    # Commond methods
    def request_post_lucky_result(self, api_url, headers, time_interval = 1):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.post(api_url, headers=headers)
            time.sleep(time_interval)
            print("Resonse status  : ", response.status_code)
        return json.loads(response.content)

