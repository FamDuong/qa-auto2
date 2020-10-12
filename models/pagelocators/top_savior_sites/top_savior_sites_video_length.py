from selenium.webdriver.common.by import By


class TopSaviorSitesVideoLengthLocators(object):
    YOUTUBE_VIDEO_LENGTH_CSS = '#movie_player div.ytp-bound-time-right'
    NHACCUATUI_MP3_LENGTH_CSS = '#utTotalTimeflashPlayer'
    NHACCUATUI_VIDEO_LENGTH_CSS = '#utTotalTimenctPlayer'
    OK_RU_VIDEO_LENGTH_CSS = '#VideoAutoplayPlayerE div.html5-vpl_time_t'
    TV_ZING_VIDEO_LENGTH_CSS = 'div.--z--control.--z--control-time span:nth-child(3)'
    DONG_PHYM_VIDEO_LENGTH_CSS = 'span.cplayer-duration-display'
    MOT_PHIMZZ_VIDEO_LENGTH = 'div.jw-icon.jw-icon-inline.jw-text.jw-reset.jw-text-duration'
    FACEBOOK_VIDEO_LENGTH = (By.XPATH, "(//span[contains(text(),'/')])[1]//following-sibling::span[contains(text(),':')]")
