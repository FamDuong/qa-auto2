from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewsFeedRedis;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewsFeedAPI;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_kafka import NewsFeedKafka;
from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
import json
from datetime import datetime

from config.environment import COCCOC_NEW_FEED_API_FE_USER_FEED
from config.environment import COCCOC_NEW_FEED_API_FE_USER_SETTING
from config.environment import COCCOC_NEW_FEED_BUCKET_URL
from config.environment import COCCOC_NEW_FEED_API_NRE_DEFAULT
from config.environment import COCCOC_NEW_FEED_API_NRE_ARTICLE_INFOMATION
from config.environment import COCCOC_NEW_FEED_API_CMS_USER_ACTION

class TestFrontEndApi:
    newsfeed_api = NewsFeedAPI()
    newsfeed_db = NewFeedDB()
    newsfeed_redis = NewsFeedRedis()
    newsfeed_kafka = NewsFeedKafka()
    common = NewFeedCommon()
    result = True

    # Set filename
    def set_filename(self, attribute):
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y%m%d%H%M%S")
        filename = "Data/" + attribute + "_" + timestamp + ".txt"
        self.common.remove_file(filename)
        return filename

    # 3. Get user feed: Front end from Cache
    # (config auto expired time 30min)
    # If Redis is online: Check if existed data of P4 with key = NRE:USER:ARTICLES:$vid.
    def test_get_user_feed(self):
        list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by update_time desc limit 100;")
        list_editor = []
        list_article_id = []
        for vid in list_vid:
            params = self.newsfeed_api.set_user_feed_data(vid)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)

            # print(params)
            # print(api_data)
            # Need to verify news information, lazy lady .. to be continues
            # ...
            # Input data from recommendation
            # P1. namespace: NRE:USERS
            print("P1. namespace: NRE:USERS")
            redis_data = self.newsfeed_redis.redis_lrange("NRE:USER:" + vid, format_data=None)
            print(redis_data)

            # P2. NRE:GENERAL
            redis_data = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)
            editor = self.common.split_string_in_list(redis_data, "@@", 1)
            list_editor.extend(editor)

            # P4. Data for each session id of users
            print("P4. Data for each session id of users")
            redis_data = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)
            print(redis_data)

            # P5: like articles by user
            print("P5: like articles by user")
            redis_data = self.newsfeed_redis.redis_smembers("NRE:USER_LIKE_ARTICLES:" + vid)
            print(redis_data)
        list_editor = self.common.remove_duplicated_items_in_list(list_editor)
        list_article_id = self.common.remove_duplicated_items_in_list(list_article_id)
        print(list_editor)
        for editor in list_editor:
            redis_data = self.newsfeed_redis.redis_lrange("NRE:GENERAL:" + editor, format_data=None)
            print(editor, ": ", redis_data)
        # P3. ( Store recommended NRE_ARTICLE) HSET: namespace: NRE:ARTICLES
        # for article_id in list_article_id:
        #     redis_data = self.newsfeed_redis.redis_get("NRE:ARTICLE:" + article_id, format_data=None)
        #    print(redis_data)

        # P4. Data for each session id of users


    # 3. Get user feed: Front end from Cache
    # (config auto expired time 30min)
    # If Redis is online: Check if existed data of P4 with key = NRE:USER:ARTICLES:$vid.
    # (T.B.D) if result is last page then remove cache P4 with key = NRE:USER:ARTICLES:$vid to refresh this list and get new data for next time
    # NF-277: [Frontend Api] Update nre api for return editor choices
    def test_get_user_feed_with_existed_vid(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by update_time desc limit 100;")
        for vid in list_vid:
            params = self.newsfeed_api.set_user_feed_data(vid)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]
            # Check if existed data of P4 with key = NRE:USER:ARTICLES:$vid. If existed then
            # P4. Data for each session id of users
            print("P4. Data for each session id of users")
            redis_user_articles = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)

            if not len(redis_user_articles):
                continue
            list_article_id = self.common.split_string_in_list(redis_user_articles, "@@", 0)
            list_editor = self.common.split_string_in_list(redis_user_articles, "@@", 1)

            print("P5: like articles by user")
            redis_user_like_articles = self.newsfeed_redis.redis_smembers("NRE:USER_LIKE_ARTICLES:" + vid)

            print("len(api_data): ", len(api_data_articles))
            for i in range(len(api_data_articles)):
                # print(i)
                article_id = self.common.get_dict(api_data_articles[i], "id")
                if article_id == None:
                    self.common.append_to_file(filename, "ERROR: Cannot get article_id", type="string")
                    break
                liked = 0
                if article_id in redis_user_like_articles:
                    liked = 1

                redis_article = self.newsfeed_redis.redis_get("NRE:ARTICLE:" + article_id)
                article_editor = self.common.get_reference_data_in_list(list_article_id, list_editor, article_id)
                article_editor = article_editor[0]
                article_addition = {'type': article_editor,
                                    'liked': liked}
                redis_article.update(article_addition)
                self.verify_article_data(api_data_articles[i], redis_article, filename)
                # print(redis_article)
        # (T.B.D) if result is last page then remove cache P4 with key = NRE:USER:ARTICLES:$vid to refresh this list and get new data for next time\
        if self.common.check_file_is_existed(filename) != "None":
            self.result = False
        assert self.result == True

    # 3. Get user feed: Front end from Cache
    # *) If not existed P4 with key = NRE:USER:ARTICLES:$vid then
    def test_get_user_feed_with_not_existed_vid(self):
        filename = self.set_filename("Userfeed_notvid")
        sample_article_rate_db = self.common.get_list_newsfeed_db("SELECT value FROM coccoc_news_feed.configs where name = 'SAMPLE_ARTICLE_RATE';")
        sample_article_rate_db = sample_article_rate_db[0]
        print("SAMPLE_ARTICLE_RATE: ", sample_article_rate_db)
        # list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by update_time desc limit 10;")
        for loop in range(10):
            params = self.newsfeed_api.set_user_feed_data()
            vid = params["vid"]
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]
            print(api_data_articles)
            # Check if existed data of P4 with key = NRE:USER:ARTICLES:$vid. If not existed then
            # P4. Data for each session id of users
            # print("P4. Data for each session id of users")
            # redis_user_articles = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)

            # Get list editor choices articles from P2 with key = NRE:GENERAL:editor
            redis_list_editor = self.newsfeed_redis.redis_lrange("NRE:GENERAL:editor")
            # Get list interest articles from P1 with key = NRE:USERS:$vid => lstInterest
            redis_list_interest = self.newsfeed_redis.redis_lrange("NRE:USERS:" + vid)
            # Get list popular articles from P2 with key = NRE:GENERAL:popular
            redis_list_popular = self.newsfeed_redis.redis_lrange("NRE:GENERAL:popular")
            # Get list sampling articles from P2 with key = NRE:GENERAL:sample
            redis_list_sample = self.newsfeed_redis.redis_lrange("NRE:GENERAL:sample")
            # Get list subscribe categories with key = NRE:USER_CATEGORIES:$vid => sub_cates
            redis_list_user_subcribe_category = self.newsfeed_redis.redis_lrange("NRE:USER_CATEGORIES:" + vid)
            # Get list block sources with key = NRE:USER_BLOCK_SOURCES:$vid => unsub_domains
            redis_list_user_block_source = self.newsfeed_redis.redis_lrange("NRE:USER_BLOCK_SOURCES:" + vid)
            # Get list block articles with key = NRE:USER_BLOCK_ARTICLES:$vid => unsub_articles
            redis_list_user_block_article = self.newsfeed_redis.redis_lrange("NRE:USER_BLOCK_ARTICLES:" + vid)
            #print(vid)
            #print(redis_list_editor)
            #print(redis_list_interest)
            #print(redis_list_popular)
            #print(redis_list_sample)
            #print(redis_list_user_subcribe_category)
            #print(redis_list_user_block_source)
            #print(redis_list_user_block_article)

            # Get userfeed setting
            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=json.loads(params))
            print(api_user_setting)

            list_different = []
            # If sub_cates & unsub_domains & unsub_articles don't have value then
            if not(len(redis_list_user_subcribe_category)) and not(len(redis_list_user_block_source)) and not(len(redis_list_user_block_article)):
                print("Case 1: If sub_cates & unsub_domains & unsub_articles don't have value then")
                list_sample = []
                list_sample.extend(redis_list_editor)
                list_sample.extend(redis_list_interest)
                list_sample.extend(redis_list_popular)
                list_sample = self.common.remove_duplicated_items_in_list(list_sample)
                sample_article_rate = int(sample_article_rate_db * len(list_sample) / 100)
                print("sample_article_rate: ", sample_article_rate)
                list_merge = [ list_sample[i] for i in range(sample_article_rate) ]
                # print(list_merge)
                list_sample.extend(list_merge)
                list_sample.extend(redis_list_sample)
                list_sample = self.common.remove_duplicated_items_in_list(list_sample)

                redis_user_articles = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)
                redis_user_articles_id = self.common.split_string_in_list(redis_user_articles, "@@", 0)
                # self.result = self.common.check_if_lists_are_different(list_sample, redis_user_articles_id)
                list_different = [item for item in redis_user_articles_id if str(item) not in list_sample]
                self.common.print_list(list_different)
            # Else If existed user setting then need filter popular & sampling by user setting
            elif len(api_user_setting):
                print("Case 2: Else If existed user setting then need filter popular & sampling by user setting")
                list_sample = []
                redis_list_popular_article = []   # Get list sample article from application cache => lstSampleArtile (T.B.D)
                if not len(redis_list_popular_article):
                    redis_list_popular_article = redis_list_popular
                redis_list_sample_article = []  # Get list editor articles from application cache => lstEditorArticle (T.B.D)
                if not len(redis_list_sample_article):
                    redis_list_sample_article = redis_list_sample
                redis_list_editor_article = [] # Get list editor articles from application cache => lstEditorArticle (T.B.D)
                if not len(redis_list_editor_article):
                    redis_list_editor_article = redis_list_editor
                list_sample.extend(redis_list_popular_article)
                list_sample.extend(redis_list_sample_article)
                list_sample.extend(redis_list_editor_article)
                list_sample = self.common.remove_duplicated_items_in_list(list_sample)
                sample_article_rate = int(sample_article_rate_db * len(list_sample) / 100)
                list_merge = [list_sample[i] for i in range(sample_article_rate)]
                list_sample.extend(list_merge)
                list_sample.extend(redis_list_sample_article)

                redis_user_articles = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)
                redis_user_articles_id = self.common.split_string_in_list(redis_user_articles, "@@", 0)
                self.result = self.common.check_if_lists_are_different(list_sample, redis_user_articles_id)
                list_different = [item for item in redis_user_articles_id if str(item) not in list_sample]
                self.common.print_list(list_different)

            if len(list_different):
                self.result = False
        assert self.result == True

    # If Redis is not working (offline) then process get feed from NRE api
    def test_get_user_feed_if_redis_not_working(self):
        list_vid = self.common.get_list_newsfeed_db(
            "SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by update_time desc limit 10;")

        api_popular_articles = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_NRE_DEFAULT)
        api_popular_articles = api_popular_articles["NRE:GENERAL:popular"]
        list_api_article_information = []

        i = 0
        for article_id in api_popular_articles:
            i += 1
            if i > 10:
                break
            api_article_information = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_NRE_ARTICLE_INFOMATION, params={"ids": article_id})
            list_api_article_information.append(api_article_information)
            print(api_article_information)

        for vid in list_vid:
            # Get from frontend api
            params = self.newsfeed_api.set_user_feed_data(vid)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            api_data_articles = api_data["news"]

            # Get from NRE
            # list_correct_article = []
            list_category_db = self.common.get_list_newsfeed_db(f'select category_id from user_categories where vid = "{vid}";')
            list_block_source_db = self.common.get_list_newsfeed_db(f'SELECT domain FROM user_block_sources WHERE vid = "{vid}";')
            list_block_article_db = self.common.get_list_newsfeed_db(f'SELECT article_id FROM coccoc_news_feed.user_block_articles where vid = "{vid}" '
                                                                     f'union SELECT article_id FROM coccoc_news_feed.user_complaint_articles where vid = "{vid}";')
            list_correct_article = [item for item in list_api_article_information if self.common.get_dict(item, "category_id") in list_category_db and self.common.get_dict(item, "domain") not in list_block_source_db
                           and self.common.get_dict(item, "article_id") not in list_block_article_db]
            # list_correct_article.extend(list_filter)
            #list_filter = [item for item in list_api_article_information if self.common.get_dict(item, "domain") not in list_block_source_db]
            #list_correct_article.extend(list_filter)
            #list_filter = [item for item in list_api_article_information if self.common.get_dict(item, "article_id") not in list_block_article_db]
            #list_correct_article.extend(list_filter)
            #list_correct_article = self.common.remove_duplicated_items_in_list(list_correct_article)
            print(list_correct_article)

            # Check if data is correct
            self.result = self.common.check_if_lists_are_different(list_correct_article, api_data_articles)
        assert self.result == True

    def verify_article_data(self, api_data, redis_data, filename):
        # print(api_data["id"])
        # print(redis_data["id"])
        self.verify_article_element(api_data, redis_data, "category_id", filename)
        self.verify_article_element(api_data, redis_data, "domain", filename)
        self.verify_article_element(api_data, redis_data, "title", filename)
        self.verify_article_element(api_data, redis_data, "description", filename)
        self.verify_article_element(api_data, redis_data, "url", filename)
        self.verify_article_element(api_data, redis_data, "image_url", filename)
        self.verify_article_element(api_data, redis_data, "color_background", filename)
        self.verify_article_element(api_data, redis_data, "color_text", filename)
        self.verify_article_element(api_data, redis_data, "event_time", filename)
        self.verify_article_element(api_data, redis_data, "id", filename)
        self.verify_article_element(api_data, redis_data, "category", filename)
        self.verify_article_element(api_data, redis_data, "source", filename)
        self.verify_article_element(api_data, redis_data, "type", filename)
        self.verify_article_element(api_data, redis_data, "liked", filename)

    def verify_article_element(self, api_data, redis_data, element_name, filename):
        error_log = []
        try:
            redis_data_element = redis_data[element_name]
            api_data_element = api_data[element_name]
        except:
            redis_data_element = ""
            api_data_element = ""
        if element_name == "image_url":
            if "{BUCKET_URL}" in redis_data_element:
                redis_data_element = redis_data_element.replace("{BUCKET_URL}", COCCOC_NEW_FEED_BUCKET_URL)
            else:
                error_log.append("ERROR: {BUCKET_URL} string still in url_image")
                error_log.append("    Api article_id  :   %s " % api_data["id"])
                error_log.append("    Redis article_id:   %s " % redis_data["id"])
                self.common.append_to_file(filename, error_log)
        if api_data_element != redis_data_element:
            error_log.append("ERROR: %s is not matched between api and redis" % element_name)
            error_log.append("    Api article_id  :   %s " % api_data["id"])
            error_log.append("    Redis article_id:   %s " % redis_data["id"])
            error_log.append("    Api:   %s " % api_data_element)
            error_log.append("    Redis: %s " % redis_data_element)
            self.common.append_to_file(filename, error_log)


    # NF-83: block_article
    # NF-288: [Frontend Api] Allow block multiple sources & update single api for return user setting
    # Allow send list current block sources for update user setting
    def test_post_user_actions_block_article(self):
        # Get list vid
        list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by rand() limit 10;")
        list_domain_db = self.common.get_list_newsfeed_db("SELECT domain FROM coccoc_news_feed.sources order by rand() limit 5;")

        for vid in list_vid:
            params = self.set_user_actions_data(vid, "block_source", list_domain_db)
            response = self.newsfeed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION, data=params)

            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=params)
            list_domain_api = []
            for i in range(len(api_user_setting["block_sources"])):
                list_domain_api.append(api_user_setting["block_sources"][i]["domain"])

            list_block_source_db = self.common.get_list_newsfeed_db(f"SELECT domain FROM coccoc_news_feed.user_block_sources where vid = '{vid}';")
            self.result = self.common.check_if_lists_are_different(list_domain_db, list_domain_api)
            self.result = self.common.check_if_lists_are_different(list_domain_db, list_block_source_db)
        assert self.result == True

    # NF-288: [Frontend Api] Allow block multiple sources & update single api for return user setting
    # Update return all categories in user_settings api
    def test_post_user_setting_all_categories(self):
        # Vid is existed
        list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by rand() limit 100;")
        list_categories_db = self.newsfeed_db.select_newfeeds_db("SELECT category_id, name, image_url FROM coccoc_news_feed.categories where status = 'active' group by name;")
        list_categories_id_db = self.newsfeed_db.get_list_db(list_categories_db, 0)
        list_categories_name_db = self.newsfeed_db.get_list_db(list_categories_db, 1)
        list_categories_image_url_db = self.newsfeed_db.get_list_db(list_categories_db, 2)
        list_categories_image_url_db = self.common.replace_string_in_list(list_categories_image_url_db, "{BUCKET_URL}", COCCOC_NEW_FEED_BUCKET_URL)
        redis_list_categories = self.newsfeed_redis.redis_get("LIST:CATEGORIES")
        redis_list_categories = redis_list_categories[0]["categories"]

        redis_list_categories_id = []
        redis_list_categories_name = []
        redis_list_categories_image_url = []
        for i in range(len(redis_list_categories)):
            redis_list_categories_id.append(redis_list_categories[i]["id"])
            redis_list_categories_name.append(redis_list_categories[i]["name"])
            redis_list_categories_image_url.append(redis_list_categories[i]["image_url"])


        self.result = self.common.check_if_lists_are_different(redis_list_categories_id, list_categories_id_db)
        self.result = self.common.check_if_lists_are_different(redis_list_categories_name, list_categories_name_db)
        self.result = self.common.check_if_lists_are_different(redis_list_categories_image_url, list_categories_image_url_db)
        if not self.result:
            print("ERROR: ALL CATEGORIES: DB and redis are incorrect")

        # Compare redis & DB

        for vid in list_vid:
            print(vid)
            # Get user setting
            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=params, wait=0)


            # Check all categories
            api_list_categories = api_user_setting["all_categories"][0]["categories"]
            if api_list_categories != redis_list_categories:
                print("ERROR: ALL CATEGORIES: Redis and api are incorrect")
                print("    api  : ", api_list_categories)
                print("    redis: ", redis_list_categories)
                self.result = False
            # List sub categories
            list_sub_categories_db = self.common.get_list_newsfeed_db(f"SELECT category_id FROM coccoc_news_feed.user_categories where vid = '{vid}';")
            api_sub_categories =  api_user_setting["sub_categories"]
            self.result = self.common.check_if_lists_are_different(list_sub_categories_db, api_sub_categories)
            if not self.result:
                print("ERROR: SUB CATEGORIES: DB and api are incorrect")
                print("    api  : ", api_sub_categories)
                print("    db   : ", list_sub_categories_db)

        assert self.result == True

    def set_user_actions_data(self, vid, action_type, domains):
        # list_actions_normal = ['like_article', 'cancel_like_article', 'block_article', 'cancel_block_article']
        list_actions_source = ['block_source', 'cancel_block_source']
        if action_type in list_actions_source:
            data = {'vid': vid,
                    'action_type': action_type,
                    'domains': domains}
        data = json.dumps(data)
        print(data)
        return data