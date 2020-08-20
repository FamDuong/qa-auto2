from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewsFeedRedis;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewsFeedAPI;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_kafka import NewsFeedKafka;
from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
import json
import time

from config.environment import COCCOC_NEW_FEED_API_CMS_PUBLISH_ARTICLE
from config.environment import COCCOC_NEW_FEED_BUCKET_URL
from config.environment import COCCOC_NEW_FEED_KAFKA_TOPIC_CMS
from config.environment import COCCOC_NEW_FEED_KAFKA_TOPIC_USERS
from config.environment import COCCOC_NEW_FEED_KAFKA_TOPIC_NRE
from config.environment import COCCOC_NEW_FEED_API_CMS_USER_SUBCRIBE_CATEGORIES
from config.environment import COCCOC_NEW_FEED_API_CMS_USER_BLOCK_ARTICLES
from config.environment import COCCOC_NEW_FEED_API_CMS_USER_BLOCK_SOURCES
from config.environment import COCCOC_NEW_FEED_API_CMS_EDITOR_CHOISES_FEED

class TestCmsApi:
    newsfeed_api = NewsFeedAPI()
    newsfeed_db = NewFeedDB()
    newsfeed_redis = NewsFeedRedis()
    newsfeed_kafka = NewsFeedKafka()
    common = NewFeedCommon()
    result = True

    # 6. Parse links (Implement as core library) (Already test at crawler)
    # 7. Parse article attributes (Implement as core library) (Already test at crawler)
    # 8. Update category feed (REMOVED)

    # 9. Publish articles to frontend cache
    # Check on Redis
    # Check on Kafka
    def test_publish_articles_to_frontend_cache(self):
        print(COCCOC_NEW_FEED_API_CMS_PUBLISH_ARTICLE)
        # status = "crawled"    # Status to select from DB: testing
        status = "publish"    # Status to select from DB: Only test script
        # list_article_crawled = self.common.get_list_newsfeed_db(f'select article_id from coccoc_news_feed.articles where status = "crawled" limit 10;')
        list_article_db = self.newsfeed_db.select_newfeeds_db(f"SELECT a.article_id as id, a.category_id, b.name as category_name, a.domain, c.name, a.title, a.description, a.url, a.cdn_image_url, a.color_background, a.color_text, a.published_time as event_time FROM articles a INNER JOIN categories b ON b.category_id = a.category_id INNER JOIN sources c ON c.domain = a.domain and a.status = '{status}' limit 2;")
        list_article_id = self.newsfeed_db.get_list_db(list_article_db, 0)
        list_article = self.convert_article_data(list_article_db)

        data = self.newsfeed_api.set_publish_article_data(list_article_id)
        response = self.newsfeed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_PUBLISH_ARTICLE, data)
        # Check on Redis
        for i in range(len(list_article_id)):
            redis = []
            article_id = list_article_id[i]
            query = "NRE:ARTICLE2:%s" % article_id
            redis_data = self.newsfeed_redis.redis_get(query)
            # print(redis_data)
            redis.append(str(redis_data["id"]))
            redis.append(str(redis_data["category"]["category_id"]))
            redis.append(redis_data["category"]["title"])
            redis.append(redis_data["source"]["domain"])
            redis.append(redis_data["source"]["title"])
            redis.append(redis_data["title"])
            redis.append(redis_data["description"])
            redis.append(redis_data["url"])
            redis.append(redis_data["image_url"])
            redis.append(redis_data["color_background"])
            redis.append(redis_data["color_text"])
            redis.append(redis_data["event_time"])

            # print(article_redis)
            print(i)
            self.result = self.common.check_if_lists_are_different(list_article[i], redis)
        # Check on Kafka: Need to update the topic name
        message_expected = self.common.get_kafka_message_cms_api("publish_articles", list_article_id)
        message_actual = self.newsfeed_kafka.get_kafka_messsage(COCCOC_NEW_FEED_KAFKA_TOPIC_CMS)
        if message_expected not in message_actual:
            self.result = False
            print("ERROR: Wrong Kafka message")
            print("    Expected: ", message_expected)
            print("    Actual  : ")
            self.common.print_list(message_actual)
        assert response == 200
        assert self.result == True

    # Convert data
    def convert_article_data(self, list_article_db):
        list_article_id = self.newsfeed_db.get_list_db(list_article_db, 0)
        number_field = len(list_article_id)
        number_rows = len(list_article_db)
        list_article = []
        for i in range(0, number_rows):
            article = []
            for j in range(0, number_field):
                article.append(list_article_db[i][j])
            article = self.common.replace_string_in_list(article, "{BUCKET_URL}", COCCOC_NEW_FEED_BUCKET_URL)
            list_article.append(article)
        return list_article

    # 10: Unpublish articles from frontend cache: Removed

    # 11. Get user subscribe categories: If vid is existed
    # NF-286
    def test_get_user_subscribe_categories_if_vid_existed(self):
        # If vid is existed
        list_vid_categories_db = self.newsfeed_db.select_newfeeds_db(f'select vid, category_id from coccoc_news_feed.user_categories order by vid;')
        list_vid = self.newsfeed_db.get_list_db(list_vid_categories_db, 0)
        list_vid_categories = self.newsfeed_db.get_list_db(list_vid_categories_db, 1)
        self.common.print_list(list_vid)

        for vid in list_vid:
            # Check api return correct data in DB
            vid_data = self.newsfeed_api.set_vid_data(vid, format=None)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_SUBCRIBE_CATEGORIES, params=vid_data)
            print(api_data)
            vid_categories_data = self.get_vid_data(list_vid, list_vid_categories, vid)
            diff = self.common.get_different_elements_between_lists(vid_categories_data, api_data)
            if len(diff):
                print("ERROR: Data is in DB not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    DB   : ", vid_categories_data)
                self.result = False
            # Check data is in Redis
            redis_data = self.newsfeed_redis.redis_get("NRE:USER_CATEGORIES:" + vid)
            diff = self.common.get_different_elements_between_lists(vid_categories_data, redis_data)
            if len(diff):
                print("ERROR: Data is in Redis not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    Redis: ", redis_data)
                self.result = False
        assert self.result == True

    # 11. Get user subscribe categories: If vid is NOT existed
    # NF-286
    def test_get_user_subscribe_categories_if_vid_not_existed(self):
        # If vid is NOT existed
        list_categories_db = self.newsfeed_db.select_newfeeds_db(f'SELECT category_id FROM categories WHERE status = "active" ORDER BY category_id;')
        vid_categories_data = self.newsfeed_db.get_list_db(list_categories_db, 0)

        for i in range(10):
            vid_data = self.newsfeed_api.set_vid_data(vid=None, format=None)
            vid = self.common.get_data(json.dumps(vid_data), "vid")

            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_SUBCRIBE_CATEGORIES, params=vid_data)
            diff = self.common.get_different_elements_between_lists(vid_categories_data, api_data)
            if len(diff):
                print("ERROR: Default categories is in DB not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    DB   : ", vid_categories_data)
                self.result = False
            # Check data is in Redis
            redis_data = self.newsfeed_redis.redis_get("NRE:USER_CATEGORIES:" + vid)
            diff = self.common.get_different_elements_between_lists(vid_categories_data, redis_data)
            if len(diff):
                print("ERROR: Data is in Redis not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    Redis: ", redis_data)
                self.result = False
        assert self.result == True

    # 12. Get block sources by user
    # NF-285
    def test_get_user_block_sources(self):
        list_vid_block_sources_db = self.newsfeed_db.select_newfeeds_db(f'select vid, domain from coccoc_news_feed.user_block_sources order by vid;')
        list_vid_block_sources = self.newsfeed_db.get_list_db(list_vid_block_sources_db, 0)
        list_block_sources = self.newsfeed_db.get_list_db(list_vid_block_sources_db, 1)
        self.common.print_list(list_vid_block_sources)

        for vid in list_vid_block_sources:
            # Check api return correct data in DB
            vid_data = self.newsfeed_api.set_vid_data(vid, format=None)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_BLOCK_SOURCES, params=vid_data)
            block_sources_data = self.get_vid_data(list_vid_block_sources, list_block_sources, vid)
            diff = self.common.get_different_elements_between_lists(block_sources_data, api_data)
            if len(diff):
                print("ERROR: Data is in DB not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    DB   : ", block_sources_data)
                self.result = False
            # Check data is in Redis
            redis_data = self.newsfeed_redis.redis_get("NRE:USER_BLOCK_SOURCES:" + vid)
            diff = self.common.get_different_elements_between_lists(block_sources_data, redis_data)
            if len(diff):
                print("ERROR: Data is in Redis not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    Redis: ", redis_data)
                self.result = False
        assert self.result == True

    # 13. Get block articles by user
    # NF-284
    def test_get_user_block_article(self):
        list_vid_block_articles_db = self.newsfeed_db.select_newfeeds_db(f'select vid, article_id from coccoc_news_feed.user_block_articles where create_time > DATE_ADD(CURRENT_DATE, INTERVAL - 3 DAY) '
                                                                      f'union select vid, article_id from coccoc_news_feed.user_complaint_articles where create_time > DATE_ADD(CURRENT_DATE, INTERVAL - 3 DAY) ')
        list_vid_block_articles = self.newsfeed_db.get_list_db(list_vid_block_articles_db, 0)
        list_block_articles = self.newsfeed_db.get_list_db(list_vid_block_articles_db, 1)
        self.common.print_list(list_vid_block_articles)
        for vid in list_vid_block_articles:
            # Check api return correct data
            vid_data = self.newsfeed_api.set_vid_data(vid, format=None)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_BLOCK_ARTICLES, params=vid_data)
            block_articles_data = self.get_vid_data(list_vid_block_articles, list_block_articles, vid)
            diff = self.common.get_different_elements_between_lists(block_articles_data, api_data)
            if len(diff):
                print("ERROR: Data is in DB not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    DB   : ", block_articles_data)
                self.result = False
            # Check data is in Redis
            redis_data = self.newsfeed_redis.redis_get("NRE:USER_BLOCK_ARTICLES:" + vid)
            diff = self.common.get_different_elements_between_lists(api_data, redis_data)
            if len(diff):
                print("ERROR: Data is in Redis not correct")
                print("    vid  : ", vid)
                print("    API  : ", api_data)
                print("    Redis: ", redis_data)
                self.result = False
        assert self.result == True

    # 15. Update editor choices cache
    def test_update_editor_choices_cache(self):
        # update articles set vote = 1 where status = "publish" and vote=0 order by published_time desc limit 250; Query for update data for testing
        editor_choice_limit = self.common.get_list_newsfeed_db(f'SELECT value FROM coccoc_news_feed.configs where name = "EDITOR_CHOICE_LIMIT";')
        editor_choice_limit = editor_choice_limit[0]
        editor_choice_expired_time = self.common.get_list_newsfeed_db(f'SELECT value FROM coccoc_news_feed.configs where name = "EDITOR_CHOICE_EXPIRED_TIME";')
        editor_choice_expired_time = int(editor_choice_expired_time[0])
        # editor_choice_expired_time = int(300) # Setting for testing script only

        list_article_id = self.common.get_list_newsfeed_db(f'SELECT a.article_id as id FROM articles as a WHERE status = "publish" AND vote = 1 AND published_time > DATE_ADD(now(), INTERVAL - %s hour) ORDER BY a.published_time DESC LIMIT %s;',
                                                           data_query=(editor_choice_expired_time, editor_choice_limit))
        # Send api
        response = self.newsfeed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_EDITOR_CHOISES_FEED)
        redis_data = self.newsfeed_redis.redis_lrange("NRE:GENERAL:editor", 0, -1, format_data=None)
        print(list_article_id)
        print(redis_data)
        # Check on Fontend cache
        diff = self.common.get_different_elements_between_lists(redis_data, redis_data)
        if len(diff):
            print("ERROR: Data is in Redis not correct")
            print("    DB   : ", list_article_id)
            print("    Redis: ", redis_data)
            self.result = False
        print("Number of artice ID on Cache editor choice: ", len(redis_data))
        if len(redis_data) > editor_choice_limit:
            print("ERROR: Number of article ID > editor_choice_limit")
            print("Number of artice ID: ", len(redis_data))
            self.result = False
        assert response == 200
        assert self.result == True

    # 15. Update editor choices cache for each 15 minutes
    def test_update_editor_choices_cache_every_15_minutes(self):
        for i in range(3):
            # Reset the vote
            editor_choice_limit = self.common.get_list_newsfeed_db(f'SELECT value FROM coccoc_news_feed.configs where name = "EDITOR_CHOICE_LIMIT";')
            editor_choice_limit = editor_choice_limit[0]
            editor_choice_expired_time = self.common.get_list_newsfeed_db(f'SELECT value FROM coccoc_news_feed.configs where name = "EDITOR_CHOICE_EXPIRED_TIME";')
            editor_choice_expired_time = int(editor_choice_expired_time[0])
            print(editor_choice_expired_time)
            # Reset the article ID
            self.newsfeed_db.update_newfeeds_db(f'update articles set vote= 0 where status = "publish" and vote= 1 and published_time > DATE_ADD(now(), INTERVAL - %s hour) limit %s;',
                                            data_query=(editor_choice_expired_time, 1000))
            # Update new list article ID
            self.newsfeed_db.update_newfeeds_db(f'update articles set vote = 1 where status = "publish" and vote=0 and published_time > DATE_ADD(now(), INTERVAL - %s hour) order by rand() limit %s;',
            data_query=(editor_choice_expired_time, editor_choice_limit))

            # Wait block time
            time.sleep(1200)

            # Check on Fontend cache
            list_article_id = self.common.get_list_newsfeed_db(
                f'SELECT a.article_id as id FROM articles as a WHERE status = "publish" AND vote = 1 AND published_time > DATE_ADD(now(), INTERVAL - %s hour) ORDER BY a.published_time DESC LIMIT %s;',
                data_query=(editor_choice_expired_time, editor_choice_limit))
            redis_data = self.newsfeed_redis.redis_lrange("NRE:GENERAL:editor", 0, -1, format_data=None)
            diff = self.common.get_different_elements_between_lists(redis_data, redis_data)
            if len(diff):
                print("ERROR: Data is in Redis not correct")
                print("    DB   : ", list_article_id)
                print("    Redis: ", redis_data)
                self.result = False
            print("Number of artice ID on Cache editor choice: ", len(redis_data))
            if len(redis_data) > editor_choice_limit:
                print("ERROR: Number of article ID > editor_choice_limit")
                print("Number of artice ID: ", len(redis_data))
                self.result = False
        assert self.result == True



    # Get data with reference index is vid
    def get_vid_data(self, list_vid, list_data, vid):
        list_vid_data = []
        temp = set(list_vid)
        index = [i for i, val in enumerate(list_vid) if (val in temp and val == vid)]
        # printing result
        # print("The matching element Indices list : " + str(index))
        for i in index:
            list_vid_data.append(list_data[i])
        return list_vid_data
