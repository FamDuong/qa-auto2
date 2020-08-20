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
