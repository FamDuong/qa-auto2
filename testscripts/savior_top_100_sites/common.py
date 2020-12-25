import logging
import time
from datetime import datetime

from models.pagelocators.top_savior_sites.top_savior_sites_social import InstagramLocators, FacebookLocators
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators
from models.pageobject.settings import SettingsClearBrowserDataPageObject
from models.pagelocators.facebook import FacebookPageLocators
from models.pageobject.basepage_object import BasePageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from models.pageobject.top_savior_sites.top_savior_sites_social import FacebookActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import assert_file_download_value, delete_all_mp4_file_download, \
    download_file_via_main_download_button, get_resolution_info
from models.pageobject.chome_store_page import ChromeStorePageObjects
from utils_automation.const import Urls, OtherSiteUrls, TopSitesUrls

LOGGER = logging.getLogger(__name__)

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
chrome_store_page_object = ChromeStorePageObjects()
base_page_object = BasePageObject()
settings_clear_browser_data_page_object = SettingsClearBrowserDataPageObject()
facebook_action = FacebookActions()
top_sites_savior_title_action = TopSitesSaviorTitleAction()
top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()


# def install_adblockplus_addon(driver):
#     driver.get(ChromeStoreUrls.ADSBLOCKPLUS_EXTENSION_URL)
#     chrome_store_page_object.click_on_add_to_chrome_button(driver)

def choose_solution_is_error(e):
    exeption_list = ['no such element', 'javascript error']
    count = 0
    for i in range(len(exeption_list)):
        if exeption_list[i] in str(e):
            count = count + 1
    if count > 0:
        return True
    else:
        return False


def choose_highest_resolution_of_video(driver):
    LOGGER.info("Choose resolution option")
    savior_page_object.choose_preferred_option(driver)
    time.sleep(5)
    e = savior_page_object.choose_quad_hd_option(driver)
    if choose_solution_is_error(e):
        e = savior_page_object.choose_full_hd_option(driver)
        if choose_solution_is_error(e):
            e = savior_page_object.choose_hd_option(driver)
            if choose_solution_is_error(e):
                e = savior_page_object.choose_standard_option(driver)
                if choose_solution_is_error(e):
                    savior_page_object.choose_small_option(driver)
                    if choose_solution_is_error(e):
                        savior_page_object.choose_mobile_option(driver)
                        if choose_solution_is_error(e):
                            savior_page_object.choose_original_option(driver)
    savior_page_object.wait_until_finished_choose_resolution(driver)


def choose_highest_resolution_of_mp3(driver):
    LOGGER.info("Choose resolution option")
    savior_page_object.choose_preferred_option(driver)
    e = savior_page_object.choose_mp3_standard_option(driver)
    if 'no such element' in str(e):
        savior_page_object.choose_mp3_medium_option(driver)
    savior_page_object.wait_until_finished_choose_resolution(driver)


def download_and_verify_video(driver, download_folder, expect_length, start_with, end_with='.mp4',
                              mouse_over_first_video=True):
    if mouse_over_first_video:
        any_site_page_object.mouse_over_first_video_element(driver)
    if '.mp4' in end_with:
        choose_highest_resolution_of_video(driver)
    else:
        choose_highest_resolution_of_mp3(driver)

    media_info = download_file_via_main_download_button(driver, start_with)
    expect_height = get_resolution_info(media_info)
    try:
        assert_file_download_value(download_folder, expect_height, expect_length, start_with=start_with,
                                   end_with=end_with)
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


def delete_all_history(driver):
    driver.get(Urls.COCCOC_SETTINGS_CLEAR_BROWSER_DATA)
    LOGGER.info("Delete all history,cached and cookies")
    settings_clear_browser_data_page_object.select_time_range(driver)
    settings_clear_browser_data_page_object.tick_browsing_history_checkbox(driver)
    settings_clear_browser_data_page_object.tick_cached_images_and_files_checkbox(driver)
    settings_clear_browser_data_page_object.tick_cookies_and_other_site_data_checkbox(driver)
    settings_clear_browser_data_page_object.click_clear_data_button(driver)


def logout_instagram(driver):
    driver.find_element_by_xpath(InstagramLocators.USER_NAME_AVATAR_NAV).click()
    logout_btn_count = driver.find_elements_by_xpath(InstagramLocators.LOGOUT_BTN)
    start_time = datetime.now()
    while len(logout_btn_count) == 0:
        time.sleep(2)
        logout_btn_count = driver.find_elements_by_xpath(InstagramLocators.LOGOUT_BTN)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 15:
            break
    driver.find_element_by_xpath(InstagramLocators.LOGOUT_BTN).click()


