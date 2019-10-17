from selenium.webdriver.common.by import By


class SaviorPageLocators(object):
    DOWNLOAD_BUTTON = '#download-main'
    FIRST_LAYER = '[style="position: absolute; top: 0px;"]'
    PREFERRED_SELECT_BTN = '[id="preferred-select"]'
    BASE_OVERLAY_CLASS = '[class="base overlay"]'
    HIGH_PREFERRED_SELECT_BTN = '//span[@data-selected-value="High"]'
    MEDIUM_SELECT_OPTION = '[data-quality-value="mp4/Medium/360p"]'
    LOW_SELECT_OPTION = '[data-quality-value="mp4/Small/240p"]'
    HIGH_SELECT_OPTION = '[data-quality-value="mp4/HD/720p"]'
    MOBILE_SHARING_VIDEO_RADIO_BUTTON = 'input[id="switch-video"]'

    MOBILE_SHARING_BUTTON = '#open-mobile'
    GOOGLE_PLAY_BUTTON = '#google-play'
    APP_STORE_BUTTON = '#app-store'
    MOBILE_FOOTER_CONTENT_PART = '[class="mobile-content mobile-footer"]'
    INSTRUCTION_IMAGE_PART = 'img[class="instruction-image"]'
    QR_CODE_PART = '[class="qrcode"]'

    LOW_FILE_DOWNLOAD_BUTTON = 'a[class="download-btn j-quality-download"][data-quality="mp4/Small/240p"]'
    MEDIUM_FILE_DOWNLOAD_BUTTON = 'a[class="download-btn j-quality-download"][data-quality="mp4/Medium/360p"]'
    HIGH_FILE_DOWNLOAD_BUTTON = 'a[class="download-btn j-quality-download"][data-quality="mp4/HD/720p"]'

    SUBTITLE_ALL_SELECTOR = 'div[data-quality-value*="yt_srt"]'

    CLASS_WRAPPER_VIDEO_OPTIONS = '[class*="quality-selector-box j-quality-selector ps"] > [class="extension-box"]'
    ALL_VIDEO_OPTIONS_AVAILABLE = '[data-quality-value]:not([data-quality-value=""])'

    CURRENT_VIDEO_QUALITY_ITEM = '[class*="quality-selector-box j-quality-selector ps"]'

    CURRENT_VIDEO_QUALITY_SELECTED_ITEM = '[class="quality-label j-quality selected"]'
    CURRENT_VIDEO_FILE_SIZE_ITEM = '[class="media-sub-info j-checked-size'

    @staticmethod
    def download_option_css_locator(title):
        return 'a[title*="%s"]' % title


