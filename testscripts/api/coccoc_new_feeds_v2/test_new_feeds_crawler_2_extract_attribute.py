from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;

class TestNewFeedCralwer:
    common = NewFeedCommon()
    newfeed_db = NewFeedDB()
    result = True

    # 2) Extract article attributes and data post processing
    # a) Extract article attributes

    # Extract title
    def test_extract_title(self):
        db_article_crawled = self.newfeed_db.get_newfeeds_db('SELECT url, title FROM coccoc_news_feed.articles where status = "crawled" limit 10;')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_title_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        self.common.print_list(list_article_title_actual)
        list_article_title_expect = []
        list_article_url_error = []
        list_article_title_expect_error = []
        list_article_title_actual_error = []
        for url in list_article_url:
            title = self.common.get_attribute_from_url(url, 'description')
            list_article_title_expect.append(str(title))
        self.common.print_list(list_article_title_expect)
        for i in range(len(list_article_url)):
            if list_article_title_expect[i] != list_article_title_actual[i]:
                list_article_url_error.append(list_article_url[i])
                list_article_title_expect_error.append("    " + list_article_title_expect[i])
                list_article_title_actual_error.append("    " + list_article_title_actual[i])
                self.result = False
        print("ERROR: Article titles are not matched")
        for i in range(len(list_article_url_error)):
            print(" %d : %s " % (i, list_article_url_error[i]))
            print(list_article_title_expect_error[i])
            print(list_article_title_actual_error[i])

        assert self.result == True

    # Extract description
    # Extract content
    # Extract image_url
    # Extract tags
    # Extract breadcumb_name
    # Extract breadcumb_url
    # Extract datetime published_time

    # Add @breadcumb and @breadcum_url to source categories
    def test_mapping_breadcumb(self):
        list_breadcumb_url_in_articles = self.get_breadcumb_url_in_article_db()
        list_breadcumb_url_in_source_categories = self.get_breadcumb_url_in_source_categories_db()
        list_different = self.common.get_different_elements_between_lists(list_breadcumb_url_in_articles, list_breadcumb_url_in_source_categories)
        if len(list_different):
            print("ERROR: Lists are not equals")
            self.print_list(list_different)
            self.result = False
        assert self.result == True

    # Get all breadcumb_url in articles in DB
    def get_breadcumb_url_in_article_db(self):
        db_breadcumb_url = self.newfeed_db.get_newfeeds_db(f'select distinct(breadcumb_url) from coccoc_news_feed.articles;')
        list_breadcumb_url = self.newfeed_db.get_list_db(db_breadcumb_url)
        return list_breadcumb_url

    # Get all breadcumb_url in source_categories in DB
    def get_breadcumb_url_in_source_categories_db(self):
        db_breadcumb_url = self.newfeed_db.get_newfeeds_db(f'select url from coccoc_news_feed.source_categories;')
        list_breadcumb_url = self.newfeed_db.get_list_db(db_breadcumb_url)
        return list_breadcumb_url

    # Update crawled article information

    # Verify if list in not null
    def verify_if_list_is_not_null(self, list, error_message):
        if len(list):
            print("ERROR: %s" % (error_message))
            self.common.print_list(list)
            self.result = False
