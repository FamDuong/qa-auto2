from selenium.webdriver.common.by import By


class YoutubePageLocators(object):

    @staticmethod
    def any_video_item(text):
        return By.XPATH, '//a[contains(text(), "%s")][@id="video-title"]' % text

    VIDEO_PLAYER_ITEM = (By.XPATH, '//div[@id="player"][@class="style-scope ytd-watch-flexy"]')

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
    FACEBOOK_VIDEO_ITEM = (By.XPATH, '//video[@preload]')
    MESSENGER_CHAT_VIDEO_ITEM = (By.XPATH, '//video')
    MESSENGER_CHAT_VIDEO_PLAY_BTN = (By.XPATH, '//*[@id="u_n_0"]')
    MESSENGER_CHAT_VIDEO_ITEM_SELECTOR = 'button[data-testid="play_pause_control"]'
    INSTAGRAM_VIDEO_ITEM = (By.XPATH, '//div[@role="button"][@aria-label]')
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
    PHUNU_GIADINH_VIDEO_ITEM = (By.ID, 'rmpPlayer')
    TIEN_PHONG_VIDEO_ITEM = (By.XPATH, '//video')
    TIEN_PHONG_PLAY_VIDEO_ITEM = (By.XPATH, '//button[@aria-label="Play"]')
    BONG_DA_DOT_COM_VIDEO_ITEM = (By.XPATH, '//iframe[@id="youtube_iframe"]')
    GIA_DINH_DOT_NET_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    A_FAMILY_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    GAME_K_VN_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    AN_NINH_THU_DO_VIDEO_ITEM = (By.ID, 'main_detail')
    TUOI_TRE_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="stream"]')
    MOT_PHIM_VIDEO_ITEM = (By.XPATH, '#player')
    MOT_PHIM_PLAY_VIDEO_BUTTON = (By.XPATH, '//div[@aria-label="Start Playback"]')
    MOT_PHIM_VIDEO_PLAYER = (By.ID, 'player')
    MOT_PHIM_EPISODE_ITEM = (By.XPATH, '//a[text()="Tập 1"]')
    MOT_PHIM_BOX_PLAYER = (By.ID, 'box-player')
    TV_HAY_VN_PLAY_BTN = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')
    TV_HAY_VN_PLAY_BTN_IN_FRAME = (By.XPATH, '//div[@class="vid_play"]')
    TV_HAY_VN_IFRAME_LEVEL = (By.XPATH, '//iframe[@width="100%"]')
    TV_HAY_VN_SKIP_ADD_BTN = (By.XPATH, '//span[text()="Bỏ qua quảng cáo"]')
    TV_HAY_VN_VIDEO_ITEM = (By.ID, 'playerjw7')
    TV_HAY_VN_PAUSE_BTN = (By.XPATH, '//div[@class="html5-vpl_panel_btn html5-vpl_play"]')
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
    THANH_NIEN_VIDEO_ITEM = (By.XPATH, '//div[@video-title][@data-enablefloat]')
    DAN_TRI_PLAY_VIDEO_BTN = (By.XPATH, '//button[@class="vjs-big-play-button"]')
    DAN_TRI_VIDEO_ITEM = (By.ID, 'video-embeb')
    NGUOI_LAO_DONG_VIDEO_ITEM = (By.CSS_SELECTOR, 'video[id*="streamid"]')
    NGUOI_LAO_DONG_PAUSE_BTN = (By.XPATH, '//button[@class="NLDPlayer-control  NLDPlayer-button play-control playing"]')
    ANIME_VSBUT_TV_CLOSE_POP_UP_WHERE_TO_START_VIDEO = (By.XPATH, '//button[@class="lobibox-btn lobibox-btn-no"]')
    ANIME_VSUB_WAIT_FOR_LOAD_PLAYER_ITEM = (By.XPATH, '//div[@id="media-player"]/center')
    ANIME_VSUB_WAIT_FOR_LOAD_PLAYER_ITEM_XPATH = '//div[@id="media-player"]/center'
    ANIME_VSUB_TV_VIDEO_ITEM = (By.ID, 'media-player-box')
    ANIME_VSUB_TV_CLOSE_AD_BUTTON = (By.ID, 'close-and-play')
    ANIME_VSUB_TV_PLAY_BUTTON = (By.XPATH, '//div[@class="jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback"]')
    NHAC_VN_VIDEO_URL = (By.ID, 'myvideo')
    OK_RU_VIDEO_ITEM = (By.XPATH,'//*[@id="VideoAutoplayPlayerE"]//video')
    XVIDEO_VIDEO_ITEM = (By.XPATH, '//div[@id="html5video"]')
    XVIDEO_PLAY_BTN = (By.XPATH, '//*[@id="hlsplayer"]/div[2]/div[2]/img')
    XNXX_VIDEO_ITEM = (By.XPATH, '//video[@preload="auto"]')
    XNXX_PLAY_BTN = (By.XPATH, '//div[@class="big-button play"]')
    FR_PORN_HUB_VIDEO_PLAY_BTN = (By.XPATH, '//div[@class="mhp1138_play"]')
    FR_PORN_HUB_VIDEO_ITEM = (By.ID, 'player')
    VLXX_VIDEO_ITEM = (By.XPATH, '//video')
    VLXX_VIDEO_ITEM_WRAPPER = (By.ID, 'vlxx')
    SEX_TOP1_VIDEO_ITEM = (By.XPATH, '//video')
    SEX_TOP1_VIDEO_WRAPPER = (By.ID, 'player')
    SEX_HIHI_VIDEO_WRAPPER = (By.ID, 'vlxx')
    SEX_HIHI_VIDEO_ITEM = (By.XPATH, '//video')
    JAV_HD_VIDEO_WRAPPER = (By.ID, 'javhd')
    JAV_HD_VIDEO_ITEM = (By.XPATH, '//video')
    PHIM_SEX_PORN_IFRAME = (By.XPATH, '//iframe[@allowfullscreen="true"]')
    PHIM_SEX_PORN_PLAY_BTN = (By.XPATH, '//div[@class="jw-display-icon-container jw-display-icon-display jw-reset"]//div[@aria-label="Play"]')
    PHIM_SEX_PORN_VIDEO_ITEM = (By.XPATH, '//div[@class="video-player"]')
    JAV_PHIM_VIDEO_ITEM_WRAPPER = (By.ID, 'player')
    JAV_PHIM_VIDEO_ITEM = (By.XPATH, '//video')
    TIN_MOI_VIDEO_ITEM = (By.ID, 'rmpPlayer')
    INFO_NET_VIDEO_ITEM = (By.ID, 'player')
    INFO_NET_VIDEO_IFRAME = (By.XPATH, '//iframe[@src][@width="490"]')
    INFO_NET_VIDEO_PLAY_BTN = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')
    BONGDA_24H_VIDEO_ITEM = (By.XPATH, '//video[@id]')
    KEO_NHA_CAI_VIDEO_ITEM = (By.ID, 'player')
    DAILY_MOTION_VIDEO_ITEM = (By.ID, 'player-body')
    VOV_VN_VIDEO_ITEM = (By.XPATH, '//*[contains(@id, "video")]/iframe')
    VOV_VN_VIDEO_ITEM_WRAPPER = (By.XPATH, '//div[@aria-label="Start Playback"]')
    VOV_VN_IFRAME = (By.XPATH, '//*[contains(@id, "video")]/iframe')
    VOV_VN_PLAY_BTN = (By.XPATH, '//div[@aria-label="Start Playback"]')
    SEX_NGON_VIDEO_ITEM = (By.ID, 'video')
    WEIBO_VIDEO_ITEM = (By.XPATH, '//video[@id]')
    VU_VI_PHIM_VIDEO_ELEMENT = (By.ID, 'media')
    VU_VI_PHIM_PLAY_BTN = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')
    VU_VI_PHIM_IFRAME = (By.XPATH, '//iframe[@data-was-processed][not(@title)]')

    @staticmethod
    def anime_tvn_server(server_number):
        return By.XPATH, '//a[@class][text()="%s"]' % server_number

    ANIME_TVN_IFRAME_VIDEO_ITEM = (By.XPATH, '//div[@id="players"]/iframe')
    ANIME_TVN_VIDEO_ITEM = (By.ID, 'myElement')
    PHIM_BAT_HU_VIDEO_ITEM = (By.ID, 'box-player')
    PHIM_BAT_HU_IFRAME = (By.XPATH, '//*[@id="box-player"]/div/iframe')
    PHIM_BAT_HU_VIDEO_INNER_ITEM = (By.XPATH, '//div[@data-module="OKVideo"]')
    PHIM_BAT_HU_PLAY_VIDEO_ITEM = (By.ID, 'media-player')
    PHIM_BAT_HU_PAUSE_BTN = (By.XPATH, '//*[@id="media-player"]/div[2]/div[9]/div[4]/div[2]/div[1]/svg[2]')
    PHIM_BAT_HU_PAUSE_BTN_XPATH = '//div[@class="jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback"]'
    PHIM_SEX_SUB_VIDEO_ITEM_WRAPPER = (By.ID, 'player-v1')
    PHIM_SEX_SUB_VIDEO_ITEM = (By.XPATH, '//video')
    VLIVE_TV_VIDEO_ITEM = (By.XPATH, '//div[@data-video-overlay]')
    ANIME_HAY_TV_WRAPPER_VIDEO_ITEM = (By.ID, 'ah-player')
    ANIME_HAY_TV_IFRAME_VIDEO_ITEM = (By.XPATH, '//iframe[@style="position: absolute;top: 0;left: 0;width: 100%;height: 100%;overflow:hidden;"]')
    DOI_SONG_PHAP_LUAT_IFRAME_VIDEO_ITEM = (By.XPATH, '//iframe[@scrolling][@style][contains(@src,"doi-ban-than")]')
    DOI_SONG_PHAP_LUAT_PLAYER_VIDEO = (By.ID, 'rmpPlayer')
    SAO_STAR_VN_VIDEO_ITEM = (By.XPATH, '//div[@class="wp-video"]')
    VIET_SUB_TV_PLAY_MIDDLE_BUTTON = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')
    VIET_SUB_TV_PLAY_MIDDLE_BUTTON_XPATH = '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]'
    VIET_SUB_TV_PLAYER_VIDEO_ITEM = (By.ID, 'player')
    VIET_SUB_TV_AD_NOT_APPEAR_ITEM_XPATH = '//div[@id="adsmessage"][@style="display: none;"]'
    DONG_PHIM_VIDEO_ITEM = (By.CSS_SELECTOR, 'div[id*="video-player"][playsinline]')
    DONG_PHIM_VIDEO_IFRAME = (By.CSS_SELECTOR, '[id*="video-wrap-video-player"] > div[style*="position"] > iframe')
    DONG_PHIM_WATCH_OPTION = (By.XPATH, '//button[@class="cplayer-discover-checkpoint-btn"]')
    DONG_PHIM_WATCH_OPTION_XPATH = '//button[@class="cplayer-discover-checkpoint-btn"]'
    DONG_PHIM_PLAY_VIDEO_ITEM = (By.CSS_SELECTOR, 'button[class="cplayer-play-control cplayer-control cplayer-button cplayer-paused"]')
    DONG_PHIM_PLAY_VIDEO_ITEM_CSS = 'button[class="cplayer-play-control cplayer-control cplayer-button cplayer-paused"]'
    HENTAIZ_NET_VIDEO_ITEM = (By.ID, 'media-player')
    HENTAIZ_NET_PLAY_BTN = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')
    VTV16_INFO_NET_VIDEO_ITEM = (By.ID, 'player-vtv')
    VTV16_INFO_NET_IFRAME_ELEMENT = (By.XPATH, '//iframe[@width="100%"]')
    BESTIE_VN_IFRAME_ELEMENT_1 = (By.XPATH, '//iframe[@allowfullscreen][@id="iframe_75083"]')
    BESTIE_VN_IFRAME_ELEMENT_2 = (By.XPATH, '//iframe[@id="player"]')
    BESTIE_VN_VIDEO_PLAYER = (By.ID, 'player')
    CLIP_ANIME_COM_VIDEO_PLAYER = (By.ID, 'player')
    VTV_GO_VN_VIDEO_ITEM = (By.ID, 'flowplayer')
    XEM_VTV_NET_VIDEO_PLAYER = (By.ID, 'media')
    XEM_VTV_NET_PLAY_BTN = (By.XPATH, '//div[@class="jw-icon jw-icon-display jw-button-color jw-reset"]')





