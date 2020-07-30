import json
import time
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_FE_CATEGORY

class TestFrontendApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()

    # NF-77: [Frontend API] Get categories
    def test_get_categories(self, coccoc_new_feeds_db_interact):
        result = True
        api_categories = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_CATEGORY)

        # Check group display correctly
        db_category = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact,
                                                                  f'select distinct(`group`) from categories where status = "active" order by `order`')
        list_api_groups = self.common.get_list_json_level_1(api_categories, 'group')
        list_db_groups = self.new_feed_db.get_list_db(db_category, 0)
        print("Number of active groups: ", len(list_api_groups))
        if list_api_groups != list_db_groups:
            print("ERROR: Number of active categories are incorrect: ", list_api_groups, list_api_groups)
            result = False