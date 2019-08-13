import time

from utils_automation.const import Urls


def pause_any_video_youtube(browser, youtube_page_object):
    browser.get(Urls.YOUTUBE_URL)
    time.sleep(2)
    youtube_page_object.choose_any_video_item(browser)
    time.sleep(4)
    youtube_page_object.mouse_over_video_item(browser)
    youtube_page_object.click_video_item(browser)
    time.sleep(2)
