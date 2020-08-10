from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewsFeedRedis;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewsFeedAPI;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_kafka import NewsFeedKafka;
from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;

from config.environment import COCCOC_NEW_FEED_API_FE_USER_FEED

class TestFrontEndApi:
    newsfeed_api = NewsFeedAPI()
    newsfeed_db = NewFeedDB()
    newsfeed_redis = NewsFeedRedis()
    newsfeed_kafka = NewsFeedKafka()
    common = NewFeedCommon()
    result = True

    # 3. Get user feed
    def test_get_user_feed(self):
        list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by update_time desc limit 10;")
        for vid in list_vid:
            params = self.newsfeed_api.set_user_feed_data(vid)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            print(params)
            print(api_data)
            # Need to verify news information, lazy lady .. to be continues
            # ...
