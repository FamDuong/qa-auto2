from selenium.webdriver.common.by import By


class TopSaviorSitesNewsLocators:
    VTC_VIDEO_CSS = 'div[aria-label="Video Player"] video'

    ZING_NEWS_PLAY_VIDEO_BTN = (By.CSS_SELECTOR, 'button[title="Phát"]')
    ZING_NEWS_PLAY_VIDEO_BTN_CSS = 'button[title="Phát"]'
    ZINGNEWS_VIDEO_CSS = 'video[preload="metadata"]'
    ZINGNEWS_VIDEO = (By.CSS_SELECTOR, 'video[preload="metadata"]')
    VTV_GO_VIDEO_CSS = '#flowplayer_html5_api'
    DANTRI_VIDEO_LENGTH_CSS = 'video[playsinline="playsinline"]'
    VIETNAMNET_VIDEO_PARENT_IFRAME1 = (By.CSS_SELECTOR, 'iframe[allow="autoplay; fullscreen"]')
    VIETNAMNET_VIDEO_PARENT_IFRAME2 = (By.CSS_SELECTOR, 'iframe[allow="autoplay"]')
    VIETNAMNET_VIDEO = (By.CSS_SELECTOR, '#setIframMobile')
    # VIETNAMNET_VIDEO = (By.CSS_SELECTOR, '#vnnplayer video')
    VIETNAMNET_VIDEO_LENGTH_CSS = 'div[class*="rmp-duration"]'
    TV_TUOITRE_VIDEO_LENGTH_CSS = 'div[aria-label="Video Player"] video'
    KENH14_VIDEO_LENGTH_CSS = 'video[playsinline="playsinline"]'
    VNEXPRESS_VIDEO_LENGTH_CSS = '#videoContainter video[preload="auto"]'
    VNEXPRESS_NEWS_VIDEO_LENGTH_CSS = 'div[class ="videoContainter"] video[preload="auto"]'
    THANH_NIEN_VIDEO_LENGTH_CSS = '#contentAvatar video'

