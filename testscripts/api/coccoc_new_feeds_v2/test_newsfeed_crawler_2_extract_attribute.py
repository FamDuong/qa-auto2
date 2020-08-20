from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from datetime import datetime

class TestNewFeedCralwer:
    common = NewFeedCommon()
    newfeed_db = NewFeedDB()
    result = True

    crawled_title_file = "Data/crawled_title_error.txt"
    crawled_description_file = "Data/crawled_description_error.txt"
    crawled_file = ""

    # Set filename
    def set_filename(self, attribute):
        self.crawled_title_file = "Data/crawled_title_error.txt"
        self.crawled_description_file = "Data/crawled_description_error.txt"
        self.crawled_file = "Data/" + attribute + "_error.txt"
        self.common.remove_file(self.crawled_title_file)
        self.common.remove_file(self.crawled_description_file)
        self.common.remove_file(self.crawled_file)

    # Set filename
    def set_crawled_filename(self, attribute, method):
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y%m%d%H%M%S")
        filename = "Data/crawled_" + attribute + "_" + method + "_" + timestamp + ".txt"
        self.common.remove_file(filename)
        return filename

    # 2) Extract article attributes and data post processing
    # a) Extract article attributes

    # Extract title
    def test_extract_title(self):
        attribute = "title"
        list_strip_expect = [" - Doanh nghiệp Việt Nam", " - VnExpress", "Video: ", " | VTV.VN"]
        list_strip_actual = [" | Báo dân sinh", " | VTV.VN", " | Dân Việt"]
        db_article_crawled = self.newfeed_db.select_newfeeds_db('SELECT url, title FROM coccoc_news_feed.articles where status = "crawled";')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_title_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        # Extract by 2 different methods to get best result
        self.verify_extract_data_by_parser_news(list_article_url, list_article_title_actual, attribute, list_strip_expect, list_strip_actual)
        self.verify_extract_data_by_parser_metadata(list_article_url, list_article_title_actual, attribute, list_strip_expect, list_strip_actual)
        assert self.result == True

    # Extract description
    def test_extract_description(self):
        attribute = "description"
        list_strip_expect = [", Báo Doanh Nghiệp Việt Nam", " - Báo Giao Thông"]
        list_strip_actual = [" - VnExpress", " - Báo Giao Thông"]
        db_article_crawled = self.newfeed_db.select_newfeeds_db('SELECT url, description FROM coccoc_news_feed.articles where status = "crawled";')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_description_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        # Extract by 2 different methods to get best result
        self.verify_extract_data_by_parser_news(list_article_url, list_article_description_actual, attribute, list_strip_expect, list_strip_actual)
        self.verify_extract_data_by_parser_metadata(list_article_url, list_article_description_actual, attribute, list_strip_expect, list_strip_actual)
        assert self.result == True

    # Extract content: BRBE-971
    def test_extract_content(self):
        attribute = "content"
        list_strip_expect = [ "Dân trí "]
        list_strip_actual = []
        db_article_crawled = self.newfeed_db.select_newfeeds_db('SELECT url, content FROM coccoc_news_feed.articles where status = "crawled" and url NOT LIKE "%video%";')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_content_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        # Extract by 2 different methods to get best result
        # self.verify_extract_data_by_parser_metadata(list_article_url, list_article_content_actual, attribute, list_strip_expect, list_strip_actual) # Not implemented for content yet
        self.verify_extract_data_by_parser_news(list_article_url, list_article_content_actual, attribute, list_strip_expect, list_strip_actual)
        assert self.result == True

    # Extract image_url
    def test_extract_image_url(self):
        attribute = "image_url"
        list_strip_expect = []
        list_strip_actual = []
        db_article_crawled = self.newfeed_db.select_newfeeds_db('SELECT url, image_url FROM coccoc_news_feed.articles where status = "crawled";')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_image_url_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        # Extract by 2 different methods to get best result
        # self.verify_extract_data_by_parser_metadata(list_article_url, list_article_content_actual, attribute, list_strip_expect, list_strip_actual) # Not implemented for content yet
        self.verify_extract_data_by_parser_news(list_article_url, list_article_image_url_actual, attribute, list_strip_expect, list_strip_actual)
        assert self.result == True

    # Extract tags
    def test_extract_tags(self):
        attribute = "tags"
        list_strip_expect = []
        list_strip_actual = []
        db_article_crawled = self.newfeed_db.select_newfeeds_db('SELECT url, tags FROM coccoc_news_feed.articles where status = "crawled";')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_tags_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        # Extract by 2 different methods to get best result
        # self.verify_extract_data_by_parser_metadata(list_article_url, list_article_content_actual, attribute, list_strip_expect, list_strip_actual) # Not implemented for content yet
        self.verify_extract_data_by_parser_news(list_article_url, list_article_tags_actual, attribute, list_strip_expect, list_strip_actual)
        assert self.result == True

    # Extract breadcumb_name (T.B.D)
    def test_extract_breadcumb_name(self):
        print("Extract breadcumb_name: T.B.D")

    # Extract breadcumb_url
    def test_extract_breadcumb_url(self):
        print("Extract breadcumb_url: T.B.D")

    # Extract datetime published_time
    def test_extract_published_time(self):
        attribute = "published_time"
        list_strip_expect = []
        list_strip_actual = []
        db_article_crawled = self.newfeed_db.select_newfeeds_db('SELECT url, published_time FROM coccoc_news_feed.articles where status = "crawled";')
        list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        list_article_published_time_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        # Extract by 2 different methods to get best result
        # self.verify_extract_data_by_parser_metadata(list_article_url, list_article_content_actual, attribute, list_strip_expect, list_strip_actual) # Not implemented for content yet
        self.verify_extract_data_by_parser_news(list_article_url, list_article_published_time_actual, attribute, list_strip_expect, list_strip_actual)
        assert self.result == True

    # Common function to verify data by parser metadata
    def verify_extract_data_by_parser_metadata(self, list_article_url, list_actual_attribute, attribute, list_strip_expect, list_strip_actual):
        if attribute == "title":
            list_parser = ["og:title", "twitter:title"]
        elif attribute == "description":
            list_parser = ["og:description", "twitter:description"]
        elif attribute == "breadcumb_name":
            list_parser = ["og:section", "twitter:section" , "article:section", "its_section"]
        filename = self.set_crawled_filename(attribute, "metadata")
        for i in range(len(list_article_url)):
            expect_attribute = str(self.common.get_parse_metadata(list_article_url[i], attribute, list_parser, list_strip_expect))
            actual_attribute = self.common.strip_string(str(list_actual_attribute[i]), list_strip_actual)
            if expect_attribute != actual_attribute:
                diff_len = abs(len(expect_attribute) - len(actual_attribute))
                if diff_len > 6:
                    error = []
                    error.append(list_article_url[i])
                    error.append("    Actual: " + actual_attribute)
                    error.append("    Expect: " + expect_attribute)
                    self.common.append_to_file(filename, error)
        if self.common.check_file_is_existed(filename):
            print("ERROR: Article %s are not matched, please check %s" % (attribute, filename))
            self.result = False
        # assert self.result == True

    # Common function to verify data by parser newspaper
    def verify_extract_data_by_parser_news(self, list_article_url, list_actual_attribute, attribute, list_strip_expect, list_strip_actual):
        threshold = 6
        list_attributes_fetch = [ "published_time" , "breadcumb_name"]
        list_attributes_release = [ "content" ]
        print("Number of url: %d" % len(list_article_url))
        filename = self.set_crawled_filename(attribute, "newspaper")
        for i in range(len(list_article_url)):
            if attribute in list_attributes_fetch:
                expect_attribute = self.common.get_parse_news_fetch(list_article_url[i], attribute, list_strip_expect)
            elif attribute in list_attributes_release:
                threshold = 50
                expect_attribute = self.common.get_parse_news_release(list_article_url[i], attribute, list_strip_expect)
            else:
                expect_attribute = self.common.get_parse_newspaper(list_article_url[i], attribute, list_strip_expect)
            actual_attribute = self.common.strip_string(str(list_actual_attribute[i]), list_strip_actual)
            if expect_attribute != actual_attribute:
                diff_len = abs(len(expect_attribute) - len(actual_attribute))
                if diff_len > threshold:
                    error = []
                    error.append(list_article_url[i])
                    error.append("    Actual: " + actual_attribute)
                    error.append("    Expect: " + expect_attribute)
                    self.common.append_to_file(filename, error)
        if self.common.check_file_is_existed(filename):
            print("ERROR: Article %s are not matched, please check %s" % (attribute, filename))
            self.result = False
        # assert self.result == True


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
        db_breadcumb_url = self.newfeed_db.select_newfeeds_db(f'select distinct(breadcumb_url) from coccoc_news_feed.articles;')
        list_breadcumb_url = self.newfeed_db.get_list_db(db_breadcumb_url)
        return list_breadcumb_url

    # Get all breadcumb_url in source_categories in DB
    def get_breadcumb_url_in_source_categories_db(self):
        db_breadcumb_url = self.newfeed_db.select_newfeeds_db(f'select url from coccoc_news_feed.source_categories;')
        list_breadcumb_url = self.newfeed_db.get_list_db(db_breadcumb_url)
        return list_breadcumb_url

    # Update crawled article information

    # Verify if list in not null
    def verify_if_list_is_not_null(self, list, error_message):
        if len(list):
            print("ERROR: %s" % (error_message))
            self.common.print_list(list)
            self.result = False

    # Extract breadcumb_name (T.B.D)
    def test_trial(self):
        from newsfetch.news import newspaper
        from newsplease import NewsPlease
        import requests
        attribute = "breadcumb_name"
        from bs4 import BeautifulSoup
        list_strip_expect = []
        list_strip_actual = []
        # db_article_crawled = self.newfeed_db.select_newfeeds_db(
        #    'SELECT url, breadcumb_name FROM coccoc_news_feed.articles where status = "crawled" limit 10;')
        #list_article_url = self.newfeed_db.get_list_db(db_article_crawled, 0)
        #list_article_published_time_actual = self.newfeed_db.get_list_db(db_article_crawled, 1)
        list_article_url = [ "https://www.giadinhmoi.vn/bang-gia-xe-o-to-honda-moi-nhat-thang-8-2020-d43924.html" , "https://afamily.vn/hinh-anh-gay-chan-dong-kbiz-hom-nay-lan-dau-tien-5-cuc-pham-soai-ca-dung-chung-mot-khung-hinh-va-con-cung-nhau-lam-dieu-nay-20200803124241415.chn" ]
        for url in list_article_url:
            article = newspaper(url)
            print(url)
            #print("Summary      : " + article.summary)
            #print("headline     : " + article.headline)
            #print("category     : " + str(article.category))
            #print("article      : " + article.article)
            #print("get_dict     : " + str(article.get_dict))
            #print("keywords     : " + str(article.keywords))
            #print("source_domain: " + article.source_domain)
            print("publication  : " + str(article.publication))
            #print("title_rss    : " + str(article.title_rss))
            #print("title_page   : " + str(article.title_page))
            #print("date_publish : " + str(article.date_publish))
            my_article = NewsPlease.from_url(url)
            print("Title      : " + my_article.title)
            print("Description: " + my_article.description)
            print("Main text:   " + my_article.maintext)
            content = self.common.remove_newlines_string(my_article.maintext)
            content = content.replace(my_article.description + ".", "")
            print("Main text:   " + content)


        # Extract by 2 different methods to get best result
        # self.verify_extract_data_by_parser_metadata(list_article_url, list_article_content_actual, attribute, list_strip_expect, list_strip_actual) # Not implemented for content yet
        # self.verify_extract_data_by_parser_news(list_article_url, list_article_published_time_actual, attribute,
        #                                         list_strip_expect, list_strip_actual)
        # assert self.result == True