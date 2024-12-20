from selenium.webdriver.common.by import By


class SaviorPageLocators(object):
    DOWNLOAD_BUTTON = "a:not([hidden])[class='download-btn j-quality-download']" #'#download-main'
    FIRST_LAYER = "[style='position: absolute; top: 0px;']"
    PREFERRED_SELECT_BTN = '#preferred-select'
    CURRENT_SELECTED_RESOLUTION = 'span:not([hidden])[class="j-quality-option quality-option"]'
    BASE_OVERLAY_CLASS = '[class="base overlay"]'
    HIGH_PREFERRED_SELECT_BTN = '//span[@data-selected-value="High"]'
    QUAD_HD_SELECT_OPTION = "div[data-quality-value*='/Quad HD/']"
    FULL_HD_SELECT_OPTION = "div[data-quality-value*='/Full HD/']"
    HD_SELECT_OPTION = "div[data-quality-value*='/HD/']"
    STANDARD_SELECT_OPTION = "div[data-quality-value*='/Standard/']"
    MEDIUM_SELECT_OPTION = "div[data-quality-value*='/Medium/']"
    SMALL_SELECT_OPTION = "div[data-quality-value*='/Small/']"
    MOBILE_SELECT_OPTION = "div[data-quality-value*='/Mobile/']"
    ORIGINAL_SELECT_OPTION = "div[data-quality-value*='/Original/']"
    MP3_STANDARD_SELECT_OPTION = "div[data-quality-value*='mp3/Standard/']"
    MP3_MEDIUM_SELECT_OPTION = "div[data-quality-value*='mp3/Medium/']"
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
    SAVIOR_RESOLUTION_TYPE = '#downloads span.selected-type'
    SAVIOR_WIGDET_DONE_SPAN_CSS = 'span.file-size.done'

    @staticmethod
    def download_option_css_locator(title):
        return 'a[title*="%s"]' % title


