
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_CMS_BLACKLIST

class TestCmsApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()

    # NF-116: [CMS API] Get list backlist keywords
    def test_get_list_blacklist(self, coccoc_new_feeds_db_interact):
        result = True
        api_data = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_BLACKLIST, "text")
        db_data = self.new_feed_db.get_newfeeds_db_connection(coccoc_new_feeds_db_interact, f'select keyword from blacklist_keywords where status = "active";')
        list_db_keyword = self.new_feed_db.get_list_db(db_data)

        # print(COCCOC_NEW_FEED_API_CMS_BLACKLIST)
        # print(api_data)
        api_data = api_data.replace("title contains [", ";")
        api_data = api_data.replace("]", "")
        api_data = api_data.replace("----------------------------------------------------------------------", "")
        api_data = api_data.replace('\n\n', "")
        api_data = api_data.split(";")
        api_data = list(filter(None, api_data))

        print("    API : ", api_data)
        print("    DB  : ", list_db_keyword)
        result = self.common.check_if_unordered_lists_are_equal(api_data, list_db_keyword)
        if result == False:
           print("ERROR: Incorrect backlist keywords")
           result = False
        assert result == True