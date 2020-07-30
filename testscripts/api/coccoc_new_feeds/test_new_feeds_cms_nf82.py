import time
import random
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_CMS_INIT_USER

class TestCmsApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()

    # NF-82: [CMS API] Create API to allow user to init user setting
    def test_init_user_if_not_existed(self, coccoc_new_feeds_db_interact):
        result = True
        data = self.new_feed_api.set_vid_data()
        vid = self.common.get_data(data, "vid")
        print("vid : ", vid)

        response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_INIT_USER, data)
        print(response)
        # Get active category
        db_category_active = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from categories where status = "active";')
        # Check user_categories inserted for new user
        db_user_category = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from user_categories where vid = "{vid}";')
        print("    active category : ", db_category_active)
        print("    user category   : ", db_user_category)
        if db_category_active != db_user_category:
            print("ERROR: vid is created NOT successfully")
            # print("    active category : ", db_category_active)
            # print("    user category   : ", db_user_category)
            result = False
        assert response == 200
        assert result == True

    # NF-82: [CMS API] Create API to allow user to init user setting
    def test_init_user_if_existed(self, coccoc_new_feeds_db_interact):
        result = True
        data = self.new_feed_api.set_vid_data()
        vid = self.common.get_data(data, "vid")
        print("vid : ", vid)

        # Insert new user many times
        for i in range (1, 10) :
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_INIT_USER, data)
            if response == 200:
                print("ERROR: response code is invalid")
                result = False
            time.sleep(3)

        # Check number of active categories
        db_category_active = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from categories where status = "active";')
        # Check final vid insert
        db_user_category = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select category_id from user_categories where vid = "{vid}";')
        if len(db_user_category) != len(db_category_active):
            print("ERROR: vid is inserted")
            print("    active category : ", db_category_active)
            print("    user category   : ", db_user_category)
            result = False
        assert result == True

