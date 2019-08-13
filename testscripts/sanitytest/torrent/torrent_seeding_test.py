import time

import pytest
from pytest_testrail.plugin import pytestrail
from selenium.webdriver.common.keys import Keys

from models.pageobject.downloads import DownloadsPageObject
from utils_automation.const import Urls
from appium import webdriver


# @pytest.fixture(scope='function', autouse=True)
# def clear_download_data(browser):
#     browser.get(Urls.COCCOC_DOWNLOAD_URL)
#     from models.pageobject.downloads import DownloadsPageObject
#     download_page_object = DownloadsPageObject()
#     download_page_object.cancel_all_current_torrent(browser)
#     download_page_object.clear_all_existed_torrent(browser)
#     time.sleep(2)


class TestTorrentSeeding:

    magnet_url_torrent = 'magnet:?xt=urn:btih:e1eed9d6a62423ecde25aa19765293a222780fce&dn=' \
                         'Deep+Learning+with+Python+-A+Hands-on+Introduction+%282017%29+Gooner&tr=udp%3A%2F%2Ftracker' \
                         '.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.openbittorrent' \
                         '.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker' \
                         '.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969'
    download_page_object = DownloadsPageObject()

    def set_up_finished_torrent(self,browser):
        browser.get(self.magnet_url_torrent)
        time.sleep(2)
        browser.get(Urls.COCCOC_DOWNLOAD_URL)

    @pytestrail.case('C54215')
    def test_seeding_state(self, browser, clear_download_data):
        self.set_up_finished_torrent(browser)
        self.download_page_object.verify_torrent_seed_up_arrow(browser)
        time.sleep(2)

    @pytestrail.case('C54217')
    def test_set_to_not_seeding_one_torrent(self, browser, clear_download_data, param):
        self.set_up_finished_torrent(browser)
        time.sleep(2)
        self.download_page_object.verify_torrent_seed_up_arrow(browser)
        time.sleep(2)

        self.download_page_object.stop_seeding_from_out_side_btn(browser)

        # Verify the up button is not displayed
        time.sleep(2)
        self.download_page_object.verify_torrent_seed_up_arrow_not_displayed(browser)
        # self.download_page_object.click_remove_torrent_download_current(browser)
        time.sleep(2)

    # def test_hard(self, browser):
    #     browser.get(Urls.COCCOC_DOWNLOAD_URL)
    #     self.download_page_object.click_more_icon_button(browser)
    #     self.download_page_object.do_not_seed_action(browser)
    #     time.sleep(2)
    #     self.download_page_object.verify_torrent_seed_up_arrow_not_displayed(browser)
    #     self.download_page_object.click_remove_torrent_download_current(browser)





