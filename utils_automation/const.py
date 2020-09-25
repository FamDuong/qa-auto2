class Urls:
    COCCOC_SETTINGS_URL = 'coccoc://settings'
    COCCOC_SETTINGS_DOWNLOAD_URL = 'coccoc://settings/downloads'
    COCCOC_SETTINGS_ONSTARTUP = 'coccoc://settings/onStartup'
    COCCOC_SETTINGS_DEFAULT = 'coccoc://settings/defaultBrowser'
    COCCOC_DOWNLOAD_URL = 'coccoc://downloads'
    COCCOC_VERSION_URL = 'coccoc://version/'
    COCCOC_EXTENSIONS = 'coccoc://extensions'
    COCCOC_COMPONENTS = 'coccoc://components'
    COCCOC_TERMS = 'coccoc://terms'
    COCCOC_ABOUT = 'coccoc://settings/help'
    COCCOC_HISTORY_URL = 'coccoc://history/'
    COCCOC_FLAGS = 'coccoc://flags'
    COCCOC_DEV_URL = 'https://dev.coccoc.com'
    COCCOC_THANK_YOU_URL_EN = 'https://dev.coccoc.com/en/win/thanks.html'
    COCCOC_THANK_YOU_URL_EN_PRO = 'https://coccoc.com/en/win/thanks.html'
    COCCOC_THANK_YOU_URL_VI = 'https://dev.coccoc.com/vi/win/thanks.html'
    COCCOC_URL = 'https://coccoc.com'
    COCCOC_ADS_BLOCK_URL = 'coccoc://settings/adsBlock'
    YOUTUBE_URL = 'https://www.youtube.com/'

    GOOGLE_URL = 'https://www.google.com/'
    FACEBOOK_URL = 'https://www.facebook.com/'
    FACEBOOK_COC_COC_BAY_PROFILE_URL = 'https://www.facebook.com/profile.php?id=100010842734556'
    MESSENDER_URL = "https://www.messenger.com/"
    FACEBOOK_MESSENDER_URL = "https://www.facebook.com/messages/t/100010842734556"
    NEW_TAB_URL = 'http://coccoc.com/webhp'
    PIRATE_BAY_URL = 'https://www.thepiratebay.asia/search'
    CC_SEARCH_URL = "https://coccoc.com/search"
    CC_SEARCH_QUERY = "https://coccoc.com/search?query="


