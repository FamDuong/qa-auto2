import pytest
from pywinauto import Desktop
from selenium.webdriver.support.wait import WebDriverWait
from testscripts.smoketest.common import delete_installer_download
from models.pagelocators.coccoc_home import CoccocHomePageLocators
from utils_automation.common import WindowsHandler
from utils_automation.const import Urls
import time
from testscripts.download_coc_coc.common import set_driver, clean_up_browser
from datetime import datetime
from models.pageobject.coccocpage import sleep_with_timeout
from testscripts.smoketest.common import check_if_installer_is_downloaded

windows_handler = WindowsHandler()


def save_file_on_ie_browser():
    start_time = datetime.now()
    save_file_popup = Desktop(backend='uia').Trình_duyệt_Cốc_Cốc_lướt_web_theo_phong_cách_Việt_Internet_Explorer
    while save_file_popup.Save.exists() is False:
        time.sleep(3)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 15:
            break
    save_file_popup.Save.click_input()


def download_coccoc_installer(browser_name, driver, download_button, language,
                              installer_name, extension):
    current_user = windows_handler.get_current_login_user()
    download_folder = "C:\\Users\\" + current_user + "\\Downloads\\"
    delete_installer_download(download_folder, language, installer_name, extension)
    try:
        time.sleep(5)
        driver.execute_script('arguments[0].click()', driver.find_element_by_xpath(download_button))
        time.sleep(3)
        driver.execute_script('document.querySelector("' + CoccocHomePageLocators.DONG_Y_BTN_CSS + '").click();')
        if browser_name in 'IE':
            save_file_on_ie_browser()
        sleep_with_timeout(download_folder, language, installer_name, extension)
        assert check_if_installer_is_downloaded(download_folder, language, installer_name, extension) is True
    finally:
        delete_installer_download(download_folder, language, installer_name, extension)


def download_button_is_visible(driver):
    start_time = datetime.now()
    download_button = driver.find_elements_by_xpath(CoccocHomePageLocators.TAI_CC_MAC_BTN_XPATH)
    while len(download_button) == 0:
        time.sleep(1)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 5:
            break
    if len(download_button) > 0:
        return True
    else:
        return False


def verify_redirect_mobile_url(driver):
    app_store_url_center = driver.find_element_by_xpath(
        CoccocHomePageLocators.APP_STORE_BTN_CENTER_XPATH).get_attribute("href")
    app_store_url_footer = driver.find_element_by_xpath(
        CoccocHomePageLocators.APP_STORE_BTN_FOOTER_XPATH).get_attribute("href")
    google_play_url_center = driver.find_element_by_xpath(
        CoccocHomePageLocators.GOODLE_PLAY_BTN_CENTER_XPATH).get_attribute("href")
    google_play_url_footer = driver.find_element_by_xpath(
        CoccocHomePageLocators.GOODLE_PLAY_BTN_FOOTER_XPATH).get_attribute("href")
    assert CoccocHomePageLocators.APP_STORE_URL in app_store_url_center
    assert CoccocHomePageLocators.APP_STORE_URL in app_store_url_footer
    assert CoccocHomePageLocators.GOODLE_PLAY_URL in google_play_url_center
    assert CoccocHomePageLocators.GOODLE_PLAY_URL in google_play_url_footer


