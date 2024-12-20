from selenium.webdriver.common.by import By


class DownloadsPageLocators:

    ADD_TORRENT_CLASS_TEXT = '[class="js-addTorrent torrentButton headerButton"]'
    PAUSE_TORRENT_CLASS_TEXT = '[class="js-pause pause-btn"]'
    RESUME_TORRENT_CLASS_TEXT = '[class="js-resume resume-btn"]'
    CANCEL_TORRENT_CLASS_TEXT = '[class="js-cancel cancel-btn"]'
    CANCEL_TORRENT_BTN = '//button[@class="js-cancel cancel-btn"]'
    REMOVE_TORRENT_FROM_LIST_TEXT = '[class="js-removeFromList removeFromList-btn"]'
    MORE_ICON_BTN = (By.XPATH, '//span[@class="more-icon"]')
    REMOVE_FILE_FROM_DISK = (By.XPATH, '//li[@class="js-removeFromDisk"]')
    DO_NOT_SEED_BTN = (By.XPATH, '//label[span="Do not seed"]')
    COPY_LINK_BTN = (By.XPATH, '//li[@class="js-copyMagnet"]')
    TORRENT_TREE_VIEW_BTN = (By.XPATH, '//span[@class="download-item-info-icon has-files"]')
    TORRENT_CHECK_ICON = (By.XPATH, '//span[@class="check-icon"]')
    TORRENT_FILE_NAME = (By.XPATH, '//span[@class="input-wrapper"]')
    TORRENT_FILE_SIZE = (By.XPATH, '//span[@class="fileSize"]/span[@class="fileSizePlace"]')
    TORRENT_FILE_PROGRESS = (By.XPATH, '//span[@class="fileSize"]/span[@class="progress"]')
    TORRENT_SEED_UP_ARROW = (By.XPATH, '//span[@class="statusText-up"]')
    TORRENT_SEED_UP_ARROW_TXT = '//span[@class="statusText-up"]'
    TORRENT_CONTROL_BOTTOM_ITEM = (By.XPATH, '//div[@class="controls control-bottom"]')
    TORRENT_STOP_SEEDING_BTN = (By.XPATH, '//button[@class="js-stopSeeding stopSeeding-btn"]')
    CLEAR_ALL_BTN = (By.XPATH, '//button[@title="Clear all"]')
    PLAY_BTN = '//span[@class="download-item-info-icon"]'
    ELEMENTS_NOT_DELETED = '//h6[@class=""]//a[@title] | //span[@title]'
    PLAY_BUTTON_BY_VIDEO_TITLE = '//a[starts-with(@title,"{param1}")]//ancestor::div[@class="download-right-content"]//button[@class="js-play play-btn"] | //a[starts-with(@title,"{param1}")]//ancestor::div[@class="download-right-content"]//button[@class="js-showInFolder showInFolder-btn"]'
    VIDEO = '//a[starts-with(@title,'')]'
    BADGE_BTN_INTERRUPTED = '//span[@class="badge badge-btn"][text()="Interrupted"]'
    STATUS_TEXT_IS_DANGEROUS = '//span[@class="statusText-isDangerous"]'


class ThePirateBayLocators(object):
    SEARCH_FIELD = (By.XPATH, '//p[@id="inp"]/input[@name="q"]')
    SEARCH_BTN = (By.XPATH, '//p[@id="subm"]/input[@value="Pirate Search"]')


class PythonSearchResult:
    SEARCH_RESULT_HREF = (By.XPATH, '//a[@title="Download this torrent using magnet"]')
