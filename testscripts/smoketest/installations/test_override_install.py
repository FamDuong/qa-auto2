from pytest_testrail.plugin import pytestrail
from pywinauto import Desktop
from selenium.webdriver.common.keys import Keys

from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.history import HistoryPageLocators
from utils_automation.const import Urls
from testscripts.smoketest.common import coccoc_instance


class TestOverrideInstall(BasePageElement):

    @pytestrail.case('C44773')
    def test_check_install_new_version_above_old_version(self):
        driver = coccoc_instance()
        old_version = self.install_old_coccoc_version(driver)
        new_version = self.install_new_coccoc_version_without_remove_old_version()

        from utils_automation.version import is_version_greater
        assert is_version_greater(new_version, old_version) is True
        self.verify_redirect_to_coccoc_is_success(driver)
        self.verify_user_data_is_kept(driver)

    @pytestrail.case('C178210')
    def test_check_install_new_version_after_remove_old_version_without_clear_user_data(self):
        from testscripts.smoketest.common import install_old_coccoc_version
        install_old_coccoc_version(is_needed_clear_user_data=True)
        driver = coccoc_instance()
        self.prepare_user_data(driver, prepare_history='no')

        from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
        uninstall_then_install_coccoc_with_default(is_needed_clean_up=False)
        self.verify_redirect_to_coccoc_is_success(driver)
        self.verify_user_data_is_kept(driver, verify_history='no')

    def install_old_coccoc_version(self, driver):
        from testscripts.smoketest.common import install_old_coccoc_version
        install_old_coccoc_version()
        self.prepare_user_data(driver)
        from testscripts.smoketest.common import get_list_coccoc_version_folder_name
        old_version = get_list_coccoc_version_folder_name()[0]
        return old_version

    def install_new_coccoc_version_without_remove_old_version(self):
        from testscripts.smoketest.common import install_coccoc_set_as_default
        install_coccoc_set_as_default()
        from testscripts.smoketest.common import get_list_coccoc_version_folder_name
        new_version = get_list_coccoc_version_folder_name()[0]
        return new_version

    def prepare_user_data(self, driver, prepare_history='yes'):
        if prepare_history in 'yes':
            # Prepare histories
            driver.get("https://vnexpress.net/")
            driver.get("https://www.google.com/")

        # Prepare extension => Comment because the part extension not stable when run by automation
        driver.get("https://chrome.google.com/webstore/category/extensions")
        from models.pagelocators.chrome_store_page import ChromeStorePageLocators
        chrome_store_page_locators = ChromeStorePageLocators()
        driver.find_element_by_id(chrome_store_page_locators.SEARCH_THE_STORE_TXT_ID).send_keys("Google Translate",
                                                                                                Keys.ENTER)
        # import time
        # time.sleep(5)
        # driver.find_element_by_xpath(chrome_store_page_locators.ADD_TO_CHROME_BTN_XPATH).click()
        self.get_add_to_chrome_btn(driver, chrome_store_page_locators).click()
        add_on_panel = Desktop(backend='uia').Chrome_Web_Store_flash_Cốc_Cốc
        add_on_panel.child_window(title='Add extension').click()
        import time
        time.sleep(3)

    def get_add_to_chrome_btn(self, driver, chrome_store_page_locators):
        index = 0
        from datetime import datetime
        start_time = datetime.now()
        domain_name_position = None
        while index == 0:
            try:
                add_to_chrome_btn = driver.find_element_by_xpath(chrome_store_page_locators.ADD_TO_CHROME_BTN_XPATH)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 3:
                    break
                index += 1
            except:
                import time
                time.sleep(1)
        return add_to_chrome_btn

    def get_domain_name_position(self, driver, history):
        index = 0
        from datetime import datetime
        start_time = datetime.now()
        domain_name_position = None
        while index == 0:
            try:
                domain_name_position = self.find_shadow_element(driver, HistoryPageLocators.HISTORY_APP,
                                                                HistoryPageLocators.HISTORY,
                                                                history,
                                                                HistoryPageLocators.WEB_NAME_ID)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 3:
                    break
                index += 1
            except:
                import time
                time.sleep(1)
        return domain_name_position.text

    def verify_user_data_is_kept(self, driver, verify_history='no'):
        # Verify history is kept
        if verify_history in 'yes':
            driver.get(Urls.COCCOC_HISTORY_URL)
            domain_chrome_store = self.get_domain_name_position(driver, HistoryPageLocators.HISTORY_CHROME_STORE)
            domain_google = self.get_domain_name_position(driver, HistoryPageLocators.HISTORY_GOODLE)
            domain_vnexpress = self.get_domain_name_position(driver, HistoryPageLocators.HISTORY_VNEXPRESS)

            assert 'chrome.google.com' in domain_chrome_store
            assert 'www.google.com' in domain_google
            assert 'vnexpress.net' in domain_vnexpress

        # Verify extension is kept => Comment because the part extension not stable when run by automation
        driver.get(Urls.COCCOC_EXTENSIONS)
        from models.pagelocators.extensions import ExtensionsPageLocators
        extension_name = self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                                  ExtensionsPageLocators.ITEMS_LIST,
                                                  ExtensionsPageLocators.GOOGLE_TRANSLATE_ID,
                                                  ExtensionsPageLocators.GOOGLE_TRANSLATE_NAME_ID).text
        assert 'Google Translate' in extension_name

    def verify_redirect_to_coccoc_is_success(self, driver):
        driver.get("https://coccoc.com/")
        assert ('Tải Cốc Cốc cho Windows' in driver.page_source)
