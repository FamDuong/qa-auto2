from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewsFeedRedis;

class TestNewFeedCralwer:
    common = NewFeedCommon()
    newfeed_db = NewFeedDB()

    # Not implemented yet, test later