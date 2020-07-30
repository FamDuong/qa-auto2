import time
import random
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_FE_USER_ACTION


class TestFrontendApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()

    # NF-153: subscribe_category: [Frontend API] Validate user subscribe at least 3 categories
    def test_post_user_actions_subscribe_category(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'subscribe_category'
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories limit 3;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        # Get list category ID which contains 2 categories
        db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from coccoc_news_feed.categories order by rand() limit 2;')
        list_category_id_2 = self.new_feed_db.get_list_db(db_data, 0)
        # Get list category ID which contains 3 categories
        db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from coccoc_news_feed.categories order by rand() limit 3;')
        list_category_id_3 = self.new_feed_db.get_list_db(db_data, 0)

        # Check response error if < 3 categories
        for i in range(min(3, len(list_vid))):
            vid = list_vid[i]

            # Check subscribe_category
            user_actions = self.new_feed_api.set_user_actions_data(action_type, categories=list_category_id_2)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_FE_USER_ACTION + vid, user_actions)

            # Validate: the category is updated
            db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from coccoc_news_feed.user_categories where vid = "{vid}";')
            db_data = self.new_feed_db.get_list_db(db_data)

            print("    API : ", vid, " : ", list_category_id_2)
            print("    DB  : ", vid, " : ", db_data)

            result_tmp = self.common.check_if_unordered_lists_are_equal(db_data, list_category_id_2)
            if response != 422:
                print("ERROR: User subscribe_category failed")
                result = False
            if result_tmp == True:
                print("ERROR: User subscribe_category failed")
                result = False

        # Check response error if = 3 categories
        for i in range(min(3, len(list_vid))):
            vid = list_vid[i]

            # Check subscribe_category
            user_actions = self.new_feed_api.set_user_actions_data(action_type, categories=list_category_id_3)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_FE_USER_ACTION + vid,
                                                                        user_actions)

            # Validate: the category is updated
            db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact,
                                                                  f'select category_id from coccoc_news_feed.user_categories where vid = "{vid}";')
            db_data = self.new_feed_db.get_list_db(db_data)

            print("    API : ", vid, " : ", list_category_id_3)
            print("    DB  : ", vid, " : ", db_data)

            result_tmp = self.common.check_if_unordered_lists_are_equal(db_data, list_category_id_3)
            if response != 200:
                print("ERROR: User subscribe_category failed")
                result = False
            if result_tmp == False:
                print("ERROR: User subscribe_category failed")
                result = False

        assert result == True