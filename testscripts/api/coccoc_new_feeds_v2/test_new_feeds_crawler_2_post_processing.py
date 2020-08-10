from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewsFeedRedis;
from datetime import datetime

from config.environment import COCCOC_NEW_FEED_BUCKET_URL

class TestNewFeedCralwer:
    common = NewFeedCommon()
    newfeed_db = NewFeedDB()
    newfeed_redis = NewsFeedRedis()
    result = True
    BUCKET_URL = 'https://coccoc-image-service.itim.vn/dev_coccoc_news_feed'

    # Set filename
    def set_filename(self, attribute):
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y%m%d%H%M%S")
        filename = "Data/" + attribute + "_" + timestamp + ".txt"
        self.common.remove_file(filename)
        return filename

    # b) Data post processing for above crawled articles
    # 1) Check update mapping category
    def test_update_mapping_category(self):
        list_category = self.get_mapping_category_db()
        assert len(list_category) == 0

    # Get mapping categories
    def get_mapping_category_db(self):
        db_category = self.newfeed_db.select_newfeeds_db(f'select a.category_id, a.url, s.category_id, a.breadcumb_url from coccoc_news_feed.articles as a inner join coccoc_news_feed.source_categories as s on a.breadcumb_url = s.url and a.status = "crawled" and a.category_id != s.category_id;')
        list_category = self.newfeed_db.get_list_db(db_category, 0)
        return list_category

    # 2) Scan for blacklist keywords (BRBE-948)
    # BRBE-948: [NF][Crawler] Post processing: Some articles are not set as blacklist
    def test_scan_title_is_blacklist(self):
        list_keyword_error = []
        list_articles_error = []
        list_keyword = self.get_blacklist_keyword_db()
        for keywork in list_keyword:
            list_articles = self.get_not_blacklist_articles_db(keywork)
            if len(list_articles):
                list_keyword_error.append(keywork)
                list_articles_error.append(list_articles)
                self.result = False
        print("ERROR: Articles not in blacklist")
        for i in range(len(list_keyword_error)):
            print("    ", list_keyword_error[i])
            self.common.print_list(list_articles_error[i])
        assert self.result == True

    # 2) Scan for wrong blacklist article, article has no blacklist keyword
    def test_scan_title_is_not_blacklist(self):
        # Check there is no wrong blacklist article, article has no blacklist keyword
        list_articles_error = []
        list_keyword = self.get_blacklist_keyword_db()
        list_articles = self.get_blacklist_articles_db()
        self.common.print_list(list_keyword)
        for article in list_articles:
            keywords_error = self.common.get_keywords_not_in_strings(article, list_keyword)
            if not len(keywords_error):
                list_articles_error.append(article)
                # list_keyword_error.append(keywords_error)
                self.result = False
        if len(list_articles_error):
            print("ERROR: Wrong Articles in blacklist")
            self.common.print_list(list_articles_error)
        assert self.result == True

    # Get blacklist keywords
    def get_blacklist_keyword_db(self):
        db_keyword = self.newfeed_db.select_newfeeds_db(f'select keyword from blacklist_keywords where status = "active";')
        list_keyword = self.newfeed_db.get_list_db(db_keyword, 0)
        return list_keyword

    # Get blacklist article
    def get_not_blacklist_articles_db(self, keyword):
        regex = "[[:<:]]" + keyword + "[[:>:]]"
        db_articles = self.newfeed_db.select_newfeeds_db(f'select title from articles where title RLIKE "{regex}" and status != "blacklist";')
        list_articles = self.newfeed_db.get_list_db(db_articles, 0)
        return list_articles

    # Get all blacklist article
    def get_blacklist_articles_db(self):
        db_articles = self.newfeed_db.select_newfeeds_db(f'select title from articles where status = "blacklist";')
        list_articles = self.newfeed_db.get_list_db(db_articles, 0)
        return list_articles

    # 3) Scan duplicate content (duplicate title) (BRBE-956)
    def test_scan_duplicated_title(self):
        list_different = []
        db_articles = self.get_duplicated_articles_db()
        list_a_article_id = self.newfeed_db.get_list_db(db_articles, 0)
        list_a_original_article_id = self.newfeed_db.get_list_db(db_articles, 1)
        list_a_title = self.newfeed_db.get_list_db(db_articles, 3)
        list_a_url = self.newfeed_db.get_list_db(db_articles, 4)
        list_a_published_time = self.newfeed_db.get_list_db(db_articles, 6)
        list_b_article_id = self.newfeed_db.get_list_db(db_articles, 2)
        list_b_url = self.newfeed_db.get_list_db(db_articles, 5)
        list_b_published_time = self.newfeed_db.get_list_db(db_articles, 7)
        for i in range(len(list_a_original_article_id)):
            if list_a_original_article_id[i] != list_b_article_id[i]:
                list_different.append(list_a_article_id[i])
                list_different.append("   Title         : " + list_a_title[i])
                list_different.append("   a.url         : " + list_a_url[i])
                list_different.append("   a.publish_time: " + str(list_a_published_time[i]))
                list_different.append("   b.url         : " + list_b_url[i])
                list_different.append("   b.publish_time: " + str(list_b_published_time[i]))
        if len(list_different):
            print("ERROR: Scan duplicated are failed")
            self.common.print_list(list_different)
            self.result = False
        assert self.result == True

    # Get all duplicated contents
    def get_duplicated_articles_db(self):
        db_articles = self.newfeed_db.select_newfeeds_db(f'select a.article_id, a.original_article_id, b.article_id as b_article_id, a.title, a.url, b.url as b_url, a.published_time, b.published_time as b_published_time, a.status from coccoc_news_feed.articles as a inner join coccoc_news_feed.articles as b on a.title_hash = b.title_hash and b.published_time < a.published_time and a.status = "crawled" group by a.article_id order by a.title_hash;')
        # list_articles = self.newfeed_db.get_list_db(db_articles, 0)
        return db_articles

    # 4) Upload image to image service
    def test_upload_cdn_image_url(self):
        # Make sure all crawled article has cdn_image_url
        list_images = self.get_not_cnd_image_url_db()
        if len(list_images):
            print("ERROR: Some articles have no cdn_image_url")
            self.common.print_list(list_images)
            self.result = False
        assert self.result == True

    # 4) Upload image to image service (T.B.D)
    def test_upload_image_url_color(self):
        # Make sure color_background are correct
        # Make sure color_text are correct
        # (T.B.D) Only check available, not check the correctness
        list_color_background = self.get_not_color_background_db()
        if len(list_color_background):
            print("ERROR: Some articles have no color background")
            self.common.print_list(list_color_background)
            self.result = False
        list_color_text = self.get_not_color_text_db()
        if len(list_color_text):
            print("ERROR: Some articles have no color text")
            self.common.print_list(list_color_text)
            self.result = False
        assert self.result == True

    # 4) Upload image to image service
    # BRBE-979: [NF][Crawler] Update logic to crop and resize images
    # We need to crop image to 640x320 before upload to cdn
    def test_upload_image_to_image_service(self):
        file_compare_image = self.set_filename("compare_image")
        self.common.remove_file(file_compare_image)
        # Make sure all original images and cdn images are matched
        # Compare image in image_url and cdn_image_url
        db_images = self.get_image_url_db()
        list_image_url = self.newfeed_db.get_list_db(db_images, 0)
        list_cdn_image_url = self.newfeed_db.get_list_db(db_images, 1)
        list_article_url = self.newfeed_db.get_list_db(db_images, 4)
        for i in range(len(list_image_url)):
            image_url = list_image_url[i]
            cdn_image_url = list_cdn_image_url[i].replace("{BUCKET_URL}", COCCOC_NEW_FEED_BUCKET_URL)
            compare_results = self.common.compare_images_from_url(image_url, cdn_image_url)
            cdn_image_mode = compare_results[0]
            cdn_image_size = compare_results[1]
            threshold = compare_results[2]
            if threshold > 30 or "(640, 320)" not in cdn_image_size:
                list_error = []
                list_error.append(list_article_url[i])
                list_error.append("image_url       : " + image_url)
                list_error.append("cdn_image_url   : " + cdn_image_url)
                list_error.append("cdn_image_mode  : " + cdn_image_mode)
                list_error.append("cdn_image_size  : " + str(cdn_image_size))
                list_error.append("threshold       : %d" % (threshold))
                self.common.append_to_file(file_compare_image, list_error)
                self.result = False
        print("ERROR: cdn images")
        assert self.result == True

    # Get image_url and cdn_image_url in DB
    def get_image_url_db(self):
        db_images = self.newfeed_db.select_newfeeds_db(f'select image_url, cdn_image_url, color_background, color_text, url from articles where status = "crawled";')
        # db_images = self.newfeed_db.select_newfeeds_db(f'select image_url, cdn_image_url, color_background, color_text, url from articles where status != "error";')
        return db_images;

    # Get image_url and cdn_image_url in DB
    def get_not_cnd_image_url_db(self):
        db_images = self.newfeed_db.select_newfeeds_db(f'select article_id, url, image_url, cdn_image_url from articles where status = "crawled" and cdn_image_url is Null;')
        list_images = self.newfeed_db.get_list_db(db_images, 3)
        return list_images;

    # Get color background in DB
    def get_not_color_background_db(self):
        db_color = self.newfeed_db.select_newfeeds_db(f'select article_id from articles where status = "crawled" and color_background is null;')
        list_color = self.newfeed_db.get_list_db(db_color, 0)
        return list_color;

    # Get color text in DB
    def get_not_color_text_db(self):
        db_color = self.newfeed_db.select_newfeeds_db(f'select article_id from articles where status = "crawled" and color_text is null;')
        list_color = self.newfeed_db.get_list_db(db_color, 0)
        return list_color;

    # 5) Publish articles
    # Check if any ready for publish article but status still in crawled
    def test_article_is_not_publish(self):
        list_article = self.common.get_list_newsfeed_db(f'select article_id from articles where status  = "crawled" and category_id is not null and cdn_image_url is not null and update_time < (CURRENT_TIMESTAMP - 3600);')
        if len(list_article):
            print("ERROR: ready for publish article but status still in crawled")
            self.common.print_list(list_article)
            self.result = False
        assert self.result == True

    # 5) Publish articles
    # Call CMS Api to publish articles to frontend cache
    def test_not_article_publish_at_frondend_cache(self):
        list_article = self.common.get_list_newsfeed_db(f'select article_id from articles where status  = "crawled" and category_id is not null and cdn_image_url is not null and update_time < (CURRENT_TIMESTAMP - 3600);')
        if len(list_article):
            print("ERROR: ready for publish article but status still in crawled")
            self.common.print_list(list_article)
            self.result = False

    # Call CMS Api to publish articles to frontend cache
    def test_article_publish_at_frondend_cache(self):
        list_article_id = self.common.get_list_newsfeed_db(
            f'select article_id from articles where status = "publish" and category_id is not null and cdn_image_url is not null and published_time > (CURRENT_TIMESTAMP - 1800);', 0)
        redis_data = self.newfeed_redis.redis_keys('NRE:ARTICLE2:*')
        redis_data = self.common.replace_string_in_list(redis_data, "NRE:ARTICLE2:", "")
        redis_data = self.common.remove_duplicated_items_in_list(redis_data)
        print(len(redis_data))
        print(len(list_article_id))
        list_diff_db = self.common.get_different_elements_between_lists(list_article_id, redis_data)
        list_diff_redis = self.common.get_different_elements_between_lists(redis_data, list_article_id)
        if len(list_diff_db):
            print("ERROR: Articles are not publish in Frontend cache")
            self.common.print_list(list_diff_db)
            print("    Ratio: %d" % (self.common.division_percentage(len(list_diff_db), len(list_article_id))))
            self.result = False
        # if len(list_diff_redis):
        #    print("ERROR: Articles are not in Database anymore")
        #    self.common.print_list(list_diff_redis)
        #    print("    Ratio: %d" % (self.common.division_percentage(len(list_article_id), len(list_diff_db))))
        #    self.result = False
        assert self.result == True


    # 6) Remove expired articles and image
    # Check no expired articles on DB
    # (T.B.D) Remove images in image service which have path /yyyymmdd/ < TODAY - @expired_times days - 3
    def test_remove_expired_articles_and_images(self):
        # Check no expired articles on DB
        list_expire_date = self.common.get_list_newsfeed_db(
            f'SELECT value FROM coccoc_news_feed.configs where name = "ARTICLE_EXPIRED_TIME" and status = 1;', 0)
        list_expire_article = self.common.get_list_newsfeed_db(
            f'select article_id from articles where published_date <  DATE_ADD(CURRENT_DATE, INTERVAL - "{list_expire_date[0]}" DAY);', 0)
        if len(list_expire_article):
            print("ERROR: Expired articles are not removed")
            self.common.print_list(list_expire_article)
            self.result = False
        # NF-282: Remove images in image service which have path /yyyymmdd/ < TODAY - @expired_times days - 3
        list_expire_image = {"{BUCKET_URL}/20200802/8306082476090925482-viet-nam-duoc-de-cu-11-hang-muc-giai-thuong-du-lich-the-gioi-2020.jpg",
                             "{BUCKET_URL}/20200802/227357852972130641-nhung-bai-tap-giup-nang-so-huu-co-cao-thon-dep-chuan-quy-co-thanh-lich.jpg",
                             "{BUCKET_URL}/20200802/543144714528028019-doc-dao-gieng-viet-bia-hoc-baohaiduong.jpg",
                             "{BUCKET_URL}/20200802/16294068208020363147-truyen-thong-trieu-tien-len-tieng-ve-sua-doi-quy-dinh-phat-trien-ten-lua-day-cua-han-quoc.jpg",
                             "{BUCKET_URL}/20200802/3971041994431886350-barca-doa-kien-va-day-la-cau-tra-loi-tu-arthur-cau-thu.jpg",
                             "{BUCKET_URL}/20200802/797451865310357597-mao-hiem-yeu-ga-trai-it-tuoi-hon-minh.jpg",
                             "{BUCKET_URL}/20200802/9305103254859730652-lang-mo-da-co-100-tuoi-giua-long-ha-noi.jpg",
                             "{BUCKET_URL}/20200802/5441616340941884408-ban-da-biet-dau-la-dia-diem-du-lich-ua-thich-cua-messi-bong-da.jpg",
                             "{BUCKET_URL}/20200802/1486591926235019700-tau-du-hanh-cua-spacex-roi-tram-khong-gian-quoc-te-quay-ve-trai-dat.jpg",
                             "{BUCKET_URL}/20200802/3697248460713700638-thue-nha-xuong-tai-che-hang-chuc-tan-gang-tay.jpg"}
        list_expire_image = self.common.replace_string_in_list(list_expire_image, "{BUCKET_URL}", COCCOC_NEW_FEED_BUCKET_URL)
        print("ERROR: Images are not removed on CDN")
        for image in list_expire_image:
            live_result = self.common.check_link_is_alive(image)
            if live_result:
                print(image)
                self.result = False
        assert self.result == True

    # BRBE-969: Add condition if content is null or blank then mark this article_urls as error
    def test_content_is_null_then_mark_as_error(self):
        list_articles_error_db = self.newfeed_db.select_newfeeds_db(
            f'SELECT a.article_id, a.url, a.status, b.status FROM coccoc_news_feed.articles as a inner join coccoc_news_feed.article_urls as b on a.content is null or a.content = "" and (a.status != "error" or b.status != "error") and a.article_id = b.article_id;')
        list_articles_id_error = self.newfeed_db.get_list_db(list_articles_error_db, 0)
        list_articles_url_error = self.newfeed_db.get_list_db(list_articles_error_db, 1)
        if len(list_articles_id_error):
            print("ERROR: Some articles which content is NULL but status is not error")
            self.common.print_list(list_articles_id_error)
            self.common.print_list(list_articles_url_error)
            self.result = False
        assert self.result == True

    # BRBE-969: There are some url still contains ? and # params. Please remove these params to normalize url when discover link: url = split url by ? and # and get first element.
    def test_url_contains_special_characters_then_mark_as_error(self):
        list_articles_error_db = self.newfeed_db.select_newfeeds_db(
            f'SELECT article_id, url FROM coccoc_news_feed.articles where (url regexp "@(:*\.:*){2,}" or url like "%#%" or url like "%&%" or url like "%?%") and status != "error";')
        list_articles_id_error = self.newfeed_db.get_list_db(list_articles_error_db, 0)
        list_articles_url_error = self.newfeed_db.get_list_db(list_articles_error_db, 1)
        if len(list_articles_id_error):
            print("ERROR: Some articles which url is ERROR but status is not error")
            self.common.print_list(list_articles_id_error)
            self.common.print_list(list_articles_url_error)
            self.result = False
        assert self.result == True