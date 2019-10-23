from datetime import datetime

from selenium.webdriver import ActionChains

from models.pageelements.downloads import DownloadsElement, ThePirateBayElements, PirateBaySearchResultElements
from models.pageobject.basepage_object import BasePageObject
from utils_automation.setup import WaitAfterEach


class DownloadsPageObject(BasePageObject):
    downloads_elem = DownloadsElement()

    def click_add_torrent(self, driver):
        add_torrent_btn = self.downloads_elem.find_add_torrent_element(driver)
        add_torrent_btn.click()
        # driver.switch_to().active_element().send_keys(os.getcwd()+"/torrent_file.torrent")
        # add_torrent_btn.send_keys(os.getcwd()+"/torrent_file.torrent")

    def click_pause_torrent_download_current(self, driver):
        pause_torrent_btn = self.downloads_elem.find_pause_torrent_download_element(driver)
        pause_torrent_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_resume_torrent_download_current(self, driver):
        resume_torrent_btn = self.downloads_elem.find_resume_torrent_download_element(driver)
        resume_torrent_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_cancel_torrent_download_current(self, driver):
        cancel_torrent_btn = self.downloads_elem.find_cancel_torrent_download_element(driver)
        cancel_torrent_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_remove_torrent_download_current(self, driver):
        remove_torrent_btn = self.downloads_elem.find_remove_torrent_download_element(driver)
        remove_torrent_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_more_icon_button(self, driver):
        more_icon_btn = self.downloads_elem.find_more_icon(driver)
        more_icon_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def remove_file_from_disk(self, driver):
        self.click_more_icon_button(driver)
        self.downloads_elem.find_remove_from_disk(driver).click()
        WaitAfterEach.sleep_timer_after_each_step()

    def hover_more_icon_button(self, driver):
        more_icon_btn = self.downloads_elem.find_more_icon(driver)
        hover = ActionChains(driver).move_to_element(more_icon_btn)
        hover.perform()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_copy_settings_button(self, driver):
        copy_settings_btn = self.downloads_elem.find_copy_settings_btn(driver)
        copy_settings_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_tree_view_button(self, driver):
        tree_view_btn = self.downloads_elem.find_tree_view_torrent_btn(driver)
        tree_view_btn.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def verify_torrent_info_displayed(self, driver):
        self.downloads_elem.is_torrent_check_icon_displayed(driver)
        self.downloads_elem.is_torrent_file_name_displayed(driver)
        self.downloads_elem.is_torrent_file_size_displayed(driver)
        self.downloads_elem.is_torrent_file_progress_displayed(driver)

    def verify_torrent_seed_up_arrow(self, driver):
        self.downloads_elem.is_torrent_seed_arrow_up_displayed(driver)

    def stop_seeding_from_out_side_btn(self, driver):
        stop_seeding_btn = self.downloads_elem.find_stop_seeding_button_out_side_displayed(driver)
        stop_seeding_btn.click()

    def verify_torrent_seed_up_arrow_not_displayed(self, driver):
        elements = self.downloads_elem.should_torrent_seed_arrow_up_not_displayed(driver)
        assert len(elements) == 0

    def do_not_seed_action(self, driver):
        do_not_seed_btn = self.downloads_elem.find_do_not_seed_button(driver)
        do_not_seed_btn.click()

    def cancel_all_current_torrent(self, driver):
        elements = self.downloads_elem.find_all_cancel_current_torrent_btn(driver)
        if len(elements) > 0:
            for i in range(len(elements)):
                elements[i].click()
                WaitAfterEach.sleep_timer_after_each_step()
        print('Number of current running torrents :', len(elements))

    def verify_cancel_button_is_existed(self, driver):
        elements = self.downloads_elem.find_all_cancel_current_torrent_btn(driver)
        assert len(elements) > 0

    def clear_all_existed_downloads(self, driver):
        element = self.downloads_elem.find_clear_all_button(driver)
        WaitAfterEach.sleep_timer_after_each_step()
        element.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def verify_play_button_existed(self, driver):
        index = 0
        if (self.downloads_elem.find_more_icon(driver) is not None) \
                and (len(self.downloads_elem.find_elements_not_deleted(driver)) > 0):
            start_time = datetime.now()
            while (datetime.now() - start_time).total_seconds() < 2000:
                if len(self.downloads_elem.find_play_button(driver)) > 0:
                    index += 1
                    break
                elif len(self.downloads_elem.find_interrupted_elements(driver)) > 0:
                    break
            WaitAfterEach.sleep_timer_after_each_step()
            # assert ((datetime.now() - start_time).total_seconds() < 2000) and index == 1, 'Verify if play button exist'
        WaitAfterEach.sleep_timer_after_each_step()
        return index


class ThePirateBayPageObject(BasePageObject):

    piratebay_elem = ThePirateBayElements()

    def search_torrent_to_download(self, driver, text_search):
        search_field = self.piratebay_elem.find_search_torrent_field(driver)
        search_field.click()
        search_field.send_keys(text_search)

        search_button = self.piratebay_elem.find_search_button(driver)
        search_button.click()


class PirateBaySearchResult(BasePageObject):
    piratebay_result_elem = PirateBaySearchResultElements()

    def click_download_magnet_value(self, driver):
        magnet_item = self.piratebay_result_elem.find_magnet_link(driver)
        magnet_item.click()
