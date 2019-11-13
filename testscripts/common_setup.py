import cv2
from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject, \
    SaviorExtensionOptionsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import YoutubePageObject, GooglePageObject, AnySitePageObject
from utils_automation.cleanup import Files
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


def delete_all_mp4_file_download(mydir, endwith):
    files = Files()
    files.delete_files_in_folder(mydir, endwith)


def download_file_via_main_download_button(browser):
    savior_page_object.download_file_via_savior_download_btn(browser)
    WaitAfterEach.sleep_timer_after_each_step_longer_load()
    media_info_element = savior_page_object.current_media_info(browser)

    # Check the file is fully downloaded
    check_if_the_file_fully_downloaded(browser)
    return media_info_element


def find_mp4_file_download(mydir, endwith):
    files_handle = FilesHandle()
    return files_handle.find_files_in_folder_by_modified_date(mydir, endwith)


def clear_data_download(driver):
    driver.get(Urls.COCCOC_DOWNLOAD_URL)
    WaitAfterEach.sleep_timer_after_each_step()
    download_page_object.clear_all_existed_downloads(driver)
    WaitAfterEach.sleep_timer_after_each_step()


def assert_file_download_value(download_folder_path, height_value):
    mp4_files = find_mp4_file_download(download_folder_path, '.mp4')
    print(mp4_files)
    vid = cv2.VideoCapture(download_folder_path + '\\' + mp4_files[0])
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    assert vid.isOpened()
    if int(height) > 720:
        assert width == if_height_frame_so_width_frame(height)
    vid.release()
    if (height_value is not None) and (height_value != ''):
        assert (str(int(height)) in height_value or abs(int(height) - int(height_value.split('p')[0])) < 10)
    else:
        assert height is not None


def assert_file_download_exist(download_folder_path):
    mp4_files = find_mp4_file_download(download_folder_path, '.mp4')
    vid = cv2.VideoCapture(download_folder_path + '\\' + mp4_files[0])
    assert vid.isOpened()
    assert len(mp4_files) > 0


def check_if_the_file_fully_downloaded(browser):
    browser.get(Urls.COCCOC_DOWNLOAD_URL)
    assert download_page_object.verify_play_button_existed(browser) == 1


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


def pause_any_video_site(browser, url):
    browser.get(url)
    any_site_page_object.click_first_video_element(browser)
    any_site_page_object.mouse_over_first_video_element(browser)


def implement_download_file(browser, get_current_download_folder):
    delete_all_mp4_file_download(get_current_download_folder, '.mp4')
    download_file_via_main_download_button(browser)
    # assert file download exist and can be opened
    assert_file_download_exist(get_current_download_folder)


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
    if len(list_windows) >= 2:
        browser.switch_to.window(list_windows[0])
        close_popup_continue_watching
    else:
        close_popup_continue_watching


def get_resolution_info(media_info):
    import re
    m = re.search('\\d+p', media_info)
    if m is not None:
        m = m.group()
    else:
        m = ''
    return m