class TestDownloadCocCoc:

    @pytest.mark.window_installer_header
    def test_download_coccoc_window_header(self, browsers, domains):
        print("Download installer window by button on header...")
        for browser in browsers:
            print("Browser: " + browser)
            for domain in domains:
                print("Domain: " + domain)
                try:
                    clean_up_browser(driver_choice=browser)
                    driver = set_driver(driver_choice=browser)
                    driver.get(domain)
                    download_coccoc_installer(browser, driver, CoccocHomePageLocators.TAI_CC_BTN_HEADER_XPATH,
                                              language='vi',
                                              installer_name='coccoc_', extension='.exe')
                finally:
                    driver.quit()

    @pytest.mark.window_installer_center
    def test_download_coccoc_window_center(self, browsers, domains):
        print("Download installer window by button on center...")
        for browser in browsers:
            print("Browser: " + browser)
            for domain in domains:
                print("Domain: " + domain)
                try:
                    clean_up_browser(driver_choice=browser)
                    driver = set_driver(driver_choice=browser)
                    driver.get(domain)
                    if domain.endswith('coccoc.com/'):
                        download_coccoc_installer(browser, driver, CoccocHomePageLocators.TAI_CC_BTN_CENTER_HOME_XPATH,
                                                  language='vi',
                                                  installer_name='coccoc_', extension='.exe')
                    else:
                        download_coccoc_installer(browser, driver,
                                                  CoccocHomePageLocators.TAI_CC_BTN_CENTER_OTHER_PAGE_XPATH,
                                                  language='vi',
                                                  installer_name='coccoc_', extension='.exe')
                finally:
                    driver.quit()

    @pytest.mark.window_installer_footer
    def test_download_coccoc_window_footer(self, browsers, domains):
        print("Download installer window by button on footer...")
        for browser in browsers:
            print("Browser: " + browser)
            for domain in domains:
                print("Domain: " + domain)
                try:
                    clean_up_browser(driver_choice=browser)
                    driver = set_driver(driver_choice=browser)
                    driver.get(domain)
                    download_coccoc_installer(browser, driver,
                                              CoccocHomePageLocators.TAI_CC_BTN_FOOTER_XPATH, language='vi',
                                              installer_name='coccoc_', extension='.exe')
                finally:
                    driver.quit()

    @pytest.mark.mac_installer
    def test_download_coccoc_mac(self, browsers, domains):
        print("Download installer mac...")
        for browser in browsers:
            print("Browser: " + browser)
            for domain in domains:
                print("Domain: " + domain)
                try:
                    clean_up_browser(driver_choice=browser)
                    driver = set_driver(driver_choice=browser)
                    driver.get(domain)
                    if download_button_is_visible(driver):
                        download_coccoc_installer(browser, driver,
                                                  CoccocHomePageLocators.TAI_CC_MAC_BTN_XPATH,
                                                  language='', installer_name='coccoc', extension='.dmg')
                finally:
                    driver.quit()

    @pytest.mark.mobile_installer
    def test_redirect_mobile_url(self, browsers):
        for browser in browsers:
            print("Browser: " + browser)
            try:
                clean_up_browser(driver_choice=browser)
                driver = set_driver(driver_choice=browser)
                driver.get(Urls.COCCOC_URL)
                # Check after click on "Trình duyệt di động" tab
                driver.find_element_by_xpath(CoccocHomePageLocators.TRINH_DUYET_DI_DONG_TAB_XPATH).click()
                verify_redirect_mobile_url(driver)

                # Check after click on "Android" icon (Bellow "Tải Cốc Cốc cho Windows" button)
                driver.get(Urls.COCCOC_URL)
                old_window = driver.current_window_handle
                from selenium.webdriver.support import expected_conditions as ec
                driver.find_element_by_xpath(CoccocHomePageLocators.ANDROID_BTN_XPATH).click()
                WebDriverWait(driver, 50).until(ec.number_of_windows_to_be(2))
                second_window = [window for window in driver.window_handles if window != old_window][0]
                driver.switch_to.window(second_window)
                time.sleep(5)
                verify_redirect_mobile_url(driver)
                if driver.title in CoccocHomePageLocators.TITTLE_MOBILE_PAGE:
                    driver.close()

                # Check after click on "Ios" icon (Bellow "Tải Cốc Cốc cho Windows" button)
                driver.switch_to.window(old_window)
                driver.find_element_by_xpath(CoccocHomePageLocators.IOS_BTN_XPATH).click()
                WebDriverWait(driver, 20).until(ec.number_of_windows_to_be(2))
                third_window = \
                    [window for window in driver.window_handles if window != old_window and window != second_window][0]
                driver.switch_to.window(third_window)
                time.sleep(5)
                verify_redirect_mobile_url(driver)
            finally:
                driver.quit()
