import pytest
from pytest_testrail.plugin import pytestrail


class TestFirstTimeRun:

    def verify_new_tab_coccoc_exist(self):
        from pywinauto import Desktop
        coccoc_instance = Desktop(backend='uia').Welcome_to_Cốc_Cốc_Cốc_CốcPane
        coccoc_instance.New_Tab.click_input()
        all_windows = Desktop(backend='uia').windows()
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

    @pytestrail.case('C44830')
    @pytestrail.defect('BR-1415')
    @pytest.mark.skip(reason='Bug BR-1415')
    def test_if_widevine_flash_plugin_exist_by_default_right_after_installing_browser(self):
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
        from testscripts.smoketest.installations.common import open_browser_from_command
        try:
            open_browser_from_command(browser_name='browser')
            from testscripts.smoketest.common import get_application_process
            import time
            time.sleep(4)
            assert 'browser' in get_application_process(application_name='browser')
            assert 'CocCocCrashHandler' in get_application_process(application_name='CocCocCrashHandler')
        finally:
            from testscripts.smoketest.common import cleanup
            cleanup(firefox=False)

    @pytestrail.case('C44832')
    def test_check_extensions_version_after_installation(self):
        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=True, is_needed_clear_user_data=False)
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
            import time
            time.sleep(1)
            assert extension_page_object.get_attribute_toggle_button_in_detail_extension(driver,
                                                                                         'aria-pressed') == 'true'
            driver.get(Urls.COCCOC_EXTENSIONS)








