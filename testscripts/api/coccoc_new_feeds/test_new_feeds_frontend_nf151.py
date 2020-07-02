from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewFeedRedis;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_FE_USER_FEED

class TestFrontendApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    new_feed_redis = NewFeedRedis()
    common = NewFeedCommon()

    # NF-151: [Frontend API] Update user feed for return liked (0,1)
    def test_get_frontend_userfeed(self):
        result = True
        vid = 'Q95CoUyM1CMMd1oCQd1d75M13QQyJQbd7Q9JWNxHKa2yhS2HQ9ks24tiMkYWW'
        sid = 'kbqcwomv1ikvdz0o8'
        page = 0
        size = 1000
        api_url = COCCOC_NEW_FEED_API_FE_USER_FEED + vid + '&sid=' + sid + '&page=' + str(page) + '&size=' + str(size)
        print(api_url)
        api_data = self.new_feed_api.request_get_new_feeds(api_url)
        redis_data = self.new_feed_redis.get_redis_smembers('NRE:USER_LIKE_ARTICLES:%s' %vid)
        redis_data = self.common.convert_byte_to_string(redis_data)
        self.common.print_list(redis_data)

        list_title = []
        for i in range(len(api_data['news'])):
            api_id = api_data['news'][i]['id']
            api_liked = api_data['news'][i]['liked']
            if api_liked == 1:
                print(api_id, " : ", api_liked)
            if api_id in redis_data:
                if api_liked == 0:
                    print("ERROR: ", api_id, " : ", api_liked)
                    result = False
            else:
                if api_liked == 1:
                    print("ERROR: ", api_id, " : ", api_liked)
                    result = False

        assert result == True
