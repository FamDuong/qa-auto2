import os
import sys

import pytz
from pytest_testrail.plugin import pytestrail


class TestBrowser:

    @pytestrail.case('C36161')
    def test_current_time_now(self):
        assert 0 == 1, 'abc'

    def test_timezone(self):
        print(pytz.all_timezones)

    def test_get_current_dir(self):
        print(os.getcwd())
        print(sys.argv[0])
        before_split = os.getcwd()
        split_things = before_split.split('\\qa-auto\\')
        print(split_things)
