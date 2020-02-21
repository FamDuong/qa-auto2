from pytest_testrail.plugin import pytestrail


class TestFirstTimeRun:

    def verify_new_tab_coccoc_exist(self):
        from pywinauto import Desktop
        coccoc_instance = Desktop(backend='uia').Welcome_to_Cốc_Cốc_Cốc_CốcPane
        # existFlag = coccoc_instance.window(title="New Tab - Cốc Cốc").is_visible()
        coccoc_instance.New_Tab.click_input()
        all_windows = Desktop(backend='uia').windows()
        # print(all_windows)
        assert 'New Tab - Cốc Cốc' in str(all_windows)

    @pytestrail.case('C44829')
    @pytestrail.defect('BR-1398')
    def test_check_first_time_run(self):
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Google Chrome')
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Google Chrome Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Cancel')
        try:
            self.verify_new_tab_coccoc_exist()
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(firefox=False)





