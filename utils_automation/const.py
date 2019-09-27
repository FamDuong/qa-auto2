
class Urls:

    COCCOC_SETTINGS_URL = 'coccoc://settings'
    COCCOC_SETTINGS_DOWNLOAD_URL = 'coccoc://settings/downloads'
    COCCOC_SETTINGS_ONSTARTUP = 'coccoc://settings/onStartup'
    COCCOC_SETTINGS_DEFAULT = 'coccoc://settings/defaultBrowser'
    COCCOC_DOWNLOAD_URL = 'coccoc://downloads'
    COCCOC_VERSION_URL = 'coccoc://version/'
    COCCOC_EXTENSIONS = 'coccoc://extensions'
    COCCOC_COMPONENTS = 'coccoc://components'
    COCCOC_DEV_URL = 'https://dev.coccoc.com'
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
    DONG_PHIM_VIDEO_URL = 'http://dongphim.net/movie/tap-1-trailer-dao-kiem-than-vuc-phan-4-chien-tranh-ngam-sword-art-online-alicization-war-of-underworld_gvwmHQQh.html'

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
    VU_VI_PHIM_VIDEO_URL = 'https://vuviphim.com/xem-phim-kochouki-wakaki-nobunaga-212770'
    AN_NINH_THU_DO_VIDEO_URL = 'https://anninhthudo.vn/truyen-hinh-atv/146.antd'
    TUOI_TRE_VIDEO_URL = 'https://tuoitre.vn/video.htm'
    TV_ZING_VIDEO_URL = 'https://tv.zing.vn/video/Goblin-Yeu-Tinh-Tap-1/IWZEIC7F.html'
    MOT_PHIM_VIDEO_URL = 'https://motphim.net/xem-phim/cuoc-doi-thu-2-tap-4-7099_90578.html'

    VTV_VN_TRUYEN_HINH_URL = 'https://vtv.vn/video/vut-xac-lon-benh-nguy-co-lay-lan-dich-ta-lon-chau-phi-theo-nguon-nuoc-390682.htm'
    TV_HAY_VIDEO_URL = 'http://tvhay.org/xem-phim-tram-yeu-360727'
    NGOI_SAO_VN_URL = 'https://ngoisao.vn/video/lieu-linh-bang-qua-dong-nuoc-lu-nguoi-dan-ong-suyt-phai-tra-gia-bang-ca-tinh-mang-273892.htm'

    VTC_VN_VIDEO_URL = 'https://vtc.vn/truyen-hinh-27.html'
    KENH14_VN_VIDEO_URL = 'http://video.kenh14.vn/dang-sau-moi-buc-anh-dep-la-mot-anh-chong-the-nay-day-245984.chn'

    CAFE_VN_VIDEO_URL = 'http://cafef.vn/videos/17236-btv-ngoc-trinh-len-tieng-truoc-tin-don-so-huu-loat-xe-sang-ca-chuc-ty-dong.chn'
    TIN_TUC_ONLINE_VIDEO_URL = 'https://tintuconline.com.vn/video/hoa-hong-tren-nguc-trai-tap-12-thai-doi-tieu-tam-phai-co-trach-nhiem-voi-minh-n-408464.html'
    GIAO_DUC_THOI_DAI_VIDEO_URL = 'https://giaoducthoidai.vn/chuyen-la/tai-xe-ngu-gat-khi-lai-xe-hanh-khach-van-than-nhien-nhu-khong-co-chuyen-gi-4032898-d.html'

    VN_EXPRESS_VIDEO_URL = 'https://video.vnexpress.net/tin-tuc/nhip-song/cay-si-co-thu-moc-100-than-3980758.html'
    THANH_NIEN_VIDEO_URL = 'https://video.thanhnien.vn/thoi-su/trom-ga-noi-hang-loat-bi-phat-tu-thi-bo-tron-bi-bat-lai-khi-dang-phuc-vu-trong-quan-karaoke-140814.html'
    DAN_TRI_VIDEO_URL = 'https://dantri.com.vn/video/tan-mat-xem-quy-trinh-lam-com-o-lang-nghe-noi-tieng-nhat-ha-noi-106661.htm'
    NGUOI_LAO_DONG_TV_URL = 'https://tv.nld.com.vn/Home-3.htm'
    ANIME_VSUB_TV_URL = 'http://animevsub.tv/phim/tay-du-3194/tap-01-61130.html'
    NHAC_VN_VIDEO_URL = 'https://nhac.vn/video/doi-that-la-phoi-phoi-hoang-yen-chibi-uni5-mvG38e'
    XVIDEOS_DOT_COM_VIDEO_URL = 'https://www.xvideos.com/video50625357/_'
    XNXX_VIDEO_URL = 'https://www.xnxx.com/video-rjo7d8b/step_son_caught_masturbating_shoots_load_into_stepmom_s_panties'
    FR_PORN_HUB_VIDEO_URL = 'https://fr.pornhub.com/view_video.php?viewkey=ph5bd4e9b96091f'
    VLXX_VIDEO_URL = 'http://vlxx.tv/video/bo-oi-con-khong-ngu-duoc/1410/'


class ExtensionIds:
    SAVIOR_EXTENSION_ID = 'jdfkmiabjpfjacifcmihfdjhpnjpiick'


