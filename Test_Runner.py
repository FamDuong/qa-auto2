

class TestBrowser:

    def test_debug(self):
        from testscripts.smoketest.common import get_list_start_up_apps
        list_apps = get_list_start_up_apps()
        assert "CocCocUpdate" in list_apps











