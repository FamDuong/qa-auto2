
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
    # TV_ZING_VIDEO_URL = 'https://tv.zing.vn/video/Goblin-Yeu-Tinh-Tap-1/IWZEIC7F.html'
    # BILU_TV_VIDEO_URL = 'https://bilutv.org/phim-bat-gap-hanh-phuc-tap-1-14433.211144.html'
    DONG_PHIM_VIDEO_URL = 'http://dongphim.net/movie/tap-57-tam-sinh-tam-the-thap-ly-dao-hoa-eternal-love_r9ofmQv5.html'

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
    MESSENGER_CHAT_URL = 'https://www.messenger.com/t/kovakop.donald.3'
    INSTAGRAM_VIDEO_URL = 'https://www.instagram.com/p/B1nlf9AhX4M/'
    KIENTHUC_VIDEO_URL = 'https://kienthuc.net.vn/truyen-hinh-video/video-duong-pho-ha-noi-ngap-sau-sau-mua-bao-1259721.html'
    MOJI_BIG_CHATBOX = 'https://www.messenger.com/t/100013968193318'
    VIETNAMNET_VIDEO_URL = 'https://video.vietnamnet.vn/thuoc-la-dien-tu-khong-nicotine-van-gay-hai-den-co-the-a-81979.html'
    TWITTER_VIDEO_URL = 'https://twitter.com/pje0n/status/1170961701455286272'
    SOHA_VIDEO_URL = 'https://soha.vn/video.htm'
    EVA_VN_VIDEO_URL = 'https://eva.vn/clip-eva/5-con-giap-nam-vua-gioi-kiem-tien-vua-chieu-chuong-thuong-yeu-vo-het-long-c157a403553.html'
    SAO_2_VN_VIDEO_URL = 'https://2sao.vn/tran-thanh-to-hari-won-an-nhieu-den-chu-quan-cung-khiep-so-n-194597.html'
    FPT_PLAY_VIDEO_URL = 'https://fptplay.vn/xem-video/ngoi-nha-chung-mua-9-love-house-series-9-5d36d6a92089bd053fc87240/tap-1.html'
    PHUNU_GIADINH_VIDEO_URL = 'https://www.phunuvagiadinh.vn/video-185'
    TIEN_PHONG_VIDEO_URL = 'https://www.tienphong.vn/video-clip/singapore-tham-vong-ngam-hoa-dat-nuoc-1459961.tpo'
    BONG_DA_DOT_COM_VIDEO_URL = 'http://www.bongda.com.vn/highlights-bayern-munich-2-2-hertha-berlin-bundesliga-v516328.html'
    GIA_DINH_DOT_NET_VIDEO_URL = 'http://giadinh.net.vn/video-6805/meo-lam-tuong-ot-chua-ngot-dam-da-sanh-sot.htm'
    A_FAMILY_VIDEO_URL = 'http://video.afamily.vn/'
    GAMEK_VN_VIDEO_URL = 'http://gamek.vn/joker-tung-trailer-thu-2-he-lo-qua-khu-dau-thuong-cua-chang-hoang-tu-he-20190829101517375.chn'
    VU_VI_PHIM_VIDEO_URL = 'https://vuviphim.com/xem-phim-bo-lo-mot-nua-222545'
    AN_NINH_THU_DO_VIDEO_URL = 'https://anninhthudo.vn/truyen-hinh-atv/146.antd'
    TUOI_TRE_VIDEO_URL = 'https://tuoitre.vn/video.htm'
    TV_ZING_VIDEO_URL = 'https://tv.zing.vn/video/Goblin-Yeu-Tinh-Tap-1/IWZEIC7F.html'


class ExtensionIds:
    SAVIOR_EXTENSION_ID = 'jdfkmiabjpfjacifcmihfdjhpnjpiick'


