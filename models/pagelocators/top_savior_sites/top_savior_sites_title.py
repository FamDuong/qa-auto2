from selenium.webdriver.common.by import By


class TopSaviorSitesTitleLocators(object):
    X_VIDEOS_VIDEO_TITLE = (By.XPATH, '//*[@id="main"]/h2')
    XNXX_VIDEO_TITLE = (By.XPATH, '//*[@id="video-content-metadata"]/div[1]/strong')
    TV_ZING_VIDEO_TITLE = (By.XPATH, '//div[@class="box-description"]//strong[@alt]')
    YOUTUBE_VIDEO_TITLE = (By.XPATH, '//*[@id="container"]/h1/yt-formatted-string')
    INSTAGRAM_VIDEO_TITLE = (By.XPATH, '//meta[@property="og:title"]')
    MESSENGER_VIDEO_TITLE = (By.XPATH, '//*[@id="pageTitle"]')
    MOT_PHIM_VIDEO_TITLE = (By.XPATH, '//meta[@name="title"]')
    PHIMMOI_VIDEO_TITLE = (By.XPATH, '//meta[@property="og:title"]')
    OK_RU_VIDEO_TITLE = (By.XPATH, '//title')
    VIDEO_ROOT_SHADOW_CSS = "div[style='position: absolute; top: 0px;']"
    VIDEO_TITLE_CSS = "#downloads span.filename"
    FR_PORNHUB_VIDEO_TITLE = (By.ID, 'main-container')
    VIDEO_VNEXPRESS_VIDEO_TITLE = (By.XPATH, '//*[@id="info_inner"]//h1[@class="title"]')
    TIKTOK_VIDEO_TITLE = (By.CSS_SELECTOR,
                              'div.video-feed-container span[class*="lazyload-wrapper"]:nth-child(1) div.tt-video-meta-caption strong')




