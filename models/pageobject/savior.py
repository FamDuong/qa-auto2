import time
import re

from models.pageelements.savior import SaviorElements
from models.pagelocators.savior import SaviorPageLocators
from models.pageobject.basepage_object import BasePageObject
from utils_automation.setup import WaitAfterEach


class SaviorPageObject(BasePageObject):
    savior_elements = SaviorElements()
    script = 'document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).click();'
    script_textContent = 'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).' \
                         'textContent'

    def download_button_is_displayed(self, driver):
        self.savior_elements.find_download_button(driver)

    def not_found_download_button(self, driver):
        self.savior_elements.not_found_download_button(driver)

    def choose_preferred_option(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFERRED_SELECT_BTN)
        WaitAfterEach.sleep_timer_after_each_step()

    def choose_medium_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MEDIUM_SELECT_OPTION)
        WaitAfterEach.sleep_timer_after_each_step()

    def choose_low_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.LOW_SELECT_OPTION)
        WaitAfterEach.sleep_timer_after_each_step()

    def choose_high_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.HIGH_SELECT_OPTION)
        WaitAfterEach.sleep_timer_after_each_step()

    def assert_value_preferred_quality(self, driver, assert_text):
        preferred_element = driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"data-selected-value")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFERRED_SELECT_BTN)
        assert preferred_element == assert_text

    def download_file_via_savior_download_btn(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.DOWNLOAD_BUTTON)

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
        len_options, text_content_list, current_video_quality, video_quality_height = self.\
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
            print('Current video quality for len == 1 is:', self.savior_elements.
                  get_current_video_quality_value(driver))
            assert current_video_quality is not None
        else:
            raise Exception.__traceback__
        return video_quality_height

    def verify_correct_video_options_chosen_medium_quality_option(self, driver):
        len_options, text_content_list, current_video_quality, video_quality_height = self.get_quality_video_options_available(driver)

        if len_options >= 3:
            if 'HD' in text_content_list:
                assert 'HD' not in current_video_quality
            else:
                assert 'Standard' or 'Medium' in current_video_quality
        elif len_options == 2:
            if ('Standard' and 'Medium') in text_content_list:
                assert 'Standard' in current_video_quality
        elif len_options == 1:
            print('Current video quality for len == 1 is:', self.savior_elements.
                  get_current_video_quality_value(driver))
            assert current_video_quality is not None
        else:
            raise Exception.__traceback__
        return video_quality_height

    def verify_correct_video_options_chosen_low_quality_option(self, driver):
        len_options, text_content_list, current_video_quality, video_quality_height = self.get_quality_video_options_available(driver)

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
            print('Current video quality for len == 1 is:', self.savior_elements.
                  get_current_video_quality_value(driver))
            assert current_video_quality is not None
        else:
            raise Exception.__traceback__
        return video_quality_height





