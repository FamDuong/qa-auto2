import os
import platform
import sys
import re
from selenium import webdriver as sele_webdriver
import pytz

from pytest_testrail.plugin import pytestrail
from utils_automation.const import Urls


class TestBrowser:

    @pytestrail.case('C36161')
    def test_current_time_now(self, request):
        print('Request node id is :', request.node.nodeid)

    def test_get_user_data_path(self):
        text = 'mp4/Standard/'

        m = re.search('\\d+p', text)
        if m:
            print(m.group())

    def test_get_current_dir(self):
        print(os.getcwd())
        print(sys.argv[0])
        before_split = os.getcwd()
        split_things = before_split.split('\\qa-auto\\')
        print(split_things)
