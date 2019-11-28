from pytest_testrail.plugin import pytestrail
from models.pageobject.downloads import DownloadsPageObject
from utils_automation.common import FilesHandle
from utils_automation.const import Urls
from utils_automation.setup import WaitAfterEach


class TestTorrentSeeding:
    files_handle = FilesHandle()

    magnet_url_torrent = 'magnet:?xt=urn:btih:e1eed9d6a62423ecde25aa19765293a222780fce&dn=' \
                         'Deep+Learning+with+Python+-A+Hands-on+Introduction+%282017%29+Gooner&tr=udp%3A%2F%2Ftracker' \
                         '.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.openbittorrent' \
                         '.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker' \
                         '.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969'
    download_page_object = DownloadsPageObject()

    def set_up_finished_torrent(self, browser):
        browser.get(self.magnet_url_torrent)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        browser.get(Urls.COCCOC_DOWNLOAD_URL)

    @pytestrail.case('C54215')
    def test_seeding_state(self, browser, clear_download_data, get_current_download_folder):
        self.files_handle.clear_downloaded_folder(get_current_download_folder)
        self.set_up_finished_torrent(browser)
        self.download_page_object.verify_torrent_seed_up_arrow(browser)
        WaitAfterEach.sleep_timer_after_each_step()
        self.files_handle.clear_downloaded_folder(get_current_download_folder)

    @pytestrail.case('C54217')
    def test_set_to_not_seeding_one_torrent(self, browser, clear_download_data, get_current_download_folder):
        self.files_handle.clear_downloaded_folder(get_current_download_folder)
        self.set_up_finished_torrent(browser)
        self.download_page_object.verify_torrent_seed_up_arrow(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        self.download_page_object.stop_seeding_from_out_side_btn(browser)
        # Verify the up button is not displayed
        WaitAfterEach.sleep_timer_after_each_step()
        self.download_page_object.verify_torrent_seed_up_arrow_not_displayed(browser)
        # self.download_page_object.click_remove_torrent_download_current(browser)
        self.files_handle.clear_downloaded_folder(get_current_download_folder)






