import csv

import requests
from utils_automation.common import FilesHandle, get_from_csv

file_handle = FilesHandle()

def test_safe_search():
    newdata = []
    header = ['query', 'is_empty_due_to_safe']
    test_data = "../../../resources/test_data/safe_search_queries.csv"
    query = get_from_csv(test_data)
    for item in query:
        response = requests.get(
            "https://dev5.coccoc.com/composer?_=1625469249474&p=0&q="+item+"&reqid=cgYgveOl&&safe=1&apiV=1")
        response.raise_for_status()
        jsonResponse = response.json()
        new_row = [item, str(jsonResponse['search']['is_empty_due_to_safe'])]
        # print(new_row)
        newdata.append(new_row)
    with open(test_data, 'r+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(newdata)
        file.close()
