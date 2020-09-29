import logging
import time

from selenium.common.exceptions import JavascriptException

from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from testscripts.common_setup import assert_file_download_value, delete_all_mp4_file_download, \
    download_file_via_main_download_button, get_resolution_info
from models.pageobject.chome_store_page import ChromeStorePageObjects
from utils_automation.const import ChromeStoreUrls

LOGGER = logging.getLogger(__name__)
any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
chrome_store_page_object = ChromeStorePageObjects()


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


def download_video(driver, download_folder, video_title):
    media_info = download_file_via_main_download_button(driver, video_title)
    resolution_info = get_resolution_info(media_info)
    try:
        assert_file_download_value(download_folder, resolution_info, start_with=video_title)
    finally:
        delete_all_mp4_file_download(download_folder, '.mp4', startwith=video_title)


def download_and_verify_video(driver, download_folder, video_title, mouse_over_first_video=True):
    if mouse_over_first_video:
        any_site_page_object.mouse_over_first_video_element(driver)
    # time.sleep(2)
    choose_highest_resolution_of_video(driver)
    media_info = download_file_via_main_download_button(driver, video_title)
    resolution_info = get_resolution_info(media_info)
    try:
        assert_file_download_value(download_folder, resolution_info, start_with=video_title)
    finally:
        delete_all_mp4_file_download(download_folder, '.mp4', start_with=video_title)
