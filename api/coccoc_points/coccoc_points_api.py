import requests
import json
import uuid
import time
from bs4 import BeautifulSoup

from config.environment import COCCOC_ACCOUNTS_HOME_URL
from config.environment import COCCOC_ACCOUNTS_API_LOGIN
from config.environment import COCCOC_POINTS_SERVICE_LOGIN

import logging
LOGGER = logging.getLogger(__name__)

class CocCocPointsAPI:
    full_api_url = ""
    DEVSID = ""

    def get_api_url(self):
        return self.full_api_url

    def request_post_login(self, email, password):
        # Get token from CocCoc Accounts page
        html_content = requests.get(COCCOC_ACCOUNTS_HOME_URL).text
        soup = BeautifulSoup(html_content, 'html.parser')
        token = soup.input['value']

        # Login
        header = {'_token': token,
                  'email': email,
                  'password': password}
        with requests.Session() as session:
            response = session.post(COCCOC_ACCOUNTS_API_LOGIN, header)
            self.DEVSID = response.cookies["DEVSID"]
            print(response.cookies["DEVSID"])
            # Redirect to points
            response = session.get(COCCOC_POINTS_SERVICE_LOGIN)
            print(response.status_code)


    def set_header(self, access_token):
        # header = {'Authorization': access_token}
        header = {'Content-Type':'application/json',
                  'Authorization': 'Bearer {}'.format(access_token)}
        return header

    def set_cookies(self):
        header = {'cookie':'DEVSID=' + self.DEVSID + ";" + "SID=" + self.DEVSID }
        # header = {'cookie':'DEVSID=' + self.DEVSID}
        return header

    def request_get_coccoc_points(self, api_url, format='json', params=None, headers = {'Content-type': 'application/json'}, wait=3):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.get(api_url, params=params, headers=headers)
            if params != None:
                self.full_api_url = api_url + "?" + '&'.join(f'{k}={v}' for k, v in params.items())
                LOGGER.info(self.full_api_url)
        if format == "json":
            api_data = json.loads(response.content)
        elif format == "text":
            api_data = response.text
        time.sleep(wait)
        return api_data

    # Commond methods
    def request_post_coccoc_points(self, api_url, data = None, headers = {'Content-type': 'application/json'}, wait = 3):
        LOGGER.info(api_url)
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.post(api_url, headers=headers, data=data)
            time.sleep(wait)
            LOGGER.info("Resonse status : %s" % response.status_code)
        # assert response.status_code != 422
        return response