def login_instagram(driver):
    # driver = coccoc_instance()
    driver.get(OtherSiteUrls.INSTAGRAM_LOGIN_URL)
    user_label = driver.find_elements_by_xpath(InstagramLocators.USER_NAME_LBL)
    if len(user_label) == 0:
        user_avatar_nav = driver.find_elements_by_xpath(InstagramLocators.USER_AVATAR_NAV)
        if len(user_avatar_nav) == 1:
            logout_instagram(driver)
        time.sleep(3)
        email_txt = driver.find_element_by_xpath(InstagramLocators.USER_NAME_TXT)
        pass_txt = driver.find_element_by_xpath(InstagramLocators.PASSWORD_TXT)
        base_page_object.clear_text_to_element(driver, email_txt)
        base_page_object.send_keys_to_element(driver, email_txt, InstagramLocators.EMAIL)
        base_page_object.clear_text_to_element(driver, pass_txt)
        base_page_object.send_keys_to_element(driver, pass_txt, InstagramLocators.PASS)
        driver.find_element_by_xpath(InstagramLocators.LOGIN_BTN).click()
        time.sleep(3)
        save_infor_btn = driver.find_elements_by_xpath(InstagramLocators.SAVE_INFO_BTN)
        if len(save_infor_btn) > 0:
            driver.find_element_by_xpath(InstagramLocators.SAVE_INFO_BTN).click()
            time.sleep(3)
        not_now_btn = driver.find_elements_by_xpath(InstagramLocators.TURN_ON_NOTIFICATIONS_NOT_NOW)
        if len(not_now_btn) > 0:
            driver.find_element_by_xpath(InstagramLocators.TURN_ON_NOTIFICATIONS_NOT_NOW).click()
            time.sleep(3)


def verify_download_file_facebook_by_url(driver, download_folder, url, need_opened_video=False,
                                         need_mouse_over_video=True):
    login_facebook(driver)
    driver.get(url)
    LOGGER.info("Check download video on " + url)
    time.sleep(3)
    facebook_action.scroll_to_facebook_video(driver, url)
    if need_opened_video:
        click_to_open_large_video(driver)
    if need_mouse_over_video:
        mouse_over_facebook_first_video_element(driver, url)
    choose_highest_resolution_of_video(driver)
    video_title_temp = top_sites_savior_title_action.get_video_title_by_javascript_from_span_tag(driver)
    video_title = top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_temp)
    expect_length = get_facebook_video_length_base_url(driver, url)
    media_info = download_file_via_main_download_button(driver, video_title)
    resolution_info = get_resolution_info(media_info)
    try:
        assert_file_download_value(download_folder, resolution_info, expect_length, start_with=video_title,
                                   end_with=".mp4")
    finally:
        delete_all_mp4_file_download(download_folder, end_with=".mp4", start_with=video_title)


def click_to_open_large_video(driver):
    facebook_action.click_on_first_video(driver)
    time.sleep(3)


def mouse_over_facebook_first_video_element(driver, url):
    if url == TopSitesUrls.FACEBOOK_HOMEPAGE_URL or url == TopSitesUrls.FACEBOOK_PROFILE_ME_URL \
            or url == TopSitesUrls.FACEBOOK_WATCH_URL or url == TopSitesUrls.FACEBOOK_VIDEO_URL:
        any_site_page_object.mouse_over_first_video_element(driver, FacebookLocators.HOME_PAGE_FIRST_VIDEO)
    elif url == OtherSiteUrls.FACEBOOK_VTVGIAITRI_PAGE_URL:
        any_site_page_object.mouse_over_first_video_element(driver,
                                                            FacebookLocators.VTV_GIAITRI_PAGE_FIRST_VIDEO)
    else:
        any_site_page_object.mouse_over_first_video_element(driver)


def get_facebook_video_length_base_url(driver, url):
    if url in TopSitesUrls.FACEBOOK_VTVGIAITRI_PAGE_URL:
        return top_savior_sites_video_length_action. \
            get_video_length(driver, css_locator="",
                             element=TopSaviorSitesVideoLengthLocators.FACEBOOK_VIDEO_LENGTH_VTV_GIAITRI_PAGE)
    else:
        return top_savior_sites_video_length_action. \
            get_video_length(driver, css_locator="",
                             element=TopSaviorSitesVideoLengthLocators.FACEBOOK_VIDEO_LENGTH_HOME_PAGE)
