import json
import time
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_FE_USER_FEED

class TestFrontendApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()

    # NF-138: [API for Frontend] Limit Title and Description
    def test_get_frontend_userfeed(self):
        result = True
        # vid = 'Gy6TVT6r1yuG31oy9u1uCJT1QJ9uJSTrC6oSW2nBb9rofPtd8jQneKDZZdOWW'
        # sid = 'kbq4hb86eof18vasz'
        # vid = 'Q95CoUyM1CMMd1oCQd1d75M13QQyJQbd7Q9JWNxHKa2yhS2HQ9ks24tiMkYWW'
        vid = 'CyJ6JyyGuQ3Q3VCT'
        sid = 'kbsrt8fihybwfx05c'
        page = 10
        size = 50
        for j in range(page):
            api_url = COCCOC_NEW_FEED_API_FE_USER_FEED + vid + '&sid=' + sid + '&page=' + str(j) + '&size=' + str(size)
            print(api_url)
            api_data = self.new_feed_api.request_get_new_feeds(api_url)

            list_title = []
            for i in range(len(api_data['news'])):
                api_title = api_data['news'][i]['title']
                api_description = api_data['news'][i]['description']
                api_url = api_data['news'][i]['url']
                list_title.append(api_title)
                if len(api_title) < 50:
                    print("ERROR: api_title")
                    print("    ", api_url)
                    print("    ", api_title)
                    print("    ", len(api_title))
                    result = False
                if len(api_description) < 50:
                    print("ERROR: api_description")
                    print("    ", api_url)
                    print("    ", api_description)
                    print("    ", len(api_description))
                    result = False
                # Check if null
                if api_title == '':
                    print("ERROR: api_title is null")
                    print("    ", i, ") ", api_url)
                    result = False
                if api_description == '':
                    print("ERROR: api_description is null")
                    print("    ", i, ") ", api_url)
                    result = False
        assert result == True


    # NF-188: [NF] Duplicated news in the newsfeed
    def test_get_frontend_userfeed_duplicated(self, coccoc_new_feeds_db_interact):
        result = True
        # vid = 'Gy6TVT6r1yuG31oy9u1uCJT1QJ9uJSTrC6oSW2nBb9rofPtd8jQneKDZZdOWW'
        # sid = 'kbq4hb86eof18vasz'
        # vid = 'Q95CoUyM1CMMd1oCQd1d75M13QQyJQbd7Q9JWNxHKa2yhS2HQ9ks24tiMkYWW'
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid, count(*) from user_categories group by vid having count(*) = 3 limit 5;;')
        list_db_vid = self.new_feed_db.get_list_db(db_data, 0)
        sid = 'kbqcwomv1ikvdz0o8'
        page = 5
        size = 36
        for vid in list_db_vid:
            for j in range(page):
                api_url = COCCOC_NEW_FEED_API_FE_USER_FEED + vid + '&sid=' + sid + '&page=' + str(j) + '&size=' + str(size)
                print(api_url)
                api_data = self.new_feed_api.request_get_new_feeds(api_url)

                list_url = []
                for i in range(len(api_data['news'])):
                    api_url = api_data['news'][i]['url']
                    print("    ", api_url)
                    list_url.append(api_url)
                result_tmp = self.common.check_if_element_duplicated(list_url)
                if result_tmp == False:
                    print("ERROR: Duplicated article")
                    result = False
        assert result == True

    # NF-162: [NF] "Block source" doesn't work as expected
    def test_get_frontend_block_source_not_display(self):
        result = True
        vid = 'CyJ6JyyGuQ3Q3VCT'
        sid = 'kbsslwm8e9w85tvw3'
        block_source = ['dantri', 'tuoitre', '24h.com.vn', 'kenh14.vn', 'vnexpress.net']
        page = 10
        size = 50
        for j in range(page):
            api_url = COCCOC_NEW_FEED_API_FE_USER_FEED + vid + '&sid=' + sid + '&page=' + str(j) + '&size=' + str(size)
            print(api_url)
            api_data = self.new_feed_api.request_get_new_feeds(api_url)

            list_title = []
            for i in range(len(api_data['news'])):
                api_url = api_data['news'][i]['url']
                # print(api_url)
                for source in block_source:
                    if source in api_url:
                        print("    ERROR: block_source")
                        print("    ", i, ") ", api_url)
                        result = False
        assert result == True