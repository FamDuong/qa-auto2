
import pytz
from pytest_testrail.plugin import pytestrail


class TestBrowser:

    @pytestrail.case('C36161')
    def test_current_time_now(self):
        assert 0 == 1, 'abc'

    def test_timezone(self):
        print(pytz.all_timezones)
