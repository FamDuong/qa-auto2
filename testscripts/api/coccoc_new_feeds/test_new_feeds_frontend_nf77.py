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
    BUCKET_URL = "https://coccoc-image-service.itim.vn"

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

        # Check each element in each group
        for group in list_api_groups:
            print("Group: ", group)
            list_api_categories = self.common.get_list_json_level_2(api_categories, 'group', group, 'categories')

            db_category = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact,
                                                                      f'SELECT category_id , name,	image_url FROM categories WHERE	`group` = "{group}" AND status = "active" order by `order`;')
            # Compare ID
            list_api_categories_id = self.common.get_list_json_level_1(list_api_categories, 'id')
            list_db_categories_id = self.new_feed_db.get_list_db(db_category, 0)
            print("    api ID: ", list_api_categories_id)
            print("    DB  ID: ", list_db_categories_id)
            if list_api_categories_id != list_db_categories_id:
                print("ERROR: ID incorrect: ")
                print("    api: ", list_api_categories_id)
                print("    db : ", list_db_categories_id)
                result = False

            # Compare name
            list_api_categories_name = self.common.get_list_json_level_1(list_api_categories, 'name')
            list_db_categories_name = self.new_feed_db.get_list_db(db_category, 1)
            print("    api name: ", list_api_categories_name)
            print("    DB  name: ", list_db_categories_name)
            if list_api_categories_name != list_db_categories_name:
                print("ERROR: Name incorrect: ")
                print("    api: ", list_api_categories_name)
                print("    db : ", list_api_categories_name)
                result = False

            # Compare url image
            list_api_categories_image_url = self.common.get_list_json_level_1(list_api_categories, 'image_url')
            list_db_categories_image_url = self.new_feed_db.get_list_db(db_category, 2)
            list_db_categories_image_url = [w.replace("{BUCKET_URL}", "https://coccoc-image-service.itim.vn") for w in list_db_categories_image_url]
            print("    api image_url: ", list_api_categories_image_url)
            print("    DB  image_url: ", list_db_categories_image_url)
            if list_api_categories_image_url != list_db_categories_image_url:
                print("ERROR: image_url incorrect: ")
                print("    api: ", list_api_categories_image_url)
                print("    db : ", list_db_categories_image_url)
                result = False
        assert result == True
