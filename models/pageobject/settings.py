from models.pageelements.settings import SettingsElements, SettingsComponentsPageElement
from models.pagelocators.settings import SettingsPageLocators
from models.pageobject.basepage_object import BasePageObject
from utils_automation.const import Urls, CocCocComponents
from utils_automation.common import wait_for_stable


class SettingsPageObject(BasePageObject):
    settings_elem = SettingsElements()

    def click_continue_where_left_off_button(self, driver):
        element_continue_left_off = self.settings_elem.find_continue_where_left_off(driver)
        element_continue_left_off.click()

    def click_open_new_tab(self, driver):
        element_open_new_tab = self.settings_elem.find_open_new_tab(driver)
        element_open_new_tab.click()

    def click_open_a_specific_page(self, driver):
        element_open_a_specific_page = self.settings_elem.find_open_a_specific_set_of_pages(driver)
        element_open_a_specific_page.click()

    def click_add_a_new_page(self, driver):
        element_add_a_new_page = self.settings_elem.find_add_a_new_page(driver)
        element_add_a_new_page.click()

    def disable_extension(self, driver, extension_id):
        self.enable_extension_toggle_dev_mode(driver)
        element = self.settings_elem.find_extension_on_off_by_id(driver, extension_id)
        is_enable = element.get_attribute("checked")
        if is_enable is not None:
            element.click()
            wait_for_stable()

    def enable_extension_toggle_dev_mode(self, driver):
        toggle_dev_mode = self.settings_elem.find_extension_toggle_developer_mode(driver)
        dev_mode_status = toggle_dev_mode.get_attribute("checked")
        if dev_mode_status is None:
            toggle_dev_mode.click()
            wait_for_stable()

    def get_default_torrent_value(self, driver):
        default_torrent_value = self.settings_elem.find_default_torrent_client(driver)
        return default_torrent_value.text

    def get_max_connection_per_torrent_client_value(self, driver):
        max_connection = self.settings_elem.find_max_number_of_connection_per_client(driver)
        test1_executed = driver.execute_script('return arguments[0].shadowRoot', max_connection)
        return test1_executed.text

    def get_download_folder(self, driver):
        return self.settings_elem.find_download_location_element(driver).text

    def update_extension(self, driver):
        self.enable_extension_toggle_dev_mode(driver)
        self.settings_elem.find_extension_update_button(driver).click()
        self.settings_elem.find_extension_update_popup(driver)

    def update_cc_version(self, driver):
        self.settings_elem.wait_until_cc_version_update(driver)

    def verify_setting_on_startup(self, driver, expect_option):
        driver.get(Urls.COCCOC_SETTINGS_ONSTARTUP)
        # element_open_new_tab = self.settings_elem.find_open_new_tab(driver)
        if expect_option == SettingsPageLocators.OPEN_NEW_TAB_PAGE_TEXT:
            checked = self.settings_elem.find_open_new_tab(driver).get_attribute("checked")
        elif expect_option == SettingsPageLocators.CONTINUE_WHERE_LEFT_OFF_TEXT:
            checked = self.settings_elem.find_continue_where_left_off(driver).get_attribute("checked")
        else:
            checked = self.settings_elem.find_open_a_specific_set_of_pages(driver).get_attribute("checked")
        assert checked is not None

    def verify_setting_default_browser(self, driver, expect_option):
        driver.get(Urls.COCCOC_SETTINGS_DEFAULT)
        if expect_option == SettingsPageLocators.DEFAULT_BROWSER_RUN_AUTO_ONSTARTUP_CHECKBOX:
            checked = self.settings_elem.find_run_automatically_on_system_startup(driver).get_attribute("checked")
        assert checked is not None

    def verify_extension_version(self, driver, extension_id, expect_version, expect_on = None):
        self.enable_extension_toggle_dev_mode(driver)
        actual_version = self.settings_elem.find_extension_version_by_id(driver, extension_id).text
        assert actual_version == expect_version
        if expect_on is not None:
            actual_on = self.settings_elem.find_extension_on_off_by_id(driver, extension_id).get_attribute("checked")
            assert actual_on is not None

    def verify_extension_status(self, driver, extension_id, expect_status):
        actual_status = self.settings_elem.find_extension_on_off_by_id(driver, extension_id).get_attribute("checked")
        assert actual_status is expect_status

    def verify_menu_base_on_language(self, driver, language):
        driver.get(Urls.COCCOC_SETTINGS_URL)
        actual_people_lbl = self.settings_elem.find_left_menu_people(driver).text
        actual_auto_fill_lbl = self.settings_elem.find_left_menu_auto_fill(driver).text
        actual_default_browser_lbl = self.settings_elem.find_left_menu_default_browser(driver).text
        if language == 'en':
            assert actual_people_lbl in 'People'
            assert actual_auto_fill_lbl in 'Autofill'
            assert actual_default_browser_lbl in 'Default browser'
        else:
            assert actual_people_lbl in 'Bạn và Google'
            assert actual_auto_fill_lbl in 'Tự động điền'
            assert actual_default_browser_lbl in 'Trình duyệt mặc định'

    def interact_ads_block(self, driver, action, script_get_attribute_aria_pressed, script_click_ads_block):
        def disable_enabled_ads_block():
            if driver.execute_script(script_get_attribute_aria_pressed) == 'true':
                driver.execute_script(script_click_ads_block)
            elif driver.execute_script(script_get_attribute_aria_pressed) == 'false':
                print("Button is already disabled")
            else:
                print("Problem when get attribute aria-pressed of enabled ads blcok")

        def enable_enabled_ads_block():
            if driver.execute_script(script_get_attribute_aria_pressed) == 'true':
                print("Button is already enabled")
            elif driver.execute_script(script_get_attribute_aria_pressed) == 'false':
                driver.execute_script(script_click_ads_block)
            else:
                print("Problem when get attribute aria-pressed of enabled ads blcok")

        if action == 'disable':
            return disable_enabled_ads_block()
        elif action == 'enable':
            return enable_enabled_ads_block()
        else:
            print("Please specify the action")

    def get_text_default_browser_element(self, driver):
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step()
        return self.settings_elem.find_default_browser_element(driver).text

    def get_text_make_default_browser_element(self, driver):
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step()
        return self.settings_elem.find_make_default_browser_element(driver).text

    def get_text_cococ_is_default_browser_element(self, driver):
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step()
        return self.settings_elem.find_coccoc_is_default_browser_element(driver).text

    def click_make_default_browser_button(self, driver):
        from utils_automation.setup import WaitAfterEach
        WaitAfterEach.sleep_timer_after_each_step()
        self.settings_elem.find_make_default_browser_button(driver).click()
        WaitAfterEach.sleep_timer_after_each_step()

    def get_attribute_aria_pressed_system_start_up_coccoc_toggle_btn(self, driver):
        return self.settings_elem.find_run_automatically_on_system_start_up_toggle(driver).get_attribute('aria-pressed')

    def check_if_relaunch_browser_displayed(self, driver):
        return self.settings_elem.find_relaunch_browser_btn(driver)

    class SettingsAdsBlockPageObject(BasePageObject):
        settings_ad_block_elem = SettingsElements.SettingsAdsBlock()

        def change_ads_block_mode(self, driver, block_mode='Strict'):
            curr_block_mod_elem = self.settings_ad_block_elem.find_current_block_mod(driver)
            if block_mode in curr_block_mod_elem.text:
                print(f"Current block mode is already : {block_mode}")
            else:
                drop_down_elem = self.settings_ad_block_elem.find_drop_down_menu_coccoc_block_ads(driver)
                if block_mode == 'Strict':
                    self.choose_drop_down_value_js(driver, drop_down_elem, 1)
                elif block_mode == 'Standard':
                    self.choose_drop_down_value_js(driver, drop_down_elem, 0)
                else:
                    raise Exception

    def find_all_extensions(self, driver):
        element = self.settings_elem.find_item_container_list_extensions(driver)
        return driver.execute_script('return arguments[0].querySelectorAll(arguments[1])', element, "extensions-item")

    def get_all_extensions_id(self, driver):
        extensions = self.find_all_extensions(driver)
        list_extensions_ids = []
        for extension in extensions:
            list_extensions_ids.append(driver.execute_script("return arguments[0].getAttribute('id')", extension))
        return list_extensions_ids


class SettingsComponentsPageObject(BasePageObject):
    settings_component_page_element = SettingsComponentsPageElement()

    def click_on_each_check_for_update_button(self, driver):
        elements = self.settings_component_page_element.find_all_check_for_update_button(driver)
        for each_element in elements:
            try:
                each_element.click()
            except Exception as e:
                print(e)
            import time
            time.sleep(1)

    def verify_all_components_version_is_updated(self, driver):
        elements = self.settings_component_page_element.find_all_components_version(driver)
        for each_element in elements:
            version = each_element.text
            each_element_id = each_element.get_attribute('id')
            if CocCocComponents.THIRD_PARTY_MODULE_LIST_ID in each_element_id:
                assert version == '2018.7.19.1'
            elif CocCocComponents.ORIGIN_TRIALS_ID in each_element_id:
                pass
            else:
                assert '0.0.0.0' not in version








