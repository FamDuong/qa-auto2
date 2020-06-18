import json
import time
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import DatafeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedsDB;

from config.environment import COCCOC_NEW_FEED_API_FE_CATEGORY
from config.environment import COCCOC_NEW_FEED_API_FE_USER_SETTING

class TestFrontendApi:
    new_feed_api = DatafeedAPI()
    new_feed_db = NewFeedsDB()
    BUCKET_URL = "https://coccoc-image-service.itim.vn"


    # NF-78	[Frontend API] Get user feed setting
    def test_get_user_feed_setting(self, coccoc_new_feeds_db_interact):
        result = True
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories;')
        list_db_vid = self.new_feed_db.get_list_db(db_data, 0)
        for vid in list_db_vid:
            print(vid)
            # Get from API
            api_data = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING + vid)
            # print(vid, " : ", api_data)
            list_api_sub_category = api_data['sub_categories']
            list_api_sub_category_id = self.new_feed_api.get_list_json_level_1(api_data['sub_categories'], "id")
            list_api_sub_category_name = self.new_feed_api.get_list_json_level_1(api_data['sub_categories'], "name")
            list_api_block_sources_domain = self.new_feed_api.get_list_json_level_1(api_data['block_sources'], "domain")
            list_api_block_sources_title = self.new_feed_api.get_list_json_level_1(api_data['block_sources'], "title")
            # list_api_block_sources = self.new_feed_api.get_list_json_level_1(api_data, "block_sources")

            # Get from DB
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select category_id, name from categories where category_id in (select category_id from user_categories where vid = "{vid}");')
            list_db_sub_category_id = self.new_feed_db.get_list_db(db_data, 0)
            list_db_sub_category_name = self.new_feed_db.get_list_db(db_data, 1)
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact,
                                                       f'SELECT	b.domain, b.name, b.logo_url FROM user_block_sources a INNER JOIN sources b ON b.domain = a.domain '
                                                       f'AND b.status = "active" WHERE a.vid = "{vid}";')
            list_db_block_sources_domain = self.new_feed_db.get_list_db(db_data, 0)
            list_db_block_sources_title = self.new_feed_db.get_list_db(db_data, 1)

            result_tmp = self.new_feed_api.check_if_element_different_in_lists(list_api_sub_category_id, list_db_sub_category_id)
            if result_tmp is False:
                print("    ERROR: Sub category id are incorrect")
                print("    api:", list_api_sub_category_id)
                print("    db :", list_db_sub_category_id)
                result = False
            result_tmp = self.new_feed_api.check_if_element_different_in_lists(list_api_sub_category_name, list_db_sub_category_name)
            if result_tmp is False:
                print("    ERROR: Sub category name are incorrect")
                print("    api:", list_api_sub_category_name)
                print("    db :", list_db_sub_category_name)
                result = False
            result_tmp = self.new_feed_api.check_if_element_different_in_lists(list_api_block_sources_domain, list_db_block_sources_domain)
            if result_tmp is False:
                print("    ERROR: Block source domains are incorrect")
                print("    api:", list_api_block_sources_domain)
                print("    db :", list_db_block_sources_domain)
                result = False
            result_tmp = self.new_feed_api.check_if_element_different_in_lists(list_api_block_sources_title, list_db_block_sources_title)
            if result_tmp is False:
                print("    ERROR: Block source domains are incorrect")
                print("    api:", list_api_block_sources_title)
                print("    db :", list_db_block_sources_title)
                result = False

        assert result == True

    # NF-78	[Frontend API] Get user feed setting - if vid not exist
    def test_get_user_feed_setting(self, coccoc_new_feeds_db_interact):
        result = True
        # Generate a new vid
        data = self.new_feed_api.set_vid_data()
        vid = self.new_feed_api.get_data(data, "vid")
        print(vid)

        api_data = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING + vid)
        time.sleep(5)
        # Check again
        # Get number of active category
        db_category_active = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select category_id from categories where status = "active";')
        # Check number of rows inserted for new user
        db_user_category = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select category_id from user_categories where vid = "{vid}";')
        print(db_category_active)
        print(db_user_category)
        if db_user_category != db_category_active:
            print("ERROR: No new user is created")
            print("    api category : ", db_category_active)
            print("    db category  : ", db_user_category)
            result = False
        assert result == True





