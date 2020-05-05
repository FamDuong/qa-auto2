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
    FACEBOOK_VIDEO_TITLE = (By.ID, 'pageTitle')
    FR_PORNHUB_VIDEO_TITLE = (By.ID, 'main-container')




