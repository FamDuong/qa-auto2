
class Urls:

    COCCOC_SETTINGS_URL = 'coccoc://settings'
    COCCOC_SETTINGS_DOWNLOAD_URL = 'coccoc://settings/downloads'
    COCCOC_DOWNLOAD_URL = 'coccoc://downloads'
    COCCOC_VERSION_URL = 'coccoc://version/'
    COCCOC_EXTENSIONS = 'coccoc://extensions'
    YOUTUBE_URL = 'https://www.youtube.com/'

    GOOGLE_URL = 'https://www.google.com/'

    NEW_TAB_URL = 'http://coccoc.com/webhp'
    PIRATE_BAY_URL = 'https://www.thepiratebay.asia/search'


class VideoUrls:

    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v=IHNzOHi8sJs'
    NEWS_ZING_VIDEO_URL = 'https://news.zing.vn/video'
    ZING_MP3_VN_VIDEO_URL = 'https://zingmp3.vn/video-clip/Attention-J-Fla/ZW7F76D6.html'

    @classmethod
    def all(cls):
        return [value for name, value in vars(cls).items() if name.isupper()]


class DiffFormatFileUrls:

    FACEBOOK_VIDEO_URL = 'https://www.facebook.com/watch/?v=2350592668328062'
    WEBM_URL = 'http://techslides.com/demos/sample-videos/small.webm'

    @classmethod
    def all(cls):
        return [value for name, value in vars(cls).items() if name.isupper()]


class OtherSiteUrls:

    TWENTY_FOUR_H_VIDEO_URL = 'https://www.24h.com.vn/bong-da/2-clb-viet-nam-thong-tri-afc-cup-bao-chau-a-noi-gi-c48a1061647.html'
    PHIMMOI_VIDEO_URL = 'http://www.phimmoi.net/phim/linh-kiem-ton-8199/xem-phim.html'



