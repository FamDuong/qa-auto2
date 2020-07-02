import json
import random

class LuckyCommon:
    def get_count_number_each_elements_in_list(self, list):
        return None

    # Print list line by line
    def print_list(self, list):
        print(*list, sep='\n')

    def get_total_user_prizes(self, my_list):
        total = 0
        for i in range(my_list):
            total = total + my_list[i][1]
        return total

    def get_ratio_get_prize(self, number_turns, number_prize):
        ratio = number_prize / number_turns
        return ratio