class VideoUrls:
    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v=RXIm1NLCSz0'
    NEWS_ZING_VIDEO_URL = 'https://news.zing.vn/video'
    ZING_MP3_VN_VIDEO_URL = 'https://zingmp3.vn/video-clip/A-Better-Day-JTL/ZWZ9CF86.html'
    NHAC_CUA_TUI_VIDEO_ITEM = 'https://www.nhaccuatui.com/video/summertime-cinnamons-ft-evening-cinema.w3rGuakkZzvg9.html'
    DONG_PHIM_VIDEO_URL = 'https://dongphym.net/video/one-piece-movie-12-z-ky-phung-dich-thu_CtT37Qt8.html'

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
    NEWS_24H_URL = 'https://www.24h.com.vn/tong-hop-video.html'
    NEWS_24H_BONGDA_URL = 'https://www.24h.com.vn/bong-da/2-clb-viet-nam-thong-tri-afc-cup-bao-chau-a-noi-gi-c48a1061647.html'
    PHIMMOI_VIDEO_URL = 'http://www.phimmoizz.net/phim/soi-100-11066/xem-phim.html'
    PHIMMOI_URL = 'http://www.phimmoizz.net/phim/ky-su-thanh-xuan-11454/'
    FACEBOOK_VIDEO_URL = 'https://www.facebook.com/watch/?v=770300356741609'
    MESSENGER_CHAT_URL = 'https://www.messenger.com/t/nganhanguyen0306'
    INSTAGRAM_VIDEO_URL = 'https://www.instagram.com/p/B1nlf9AhX4M/'
    NEWS_KIENTHUC_VIDEO_URL = 'https://kienthuc.net.vn/truyen-hinh-video/video-duong-pho-ha-noi-ngap-sau-sau-mua-bao-1259721.html'
    MOJI_BIG_CHATBOX = 'https://www.messenger.com/t/100013968193318'
    VIETNAMNET_VIDEO_URL = 'https://video.vietnamnet.vn/thuoc-la-dien-tu-khong-nicotine-van-gay-hai-den-co-the-a-81979.html'
    TWITTER_VIDEO_URL = 'https://twitter.com/pje0n/status/1170961701455286272'
    SOHA_VIDEO_URL = 'https://soha.vn/video.htm'
    EVA_VN_VIDEO_URL = 'https://eva.vn/clip-eva/5-con-giap-nam-vua-gioi-kiem-tien-vua-chieu-chuong-thuong-yeu-vo-het-long-c157a403553.html'
    SAO_2_VN_VIDEO_URL = 'https://2sao.vn/tran-thanh-to-hari-won-an-nhieu-den-chu-quan-cung-khiep-so-n-194597.html'
    PHUNU_GIADINH_VIDEO_URL = 'https://www.phunuvagiadinh.vn/video-185'
    TIEN_PHONG_VIDEO_URL = 'https://www.tienphong.vn/video-clip/singapore-tham-vong-ngam-hoa-dat-nuoc-1459961.tpo'
    BONG_DA_DOT_COM_VIDEO_URL = 'http://www.bongda.com.vn/highlights-bayern-munich-2-2-hertha-berlin-bundesliga-v516328.html'
    GIA_DINH_DOT_NET_VIDEO_URL = 'http://giadinh.net.vn/video-6805/meo-lam-tuong-ot-chua-ngot-dam-da-sanh-sot.htm'
    A_FAMILY_VIDEO_URL = 'http://video.afamily.vn/'
    GAMEK_VN_VIDEO_URL = 'http://gamek.vn/joker-tung-trailer-thu-2-he-lo-qua-khu-dau-thuong-cua-chang-hoang-tu-he-20190829101517375.chn'
    VU_VI_PHIM_VIDEO_URL = 'https://vuviphimzz.com/xem-phim-ta-ga-tame-no-alchemist-314105'
    AN_NINH_THU_DO_VIDEO_URL = 'https://anninhthudo.vn/truyen-hinh-atv/146.antd'
    TUOI_TRE_VIDEO_URL = 'https://tv.tuoitre.vn/'
    TV_ZING_VIDEO_URL = 'https://tv.zing.vn/video/id/IWZEAUO9.html'
    MOT_PHIM_VIDEO_URL = 'https://motphim.net/xem-phim/cuoc-doi-thu-2-tap-4-7099_90578.html'
    TV_HAY_VIDEO_URL = 'http://tvhay.org/xem-phim-dao-kiem-than-vuc-phan-4-421702'
    NGOI_SAO_VN_URL = 'https://ngoisao.vn/video/lieu-linh-bang-qua-dong-nuoc-lu-nguoi-dan-ong-suyt-phai-tra-gia-bang-ca-tinh-mang-273892.htm'
    VTC_VN_VIDEO_URL = 'https://vtc.vn/truyen-hinh-27.html'
    KENH14_VN_VIDEO_URL = 'http://video.kenh14.vn/dang-sau-moi-buc-anh-dep-la-mot-anh-chong-the-nay-day-245984.chn'
    CAFE_VN_VIDEO_URL = 'http://cafef.vn/videos/17236-btv-ngoc-trinh-len-tieng-truoc-tin-don-so-huu-loat-xe-sang-ca-chuc-ty-dong.chn'
    TIN_TUC_ONLINE_VIDEO_URL = 'https://tintuconline.com.vn/video/hoa-hong-tren-nguc-trai-tap-12-thai-doi-tieu-tam-phai-co-trach-nhiem-voi-minh-n-408464.html'
    GIAO_DUC_THOI_DAI_VIDEO_URL = 'https://giaoducthoidai.vn/chuyen-la/tai-xe-ngu-gat-khi-lai-xe-hanh-khach-van-than-nhien-nhu-khong-co-chuyen-gi-4032898-d.html'
    VIDEO_VNEXPRESS_URL = 'https://video.vnexpress.net/tin-tuc/nhip-song/cay-si-co-thu-moc-100-than-3980758.html'
    NEWS_VNEXPRESS_URL = 'https://vnexpress.net/thu-mon-nhan-the-do-vi-bat-bong-ngo-ngan-o-giay-13-4000749.html'
    THANH_NIEN_VIDEO_URL = 'https://video.thanhnien.vn/thoi-su/trom-ga-noi-hang-loat-bi-phat-tu-thi-bo-tron-bi-bat-lai-khi-dang-phuc-vu-trong-quan-karaoke-140814.html'
    DAN_TRI_VIDEO_URL = 'https://dantri.com.vn/video-page.htm'
    NGUOI_LAO_DONG_TV_URL = 'https://tv.nld.com.vn/thoi-su-trong-nuoc/co-to-quoc-den-tay-ngu-dan-huyen-can-gio-14531.htm'
    ANIME_VSUB_TV_URL = 'http://animevsub.tv/phim/tay-du-3194/tap-01-61130.html'
    NHAC_VN_VIDEO_URL = 'https://nhac.vn/video/doi-that-la-phoi-phoi-hoang-yen-chibi-uni5-mvG38e'
    XVIDEOS_DOT_COM_VIDEO_URL = 'https://www.xvideos.es/video50625357/_'
    XNXX_VIDEO_URL = 'http://www.xnxx.es/video-rjo7d8b/step_son_caught_masturbating_shoots_load_into_stepmom_s_panties'
    FR_PORN_HUB_VIDEO_URL = 'https://fr.pornhub.com/view_video.php?viewkey=ph5bd4e9b96091f'
    VLXX_VIDEO_URL = 'http://vlxx.tv/video/bo-oi-con-khong-ngu-duoc/1410/'
    SEX_TOP1_VIDEO_URL = 'http://sextop1.net/tinh-mot-dem-voi-nu-dong-nghiep/'
    SEX_HIHI_VIDEO_URL = 'http://sexhihi.net/nu-sinh-thuc-tap-buoi-dau-lam-da-bi-sep-dit.html'
    JAV_HD_PRO_VIDEO_URL = 'http://javhd.pro/phim-sex-au-my---anh-chu-nha-kho-tinh-lanna-carter-1536.html'
    PHIM_SEX_PORN_VIDEO_URL = 'http://phimsexporn.com/goi-tinh-nhu-em-thi-sao-phai-tu-choi.html'
    JAV_PHIM_VIDEO_URL = 'http://javphim.net/movie/cha-duong-du-hai-co-con-gai-xinh-dep/'
    TIN_MOI_VIDEO_URL = 'https://www.tinmoi.vn/video/video-giai-tri/mo-hai-cao-thai-ha-huong-dan-cach-an-che-ma-khong-bi-troi-son-moi-011530843.html'
    INFO_NET_VIDEO_URL = 'https://infonet.vn/video-giay-phut-xe-bon-lao-vao-nha-dan-no-tung-va-lam-chet-6-nguoi-post282661.info'
    BONG_DA_24H_VIDEO_URL = 'https://bongda24h.vn/doi-tuyen-viet-nam/video-biet-doi-chan-thuong-tap-luyen-duoi-su-tro-giup-cua-bac-si-choi-292-231874.html'
    KEO_NHA_CAI_VIDEO_URL = 'http://keonhacai.net/video-real-madrid-vs-psg-5879.html'
    DAILY_MOTION_VIDEO_URL = 'https://www.dailymotion.com/video/x7lxiix'
    VOV_VIDEO_URL = 'https://vov.vn/the-thao/bong-da/hlv-park-hang-seo-da-tim-thay-phan-van-duc-moi-cho-u22-viet-nam-960993.vov'
    SEX_NGON_VIDEO_URL = 'https://sexngon.net/phim-sex-my-hay-lop-hoc-tinh-duc-danh-cho-cac-quy-co/'
    WEIBO_VIDEO_URL = 'https://www.weibo.com/1640601392/I9rIXuIRC?from=page_1002061640601392_profile&wvr=6&mod=weibotime&type=comment'
    ANIME_TVN_VIDEO_URL = 'https://animetvn.tv/xem-phim/f152111-circlet-princess-tap-01.html'
    PHIM_BAT_HU_VIDEO_URL = 'https://phimbathu.org/phim-tinh-yeu-voi-ke-bat-coc-tap-1-11480.135976.html'
    PHIM_SEX_SUB_VIDEO_URL = 'https://phimsexsub.com/quay-clip-vo-lam-ky-niem-hana-aoyama/'
    VLIVE_TV_VIDEO_URL = 'https://www.vlive.tv/video/150718'
    ANIME_HAY_TV_VIDEO_URL = 'http://animehay.tv/phim/black-clover-tap-1-e45482.html'
    DOI_SONG_PHAP_LUAT_VIDEO_URL = 'https://www.doisongphapluat.com/video/video-hot/video-rung-tim-vi-khoanh-khac-doi-ban-than-2-tuoi-chay-toi-om-cham-lay-nhau-sau-2-ngay-xa-cach-a292398.html'
    SAO_STAR_VIDEO_URL = 'https://saostar.vn/am-nhac/fan-khoc-thet-voi-bts-doll-phien-ban-album-answer-6388198.html'
    VIET_SUB_TV_VIDEO_URL = 'https://vietsubtv.org/xem-phim/doi-mat-12204/tap-3.html'
    HENTAIZ_NET_VIDEO_URL = 'https://hentaiz.net/kutsujoku/xem-phim/tap-1.html'
    VTV16_INFO_VIDEO_URL = 'http://vtv16.info/phim/ve-nha-di-con-tron-bo-7116/xem-phim.html'
    BESTIE_VN_VIDEO_URL = 'https://bestie.vn/2019/06/giam-thieu-tinh-trang-rang-e-buot-tai-nha-video'
    CLIP_ANIME_VN_VIDEO_URL = 'https://clipanime.com/video/177008'
    VTV_GO_VN_VIDEO_URL = 'https://vtvgo.vn'
    XEM_VTV_NET = 'http://ww.xemvtv.net/xem-phim/nhan-sinh-cua-bach-ho-ly-tap-1/UUWOI65.html'
    OK_RU = 'https://ok.ru/video/2394372770490'


