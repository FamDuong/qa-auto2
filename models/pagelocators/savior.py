from selenium.webdriver.common.by import By


class SaviorPageLocators(object):
    DOWNLOAD_BUTTON = '#download-main'

    FIRST_LAYER = '[style="position: absolute; top: 0px;"]'

    PREFFERED_SELECT_BTN = '[id="preferred-select"]'
    BASE_OVERLAY_CLASS = '[class="base overlay"]'

    HIGH_PREFFERRED_SELECT_BTN = '//span[@data-selected-value="High"]'

    MEDIUM_SELECT_OPTION = '[data-quality-value="mp4/Medium/360p"]'
