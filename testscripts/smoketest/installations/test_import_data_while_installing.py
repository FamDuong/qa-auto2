import platform

import pytest
from pytest_testrail.plugin import pytestrail


class TestImportDataWhileInstalling:
    """
    browser_name = 'chrome', 'firefox', 'microsoft-edge:', 'iexplore'
    """

    @pytestrail.case('C44825')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7", "10"], reason=
    "Takes time set default browser so later and cannot detect windows from pywinauto when open monitor")
    def test_import_data_from_chrome(self):
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Google Chrome')
        from testscripts.smoketest.installations.common import open_browser_from_command
        open_browser_from_command(browser_name='chrome')
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Google Chrome Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Continue')
        from testscripts.smoketest.common import is_popup_import_browser_settings_displayed
        try:
            assert is_popup_import_browser_settings_displayed() is True
            from testscripts.smoketest.common import kill_browser_process
            kill_browser_process(browser_name='chrome.exe')
            assert is_popup_import_browser_settings_displayed() is False
            from testscripts.smoketest.common import get_list_files_dirs_in_a_folder
            import time
            time.sleep(5)
            assert 'Bookmarks' in get_list_files_dirs_in_a_folder(
                application_path="\"AppData/Local/CocCoc/Browser/User Data/Default\"")
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(coccoc_update=False, firefox=False)

    @pytestrail.case('C44826')
    @pytest.mark.skip(reason='Bug BR-947')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7", "10"], reason=
    "Takes time set default browser so later and cannot detect windows from pywinauto when open monitor")
    def test_import_data_from_firefox(self):
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Firefox')
        from testscripts.smoketest.installations.common import open_browser_from_command
        open_browser_from_command(browser_name='firefox')
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Mozilla Firefox Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Continue', browser_name='Firefox')
        from testscripts.smoketest.common import is_popup_import_browser_settings_displayed
        try:
            assert is_popup_import_browser_settings_displayed(
                browser_import_name='Import Mozilla Firefox Settings') is True
            from testscripts.smoketest.common import kill_browser_process
            kill_browser_process(browser_name='firefox.exe')
            assert is_popup_import_browser_settings_displayed(
                browser_import_name='Import Mozilla Firefox Settings') is False
            from testscripts.smoketest.common import get_list_files_dirs_in_a_folder
            import time
            time.sleep(5)
            assert 'Bookmarks' in get_list_files_dirs_in_a_folder(
                application_path="\"AppData/Local/CocCoc/Browser/User Data/Default\"")
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(coccoc_update=False)

    @pytestrail.case('C44827')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7", "10"], reason=
    "Takes time set default browser so later and cannot detect windows from pywinauto when open monitor")
    def test_import_data_from_internet_explorer(self):
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Internet Explorer')
        from testscripts.smoketest.installations.common import open_browser_from_command
        open_browser_from_command(browser_name='iexplore')
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Microsoft Internet Explorer Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Continue', browser_name='Internet Explorer')
        try:
            from testscripts.smoketest.common import get_list_files_dirs_in_a_folder
            import time
            time.sleep(5)
            assert 'Bookmarks' in get_list_files_dirs_in_a_folder(
                application_path="\"AppData/Local/CocCoc/Browser/User Data/Default\"")
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(coccoc_update=False, firefox=False)

    @pytestrail.case('C44828')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7", "10"], reason=
    "Takes time set default browser so later and cannot detect windows from pywinauto when open monitor and Bug BR-930")
    def test_import_data_from_microsoft_edge(self):
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Microsoft Edge')
        from testscripts.smoketest.installations.common import open_browser_from_command
        open_browser_from_command(browser_name='microsoft-edge:')
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Microsoft Edge Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Continue', browser_name='Microsoft Edge')
        try:
            from testscripts.smoketest.common import get_list_files_dirs_in_a_folder
            import time
            time.sleep(5)
            assert 'Bookmarks' in get_list_files_dirs_in_a_folder(
                application_path="\"AppData/Local/CocCoc/Browser/User Data/Default\"")
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(coccoc_update=False, firefox=False)