class ExtensionIds:
    SAVIOR_EXTENSION_ID = 'jdfkmiabjpfjacifcmihfdjhpnjpiick'


class SkypeGroupIds:
    COCCOC_MUSIC_GROUP_ID = '19:3cdd71db361c4d56ad8a69a7cf271c0f@thread.skype'
    TEST_GROUP_ID = '19:c4cf2ed7ac634b7f8efbd7afcaabdebd@thread.skype'


class CocCocComponents:
    THIRD_PARTY_MODULE_LIST_ID = 'ehgidpndbllacpjalkiimkbadgjfnnmc'
    ORIGIN_TRIALS_ID = 'llkgjffcdpffmhiakmfcdcblohccpfmo'


class ChromeStoreUrls:
    RUNG_RINH_EXTENSION_URL = 'https://chrome.google.com/webstore/detail/r%E1%BB%A7ng-r%E1%BB%89nh-d%E1%BB%8Bch-v%E1%BB%A5-ho%C3%A0n-ti/paenbjlckelooppiepeiechkeehogoha'
    ADSBLOCKPLUS_EXTENSION_URL = 'https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb'

class CocCocExtensions:
    AD_BLOCK_STANDARD_MODE = 'Standard'
    AD_BLOCK_STRICT_MODE = 'Strict'