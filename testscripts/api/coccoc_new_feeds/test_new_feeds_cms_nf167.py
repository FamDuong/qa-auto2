import time
import random
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_CMS_BLOCK_ARTICLE


class TestCmsApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()

    # NF-167: [CMS API] Return blocked articles
    def test_get_list_block_article(self, coccoc_new_feeds_db_interact):
        result = True
        api_data = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_BLOCK_ARTICLE)
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select article_id from user_complaint_articles where status = "block" and update_time > date_sub(now(), interval 3 day) and now();')
        db_data = self.new_feed_db.get_list_db(db_data, 0)
        result = self.common.check_if_unordered_lists_are_equal(api_data, db_data)

        if result == False:
            print("ERROR: Data is not correct")
            print("    API : ", api_data)
            print("    DB  : ", db_data)
        assert result == True
