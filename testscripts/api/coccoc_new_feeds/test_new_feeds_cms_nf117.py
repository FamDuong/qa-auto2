import time
import random
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;

from config.environment import COCCOC_NEW_FEED_API_CMS_WHITELIST_DOMAIN

class TestCmsApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()

    # NF-117: [CMS API] Get list domains
    def test_get_whitelist_domain(self, coccoc_new_feeds_db_interact):
        result = True
        api_data = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_WHITELIST_DOMAIN)
        db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select domain from sources where status = "active";')
        list_db_domain = self.new_feed_db.get_list_db(db_data)
        print(api_data)
        print(list_db_domain)
        if api_data != list_db_domain:
            print("ERROR: Incorrect whitelist domain")
            result = False
        assert result == True


