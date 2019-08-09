import os
import platform
import sys

from selenium import webdriver as sele_webdriver
import pytz

from pytest_testrail.plugin import pytestrail
from utils_automation.const import Urls


class TestBrowser:

    @pytestrail.case('C36161')
    def test_current_time_now(self, request):
        print('Request node id is :', request.node.nodeid)

    def get_user_data_path(self):
        from models.pageobject.version import VersionPageObject
        version_page_object = VersionPageObject()
        local_driver = sele_webdriver.Chrome()
        local_driver.maximize_window()
        local_driver.get(Urls.COCCOC_VERSION_URL)
        path_full = version_page_object.get_profile_path(local_driver)
        split_after = path_full.split('\\Local')
        return split_after[0]+u'\\Local\\CocCoc\\Browser\\User Data'

    def test_get_current_dir(self):
        print(os.getcwd())
        print(sys.argv[0])
        before_split = os.getcwd()
        split_things = before_split.split('\\qa-auto\\')
        print(split_things)
