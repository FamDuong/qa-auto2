import requests
import json
import uuid
import time
import random
import base64
import os

from config.environment import COCCOC_NEW_FEED_DATA_URL
from config.environment import COCCOC_NEW_FEED_API_CMS_RULE
from config.environment import COCCOC_NEW_FEED_API_CMS_INIT_USER
from config.environment import COCCOC_NEW_FEED_API_CMS_USER_ACTION

class NewsFeedAPI:
    def request_get_new_feeds(self, api_url, format='json', params=None, headers = {'Content-type': 'application/json'}):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            # response = session.get(api_url)
            response = session.get(api_url, params=params, headers=headers)
            # print(response.status_code)
        if format == "json":
            api_data = json.loads(response.content)
        elif format == "text":
            api_data = response.text
        return api_data

    def get_data_crawler(self):
         response_api_get_data = requests.get(COCCOC_NEW_FEED_DATA_URL)
         return json.loads(response_api_get_data.content)

    def get_rules_crawler(self):
        response_api_get_data = requests.get(COCCOC_NEW_FEED_API_CMS_RULE)
        return json.loads(response_api_get_data.content)

    def init_user_settings(self, data):
        self.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_INIT_USER, data)


    # Commond methods
    def request_post_new_feeds(self, api_url, data = None, headers = {'Content-type': 'application/json'}):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.post(api_url, headers=headers, data=data)
            time.sleep(3)
            print("Resonse status : ", response.status_code)
        # assert response.status_code != 422
        return response.status_code

    def save_user_actions(self, vid="b717eaa88154e62be2fe4288626b41d6", action_type="block_article", article_id="1", complaint_type="wrong_info", categories="11000", domain="dantri.com.vn"):
        data = {'vid': vid, 'action_type': action_type, 'article_id': article_id, 'complaint_type': complaint_type, 'categories': categories, 'domain': domain}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(COCCOC_NEW_FEED_API_CMS_INIT_USER, data=json.dumps(data),
                                 headers=headers)
        return response.status_code

    # If vid is empty, set random vid
    def set_vid_data(self, vid = None, format = "json"):
        if vid is None:
            vid = uuid.uuid4().hex.upper()[0:20]
        # print("\n vid: ", vid)
        data = {'vid': vid}
        if format == "json":
            data = json.dumps(data)
        # data = json.loads(data)
        return data

    # If sid is empty, set random vid
    def set_user_feed_data(self, vid, sid = None, page = 1, size = 39, format = "json"):
        if sid is None:
            sid = base64.b64encode(os.urandom(16))
        data = {'vid': vid,
                'sid': sid,
                'page': page,
                'size': size}
        # if format == "json":
        #    data = json.dumps(data)
        # data = json.loads(data)
        return data

    def set_user_actions_data(self, action_type, article_id = None, complaint_type = None, categories = None, domain = None):
        list_actions_normal = ['like_article', 'cancel_like_article', 'block_article', 'cancel_block_article']
        list_actions_source = ['block_source', 'cancel_block_source']

        if action_type in list_actions_normal:
            data = {'action_type': action_type,
                    'article_id': article_id}
        elif action_type == 'complaint_article':
            data = {'action_type': action_type,
                    'article_id': article_id,
                    'complaint_type': complaint_type}
        elif action_type == 'subscribe_category':
            data = {'action_type': action_type,
                    'categories': categories}
        elif action_type in list_actions_source:
            data = {'action_type': action_type,
                    'domain': domain}
        else:
            data = {'action_type': action_type,
                'article_id': article_id,
                'complaint_type': complaint_type,
                'categories': categories,
                'domain': domain}
        data = json.dumps(data)
        print(data)
        return data

    # Set data for publish article
    def set_publish_article_data(self, list):
        # Convert int to string
        list = [str(i) for i in list]
        data = {'list_article_id': list}
        data = json.dumps(data)
        return data
