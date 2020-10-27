import logging
import time
from datetime import datetime

import cv2
from models.pageelements.savior import SaviorElements
from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject, \
    SaviorExtensionOptionsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import YoutubePageObject, GooglePageObject, AnySitePageObject
from utils_automation.common import FilesHandle, if_height_frame_so_width_frame
from utils_automation.const import Urls, ExtensionIds, VideoUrls
from utils_automation.setup import Browser, WaitAfterEach

extension_page_object = ExtensionsPageObject()

extension_detail_page_object = ExtensionsDetailsPageObject()
youtube_page_object = YoutubePageObject()
savior_page_object = SaviorPageObject()

browser_incognito = Browser()
savior_extension = SaviorExtensionOptionsPageObject()
google_page_object = GooglePageObject()

download_page_object = DownloadsPageObject()
any_site_page_object = AnySitePageObject()
savior_element = SaviorElements()

LOGGER = logging.getLogger(__name__)


def delete_all_mp4_file_download(mydir, end_with, start_with=None):
    LOGGER.info("Delete video")
    files_handle = FilesHandle()
    if isinstance(start_with, list):
        for title in start_with:
            files_handle.delete_files_in_folder(mydir, end_with, start_with=title)
    else:
        files_handle.delete_files_in_folder(mydir, end_with, start_with=start_with)


def download_file_via_main_download_button(browser, stard_with):
    LOGGER.info("Downloading video...")

    savior_page_object.download_file_via_savior_download_btn(browser)
    media_info_element = savior_page_object.current_media_info(browser)

    # Check the file is fully downloaded
    open_coccoc_download_then_check_if_the_file_fully_downloaded(browser, stard_with)
    return media_info_element


def find_mp4_file_download(mydir, end_with, start_with=None):
    files_handle = FilesHandle()
    return files_handle.find_files_in_folder_by_modified_date(mydir, end_with, start_with=start_with)


def clear_data_download(driver):
    driver.get(Urls.COCCOC_DOWNLOAD_URL)
    WaitAfterEach.sleep_timer_after_each_step()
    download_page_object.clear_all_existed_downloads(driver)
    WaitAfterEach.sleep_timer_after_each_step()


def assert_file_download_value(download_folder_path, expect_height, expect_length, start_with, end_with):
    LOGGER.info("Verify video title same as: " + str(start_with))
    if isinstance(start_with, list):
        for title in start_with:
            mp4_files = find_mp4_file_download(download_folder_path, end_with, start_with=title)
    else:
        mp4_files = find_mp4_file_download(download_folder_path, end_with, start_with=start_with)
    vid = cv2.VideoCapture(download_folder_path + '\\' + mp4_files[0])

    actual_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    if '.mp4' in end_with:
        assert vid.isOpened()
    assert len(mp4_files) > 0
    vid.release()
    actual_length, bit_rate = get_length_and_bit_rate(download_folder_path, mp4_files[0])

    assert_video_height_width(end_with, actual_height, expect_height, actual_width)
    assert_video_length(expect_length, actual_length)
    assert bit_rate == 320 or bit_rate == 128 or bit_rate == 126 or bit_rate > 0


def get_length_and_bit_rate(download_folder_path, mp4_file):
    import mutagen
    file = mutagen.File(download_folder_path + '\\' + mp4_file)
    length = file.info.length
    bit_rate = round(file.info.bitrate / 1000)
    LOGGER.info("Length: {}s; Bitrate: {}".format(length, bit_rate))
    return length, bit_rate


def get_sec(time_str):
    """Get Seconds from time."""
    LOGGER.info("Time string: " + str(time_str))
    if ':' in str(time_str):
        try:
            h, m, s = str(time_str).split(':')
            return int(h) * 3600 + int(m) * 60 + int(s)
        except Exception:
            m, s = str(time_str).split(':')
            return int(m) * 60 + int(s)
    else:
        return time_str


def assert_video_length(actual_length, expect_length):
    if expect_length == 0:
        expect_length_seconds = get_sec(expect_length)
        LOGGER.info("Expect video length: " + str(expect_length_seconds))
        LOGGER.info("Actual video length2: " + str(actual_length))
        diff_length_date_time = abs(actual_length - expect_length_seconds)
        LOGGER.info("Diff video length seconds: " + str(diff_length_date_time))
        assert diff_length_date_time < 2


def get_hours_and_minutes_in_video_length(video_length):
    if video_length.count('.') == 2:
        video_length_hours = video_length.split(".")[1]
        video_length_minutes = video_length.split(".")[2]
        video_length_new = video_length_hours + '.' + video_length_minutes
        LOGGER.info("Video length after get minutes and seconds " + video_length)
        return video_length_new
    else:
        return video_length


def assert_video_height_width(end_with, actual_height, expect_height, actual_width):
    if '.mp4' in end_with:
        LOGGER.info("Actual height x Actual width: " + str(actual_height) + "x" + str(actual_width))
        LOGGER.info("Expect height: " + str(expect_height))
        try:
            if int(actual_height) > 720:
                expect_width = if_height_frame_so_width_frame(expect_height)
                LOGGER.info("Assert video with high resolution" + str(actual_height) + "x" + str(expect_width))
                assert actual_width == expect_width
        except Exception:
            LOGGER.info("Assert video with Standard/ Medium/ Low resolution")
            if (expect_height is not None) and (expect_height != ''):
                diff_value = abs(int(actual_height) - int(expect_height.split('p')[0]))
                LOGGER.info("Diff height: " + str(diff_value))
                assert (str(int(actual_height)) in expect_height or diff_value < 10)
        except Exception:
            LOGGER.info("Assert video is not None")
            assert actual_height is not None


