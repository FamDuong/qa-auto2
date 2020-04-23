import platform

import pytest
from pytest_testrail.plugin import pytestrail
import testscripts.smoketest.common as common


class TestFirstTimeRun:

    def  verify_new_tab_coccoc_exist(self):
        from pywinauto import Desktop
        coccoc_instance = Desktop(backend='uia').Welcome_to_Cốc_Cốc_Cốc_Cốc
        common.wait_for_panel_is_exist(coccoc_instance)
        welcome_coccoc_tab = coccoc_instance.child_window(title='Welcome to Cốc Cốc', control_type=50019)
        new_tab = coccoc_instance.child_window(title_re='New Tab', control_type=50019)
        common.wait_for_panel_is_exist(welcome_coccoc_tab)
        common.wait_for_panel_is_exist(new_tab)
        assert welcome_coccoc_tab.exists() is True
        assert new_tab.exists() is True

    def pre_condition_before_run_first_time(self):
        from utils_automation.common import WindowsHandler
        windows_handler = WindowsHandler()
        windows_handler.delete_coccoc_firewall_rules()
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=True, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import chrome_options_preset
        from selenium import webdriver
        driver = webdriver.Chrome(options=chrome_options_preset())
        import time
        time.sleep(4)
        driver.quit()

    def verify_open_browser_for_the_first_time(self, coccoc_is_default):
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        common.uninstall_then_install_coccoc_with_default(coccoc_is_default, is_needed_clean_up=False,
                                                          is_needed_clear_user_data=True)
        browser_name = common.get_browser_name()
        common.choose_import_browser_settings('Continue', browser_name)
        try:
            self.verify_new_tab_coccoc_exist()
        finally:
            cleanup(firefox=False)

    @pytestrail.case('C44829')
    def test_check_first_time_run(self):
        self.verify_open_browser_for_the_first_time(coccoc_is_default='yes')
        # In win 8, 8.1 not show checkbox "Make Cốc Cốc your default browser"
        if platform.release() not in ["8", "8.1"]:
            self.verify_open_browser_for_the_first_time(coccoc_is_default='no')

    @pytestrail.case('C44830')
    @pytestrail.defect('BR-1415', 'BR-1205')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7", "10"], reason=
    "Takes time set default browser so later and cannot detect windows from pywinauto when open monitor")
    def test_if_widevine_flash_plugin_exist_by_default_right_after_installing_browser(self):
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Google Chrome')
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Google Chrome Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Continue')
        from selenium import webdriver
        from testscripts.smoketest.common import chrome_options_preset
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        driver = webdriver.Chrome(options=chrome_options_preset())
        from models.pageobject.settings import SettingsComponentsPageObject
        settings_component_page_object = SettingsComponentsPageObject()
        try:
            from utils_automation.const import Urls
            driver.maximize_window()
            driver.get(Urls.COCCOC_COMPONENTS)
            settings_component_page_object.click_on_each_check_for_update_button(driver)
            settings_component_page_object.verify_all_components_version_is_updated(driver)
        finally:
            driver.quit()
            cleanup(firefox=False)

    @pytestrail.case('C44831')
    def test_check_task_manager_start_browser(self):
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default()
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        from testscripts.smoketest.installations.common import open_browser_from_command
        try:
            open_browser_from_command(browser_name='browser')
            from testscripts.smoketest.common import get_application_process
            import time
            time.sleep(8)
            assert 'browser' in get_application_process(application_name='browser')
            assert 'CocCocCrash' in get_application_process(application_name='CocCocCrashHandler')
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(firefox=False)

    @pytestrail.case('C44832')
    @pytest.mark.skipif(platform.release() in ["8", "8.1", "7", "10"], reason=
    "Takes time set default browser so later and issue detect windows when not open monitor")
    def test_check_extensions_version_after_installation(self):
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Google Chrome')
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        from testscripts.smoketest.common import wait_for_window_appear
        wait_for_window_appear(window_name='Import Google Chrome Settings')
        from testscripts.smoketest.common import choose_import_browser_settings
        choose_import_browser_settings(action='Continue')
        import time
        time.sleep(5)
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        # Enable coccoc mojichat by opening browser with --enable-features=CocCocMojichat
        from testscripts.smoketest.installations.common import open_browser_from_command
        open_browser_from_command(browser_name='browser --enable-features=CocCocMojichat')
        time.sleep(5)
        cleanup(firefox=False)
        from selenium import webdriver
        from testscripts.smoketest.common import chrome_options_preset
        driver = webdriver.Chrome(options=chrome_options_preset())
        from models.pageobject.settings import SettingsPageObject
        from utils_automation.const import Urls
        driver.get(Urls.COCCOC_EXTENSIONS)
        settings_page_object = SettingsPageObject()
        settings_page_object.enable_extension_toggle_dev_mode(driver)
        assert len(settings_page_object.find_all_extensions(driver)) == 4
        list_extensions_id = settings_page_object.get_all_extensions_id(driver)
        from models.pageobject.extensions import ExtensionsPageObject
        extension_page_object = ExtensionsPageObject()
        for each_extension_id in list_extensions_id:
            extension_page_object.click_extension_detail_button(driver, '#' + each_extension_id)
            time.sleep(1)
            assert extension_page_object.get_attribute_toggle_button_in_detail_extension(driver,
                                                                                         'aria-pressed') == 'true'
            driver.get(Urls.COCCOC_EXTENSIONS)

    @pytestrail.case('C44833')
    def test_folders_after_the_installation(self):
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        self.pre_condition_before_run_first_time()
        from utils_automation.common import FilesHandle
        file = FilesHandle()
        from testscripts.smoketest.common import get_coccoc_version_folder_name
        coccoc_version = get_coccoc_version_folder_name()
        assert file.is_file_exist_in_folder('uid', file.appdata) is True
        assert file.is_file_exist_in_folder('hid3', file.appdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser', file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'CrashReports', file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Update', file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser\Application', file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser\User Data', file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser\Application' + '\\' + coccoc_version,
                                                 file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser\Application\Dictionaries',
                                                 file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser\Application\SetupMetrics',
                                                 file.localappdata) is True
        assert file.is_file_exist_in_folder(r'Browser\Application\browser.exe', file.localappdata) is True
        assert file.is_file_exist_in_folder(r'Browser\Application\browser_proxy.exe',
                                            file.localappdata) is True
        assert file.is_file_exist_in_folder(r'Browser\Application\VisualElementsManifest.xml',
                                            file.localappdata) is True

    @pytestrail.case('C44838')
    def test_the_company_signature_in_file_exe_and_dll(self):
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        self.pre_condition_before_run_first_time()
        from utils_automation.common import FilesHandle
        file = FilesHandle()
        signatures = file.get_signature_of_files_in_folder('.exe', file.localappdata)
        for signature in signatures:
            assert "COC COC COMPANY LIMITED" in signature
        signatures = file.get_signature_of_files_in_folder('.dll', file.localappdata)
        index = 0
        for signature in signatures:
            index += 1
            print(f" {index} Signature is : {signature} \n")
            assert "COC COC COMPANY LIMITED" in signature

    @pytestrail.case('C44839')
    def test_check_task_scheduler_after_installation(self):
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        self.pre_condition_before_run_first_time()
        from testscripts.smoketest.installations.common import check_task_scheduler
        coccoc_update_tasks = check_task_scheduler(task_name="CocCoc")
        import re
        assert len(re.findall('CocCocUpdateTaskUser.*Core.*Ready', coccoc_update_tasks)) == 1
        assert len(re.findall('CocCocUpdateTaskUser.*UA.*Ready', coccoc_update_tasks)) == 1

    @pytestrail.case('C44840')
    @pytest.mark.skip(reason="Take times to handle with User Account Control is Always notify")
    def test__rule_in_firewall_of_windows_if_user_selects_allow_access_btn(self):
        # Note: Default when setting, user always select "Allow access" button
        # Inbound
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        self.pre_condition_before_run_first_time()
        import time
        time.sleep(100)
        from utils_automation.common import WindowsHandler
        windows = WindowsHandler()
        windows.verify_netfirewall_rule('Cốc Cốc (mDNS-In)', 'In', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc (TCP-In)', 'In', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc (UDP-In)', 'In', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (TCP-In)', 'In', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (UDP-In)', 'In', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc (TCP-Out)', 'Out', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc (UDP-Out)', 'Out', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (TCP-Out)', 'Out', 'Allow')
        windows.verify_netfirewall_rule('Cốc Cốc Torrent Update (UDP-Out)', 'Out', 'Allow')
