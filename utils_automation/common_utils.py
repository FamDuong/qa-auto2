class CommonUtils:
    # Remove invalid links
    def remove_duplicate_elements_in_lists(self, list_1, list_2):
        list = [i for i in list_1 if i not in list_2]
        return list