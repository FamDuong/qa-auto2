import logging
import time
from datetime import datetime

from models.pagelocators.facebook import FacebookPageLocators
from models.pageobject.basepage_object import BasePageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from testscripts.common_setup import assert_file_download_value, delete_all_mp4_file_download, \
    download_file_via_main_download_button, get_resolution_info
from models.pageobject.chome_store_page import ChromeStorePageObjects
from utils_automation.const import Urls

LOGGER = logging.getLogger(__name__)
any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
chrome_store_page_object = ChromeStorePageObjects()
base_page_object = BasePageObject()


# def install_adblockplus_addon(driver):
#     driver.get(ChromeStoreUrls.ADSBLOCKPLUS_EXTENSION_URL)
#     chrome_store_page_object.click_on_add_to_chrome_button(driver)


def choose_highest_resolution_of_video(driver):
    LOGGER.info("Choose resolution option")
    savior_page_object.choose_preferred_option(driver)
    try:
        savior_page_object.choose_full_hd_option(driver)
    except Exception:
        savior_page_object.choose_hd_option(driver)
    except Exception:
        savior_page_object.choose_standard_option(driver)
    except Exception:
        savior_page_object.choose_medium_option(driver)
    except Exception:
        savior_page_object.choose_small_option(driver)
    except Exception:
        savior_page_object.choose_mobile_option(driver)
    except Exception:
        savior_page_object.choose_original_option(driver)


def choose_highest_resolution_of_mp3(driver):
    LOGGER.info("Choose resolution option")
    savior_page_object.choose_preferred_option(driver)
    try:
        savior_page_object.choose_mp3_standard_option(driver)
    except:
        savior_page_object.choose_mp3_medium_option(driver)


def download_and_verify_video(driver, download_folder, expect_length, start_with, end_with='.mp4', mouse_over_first_video=True):
    if mouse_over_first_video:
        any_site_page_object.mouse_over_first_video_element(driver)
    if '.mp4' in end_with:
        choose_highest_resolution_of_video(driver)
    else:
        choose_highest_resolution_of_mp3(driver)
    media_info = download_file_via_main_download_button(driver, start_with)
    expect_height = get_resolution_info(media_info)
    try:
        assert_file_download_value(download_folder, expect_height, expect_length, start_with=start_with, end_with=end_with)
    finally:
        delete_all_mp4_file_download(download_folder, end_with, start_with=start_with)


def logout_facebook(driver):
    driver.find_element_by_id(FacebookPageLocators.COCCOC_AT_NAME_XPATH).click()
    logout_btn_count = driver.find_elements_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH)
    start_time = datetime.now()
    while len(logout_btn_count) == 0:
        time.sleep(2)
        logout_btn_count = driver.find_elements_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 15:
            break
    driver.find_element_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH).click()


def login_facebook(driver):
    driver.get(Urls.FACEBOOK_URL)
    coccoc_at_user_lbl = driver.find_elements_by_xpath(FacebookPageLocators.COCCOC_AT_NAME_XPATH)
    if len(coccoc_at_user_lbl) == 0:
        show_menu_setting_icon = driver.find_elements_by_xpath(FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)
        if len(show_menu_setting_icon) == 1:
            logout_facebook(driver)
        email_txt = driver.find_element_by_id(FacebookPageLocators.EMAIL_TXT_ID)
        pass_txt = driver.find_element_by_id(FacebookPageLocators.PASS_TXT_ID)
        base_page_object.clear_text_to_element(driver, email_txt)
        base_page_object.send_keys_to_element(driver, email_txt, FacebookPageLocators.EMAIL)
        base_page_object.clear_text_to_element(driver, pass_txt)
        base_page_object.send_keys_to_element(driver, pass_txt, FacebookPageLocators.PASS)
        driver.find_element_by_xpath(FacebookPageLocators.SUBMIT_BTN_XPATH).click()
        show_menu_setting_icon = driver.find_elements_by_xpath(FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)

        start_time = datetime.now()
        while len(show_menu_setting_icon) == 0:
            time.sleep(2)
            show_menu_setting_icon = driver.find_elements_by_xpath(
                FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 15:
                break

