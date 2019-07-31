from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.downloads import DownloadsPageLocators, ThePirateBayLocators, PythonSearchResult


class DownloadsElement(BasePageElement):

    def find_add_torrent_element(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, DownloadsPageLocators.ADD_TORRENT_CLASS_TEXT)))

    def find_pause_torrent_download_element(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, DownloadsPageLocators.PAUSE_TORRENT_CLASS_TEXT)))

    def find_resume_torrent_download_element(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, DownloadsPageLocators.RESUME_TORRENT_CLASS_TEXT)))

    def find_cancel_torrent_download_element(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, DownloadsPageLocators.CANCEL_TORRENT_CLASS_TEXT)))

    def find_remove_torrent_download_element(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, DownloadsPageLocators.REMOVE_TORRENT_FROM_LIST_TEXT)))

    def find_more_icon(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.MORE_ICON_BTN))

    def find_copy_settings_btn(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.COPY_LINK_BTN))

    def find_tree_view_torrent_btn(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_TREE_VIEW_BTN))

    def is_torrent_check_icon_displayed(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_CHECK_ICON))

    def is_torrent_file_name_displayed(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_FILE_NAME))

    def is_torrent_file_size_displayed(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_FILE_SIZE))

    def is_torrent_file_progress_displayed(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_FILE_PROGRESS))

    def is_torrent_seed_arrow_up_displayed(self, driver):
        wait = WebDriverWait(driver, 90)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_SEED_UP_ARROW))

    def should_torrent_seed_arrow_up_not_displayed(self, driver):
        return driver.find_elements_by_xpath(DownloadsPageLocators.TORRENT_SEED_UP_ARROW_TXT)

    def find_stop_seeding_button_out_side_displayed(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.TORRENT_STOP_SEEDING_BTN))

    def find_do_not_seed_button(self,driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(DownloadsPageLocators.DO_NOT_SEED_BTN))


class ThePirateBayElements(BasePageElement):

    def find_search_torrent_field(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(ThePirateBayLocators.SEARCH_FIELD))

    def find_search_button(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(ThePirateBayLocators.SEARCH_BTN))


class PirateBaySearchResultElements(BasePageElement):
    def find_magnet_link(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(PythonSearchResult.SEARCH_RESULT_HREF))


