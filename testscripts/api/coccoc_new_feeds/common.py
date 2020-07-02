import json
import random

class NewFeedCommon:
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

    # Convert all items in list to string
    def convert_byte_to_string(self, my_list):
        encoding = 'utf-8'
        convert_list = [i.decode(encoding) for i in my_list]
        return convert_list