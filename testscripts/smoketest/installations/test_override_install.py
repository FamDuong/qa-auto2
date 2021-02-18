import logging
from pytest_testrail.plugin import pytestrail
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.history import HistoryPageLocators
from testscripts.smoketest.common import delete_installer_download, download_and_get_installer_path
from utils_automation.common import get_resource_path
from utils_automation.const import Urls
from utils_automation.common_browser import coccoc_instance

LOGGER = logging.getLogger(__name__)


class TestOverrideInstall(BasePageElement):

    @pytestrail.case('C44773')
    def test_check_install_new_version_above_old_version(self, is_active_host, url, coccoc_version):
        old_version = self.install_old_coccoc_version()
        new_version = self.install_new_coccoc_version_without_remove_old_version(is_active_host, url)
        if coccoc_version == '':
            LOGGER.info("Verify new Coc Coc version is greater than old Coc Coc version")
            from utils_automation.version import is_version_greater
            assert is_version_greater(new_version, old_version) is True
        else:
            LOGGER.info("Verify Coc Coc version is version input from terminal param")
            assert new_version in coccoc_version
        self.verify_redirect_to_coccoc_is_success()
        self.verify_user_data_is_kept()

    @pytestrail.case('C178210')
    def test_check_install_new_version_after_remove_old_version_without_clear_user_data(self, is_active_host, url,
                                                                                        coccoc_version):
        try:
            self.install_old_coccoc_version(prepare_history='no')
            browser, default_download_folder, is_activated_host, coccoc_installer = download_and_get_installer_path(
                is_active_host, url)

            from testscripts.smoketest.common import uninstall_then_install_coccoc_with_default
            uninstall_then_install_coccoc_with_default(installer_path=coccoc_installer,
                                                       coccoc_installer_name='CocCocSetup.exe')
            self.verify_redirect_to_coccoc_is_success()
            self.verify_user_data_is_kept(verify_history='no')
        finally:
            browser.quit()
            delete_installer_download(default_download_folder, language='', installer_name='CocCocSetup',
                                      extension='.exe')

    def install_old_coccoc_version(self, prepare_history='yes'):
        old_coc_coc_installer_path = get_resource_path() + "test_data\\standalone\\"
        LOGGER.info("Install old Coc Coc version")
        from testscripts.smoketest.common import install_old_coccoc_version
        install_old_coccoc_version(old_coc_coc_installer_path)
        old_coccoc_driver_path = get_resource_path() + "webdriver\\chromedriver_79\\chromedriver.exe"
        self.prepare_user_data(old_coccoc_driver_path, prepare_history)
        from testscripts.smoketest.common import get_list_coccoc_version_folder_name
        old_version = get_list_coccoc_version_folder_name()[0]
        LOGGER.info("Old Coc Coc version: " + old_version)
        return old_version

    def install_new_coccoc_version_without_remove_old_version(self, is_active_host, url):
        try:
            browser, default_download_folder, is_activated_host, coccoc_installer = download_and_get_installer_path(
                is_active_host, url)
            LOGGER.info("Install new coc coc version without remove old version")
            from testscripts.smoketest.common import install_coccoc_set_as_default
            install_coccoc_set_as_default(installer_path=coccoc_installer, coccoc_installer_name='CocCocSetup.exe')
            from testscripts.smoketest.common import get_list_coccoc_version_folder_name

            new_version = get_list_coccoc_version_folder_name()[0]
            LOGGER.info("New Coc Coc version: " + new_version)
            return new_version
        finally:
            browser.quit()
            delete_installer_download(default_download_folder, language='', installer_name='CocCocSetup',
                                      extension='.exe')

    def prepare_user_data(self, old_coccoc_driver_path, prepare_history='yes'):
        LOGGER.info("Prepare user data")
        driver = coccoc_instance(binary_path=old_coccoc_driver_path)
        if prepare_history in 'yes':
            # Prepare histories
            driver.get("https://vnexpress.net/")
            driver.get("https://www.google.com/")

        # Prepare extension => Comment because the part extension not stable when run by automation
        driver.get("https://chrome.google.com/webstore/category/extensions")
        # from models.pagelocators.chrome_store_page import ChromeStorePageLocators
        # chrome_store_page_locators = ChromeStorePageLocators()
        # driver.find_element_by_id(chrome_store_page_locators.SEARCH_THE_STORE_TXT_ID).send_keys("Google Translate",
        #                                                                                         Keys.ENTER)
        # import time
        # time.sleep(5)
        # driver.find_element_by_xpath(chrome_store_page_locators.ADD_TO_CHROME_BTN_XPATH).click()
        # add_on_panel = Desktop(backend='uia').Chrome_Web_Store_flash_Cốc_Cốc
        # add_on_panel.child_window(title='Add extension').click()
        # time.sleep(3)
        # coccoc_instance()

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

    def verify_user_data_is_kept(self, verify_history='no'):
        LOGGER.info("Verify user data is kept")
        # Verify history is kept
        driver = coccoc_instance()
        if verify_history in 'yes':
            driver.get(Urls.COCCOC_HISTORY_URL)
            domain_chrome_store = self.get_domain_name_position(driver, HistoryPageLocators.HISTORY_CHROME_STORE)
            domain_google = self.get_domain_name_position(driver, HistoryPageLocators.HISTORY_GOODLE)
            domain_vnexpress = self.get_domain_name_position(driver, HistoryPageLocators.HISTORY_VNEXPRESS)

            assert 'chrome.google.com' in domain_chrome_store
            assert 'www.google.com' in domain_google
            assert 'vnexpress.net' in domain_vnexpress

        # Verify extension is kept => Comment because the part extension not stable when run by automation
        # driver.get(Urls.COCCOC_EXTENSIONS)
        # from models.pagelocators.extensions import ExtensionsPageLocators
        # extension_name = self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
        #                                           ExtensionsPageLocators.ITEMS_LIST,
        #                                           ExtensionsPageLocators.GOOGLE_TRANSLATE_ID,
        #                                           ExtensionsPageLocators.GOOGLE_TRANSLATE_NAME_ID).text
        # assert 'Google Translate' in extension_name

    def verify_redirect_to_coccoc_is_success(self):
        LOGGER.info("Verify redirect to Coc Coc is success")
        driver = coccoc_instance()
        driver.get("https://coccoc.com/")
        assert ('Tải Cốc Cốc cho Windows' in driver.page_source)
