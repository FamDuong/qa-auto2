import os
import pytest
from pytest_testrail.plugin import pytestrail

from testscripts.darkmode_top_sites.common import click_dark_mode_enable_on_sites
from utils_automation.image_utils import ImageUtils
from utils_automation.file_utils import FileUtils
from utils_automation.url_utils import URLUtils
from utils_automation.common_utils import CommonUtils
from utils_automation.date_time_utils import get_current_timestamp
from utils_automation.const import Urls
from models.pageobject.settings import SettingsDarkmodePageObject
from config.credentials import SKYPE_GROUP_AUTOMATION_ID, SKYPE_GROUP_AUTOMATION_ID_1
from utils_automation.skype_utils import SkypeLocalUtils

import logging

LOGGER = logging.getLogger(__name__)


class TestBrowserDarkMode:
    darkmode = SettingsDarkmodePageObject()
    image = ImageUtils()
    file = FileUtils()
    urls = URLUtils()
    common = CommonUtils()
    skype = SkypeLocalUtils()
    file_list_websites = None
    file_list_websites_exception = None
    dirname = None
    capture_dirname = None
    file_list_websites_valid = None
    file_list_websites_invalid = None
    file_list_websites_result = None
    number_of_failed = 0
    darkmode_icon = None
    timestamp = None

    def pytest_namespace(self):
        return {'message': 0}

    def init_websites_extend(self):
        self.dirname, runname = os.path.split(os.path.abspath(__file__))
        self.file_list_websites = self.dirname + "\\test_data" + r"\list_websites.csv"
        # self.file_list_websites_exception = self.dirname + r"\list_websites_exception.csv"
        self.file_list_websites_extend = self.dirname + "\\test_data" + r"\list_websites_extend.csv"
        self.file_list_websites_valid = self.dirname + "\\test_data" + r"\list_websites_valid.csv"
        self.file_list_websites_invalid = self.dirname + "\\test_data" + r"\list_websites_invalid.csv"
        self.file.remove_file(self.file_list_websites_extend)
        self.file.remove_file(self.file_list_websites_valid)
        self.file.remove_file(self.file_list_websites_invalid)

    def init_dark_mode(self):
        self.timestamp = get_current_timestamp("%Y%m%d%H%M")
        self.dirname, runname = os.path.split(os.path.abspath(__file__))
        self.capture_dirname = self.dirname + r"\\" + self.timestamp
        self.file.create_empty_folder(self.capture_dirname)
        self.file_list_websites = self.dirname + r"\list_websites.csv"
        self.file_list_websites_exception = self.dirname + r"\list_websites_exception.csv"
        self.file_list_websites_extend = self.dirname + r"\list_websites_extend.csv"
        self.file_list_websites_result = self.capture_dirname + r"\list_websites_result.csv"
        self.darkmode_icon = self.dirname + r'\darkmode_icon.png'

    # Capture all images
    def get_fullpage_screenshot_dark_mode(self, browser, url, times=1):
        filename = url.replace('https://', '').replace(r'/', '').replace('.', '').replace('www', '')
        filename_website = "\\" + filename + str(times) + ".png"
        filename_website_full = self.capture_dirname + filename_website
        filename_screenshot = "\\" + filename + "_screenshot" + str(times) + ".png"
        filename_screenshot_full = self.capture_dirname + filename_screenshot
        self.image.get_fullpage_screenshot_screen(filename_screenshot_full)
        self.image.get_fullpage_screenshot_clipping(browser, self.capture_dirname, filename_website)
        return filename_website_full, filename_screenshot_full

    def switch_dark_mode_for_site(self, browser, url):
        self.urls.wait_for_page_to_load(browser, url)
        click_dark_mode_enable_on_sites()
        # self.darkmode.enable_dark_mode_for_site(browser)
        self.urls.wait_for_page_to_load(browser, url)

    # Verify image after finishing capture
    def verify_images(self, url, filename):
        image_website = filename[0]
        image_screenshot = filename[1]

        # Check if file is lightmode or darkmode
        dark_mode = self.image.find_subimage_in_image(image_screenshot, self.darkmode_icon)
        LOGGER.info("The websites is dark mode: %s" % str(dark_mode))
        dominant_color = self.image.get_dominant_color(image_website)
        result = self.image.compare_dominant_color_threshold(dominant_color, dark_mode)
        if not result:
            self.number_of_failed += 1
            self.skype.send_message_group_skype_with_image(SKYPE_GROUP_AUTOMATION_ID_1,
                                                           "Screenshot of Error domain: %s" % url, image_screenshot)
            self.skype.send_message_group_skype_with_image(SKYPE_GROUP_AUTOMATION_ID_1,
                                                           "Website of Error domain: %s" % url, image_website)
        image_result = image_website + ", " + str(result)
        return image_result

    def move_browser_to_other_position(self, browser):
        browser.set_window_position(1050, -645)
        browser.maximize_window()

    def is_url_exception(self, url):
        result = False
        urls_exception = self.file.get_from_csv(self.file_list_websites_exception)
        for url_2 in urls_exception:
            result = self.urls.is_same_domain(url, url_2)
            if result:
                break
        return result

    @pytestrail.case('')
    def test_create_websites_extend(self):
        self.init_websites_extend()
        number_sublinks = 1
        urls_all = self.file.get_from_csv(self.file_list_websites)

        # Separate valid and invalid links
        self.file.clear_content_file(self.file_list_websites_invalid)
        self.file.clear_content_file(self.file_list_websites_valid)
        self.file.clear_content_file(self.file_list_websites_extend)
        urls_not_live = self.urls.get_all_links_in_file_are_not_alive(self.file_list_websites)
        self.file.append_list_to_file(self.file_list_websites_invalid, urls_not_live)
        urls_live = self.common.remove_duplicate_elements_in_lists(urls_all, urls_not_live)
        self.file.append_list_to_file(self.file_list_websites_valid, urls_live)

        for url in urls_live:
            self.urls.get_all_website_links(url)
            self.file.append_to_file(self.file_list_websites_extend, url)
            if len(self.urls.internal_urls) != 0:
                sub_urls = self.urls.get_random_valid_links_same_domain(url, tuple(self.urls.internal_urls), number_sublinks)
                self.file.append_list_to_file(self.file_list_websites_extend, sub_urls)


    @pytestrail.case('')
    def test_desktop_dark_mode(self, get_enabled_dark_mode):
        self.init_dark_mode()
        # urls_all = self.file.get_from_csv(self.file_list_websites)
        browser = get_enabled_dark_mode

        # For internal PC, set to open browser on second monitor
        # self.move_browser_to_other_position(browser)

        # Using UISpy to define locator then mouse move => Need to improve
        self.darkmode.enable_dark_mode_in_setting_page(browser)
        self.urls.wait_for_page_to_load(browser, Urls.COCCOC_URL)

        # Get list of urls again
        urls_live = self.file.get_from_csv(self.file_list_websites_extend)
        # Capture imagespi
        for url in urls_live:
            LOGGER.info("Capture website: " + url)
            # self.switch_dark_mode_for_site(browser, url)
            self.urls.wait_for_page_to_load(browser, url)
            image_website_1, image_screenshot_1 = self.get_fullpage_screenshot_dark_mode(browser, url, times=1)
            # Capture second image
            # self.switch_dark_mode_for_site(browser, url)
            # image_website_2, image_screenshot_2 = self.get_fullpage_screenshot_dark_mode(browser, url, times=2)

            # list_images.add((image_website_1, image_screenshot_1))
            # list_images.add((image_website_2, image_screenshot_2))

            # images = (image_website_1, image_screenshot_1)
            # image_result = self.verify_images(url, images)
            # self.file.append_to_file(self.file_list_websites_result, image_result)

            # images = (image_website_2, image_screenshot_2)
            # image_result = self.verify_images(url, images)
            self.file.append_to_file(self.file_list_websites_result, image_result)
            self.file.remove_first_line_in_file(self.file_list_websites_extend)  # Remove url in file extend

        pytest.message = "Finished run dark mode capture test: \n" + str(self.number_of_failed) + "/" + str(
            len(urls_live) * 2) \
                         + " Failed / Total Images\nPlease check at: " + self.capture_dirname
        assert self.number_of_failed == 0
