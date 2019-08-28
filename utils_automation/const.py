
class Urls:

    COCCOC_SETTINGS_URL = 'coccoc://settings'
    COCCOC_SETTINGS_DOWNLOAD_URL = 'coccoc://settings/downloads'
    COCCOC_DOWNLOAD_URL = 'coccoc://downloads'
    COCCOC_VERSION_URL = 'coccoc://version/'
    COCCOC_EXTENSIONS = 'coccoc://extensions'
    YOUTUBE_URL = 'https://www.youtube.com/'

    GOOGLE_URL = 'https://www.google.com/'
    FACEBOOK_URL = 'https://www.facebook.com/'

    NEW_TAB_URL = 'http://coccoc.com/webhp'
    PIRATE_BAY_URL = 'https://www.thepiratebay.asia/search'


class VideoUrls:

    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v=IHNzOHi8sJs'
    NEWS_ZING_VIDEO_URL = 'https://news.zing.vn/video'
    ZING_MP3_VN_VIDEO_URL = 'https://zingmp3.vn/video-clip/Attention-J-Fla/ZW7F76D6.html'
    NHAC_CUA_TUI_VIDEO_ITEM = 'https://www.nhaccuatui.com/video/summer-girl-haim.Q1gHbL4BuuEXJ.html'
    TV_ZING_VIDEO_URL = 'https://tv.zing.vn/video/Goblin-Yeu-Tinh-Tap-1/IWZEIC7F.html'
    BILU_TV_VIDEO_URL = 'https://bilutv.org/phim-bat-gap-hanh-phuc-tap-1-14433.211144.html'

    @classmethod
    def all(cls):
        return [value for name, value in vars(cls).items() if name.isupper()]


class DiffFormatFileUrls:

    FACEBOOK_VIDEO_URL = 'https://www.facebook.com/watch/?v=682897505204114'
    WEBM_URL = 'http://techslides.com/demos/sample-videos/small.webm'

    @classmethod
    def all(cls):
        return [value for name, value in vars(cls).items() if name.isupper()]


class OtherSiteUrls:

    TWENTY_FOUR_H_VIDEO_URL = 'https://www.24h.com.vn/bong-da/2-clb-viet-nam-thong-tri-afc-cup-bao-chau-a-noi-gi-c48a1061647.html'
    PHIMMOI_VIDEO_URL = 'http://www.phimmoi.net/phim/linh-kiem-ton-8199/xem-phim.html'
    FACEBOOK_VIDEO_URL = 'https://www.facebook.com/watch/?v=682897505204114'
    MESSENGER_CHAT_URL = 'https://www.messenger.com/t/2035107526617289'
    INSTAGRAM_VIDEO_URL = 'https://www.instagram.com/p/B1nlf9AhX4M/'
    KIENTHUC_VIDEO_URL = 'https://kienthuc.net.vn/truyen-hinh-video/video-duong-pho-ha-noi-ngap-sau-sau-mua-bao-1259721.html'
    MOJI_BIG_CHATBOX = 'https://www.messenger.com/t/100013968193318'
    VIETNAMNET_VIDEO_URL = 'https://video.vietnamnet.vn/thuoc-la-dien-tu-khong-nicotine-van-gay-hai-den-co-the-a-81979.html'
    TWITTER_VIDEO_URL = 'https://twitter.com/downloaderbot?lang=en'
    SOHA_VIDEO_URL = 'https://soha.vn/video.htm'
    EVA_VN_VIDEO_URL = 'https://eva.vn/clip-eva/5-con-giap-nam-vua-gioi-kiem-tien-vua-chieu-chuong-thuong-yeu-vo-het-long-c157a403553.html'
    SAO_2_VN_VIDEO_URL = 'http://2sao.vn/clip/'
    FPT_PLAY_VIDEO_URL = 'https://fptplay.vn/xem-video/ngoi-nha-chung-mua-9-love-house-series-9-5d36d6a92089bd053fc87240/tap-1.html'
    PHUNU_GIADINH_VIDEO_URL = 'https://www.phunuvagiadinh.vn/video-185'


class ExtensionIds:
    SAVIOR_EXTENSION_ID = 'jdfkmiabjpfjacifcmihfdjhpnjpiick'


