import time

from models.pageobject.sites import AnySitePageObject
from testscripts.common_setup import assert_file_download_value, delete_all_mp4_file_download, \
    download_file_via_main_download_button, get_resolution_info

any_site_page_object = AnySitePageObject()


def download_and_verify_video(browser, download_folder, video_title, mouse_over_first_video=True):
    if mouse_over_first_video:
        any_site_page_object.mouse_over_first_video_element(browser)
    media_info = download_file_via_main_download_button(browser, time_sleep=15)
    resolution_info = get_resolution_info(media_info)
    try:
        assert_file_download_value(download_folder, resolution_info, start_with=video_title)
    finally:
        delete_all_mp4_file_download(download_folder, '.mp4', startwith=video_title)
