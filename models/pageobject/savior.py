import time
import re
import logging
from datetime import datetime

from selenium.common.exceptions import JavascriptException

from models.pageelements.basepage_elements import BasePageElement
from models.pageelements.savior import SaviorElements
from models.pagelocators.savior import SaviorPageLocators
from models.pageobject.basepage_object import BasePageObject
from utils_automation.setup import WaitAfterEach

LOGGER = logging.getLogger(__name__)


class SaviorPageObject(BasePageObject):
    savior_elements = SaviorElements()
    base_page_element = BasePageElement()
    script = 'document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).click();'
    script_find = 'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])' \
                  '.getAttribute("data-quality")'
    script_textContent = 'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).' \
                         'textContent'

    def download_button_is_displayed(self, driver):
        self.savior_elements.find_download_button(driver)

    def not_found_download_button(self, driver):
        self.savior_elements.not_found_download_button(driver)

    def choose_preferred_option(self, driver):
        try:
            time.sleep(2)
            # preferred_option = self.savior_elements.find_preferred_option(driver)
            # preferred_option.click()
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFERRED_SELECT_BTN)
        except JavascriptException:
            preferred_option = self.savior_elements.find_preferred_option(driver)
            start_time = datetime.now()
            if preferred_option is None:
                while preferred_option is None:
                    time.sleep(2)
                    preferred_option = self.savior_elements.find_preferred_option(driver)
                    # preferred_option.click()
                    driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER,
                                          SaviorPageLocators.PREFERRED_SELECT_BTN)

                    time_delta = datetime.now() - start_time
                    if time_delta.total_seconds() >= 15:
                        break

    def choose_quad_hd_option(self, driver):
        try:
            LOGGER.info("Select Quad HD option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.QUAD_HD_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.QUAD_HD_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Quad HD option")
            LOGGER.info(e)
            return e

    def choose_full_hd_option(self, driver):
        try:
            LOGGER.info("Select Full HD option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.FULL_HD_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.FULL_HD_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Full HD option")
            LOGGER.info(e)
            return e

    def choose_hd_option(self, driver):
        try:
            LOGGER.info("Select HD option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.HD_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.HD_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select HD option")
            LOGGER.info(e)
            return e

    def choose_standard_option(self, driver):
        try:
            LOGGER.info("Select Standard option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.STANDARD_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.STANDARD_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Standard option")
            LOGGER.info(e)
            return e

    def choose_medium_option(self, driver):
        try:
            LOGGER.info("Select Medium option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MEDIUM_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.MEDIUM_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Medium option")
            LOGGER.info(e)
            return e

    def choose_small_option(self, driver):
        try:
            LOGGER.info("Select Small option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.SMALL_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.SMALL_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Small option")
            LOGGER.info(e)
            return e

    def choose_mobile_option(self, driver):
        try:
            LOGGER.info("Select Mobile option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.MOBILE_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Mobile option")
            LOGGER.info(e)
            return e

    def choose_original_option(self, driver):
        try:
            LOGGER.info("Select Original option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.ORIGINAL_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.ORIGINAL_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Original option")
            LOGGER.info(e)
            return e

    def choose_mp3_standard_option(self, driver):
        try:
            LOGGER.info("Select Mp3 Standard option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MP3_STANDARD_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.MP3_STANDARD_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select Mp3 Standard option")
            return e

    def choose_mp3_medium_option(self, driver):
        try:
            LOGGER.info("Select mp3 Medium option")
            driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MP3_MEDIUM_SELECT_OPTION)
            # option = self.savior_elements.find_resotion_option_by_css_selector(driver,
            #                                                                    SaviorPageLocators.MP3_MEDIUM_SELECT_OPTION)
            # option.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            LOGGER.info("Failed to select mp3 Medium option")
            return e

    def assert_value_preferred_quality(self, driver, assert_text):
        preferred_element = driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"data-selected-value")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFERRED_SELECT_BTN)
        assert preferred_element == assert_text

    def download_file_via_savior_download_btn(self, driver):
        choose_resolution_status = self.savior_elements.get_savior_wigdet_choose_resolution_status(driver)
        if 'Error' in choose_resolution_status:
            LOGGER.info("Error when choose resolution!")
        assert 'Error' not in choose_resolution_status
        start_time = datetime.now()
        if self.savior_elements.find_download_button(driver) is None:
            while self.savior_elements.find_download_button(driver) is None:
                time.sleep(1)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 10:
                    break
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.DOWNLOAD_BUTTON)

    def current_media_info(self, driver):
        media_info = driver.execute_script(self.script_find, SaviorPageLocators.FIRST_LAYER,
                                           SaviorPageLocators.CURRENT_SELECTED_RESOLUTION)
        LOGGER.info("Media info: " + media_info)
        return media_info

    def download_file_title_via_savior_download_btn(self, driver, title):
        i = 0
        while i == 0:
            if driver.execute_script(self.script_find, SaviorPageLocators.FIRST_LAYER,
                                     SaviorPageLocators.download_option_css_locator(title)) is not None:
                driver.execute_script(
                    self.script,
                    SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.download_option_css_locator(title))
                i += 1

    def download_file_medium_quality(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MEDIUM_FILE_DOWNLOAD_BUTTON)

    def download_file_high_quality(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.HIGH_FILE_DOWNLOAD_BUTTON)

    def download_file_low_quality(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.LOW_FILE_DOWNLOAD_BUTTON)

    def verify_mobile_sharing_button_displayed(self, driver):
        return driver.execute_script(
            self.script_textContent,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SHARING_BUTTON)

    def choose_mobile_sharing_button(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SHARING_BUTTON)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()

    def verify_if_video_is_focused(self, driver):
        return driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"checked")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SHARING_VIDEO_RADIO_BUTTON)

    def verify_instruction_image_part_displayed(self, driver):
        return driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"src")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.INSTRUCTION_IMAGE_PART)

    def verify_qr_code_image_part_displayed(self, driver):
        return driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])'
            '.firstElementChild.getAttribute("src")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.QR_CODE_PART)

    def verify_mobile_footer_content_part_displayed(self, driver):
        return driver.execute_script(
            self.script_textContent,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_FOOTER_CONTENT_PART)

    def choose_google_play_button(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.GOOGLE_PLAY_BUTTON)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()

    def choose_app_store_button(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.APP_STORE_BUTTON)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()

    def verify_all_subtitles_displayed(self, driver, *assert_language_sub):
        list_elements = self.savior_elements.find_all_subtitles(driver)
        assert len(list_elements) == len(assert_language_sub)

    def get_quality_video_options_available(self, driver):
        global video_quality_height_frame_value
        all_video_options = self.savior_elements.find_all_video_options(driver)
        text_content_list = []
        len_options = len(all_video_options)
        current_video_quality = self.savior_elements.get_current_video_quality_value(driver)
        # Extract video quality height frame value
        m = re.search('\\d+p', current_video_quality)
        if m:
            video_quality_height_frame_value = m.group()
        else:
            video_quality_height_frame_value = ''
        for i in range(len_options):
            text_content_list.append((self.savior_elements.
                                      get_each_quality_info_video_options(driver, i)))
        return len_options, text_content_list, current_video_quality, video_quality_height_frame_value

    def verify_correct_video_options_chosen_high_quality_option(self, driver):
        len_options, text_content_list, current_video_quality, video_quality_height = self. \
            get_quality_video_options_available(driver)

        if len_options >= 3:
            if 'HD' in text_content_list:
                assert 'HD' in current_video_quality
            else:
                assert 'Standard' or 'Medium' in current_video_quality
        elif len_options == 2:
            if ('Standard' or 'Medium') in text_content_list:
                assert ('Standard' or 'Medium') in current_video_quality
        elif len_options == 1:
            LOGGER.info('Current video quality for len == 1 is:', self.savior_elements.
                        get_current_video_quality_value(driver))
            assert current_video_quality is not None
        else:
            raise Exception.__traceback__
        return video_quality_height

    # Currently there is no specific requirement about file size => no need to assert this
    def verify_current_file_size_selected_not_null(self, driver):
        assert ('MB' or 'KB' or 'GB') in self.savior_elements.get_current_video_file_size(driver)

    def verify_correct_video_options_chosen_medium_quality_option(self, driver):
        len_options, text_content_list, current_video_quality, video_quality_height = \
            self.get_quality_video_options_available(driver)

        if len_options >= 3:
            if 'HD' in text_content_list:
                assert 'HD' not in current_video_quality
            else:
                assert 'Standard' or 'Medium' in current_video_quality
        elif len_options == 2:
            if ('Standard' and 'Medium') in text_content_list:
                assert 'Standard' in current_video_quality
        elif len_options == 1:
            LOGGER.info('Current video quality for len == 1 is:',
                        self.savior_elements.get_current_video_quality_value(driver))
            assert current_video_quality is not None
        else:
            raise Exception.__traceback__
        return video_quality_height

    def verify_correct_video_options_chosen_low_quality_option(self, driver):
        len_options, text_content_list, current_video_quality, video_quality_height = \
            self.get_quality_video_options_available(driver)

        if len_options >= 3:
            if 'HD' in text_content_list:
                assert 'HD' not in current_video_quality
            else:
                assert ('Small' in current_video_quality) or ('Mobile' in current_video_quality)
        elif len_options == 2:
            if 'Standard' and 'Medium' in text_content_list:
                assert 'Medium' in current_video_quality
            else:
                pass
        elif len_options == 1:
            LOGGER.info('Current video quality for len == 1 is:',
                        self.savior_elements.get_current_video_quality_value(driver))
            assert current_video_quality is not None
        else:
            raise Exception.__traceback__
        return video_quality_height

    def wait_until_finished_choose_resolution(self, driver):
        start_time = datetime.now()
        resolution_type = ""
        try:
            resolution_type = driver.execute_script(
                "return document.querySelector(\"" + SaviorPageLocators.FIRST_LAYER + "\").shadowRoot.querySelector(\""
                + SaviorPageLocators.SAVIOR_RESOLUTION_TYPE + "\").textContent")
        except Exception:
            time.sleep(5)
            resolution_type = driver.execute_script(
                "return document.querySelector(\"" + SaviorPageLocators.FIRST_LAYER
                + "\").shadowRoot.querySelector(\"" +
                SaviorPageLocators.SAVIOR_RESOLUTION_TYPE + "\").textContent")
            if resolution_type != 'Audio' or resolution_type != 'Video':
                while resolution_type != 'Audio' or resolution_type != 'Video':
                    time.sleep(2)
                    resolution_type = driver.execute_script(
                        "return document.querySelector(\"" + SaviorPageLocators.FIRST_LAYER
                        + "\").shadowRoot.querySelector(\"" +
                        SaviorPageLocators.SAVIOR_RESOLUTION_TYPE + "\").textContent")
                    time_delta = datetime.now() - start_time
                    if time_delta.total_seconds() >= 15 or resolution_type == 'Audio' or resolution_type == 'Video':
                        break
