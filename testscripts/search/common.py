import json
import pygsheets

from utils_automation.common import FilesHandle
from google.oauth2 import service_account

file_handle = FilesHandle()


def google_authorize():
    credentials_path_file = file_handle.get_absolute_filename("\\qa-auto_service_credentials.json")
    credentials_path_file = credentials_path_file.replace('\\utils_automation', '\\resources')
    SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file')
    with open(credentials_path_file, 'r') as j:
        service_account_info = json.loads(j.read())
    my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    authorize = pygsheets.authorize(custom_credentials=my_credentials)
    return authorize


def get_worksheet(spreed_sheet_id, sheet_name):
    sheet = google_authorize().open_by_key(spreed_sheet_id)
    worksheet = sheet.worksheet('title', sheet_name)
    return worksheet


def get_keyword_without_bracket(keyword):
    start = keyword.find("['") + len("['")
    end = keyword.find("']")
    keyword_without_bracket = keyword[start:end]
    return keyword_without_bracket


def split_index_from_sheet_range(sheet_range):
    index_list = sheet_range.split(":")
    if index_list is None:
        raise Exception
    index_list_int = []
    for index in index_list:
        index_list_int.append(int(index[1:5]))
        index_list_int_without_duplicate = list(dict.fromkeys(index_list_int))
    return index_list_int_without_duplicate


def split_col_from_sheet_range(sheet_range):
    col_list = sheet_range.split(":")
    if col_list is None:
        raise Exception
    for col in col_list:
        col_without_duplicate = list(dict.fromkeys(col[0:1]))
    return col_without_duplicate


def get_diff_worlds(string1, string2):
    import difflib
    # initiate the Differ object
    dif_lib = difflib.Differ()
    # calculate the difference between the two texts
    diff_words = list(dif_lib.compare(string1.split(), string2.split()))
    diff_words_string1 = []
    diff_words_string2 = []
    for world in diff_words:
        if world.startswith('- '):
            world = world.replace('- ', '')
            diff_words_string1.append(world)
        elif world.startswith('+ '):
            world = world.replace('+ ', '')
            diff_words_string2.append(world)
    return diff_words_string1, diff_words_string2
