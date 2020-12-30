from selenium.webdriver.common.by import By


class TopSaviorSitesVideoLengthLocators(object):
    YOUTUBE_VIDEO_LENGTH_CSS = '#movie_player div.ytp-bound-time-right'
    NHACCUATUI_MP3_LENGTH_CSS = '#utTotalTimeflashPlayer'
    NHACCUATUI_VIDEO_LENGTH_CSS = '#utTotalTimenctPlayer'
    OK_RU_VIDEO_LENGTH_CSS = '#VideoAutoplayPlayerE div.html5-vpl_time_t'
    TV_ZING_VIDEO_LENGTH_CSS = 'div.--z--control.--z--control-time span:nth-child(3)'
    DONG_PHYM_VIDEO_LENGTH_CSS = 'span.cplayer-duration-display'
    MOT_PHIMZZ_VIDEO_LENGTH = 'div.jw-icon.jw-icon-inline.jw-text.jw-reset.jw-text-duration'
    # FACEBOOK_VIDEO_LENGTH_ONE_VIDEO = (By.XPATH, "(//span[contains(text(),'/')])[1]//following-sibling::span[contains(text(),':')]")
    FACEBOOK_VIDEO_LENGTH_HOME_PAGE = (By.XPATH,
                                       "(//div[@aria-label='Change Position'])[1]//ancestor::div[contains(@data-instancekey,'id-vpuid')]//span[contains(text(),':')][2]")
    FACEBOOK_VIDEO_LENGTH_VTV_GIAITRI_PAGE = \
        (By.XPATH,
         '(//div[@data-ad-comet-preview="message"]//ancestor::div[@dir="auto" and @class=""]//following-sibling::div//span[contains(text(),":")][2])[1]')


class OnlineMusicVideoLengthLocators(object):
    SOUNDCLOUD_MP3_LENGTH_CSS = 'div.playbackTimeline__duration span[aria-hidden="true"]'
    NHAC_VN_VIDEO_LENGTH_CSS = '#myvideo video'
    ZING_MP3_VIDEO_LENGTH_CSS = 'video[preload="metadata"]'


class SocialNetworkVideoLengthLocators(object):
    INSTAGRAM_VIDEO_HOMEPAGE_CSS = 'article:nth-child(1) video'
    INSTAGRAM_VIDEO_OTHERS_PAGE_CSS = 'article:nth-child(1) video'


class NewsVideoLengthLocators(object):
    NEWS_24H_BONGDA_VIDEO_CSS = 'video[id*="my-video"]'
    NEWS_24H_BONGDA_VIDEO_LENGTH_CSS = 'div[class*="duration-display"]'


class VideoClipTVShowVideoLengthLocators(object):
    DAILY_MOTION_VIDEO_CSS = '#dmp_Video'
    TIKTOK_VIDEO_CSS = 'video:nth-child(1)'


class OnlinePornVideoLengthLocators(object):
    FR_PORN_HUB_VIDEO_CSS = '#player video'
    XHAMSTER_ONE_VIDEO_LENGHT_CSS = '#player-container span.eta'
    THUMBZILLA_VIDEO_LENGHT_CSS = 'video'
    FR_SPANKBANG_VIDEO_LENGHT_CSS = '#main_video_player_html5_api'

