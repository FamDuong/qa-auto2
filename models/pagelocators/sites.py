from selenium.webdriver.common.by import By


class YoutubePageLocators(object):

    @staticmethod
    def any_video_item(text):
        return By.XPATH, '//a[contains(text(), "%s")][@id="video-title"]' % text

    VIDEO_PLAYER_ITEM = (By.ID, 'movie_player')

    SEARCH_BOX = (By.ID, 'search')

    SEARCH_BTN = (By.ID, 'search-icon-legacy')


class GooglePageLocators(object):

    SEARCH_FIELD = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="VlcLAe"]/input[@class="gNO89b"]')
    VIDEO_SEARCH_BTN = (By.XPATH, '//a[contains(text(),"Videos")]')

    SHADOW_ROOT_CONTENT = (By.XPATH, '(//div[starts-with(@data-hveid, "4")]//div[@class="s"]//div)[6]')
    SAVIOR_ICON = '[class="button-block shown"]'


class AnySite(object):
    TWENTY_FOUR_H_VIDEO_ITEM = (By.CSS_SELECTOR, '[class="v-24h-media-player"]')
    PHIMMOI_VIDEO_ITEM = (By.ID, 'media-player-box')
    PHIMMOI_VIDEO_MOUSE_OVER = (By.ID, 'media-player')
    PHIMMOI_IFRAME_SKIP_AD_ITEM = (By.CSS_SELECTOR, 'iframe[gesture="media"][src="javascript:false"]')
    PHIMMOI_IFRAME_MAIN_PEROL_ADS_ID = (By.ID, 'main_preroll_ads')
    PHIMMOI_IFRAME_MAIN_PEROL_ADS_ID_TEXT = 'iframe[id="main_preroll_ads"]'
    PHIMMOI_IFRAME_SKIP_AD_ITEM_CSS_SELECTOR = 'iframe[gesture="media"][src="javascript:false"]'
    PHIMMOI_SKIP_VIDEO_AD = (By.ID, 'an_skip_button')
    PHIMMOI_SKIP_VIDEO_AD_ID = 'an_skip_button'
    PHIMMOI_BO_QUA_QUANG_CAO = (By.XPATH, '//span[@class="jw-text jw-skiptext jw-reset"]')
    PHIMMOI_BO_QUA_QUANG_CAO_XPATH = '//span[@class="jw-text jw-skiptext jw-reset"]'
    PHIMMOI_SKIP_BY_ID = 'preroll-skip'
    PHIMMOI_IFRAME_NOT_DISPLAYED_SKIP_BTN_XPATH = '//div[@id="an_skip_button"][text()][@style="display: none;"]'
    PHIMMOI_SKIP_AD_BUTTON = (By.XPATH, '//div[@class="jw-skip jw-reset jw-skippable"]')
    PHIMMOI_CONTINUE_WATCHING_CLOSE_ELEMENT = (By.ID, 'watching-messbox-close')
    PHIMMOI_CLOSE_IMAGE_AD = (By.XPATH, '//a[@class="close"]')
    PHIMMOI_VIDEO_AD_LENGTH_LOCATOR = (By.XPATH, '//div[@class="jw-icon jw-icon-inline jw-text jw-reset jw-text-duration"]')
    FACEBOOK_VIDEO_ITEM = (By.XPATH, '//video[@muted="1"]')
    MESSENGER_CHAT_VIDEO_ITEM = (By.XPATH, '//video')
    MESSENGER_CHAT_VIDEO_ITEM_SELECTOR = 'button[data-testid="play_pause_control"]'
    INSTAGRAM_VIDEO_ITEM = (By.XPATH, '//a[@role="button"]')
    KIENTHUC_VIDEO_ITEM = (By.XPATH, '//div[@style="text-align:center; width:480px;"]')
    VIETNAMNET_VIDEO_ITEM = (By.ID, 'videoDetail')
    TWITTER_VIDEO_ITEM = (By.XPATH, '//video[@preload="auto"]')
    TWITTER_MEDIA_VIEW_OPTION = (By.XPATH, '(//span[contains(text(), "Media")])[2]')
    TWITTER_AUTHORIZE_RESTRICTED_USER_BTN = '//span[text()="Yes, view profile"]'
    TWITTER_AUTHORIZE_RESTRICTER_USER_PARENT_BTN = (By.XPATH, '//span[text()="Yes, view profile"]/parent::span/parent::div')
    TWITTER_AUTHORIZE_RESTRICTED_USER_BTN_JAVASCRIPT = 'div:nth-of-type(3)[role="button"] > div > span'
    SOHA_VIDEO_ITEM = (By.ID, 'video-embeb')
    EVA_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="zplayer"]')
    SAO_2_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'iframe[src*="https://embed.vietnamnettv.vn"]')
    FPT_PLAY_WATCH_FROM_BEGINNING_BTN = (By.ID, 'onCancel')
    FPT_VIDEO_ITEM = (By.XPATH, '(//video)[1]')
    PHUNU_GIADINH_VIDEO_ITEM = (By.ID, 'rmpPlayer')
    TIEN_PHONG_IFRAME = (By.XPATH, '//iframe[@class="cms-video"]')
    TIEN_PHONG_VIDEO_ITEM = (By.XPATH, '//div[@aria-label="Start Playback"]')
    TIEN_PHONG_PLAY_VIDEO_ITEM = (By.XPATH, '//video')
    BONG_DA_DOT_COM_IFRAME = (By.ID, 'youtube_iframe')
    BONG_DA_DOT_COM_VIDEO_ITEM = (By.XPATH, '//button[@class="ytp-play-button ytp-button"]')
    GIA_DINH_DOT_NET_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    A_FAMILY_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    GAME_K_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    VU_VI_PHIM_IFRAME = (By.XPATH, '//iframe[@allow="autoplay"]')
    VU_VI_PHIM_VIDEO_ITEM = (By.ID, 'embedVideoE')
    VU_VI_PHIM_PLAY_VIDEO_BUTTON = (By.XPATH, '//div[@class="html5-vpl_panel_btn html5-vpl_play"]')
    VU_VI_PHIM_FULL_SCREEN_BUTTON = (By.XPATH, '//div[@class="html5-vpl_panel_btn html5-vpl_fullscreen"]')
    AN_NINH_THU_DO_VIDEO_ITEM = (By.ID, 'main_detail')
    TUOI_TRE_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    MOT_PHIM_VIDEO_ITEM = (By.XPATH, '//video')
    MOT_PHIM_PLAY_VIDEO_BUTTON = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')
    MOT_PHIM_VIDEO_PLAYER = (By.ID, 'player')
    MOT_PHIM_EPISODE_ITEM = (By.XPATH, '//a[text()="Tập 1"]')
    MOT_PHIM_BOX_PLAYER = (By.ID, 'box-player')
    VTV_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    TV_HAY_VN_PLAY_BTN = (By.XPATH, '//div[@aria-label="Play"][1]')
    TV_HAY_VN_SKIP_ADD_BTN = (By.XPATH, '//span[text()="Bỏ qua quảng cáo"]')
    TV_HAY_VN_VIDEO_ITEM = (By.XPATH, '//video')
    NGOI_SAO_VN_VIDEO_ITEM = (By.XPATH, '(//video[@class="jw-video jw-reset"])[1]')
    VTC_VN_VIDEO_PLAY_ITEM = (By.ID, 'myElementV0')
    VTC_VN_VIDEO_ITEM = (By.XPATH, '//video')
    KENH14_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    CAFE_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    TIN_TUC_VN_VIDEO_IFRAME = (By.XPATH, '//iframe[@onload]')
    TIN_TUC_VN_VIDEO_ITEM = (By.XPATH, '//div[@id="vnnplayer"]')
    TIN_TUC_VN_VIDEO_DETAIL = (By.ID, 'videoDetail')
    GIAO_DUC_THOI_DAI_VIDEO_ITEM = (By.CSS_SELECTOR, 'div[id*="video"]')
    VN_EXPRESS_VIDEO_ITEM = (By.ID, 'videoContainter')
    THANH_NIEN_VIDEO_ITEM = (By.ID, 'mainplayer')
    DAN_TRI_VIDEO_ITEM = (By.ID, 'video-embeb')
    NGUOI_LAO_DONG_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="streamid"]')
    ANIME_VSBUT_TV_CLOSE_POP_UP_WHERE_TO_START_VIDEO = (By.XPATH, '//button[@class="lobibox-btn lobibox-btn-no"]')
    ANIME_VSUB_TV_VIDEO_ITEM = (By.ID, 'media-player')
    ANIME_VSUB_TV_CLOSE_AD_BUTTON = (By.ID, 'close-and-play')
    NHAC_VN_VIDEO_URL = (By.ID, 'myvideo')
    XVIDEO_VIDEO_ITEM = (By.XPATH, '//video')
    XNXX_VIDEO_ITEM = (By.XPATH, '//video[@preload="auto"]')
    FR_PORN_HUB_VIDEO_ITEM = (By.ID, 'player')
    VLXX_VIDEO_ITEM = (By.XPATH, '//video')
    VLXX_VIDEO_ITEM_WRAPPER = (By.ID, 'vlxx')
    SEX_TOP1_VIDEO_ITEM = (By.XPATH, '//video')
    SEX_TOP1_VIDEO_WRAPPER = (By.ID, 'player')
    SEX_HIHI_VIDEO_WRAPPER = (By.ID, 'vlxx')
    SEX_HIHI_VIDEO_ITEM = (By.XPATH, '//video')
    JAV_HD_VIDEO_WRAPPER = (By.ID, 'javhd')
    JAV_HD_VIDEO_ITEM = (By.XPATH, '//video')
    PHIM_SEX_PORN_VIDEO_ITEM_WRAPPER = (By.XPATH, '//div[@class="margin-10"]')
    PHIM_SEX_PORN_VIDEO_ITEM = (By.XPATH, '//iframe[@allowfullscreen="true"]')
    JAV_PHIM_VIDEO_ITEM_WRAPPER = (By.ID, 'player')
    JAV_PHIM_VIDEO_ITEM = (By.XPATH, '//video')
    TIN_MOI_VIDEO_ITEM = (By.ID, 'rmpPlayer')
    INFO_NET_VIDEO_ITEM = (By.XPATH, '//video[@id]')
    BONGDA_24H_VIDEO_ITEM = (By.XPATH, '//video[@id]')
    KEO_NHA_CAI_VIDEO_ITEM = (By.ID, 'player')
    DAILY_MOTION_VIDEO_ITEM = (By.ID, 'player-body')
    VOV_VN_VIDEO_ITEM = (By.XPATH, '//video')
    VOV_VN_VIDEO_ITEM_WRAPPER = (By.XPATH, '//div[@aria-label="Start Playback"]')
    VOV_VN_IFRAME = (By.XPATH, '//div[contains(@id,"video")]/iframe')
    SEX_NGON_VIDEO_ITEM = (By.ID, 'video')
    WEIBO_VIDEO_ITEM = (By.XPATH, '//video[@id]')

    @staticmethod
    def anime_tvn_server(server_number):
        return By.XPATH, '//a[@class][text()="%s"]' % server_number

    ANIME_TVN_IFRAME_VIDEO_ITEM = (By.XPATH, '//div[@id="players"]/iframe')
    ANIME_TVN_VIDEO_ITEM = (By.ID, 'myElement')
    PHIM_BAT_HU_VIDEO_ITEM = (By.XPATH, '//video')
    PHIM_BAT_HU_PLAY_VIDEO_ITEM = (By.ID, 'media-player')
    PHIM_SEX_SUB_VIDEO_ITEM_WRAPPER = (By.ID, 'player-v1')
    PHIM_SEX_SUB_VIDEO_ITEM = (By.XPATH, '//video')
    VLIVE_TV_VIDEO_ITEM = (By.XPATH, '//div[@data-video-overlay]')



