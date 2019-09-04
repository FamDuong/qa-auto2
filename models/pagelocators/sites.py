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

    PHIMMOI_CONTINUE_WATCHING_CLOSE_ELEMENT = (By.ID, 'watching-messbox-close')

    FACEBOOK_VIDEO_ITEM = (By.XPATH, '//video[@muted="1"]')

    MESSENGER_CHAT_VIDEO_ITEM = (By.XPATH, '//video')
    MESSENGER_CHAT_VIDEO_ITEM_SELECTOR = 'button[data-testid="play_pause_control"]'
    INSTAGRAM_VIDEO_ITEM = (By.XPATH, '//a[@role="button"]')
    KIENTHUC_VIDEO_ITEM = (By.XPATH, '//div[@style="text-align:center; width:480px;"]')
    VIETNAMNET_VIDEO_ITEM = (By.ID, 'videoDetail')
    TWITTER_VIDEO_ITEM = (By.XPATH, '//video[@preload="auto"]')
    TWITTER_MEDIA_VIEW_OPTION = (By.XPATH, '(//span[contains(text(), "Media")])[2]')
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




