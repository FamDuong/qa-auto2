import time
import pytest
import win32clipboard
from pytest_testrail.plugin import pytestrail
from models.pageobject.downloads import DownloadsPageObject, ThePirateBayPageObject, PirateBaySearchResult
from utils.const import Urls


class TestTorrentDownload:

    # @pytest.fixture(scope='session')
    # def clear_data_torrent_download(self, browser):
    #     browser.get(Urls.COCCOC_DOWNLOAD_URL)
    #     def cancel_download_process():


    download_page_object = DownloadsPageObject()

    pirate_bay_object = ThePirateBayPageObject()

    pirate_bay_search_result = PirateBaySearchResult()

    def prepare_torrent_running(self, browser):
        browser.get('https://www.thepiratebay.org/')
        self.pirate_bay_object.search_torrent_to_download(browser, "Python")

        self.pirate_bay_search_result.click_download_magnet_value(browser)

    @pytest.mark.skip
    def test_download_fromt_torrent_link(self, browser):
        browser.get('https://fileslicious.tf/justcause4cpy')
        time.sleep(3)

    @pytest.mark.skip
    def test_download_from_torrent_file(self, browser):
        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.click_add_torrent(browser)
        # self.upload_file("D:\\Automation Test Coc Coc\\qa-auto\\qa-auto\\testdata\\torrent_file.torrent")
        time.sleep(3)

    @pytestrail.case('C44975')
    def test_pause_resume_torrent_download(self, browser):
        browser.get('https://fileslicious.tf/justcause4cpy')
        time.sleep(3)
        # browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.click_pause_torrent_download_current(browser)
        self.download_page_object.click_resume_torrent_download_current(browser)
        self.download_page_object.click_cancel_torrent_download_current(browser)
        self.download_page_object.click_remove_torrent_download_current(browser)
        time.sleep(2)

    @pytestrail.case('C44976')
    def test_download_from_magnet_link(self, browser):
        browser.get('https://www.thepiratebay.org/')
        self.pirate_bay_object.search_torrent_to_download(browser, "Python")

        self.pirate_bay_search_result.click_download_magnet_value(browser)

        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.click_cancel_torrent_download_current(browser)
        self.download_page_object.click_remove_torrent_download_current(browser)
        time.sleep(2)

    @pytestrail.case('C54211')
    def test_copy_magnet_link(self, browser):
        """
        Prepare data for copy magnet link
        :param browser:
        :return:
        """
        # Prepare torrent running file
        self.prepare_torrent_running(browser)

        # Go to download page
        browser.get(Urls.COCCOC_DOWNLOAD_URL)

        # Copy url for torrent

        self.download_page_object.click_more_icon_button(browser)
        self.download_page_object.click_copy_settings_button(browser)

        # Stop and remove torrent
        self.download_page_object.click_cancel_torrent_download_current(browser)
        self.download_page_object.click_remove_torrent_download_current(browser)

        # Get magnet link from clipboard
        win32clipboard.OpenClipboard()
        magnet_link = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        print('Magnet link is:', magnet_link)

        # Download torrent from magnet link
        browser.get(magnet_link)

        # Remove torrent
        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.click_cancel_torrent_download_current(browser)
        self.download_page_object.click_remove_torrent_download_current(browser)

        time.sleep(2)

    @pytestrail.case('C54212')
    def test_torrent_download_tree_view(self, browser):
        """

        :param browser:
        :return:
        """
        # Prepare torrent running file
        self.prepare_torrent_running(browser)

        # Go to download page
        browser.get(Urls.COCCOC_DOWNLOAD_URL)

        # Verify tree view button
        self.download_page_object.click_tree_view_button(browser)

        self.download_page_object.verify_torrent_info_displayed(browser)
        time.sleep(2)













