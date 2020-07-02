import time
import random
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;

from config.environment import COCCOC_NEW_FEED_API_CMS_USER_ACTION

# NF-83: [CMS API] Create API to save user's actions
class TestCmsApi:
    new_feed_api = NewFeedAPI()
    new_feed_db = NewFeedDB()
    common = NewFeedCommon()


    # NF-83: like_article
    def test_post_user_actions_like_article(self, coccoc_new_feeds_db_interact):
        result = True
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories order by rand() limit 10;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        # Get list article ID
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select article_id from articles order by rand() limit 10;')
        list_article_id = self.new_feed_db.get_list_db(db_data)

        # Check like_article
        print("Check like_article")
        list_user_like_articles = []
        article_id = self.common.get_random_element(list_article_id)
        for i in range(3):
            vid = random.choice(list_vid)
            list_user_like_articles.append(vid)
            # Check like_article
            user_actions = self.new_feed_api.set_user_actions_data('like_article', article_id)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
        # Validate: Not correct but don't know how to check
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid from user_like_articles where article_id = "{article_id}";')
        db_data = self.new_feed_db.get_list_db(db_data)
        list_user_like_articles = self.common.remove_duplicated_items(list_user_like_articles)
        print("    API : ", list_user_like_articles)
        print("    DB  : ", db_data)
        result_tmp = self.common.check_is_sublist(db_data, list_user_like_articles)
        if result_tmp == False:
            print("ERROR: Insert into user_like_articles failed")
            result = False

        assert result == True

    # NF-83: cancel_like_article
    def test_post_user_actions_cancel_like_article(self, coccoc_new_feeds_db_interact):
        result = True
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid, article_id from user_like_articles limit 10;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        list_article_id = self.new_feed_db.get_list_db(db_data, 1)

        # Check like_article
        print("Check cancel_like_article")
        list_user_cancel_like_articles = []
        # article_id = self.new_feed_api.get_random_element(list_article_id)
        # print("article_id : ", article_id)
        for i in range(min(3, len(list_vid))):
            vid = list_vid[i]
            article_id = list_article_id[i]
            print(vid, ": ", article_id)

            # Check cancel_like_article
            user_actions = self.new_feed_api.set_user_actions_data('cancel_like_article', article_id)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
            list_user_cancel_like_articles.append(vid)
            # Validate: Not correct but don't know how to check
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid from user_like_articles where article_id = "{article_id}";')
            db_data = self.new_feed_db.get_list_db(db_data)

            result_tmp = self.common.check_if_lists_are_different(db_data, list_user_cancel_like_articles)
            if result_tmp == False:
                print("ERROR: User cancel_like_article failed")
                print("    API : ", list_user_cancel_like_articles)
                print("    DB  : ", db_data)
                result = False

        assert result == True

    # NF-83: block_article
    def test_post_user_actions_block_article(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'block_article'
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories limit 10;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        # Get list article ID
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select article_id from articles limit 10;')
        list_article_id = self.new_feed_db.get_list_db(db_data)

        # Check like_article
        print("Check block_article")
        list_user_block_article = []
        list_kafka_message = []
        article_id = self.common.get_random_element(list_article_id)
        for i in range(3):
            vid = random.choice(list_vid)
            list_user_block_article.append(vid)
            print(vid, " : ", article_id)
            # Check like_article
            user_actions = self.new_feed_api.set_user_actions_data(action_type, article_id)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)

            # Validate: Not correct but don't know how to check
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid from user_block_articles where article_id = "{article_id}";')
            db_data = self.new_feed_db.get_list_db(db_data)
            list_user_block_article = self.common.remove_duplicated_items(list_user_block_article)
            result_tmp = self.common.check_is_sublist(db_data, list_user_block_article)
            print("    API : ", list_user_block_article)
            print("    DB  : ", db_data)
            list_kafka_message.append(self.common.get_kafka_message(action_type, vid, article_id))
            if result_tmp == False:
                print("ERROR: User block_articles failed")
                # print("    API : ", list_user_block_article)
                # print("    DB  : ", db_data)
                result = False

        self.common.print_list(list_kafka_message)
        assert result == True


    # NF-83: cancel_block_article
    def test_post_user_actions_cancel_block_article(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'cancel_block_article'
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid, article_id from user_block_articles limit 10;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        list_article_id = self.new_feed_db.get_list_db(db_data, 1)

        # Check like_article
        print("Check cancel_block_article ")
        list_user_cancel_block_articles = []
        list_kafka_message = []
        for i in range(min(3, len(list_vid))):
            vid = list_vid[i]
            article_id = list_article_id[i]
            print(vid, ": ", article_id)

            # Check cancel_like_article
            user_actions = self.new_feed_api.set_user_actions_data(action_type, article_id)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
            list_user_cancel_block_articles.append(vid)
            list_kafka_message.append(self.common.get_kafka_message(action_type, vid, article_id))
            # Validate
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid from user_block_articles where article_id = "{article_id}";')
            db_data = self.new_feed_db.get_list_db(db_data)

            print("    API : ", list_user_cancel_block_articles)
            print("    DB  : ", db_data)
            result_tmp = self.common.check_if_lists_are_different(db_data, list_user_cancel_block_articles)
            if result_tmp == False:
                print("ERROR: User cancel_block_article failed")
                # print("    API : ", list_user_cancel_like_articles)
                #print("    DB  : ", db_data)
                result = False
        self.common.print_list(list_kafka_message)

        assert result == True


    # NF-83: complaint_article
    def test_post_user_actions_complaint_article(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'complaint_article'
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories order by rand() limit 10;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        # Get list article ID
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select article_id from articles order by rand() limit 10;')
        list_article_id = self.new_feed_db.get_list_db(db_data)
        # Complaint type
        list_complaint_type = ['old_news', 'wrong_info', 'bad_content', 'others']

        # Check like_article
        print("Check complaint_article ")
        list_user_complaint_article = []
        list_kafka_message = []
        for i in range(min(3, len(list_vid))):
            vid = list_vid[i]
            article_id = list_article_id[i]
            complaint_type = self.common.get_random_element(list_complaint_type)

            # Check cancel_like_article
            user_actions = self.new_feed_api.set_user_actions_data(action_type, article_id=article_id, complaint_type=complaint_type)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
            list_user_complaint_article.append(vid)
            list_kafka_message.append(self.common.get_kafka_message(action_type, vid, article_id))
            # Validate
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid from user_complaint_articles where article_id = "{article_id}" and status = "new" and complaint_type = "{complaint_type}";')
            db_data = self.new_feed_db.get_list_db(db_data, 0)

            print("    API : ", vid, " : ", article_id, " : ", complaint_type)
            print("    DB  : ", db_data)
            result_tmp = self.common.check_if_element_in_list(db_data, vid)
            if result_tmp == False:
                print("ERROR: User complaint_article failed")
                # print("    API : ", list_user_cancel_like_articles)
                #print("    DB  : ", db_data)
                result = False
        self.common.print_list(list_kafka_message)

        assert result == True

    # NF-83: subscribe_category
    def test_post_user_actions_subscribe_category(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'subscribe_category'
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories limit 10;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        # Get list category ID
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select category_id from coccoc_news_feed.categories order by rand() limit 10;')
        list_category_id = self.new_feed_db.get_list_db(db_data, 0)

        # Check subscribe_category
        print("Check subscribe_category ")
        list_kafka_message = []
        for i in range(min(3, len(list_vid))):
            vid = list_vid[i]

            # Check subscribe_category
            user_actions = self.new_feed_api.set_user_actions_data(action_type, categories=list_category_id)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)

            # Validate: the category is updated
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select category_id from coccoc_news_feed.user_categories where vid = "{vid}";')
            db_data = self.new_feed_db.get_list_db(db_data)

            print("    API : ", vid, " : ", list_category_id)
            print("    DB  : ", vid, " : ", db_data)
            list_kafka_message.append(self.common.get_kafka_message(action_type, vid, db_data))

            result_tmp = self.common.check_if_unordered_lists_are_equal(db_data, list_category_id)
            if result_tmp == False:
                print("ERROR: User subscribe_category failed")
                result = False
        self.common.print_list(list_kafka_message)
        assert result == True



    # NF-83: block_source
    def test_post_user_actions_block_source(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'block_source'
        # Get list vid
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(vid) from user_categories limit 5;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        # Get list category ID
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select domain from coccoc_news_feed.sources order by rand() limit 5;')
        list_domain = self.new_feed_db.get_list_db(db_data, 0)

        # Check block_source
        print("Check block_source ")
        list_kafka_message = []
        for i in range(min(2, len(list_vid))):
            vid = list_vid[i]
            domain = list_domain[i]

            # Check total block_source before api
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select domain from user_block_sources where vid = "{vid}";')
            list_domain_db = self.new_feed_db.get_list_db(db_data, 0)
            list_domain_db.append(domain)
            list_domain_db = self.common.remove_duplicated_items(list_domain_db)

            # Check block_source
            user_actions = self.new_feed_api.set_user_actions_data('block_source', domain=domain)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
            # Validate: the category is updated
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select domain from user_block_sources where vid = "{vid}";')
            db_data = self.new_feed_db.get_list_db(db_data)

            list_kafka_message.append(self.common.get_kafka_message(action_type, vid, db_data))

            print("    API : ", vid, " : ", list_domain_db)
            print("    DB  : ", vid, " : ", db_data)

            result_tmp = self.common.check_if_unordered_lists_are_equal(db_data, list_domain_db)
            if result_tmp == False:
                print("ERROR: User block_source failed")
                result = False
        self.common.print_list(list_kafka_message)
        assert result == True

    # NF-83: cancel_block_source
    def test_post_user_actions_cancel_block_source(self, coccoc_new_feeds_db_interact):
        result = True
        action_type = 'cancel_block_source'
        # Get list vid & domain
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid, domain from coccoc_news_feed.user_block_sources order by rand() limit 5;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        list_domain = self.new_feed_db.get_list_db(db_data, 1)

        # Check cancel_block_source
        print("Check cancel_block_source ")
        list_kafka_message = []
        for i in range(min(2, len(list_vid))):
            vid = list_vid[i]
            domain = list_domain[i]

            # Check total block_source before api
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact,
                                                       f'select domain from user_block_sources where vid = "{vid}";')
            list_domain_db = self.new_feed_db.get_list_db(db_data, 0)
            list_domain_db.remove(domain)

            # Check block_source
            user_actions = self.new_feed_api.set_user_actions_data(action_type, domain=domain)
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
            # Validate: the domain is updated
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select domain from user_block_sources where vid = "{vid}";')
            db_data = self.new_feed_db.get_list_db(db_data)
            list_kafka_message.append(self.common.get_kafka_message(action_type, vid, db_data))

            print("    API : ", vid, " : ", list_domain_db)
            print("    DB  : ", vid, " : ", db_data)

            result_tmp = self.common.check_if_unordered_lists_are_equal(db_data, list_domain_db)
            if result_tmp == False:
                print("ERROR: User cancel_block_source failed")
                result = False

        self.common.print_list(list_kafka_message)
        assert result == True

    # NF-83: invalid data
    def test_post_user_actions_invalid(self, coccoc_new_feeds_db_interact):
        result = True
        # Get list vid & domain
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select vid, domain from coccoc_news_feed.user_block_sources order by rand() limit 5;')
        list_vid = self.new_feed_db.get_list_db(db_data, 0)
        list_domain = self.new_feed_db.get_list_db(db_data, 1)

        # Check cancel_block_source
        print("Check invalid data ")
        for i in range(min(2, len(list_vid))):
            vid = list_vid[i]

            # Check block_source
            user_actions = self.new_feed_api.set_user_actions_data('cancel_block_source', domain='')
            response = self.new_feed_api.request_post_new_feeds(COCCOC_NEW_FEED_API_CMS_USER_ACTION + vid, user_actions)
            print(vid)

        assert result == True