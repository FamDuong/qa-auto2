import logging
LOGGER = logging.getLogger(__name__)

class CommonUtils:
    # Remove invalid links
    def remove_duplicate_elements_in_lists(self, list_1, list_2):
        list = [i for i in list_1 if i not in list_2]
        return list

    # Print element in list
    def print_list(message, list, number = None):
        if number == None:
            number = len(list)
        for i in range(number):
            LOGGER.info("%s. %s: %s" % (i, message, list[i]))

    # Get data with reference index is
    def get_reference_data_in_list(self, list_1, list_2, reference):
        list_data = []
        temp = set(list_1)
        index = [i for i, val in enumerate(list_1) if (val in temp and val == reference)]
        for i in index:
            list_data.append(list_2[i])
        return list_data