def assert_file_download_exist(download_folder_path, file_size=2.00, start_with=None):
    LOGGER.info("Verify video title same as: " + str(start_with))
    import os
    mp4_files = find_mp4_file_download(download_folder_path, '.mp4', start_with=start_with)
    file_path = download_folder_path + '\\' + mp4_files[0]
    vid = cv2.VideoCapture(file_path)
    size_file = round(os.stat(file_path).st_size / (1024 * 1024), 2)
    video_is_opened = vid.isOpened()
    vid.release()
    assert video_is_opened is True
    assert len(mp4_files) > 0
    assert size_file > file_size


def check_if_the_file_fully_downloaded(browser):
    browser.get(Urls.COCCOC_DOWNLOAD_URL)
    assert download_page_object.verify_play_button_existed(browser) == 1


def check_if_file_with_title_fully_downloaded(browser, video_title):
    LOGGER.info("Video is downloading")
    play_button_by_video_title = savior_element.find_play_button_by_video_title(browser, video_title)
    start_time = datetime.now()
    if play_button_by_video_title is None:
        while play_button_by_video_title is None:
            time.sleep(2)
            play_button_by_video_title = savior_element.find_play_button_by_video_title(browser, video_title)
            # LOGGER.info("Play button after timeout: " + str(play_button_by_video_title))
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 10000:
                break


def open_coccoc_download_then_check_if_the_file_fully_downloaded(browser, video_title):
    browser.get(Urls.COCCOC_DOWNLOAD_URL)
    if isinstance(video_title, list):
        for title in video_title:
            check_if_file_with_title_fully_downloaded(browser, title)
    else:
        check_if_file_with_title_fully_downloaded(browser, video_title)


def pause_any_video_youtube(browser):
    browser.get(VideoUrls.YOUTUBE_VIDEO_URL)
    WaitAfterEach.sleep_timer_after_each_step()
    youtube_page_object.mouse_over_video_item(browser)
    youtube_page_object.click_video_item(browser)


def get_downloaded_folder_setting(browser, setting_page_object):
    browser.get(Urls.COCCOC_SETTINGS_URL)
    return setting_page_object.get_download_folder()


def navigate_savior_details(browser):
    browser.get(Urls.COCCOC_EXTENSIONS)
    extension_page_object.savior_extension_is_displayed(browser)
    extension_page_object.savior_extension_detail_is_clicked(browser)


def check_instant_download(browser, text):
    browser.get(u'chrome-extension://' + text + u'/options.html')
    savior_extension.choose_show_instant_download_youtube(browser)
    # self.savior_extension.choose_save_and_close_button(browser)


def not_found_download_button_in_page(browser):
    pause_any_video_youtube(browser)
    WaitAfterEach.sleep_timer_after_each_step()
    savior_page_object.not_found_download_button(browser)


def choose_video_quality_medium_option(browser):
    browser.get(u'chrome-extension://' + ExtensionIds.SAVIOR_EXTENSION_ID + u'/options.html')
    savior_extension.choose_video_quality_medium(browser)
    WaitAfterEach.sleep_timer_after_each_step()


def choose_video_quality_low_option(browser):
    browser.get(u'chrome-extension://' + ExtensionIds.SAVIOR_EXTENSION_ID + u'/options.html')
    savior_extension.choose_video_quality_low(browser)
    WaitAfterEach.sleep_timer_after_each_step()


def pause_or_play_video_by_javascript(browser, css_locator, action='play'):
    if 'play' in action:
        browser.execute_script("document.querySelector('"+css_locator+"').play()")
    else:
        browser.execute_script("document.querySelector('" + css_locator + "').pause()")
    time.sleep(3)


def pause_any_video_site(browser, url):
    LOGGER.info("Open " + url)
    browser.get(url)
    any_site_page_object.click_first_video_element(browser)
    any_site_page_object.mouse_over_first_video_element(browser)


def implement_download_file(browser, get_current_download_folder, time_sleep=5, **kwargs):
    download_file_via_main_download_button(browser, time_sleep=time_sleep)
    # assert file download exist and can be opened
    assert_file_download_exist(get_current_download_folder, **kwargs)


def clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder):
    clear_data_download(browser)
    delete_all_mp4_file_download(get_current_download_folder, '.mp4')


def verify_download_quality_high_frame(browser, get_current_download_folder, prepare_savior_option_displayed, ):
    download_file_via_main_download_button(browser, )
    prepare_savior_option_displayed(browser)
    savior_page_object.choose_preferred_option(browser)
    height_frame = savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
    # File mp4 file and assert
    assert_file_download_value(get_current_download_folder, height_frame)


def handle_windows_watch_option(browser, close_popup_continue_watching):
    WaitAfterEach.sleep_timer_after_each_step()
    list_windows = browser.window_handles
    if len(list_windows) > 2:
        browser.switch_to.window(list_windows[0])
        close_popup_continue_watching(browser)
    else:
        LOGGER.info("Does not have pop up continue watching")


def get_resolution_info(media_info):
    import re
    m = re.search('\\d+p', media_info)
    if m is not None:
        m = m.group()
    else:
        m = ''
    LOGGER.info("Get expect height: " + str(m))
    return m
