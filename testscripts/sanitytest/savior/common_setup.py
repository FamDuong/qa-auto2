import time

from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject, \
    SaviorExtensionOptionsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import YoutubePageObject, GooglePageObject
from utils_automation.const import Urls
from utils_automation.setup import Browser

extension_page_object = ExtensionsPageObject()

extension_detail_page_object = ExtensionsDetailsPageObject()
youtube_page_object = YoutubePageObject()
savior_page_object = SaviorPageObject()

browser_incognito = Browser()
savior_extension = SaviorExtensionOptionsPageObject()
google_page_object = GooglePageObject()

download_page_object = DownloadsPageObject()


def pause_any_video_youtube(browser):
    text_in_video = 'DDU-DU'
    browser.get(Urls.YOUTUBE_URL)
    time.sleep(2)
    youtube_page_object.search_video_item(browser, text_in_video)
    time.sleep(3)
    youtube_video_link = youtube_page_object.choose_any_video_item(browser,text_in_video)
    browser.get(youtube_video_link)
    time.sleep(2)
    youtube_page_object.mouse_over_video_item(browser)
    time.sleep(2)
    youtube_page_object.click_video_item(browser)
    time.sleep(2)


def get_downloaded_folder_setting(browser,setting_page_object):
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
    time.sleep(2)
    savior_page_object.not_found_download_button(browser)


def get_text_extension_option(browser):
    navigate_savior_details(browser)
    time.sleep(1)
    extension_detail_page_object.open_extension_options_view(browser)
    time.sleep(1)
    return savior_extension.get_show_instant_download_youtube_value(browser)


def revert_high_quality_default_option(browser):
    text = get_text_extension_option(browser)
    browser.get(u'chrome-extension://' + text + u'/options.html')
    savior_extension.choose_video_quality_high(browser)
    time.sleep(1)
