import requests
import json
import uuid
import time
import random

from config.environment import COCCOC_NEW_FEED_DATA_URL
from config.environment import COCCOC_NEW_FEED_API_CMS_RULE
from config.environment import COCCOC_NEW_FEED_API_CMS_INIT_USER
from config.environment import COCCOC_NEW_FEED_API_CMS_USER_ACTION

class DatafeedAPI:
    def request_get_new_feeds(self, api_url, format='json'):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.get(api_url)
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
    def request_post_new_feeds(self, api_url, data, headers = {'Content-type': 'application/json'}):
        with requests.Session() as session:
            initial_response = session.get(api_url)
            response = session.post(api_url, headers=headers, data=data)
            time.sleep(3)
            print("Resonse status : ", response.status_code)
        assert response.status_code != 422
        return response.status_code

    def save_user_actions(self, vid="b717eaa88154e62be2fe4288626b41d6", action_type="block_article", article_id="1", complaint_type="wrong_info", categories="11000", domain="dantri.com.vn"):
        data = {'vid': vid, 'action_type': action_type, 'article_id': article_id, 'complaint_type': complaint_type, 'categories': categories, 'domain': domain}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(COCCOC_NEW_FEED_API_CMS_INIT_USER, data=json.dumps(data),
                                 headers=headers)
        return response.status_code

    def set_vid_data(self):
        vid = uuid.uuid4().hex.upper()[0:20]
        # print("\n vid: ", vid)
        data = {'vid': vid}
        data = json.dumps(data)
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

    def get_data(self, data, key):
        data = json.loads(data)
        return data[key]

    def get_list_json_level_1(self, data, key):
        list_groups = []
        for i in range(len(data)):
            group = data[i][key]
            list_groups.append(group)
        return list_groups

    def get_list_json_level_2(self, data, key_1, value_1, key_2):
        list_groups = []
        for i in range(len(data)):
            value = data[i][key_1]
            if value == value_1:
                for j in range(len(data[i][key_2])):
                    value_2 = data[i][key_2][j]
                    list_groups.append(value_2)
                    # print(value_2)
        return list_groups


    # Check if element in a list
    def check_if_element_in_list(self, my_list, element):
        result = True
        my_list = set(my_list)
        if element not in my_list:
            result = False
        return result

    # Return true if there are duplicated items
    def check_if_element_duplicated(self, list):
        ''' Check if given list contains any duplicates '''
        result = True
        list_lower = set()
        for element in list:
            element_lower = element.lower()
            if element_lower in list_lower:
                print("    ", element)
                print("    ", element_lower)
                result = False
            else:
                list_lower.add(element_lower)
        return result


    # Return different elements between lists
    def check_if_element_different_in_lists(self, list_1, list_2):
        result = True
        temp = [item for item in list_1 if item not in list_2]
        if len(temp) != 0:
            print("    Different elements: ", temp)
            result = False
        return result

    # Check if all items contains string
    def check_if_elements_in_lists_contains_string(self, list, str):
        result = True
        temp = [item for item in list if str not in item]
        if len(temp) != 0:
            print("    Elements not contains string: ", temp)
            result = False
        return result

    # Remove duplicated items in list
    def remove_duplicated_items(self, my_list):
        return list(dict.fromkeys(my_list))

    # Check if list contains sublist
    def check_is_sublist(self, list_1, sub_list):
        ls1 = [element for element in list_1 if element in sub_list]
        ls2 = [element for element in sub_list if element in list_1]
        return self.check_if_element_different_in_lists(ls1, ls2)

    # Get random value in list
    def get_random_element(self, list):
        return random.choice(list)

    # Check if no common elements in two lists
    def check_if_lists_are_different(self, list_1, list_2):
        result = True
        common = list(set(list_1).intersection(list_2))
        if len(common) != 0:
            print(common)
            result = False
        return result

    # Check if two unordered lists are equasl
    def check_if_unordered_lists_are_equal(self, list_1, list_2):
        return set(list_1) == set(list_2)

    # Print list line by line
    def print_list(self, list):
        print(*list, sep='\n')

    # Get Kafka message
    def get_kafka_message(self, action_type, vid, vid_data):
        if action_type == 'subscribe_category':
            message = '{"message_type":"sub_categories","message":{"vid":"%s","sub_categories":%s}}' % (vid, vid_data)
        elif action_type in ['block_source', 'cancel_block_source']:
            message = '{"message_type":"block_source","message":{"vid":"%s","block_sources":%s}}' % (vid, vid_data)
        else:
            message = '{"message_type":"%s","message":{"vid":"%s","article_id":%s}}' % (action_type, vid, vid_data)
        return message