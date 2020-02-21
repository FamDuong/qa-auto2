

class TestFirstTimeRun:

    def test_check_first_time_run(self):
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Google Chrome')
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Google Chrome Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Cancel')





