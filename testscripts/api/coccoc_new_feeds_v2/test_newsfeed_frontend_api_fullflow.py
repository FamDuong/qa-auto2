from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_redis import NewsFeedRedis;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewsFeedAPI;
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_kafka import NewsFeedKafka;
from testscripts.api.coccoc_new_feeds_v2.common import NewFeedCommon;
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
import json
import time
from datetime import datetime
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shutil
import subprocess

import logging
LOGGER = logging.getLogger(__name__)

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
    wait_time = 1200 # 15 minutes + threshold 10 minutes
    wait_time_interest = 1020 # 15 minutes + threshold 2 minutes
    # list_vid = ["T6rQC3J61u9rg1oTyC1uuJg1o9JGC9oJCGSyW2nBb9rofPtd8jQneKDZZdOWW"]
    # list_vid = ["693y6GJ61CGT91oTSu1u9GV1J9J6Gu996TuoW2nBb9rofPtd8jQneKDZZdOWW"]     # Browser version 83.0.4103.120
    # list_vid = ["bT9J9g3319r9o1oJSy1G9gb1oJTT9uo6GSQoW2nBb9rofPtd8jQneKDZZdOWW"]     # Browser version 83.0.4103.122
    # list_vid = ["SC3Qrgog1bg3V1oTgJ1GSJu1ub3VoTVQTGV6W2nBb9rofPtd8jQneKDZZdOWW"]     # Browser version 83.0.4103.124
    list_vid = ["S6rJSubS13gVV1oSQr1TbGC16C9gry3T9orSW2nBb9rofPtd8jQneKDZZdOWW"]     # Browser version 84.0.4147.144
    # list_vid = ["Vyb9uoGb1966Q1oQgo1uogQ1C6g3rSoVSJuyW2nBb9rofPtd8jQneKDZZdOWW"]     # Browser version 85.0.4183.122
    list_sid = ["kdz9reois5thzq4ew"]

    # Set filename
    def set_filename(self, attribute):
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y%m%d%H%M%S")
        filename = "Data/" + attribute + "_" + timestamp + ".txt"
        self.common.remove_file(filename)
        return filename

    def test_post_user_setting_all_categories(self):
        # Vid is existed
        list_vid = self.list_vid
        for vid in list_vid:
            print(vid)
            # Get user setting
            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=params, wait=0)
            api_sub_categories =  api_user_setting["sub_categories"]
            print(api_sub_categories)

    # NF-211: [NRE] Feedback and Improvement
    # User change feed settings (subscribe categories, block domain) then feed should show as user settings
    def test_get_user_feed_with_existed_vid(self):
        filename = self.set_filename("Userfeed")
        # list_vid = self.common.get_list_newsfeed_db("SELECT distinct(vid) FROM coccoc_news_feed.user_categories order by update_time desc limit 100;")
        list_vid = self.list_vid
        list_sid = self.list_sid
        for i in range(len(list_vid)):
            vid = list_vid[i]
            sid = list_sid[i]
            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=sid, size=1000)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]
            # Check if existed data of P4 with key = NRE:USER:ARTICLES:$vid. If existed then
            # P4. Data for each session id of users
            print("P4. Data for each session id of users")
            redis_user_articles = self.newsfeed_redis.redis_lrange("NRE:USER:ARTICLES:" + vid, format_data=None)
            print(redis_user_articles)

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
                # self.verify_article_data(api_data_articles[i], redis_article, filename)
                print(api_data_articles[i])
                # print(redis_article)
        # (T.B.D) if result is last page then remove cache P4 with key = NRE:USER:ARTICLES:$vid to refresh this list and get new data for next time\
        if self.common.check_file_is_existed(filename) != "None":
            self.result = False
        assert self.result == True

    # NF-211: [NRE] Feedback and Improvement
    # User change feed settings (subscribe categories, block domain) then feed should show as user settings
    def test_get_user_feed_with_feed_setting(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid
        for i in range(len(list_vid)):
            vid = list_vid[i]
            sid = list_sid[i]

            # Get user setting
            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=params, wait=0)
            api_sub_categories = api_user_setting["sub_categories"]
            print(api_sub_categories)

            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=sid, size=1000)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]

            list_article_error = []
            for i in range(len(api_data_articles)):
                article_id = api_data_articles[i]["id"]
                category_id = api_data_articles[i]["category_id"]
                title = api_data_articles[i]["title"]
                if category_id not in api_sub_categories:
                    print("ERROR: Articles do not belongs to sub categories")
                    print(category_id)
                    print(title)
                    list_article_error.append(article_id)
        if len(list_article_error):
            # self.common.print_list(list_article_error)
            self.result = False
        assert self.result == True


    # NF-211: [NRE] Feedback and Improvement
    # Feed display for user must contains 4 type: editor, interest, popular, sample
    def test_get_user_feed_with_type(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid
        list_type = [ "editor", "interest", "popular", "sample" ]
        size = 1000
        for i in range(len(list_vid)):
            vid = list_vid[i]
            sid = list_sid[i]

            # Get user setting
            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=params, wait=0)
            api_sub_categories = api_user_setting["sub_categories"]
            print(api_sub_categories)

            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=size)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]

            list_article_error = []
            list_type_editor = []
            list_type_interest = []
            list_type_popular = []
            list_type_sample = []
            for i in range(len(api_data_articles)):
                article_id = api_data_articles[i]["id"]
                type = api_data_articles[i]["type"]
                title = api_data_articles[i]["title"]
                if type == "editor":
                    list_type_editor.append(article_id)
                elif type == "interest":
                    list_type_interest.append(article_id)
                elif type == "popular":
                    list_type_popular.append(article_id)
                elif type == "sample":
                    list_type_sample.append(article_id)
                elif type not in list_type:
                    print("ERROR: Articles do not belongs to sub categories")
                    print(type)
                    print(title)
                    list_article_error.append(article_id)
            print("Total feeds :            ", len(api_data_articles))
            print("Number of type editor  : ", len(list_type_editor), ", weight: ", len(list_type_editor)/len(api_data_articles)*100, "%")
            print("Number of type interest: ", len(list_type_interest), ", weight: ", len(list_type_interest)/len(api_data_articles)*100, "%")
            print("Number of type popular : ", len(list_type_popular), ", weight: ", len(list_type_popular)/len(api_data_articles)*100, "%")
            print("Number of type sample  : ", len(list_type_sample), ", weight: ", len(list_type_sample)/len(api_data_articles)*100, "%")

        if len(list_article_error):
            # self.common.print_list(list_article_error)
            self.result = False
        assert self.result == True

    # NF-211: [NRE] Feedback and Improvement
    # On CMS, if we vote for an article, it should display on user feed after 15 minutes
    def test_get_user_feed_with_vote_articles(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid

        for i in range(len(list_vid)):
            vid = list_vid[i]
            sid = list_sid[i]

            list_article_vote = self.newsfeed_db.select_newfeeds_db(f'select article_id, title from coccoc_news_feed.articles where vote = "0" and status = "publish" order by update_time desc limit 2;')
            list_article_vote_id = self.newsfeed_db.get_list_db(list_article_vote, 0)
            list_article_vote_title = self.newsfeed_db.get_list_db(list_article_vote, 1)

            list_article_vote_id_str = self.common.convert_list_to_string(list_article_vote_id)
            print(list_article_vote_id_str)
            self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.articles set vote=1 where article_id in ("{list_article_vote_id_str}");')

            time.sleep(self.wait_time)

            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=1000)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]

            list_article_frontend = []
            for i in range(len(api_data_articles)):
                article_id = api_data_articles[i]["id"]
                list_article_frontend.append(article_id)
            for i in range(len(list_article_vote_id)):
                if list_article_vote_id[i] not in list_article_frontend:
                    print("ERROR: Vote article not display on frontend")
                    print("    ", list_article_vote_id[i])
                    print("    ", list_article_vote_title[i])
                    self.result = False
        assert self.result == True

    # NF-211: [NRE] Feedback and Improvement
    # On CMS, if we block article or source, then it will not show to user on feed after 15 minutes
    def test_get_user_feed_with_vote_articles(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid

        for i in range(len(list_vid)):
            vid = list_vid[i]
            # sid = list_sid[i]

            list_article_vote = self.newsfeed_db.select_newfeeds_db(f'select article_id, title from coccoc_news_feed.articles where vote = "0" and status = "publish" order by update_time desc limit 2;')
            list_article_vote_id = self.newsfeed_db.get_list_db(list_article_vote, 0)
            list_article_vote_title = self.newsfeed_db.get_list_db(list_article_vote, 1)

            # list_article_vote_id_str = self.common.convert_list_to_string(list_article_vote_id)
            # print(list_article_vote_id_str)
            # print(f'update coccoc_news_feed.articles set vote=1 where article_id in ("{list_article_vote_id_str}");')
            # self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.articles set vote=1 where article_id in ("{list_article_vote_id_str}");')
            for article_id in list_article_vote_id:
                self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.articles set vote=1 where article_id = "{article_id}";')

            time.sleep(self.wait_time)

            for j in range(10):
                params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=1000)
                api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
                self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
                api_data_articles = api_data["news"]

                list_article_frontend = []
                for i in range(len(api_data_articles)):
                    article_id = api_data_articles[i]["id"]
                    list_article_frontend.append(article_id)
                for i in range(len(list_article_vote_id)):
                    if list_article_vote_id[i] not in list_article_frontend:
                        print("ERROR: Vote article not display on frontend")
                        print("    ", list_article_vote_id[i])
                        print("    ", list_article_vote_title[i])
                        self.result = False
        assert self.result == True


    # NF-211: [NRE] Feedback and Improvement
    # On CMS, if we block article or source, then it will not show to user on feed after 15 minutes
    def test_get_user_feed_with_vote_articles(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid

        for i in range(len(list_vid)):
            vid = list_vid[i]
            # sid = list_sid[i]

            list_article_vote = self.newsfeed_db.select_newfeeds_db(f'select article_id, title from coccoc_news_feed.articles where vote = "0" and status = "publish" order by update_time desc limit 2;')
            list_article_vote_id = self.newsfeed_db.get_list_db(list_article_vote, 0)
            list_article_vote_title = self.newsfeed_db.get_list_db(list_article_vote, 1)

            # list_article_vote_id_str = self.common.convert_list_to_string(list_article_vote_id)
            # print(list_article_vote_id_str)
            # print(f'update coccoc_news_feed.articles set vote=1 where article_id in ("{list_article_vote_id_str}");')
            # self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.articles set vote=1 where article_id in ("{list_article_vote_id_str}");')
            for article_id in list_article_vote_id:
                self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.articles set vote=1, vote_user_id=28 where article_id = "{article_id}";')

            time.sleep(self.wait_time)

            for j in range(10):
                params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=1000)
                api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
                self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
                api_data_articles = api_data["news"]
                print("Number of articles: ", len(api_data_articles))

                list_article_frontend = []
                for i in range(len(api_data_articles)):
                    article_id = api_data_articles[i]["id"]
                    list_article_frontend.append(article_id)
                for i in range(len(list_article_vote_id)):
                    if list_article_vote_id[i] not in list_article_frontend:
                        print("ERROR: Vote article not display on frontend")
                        print("    ", list_article_vote_id[i], ": ", list_article_vote_title[i])
                        self.result = False
        assert self.result == True

    # NF-211: [NRE] Feedback and Improvement
    # On CMS, if we block article or source, then it will not show to user on feed
    def test_get_user_feed_with_block_sources(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid

        list_block_source = self.common.get_list_newsfeed_db(f'SELECT domain FROM coccoc_news_feed.sources where status = "inactive";')
        # list_block_source = [ "kenh14.vn" ]
        print(list_block_source)
        # for domain in list_block_source:
        #     self.newsfeed_db.update_newfeeds_db(
        #        f'update coccoc_news_feed.sources set status="inactive" where domain = "{domain}";')
        # time.sleep(self.wait_time)

        for i in range(len(list_vid)):
            vid = list_vid[i]
            sid = "ke15eloqe6hrpmbku"

            for j in range(10):
                params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=1000)
                api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
                self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
                api_data_articles = api_data["news"]
                print("Number of articles: ", len(api_data_articles))

                list_article_frontend_error = []
                # list_article_frontend_id = []
                # list_article_frontend_title = []
                for i in range(len(api_data_articles)):
                    article_id = api_data_articles[i]["id"]
                    domain = api_data_articles[i]["domain"]
                    title = api_data_articles[i]["title"]
                    if domain in list_block_source:
                        list_article_frontend_error.append(article_id + ": " + domain + ": " + title)
                if len(list_article_frontend_error):
                    print("ERROR: Article belongs blocked sources")
                    self.result = False
                    self.common.print_list(list_article_frontend_error)

        # Reset after testign
        # for source in list_block_source:
        #    self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.sources set status="active" where domain = "{source}";')

        assert self.result == True

    # NF-211: [NRE] Feedback and Improvement
    # On CMS, if we block article or source, then it will not show to user on feed after 15 minutes
    def test_get_user_feed_with_block_articles(self):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        list_sid = self.list_sid

        # Block some articles
        self.newsfeed_db.update_newfeeds_db(f'update coccoc_news_feed.articles set status="block" where status = "publish" order by rand() limit 5;')
        time.sleep(self.wait_time)

        for i in range(len(list_vid)):
            vid = list_vid[i]
            # sid = list_sid[i]

            list_block_articles = self.newsfeed_db.select_newfeeds_db(f'select article_id from coccoc_news_feed.articles where status = "block" order by update_time desc;')

            for j in range(10):
                params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=1000)
                api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
                self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
                api_data_articles = api_data["news"]
                print("Number of articles: ", len(api_data_articles))

                list_article_frontend = []
                for i in range(len(api_data_articles)):
                    article_id = api_data_articles[i]["id"]
                    title = api_data_articles[i]["title"]
                    if article_id in list_block_articles:
                        list_article_frontend.append(article_id + ": " + title)
                if len(list_article_frontend):
                    print("ERROR: Block articles still display on frontend")
                    self.common.print_list(list_article_frontend)
                    self.result = False
        assert self.result == True

    # NF-238: [NF-NRE] Select number of articles based on the interest proportion of topic & category
    # Open 100 websites by topics to make history
    # 1) expect chuẩn là với user đã có interest thì tỉ lệ interest là 80/100 tổng số bài phải ko?
    #    Em expect vậy, nhưng logic hiện tại đang chờ anh thắng confirm phần tỉ lệ đó
    # 2) nếu user đã có interest, trong đó có 70% sport, 30% education, vậy toàn bộ các bài trong interest sẽ chỉ là sport và education, hay còn bài nào khác ko?
    #    + với ngoài công thức em viết trong ticket chị thấy sẽ apply thêm một số Logic liên quan đến LAL + recommend content based , user based -> sẽ chèn thêm các bài người dùng tương tự đang quan tâm vào
    #    nên hiện tại phần user -> sẽ có các chuyên mục khác ( sẽ có tỉ lệ nhất định hiện tại em không control phân tỉ lệ đấy)
    # 3) nếu user mới tinh, chưa có interest thì tỉ lệ interest là bao nhiêu? hay mình ko quan tâm?
    #    mới tinh sẽ không có tỉ lệ interest
    # 4) để tính trọng số interest như sport 70%, education 30% thì mình dựa vào history của user trong 30 phút gần nhất phải ko ?
    #    trong khoảng 2 tuần chị, có decay weight. Nếu chị đọc 100 bài tuần trước về thể thao. 100 bài tuần này về sức khỏe. Thì trọng số của sức khỏe cao hơn
    # 5) Logic to apply:
    # - Allocate top 3 categories, following category weights ( eg. 70/30)
    # - Allocate top 5 topics ( following topic weight), AND lookalike articles to user profile
    # đoạn comment này em chỉ nói về interest thôi, hay đang nói chung toàn bộ bài vậy?
    #     chỉ cho interest thôi chị nhé
    # 6) category khác gì topic vậy ?
    #    topic nó chia  sâu và rộng hơn categories, nó thuộc phần thuật toán chạy ẩn bên trong recommendation

    # Make history
    def test_open_browser_with_urls(self, binary_path, default_directory):
        list_url = self.common.read_to_file("list_vehicle_articles.txt")    # Get from BI team: 100 url category_id = 10000 (Xã hội), 200 url category_id = 13000 (Kinh tế)
        # Open browser to get history
        self.open_list_webpage(binary_path, default_directory, list_url)
        # Wait for BI update
        time.sleep(self.wait_time_interest)


    def test_get_user_feed_with_1_interest(self, binary_path, default_directory):
        # global list_vid
        filename = self.set_filename("Userfeed")
        ratio_interest_expect = 80   # 80%
        category_id = 10000

        vid = self.list_vid[0]    # Check for 1 vid
        for j in range(5):
            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=5000)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]
            print("Number of articles: ", len(api_data_articles))

            list_article_frontend = []
            list_article_frontend_interest = []
            list_article_frontend_category_interest = []
            list_article_frontend_category_editor = []
            list_article_frontend_category_popular = []
            list_article_frontend_category_sample = []
            list_article_frontend_category = []
            for i in range(len(api_data_articles)):
                article_id = api_data_articles[i]["id"]
                title = api_data_articles[i]["title"]
                type = api_data_articles[i]["type"]
                category_id_api = api_data_articles[i]["category_id"]
                if type == "interest":
                    list_article_frontend_interest.append(article_id + ": " + title)
                if type == "interest" and category_id_api == category_id:
                    list_article_frontend_category_interest.append(article_id + ": " + title)
                if type == "editor" and category_id_api == category_id:
                    list_article_frontend_category_editor.append(article_id + ": " + title)
                if type == "popular" and category_id_api == category_id:
                    list_article_frontend_category_popular.append(article_id + ": " + title)
                if type == "sample" and category_id_api == category_id:
                    list_article_frontend_category_sample.append(article_id + ": " + title)
                if category_id_api == category_id:
                    list_article_frontend_category.append(article_id + ": " + title)
                list_article_frontend.append(article_id + ": " + title)

            print("list_article_frontend_interest         : ", len(list_article_frontend_interest))
            print("list_article_frontend_category_interest: ", len(list_article_frontend_category_interest))
            print("list_article_frontend_category_editor  : ", len(list_article_frontend_category_editor))
            print("list_article_frontend_category_popular : ", len(list_article_frontend_category_popular))
            print("list_article_frontend_category_sample  : ", len(list_article_frontend_category_sample))
            ratio_interest_actual = self.common.division_percentage(len(list_article_frontend_category_interest), len(list_article_frontend_interest))
            print("Ratio of category ", category_id, " in total interest  : ", ratio_interest_actual, "%")
            if ratio_interest_actual != ratio_interest_expect:
                print("ERROR: Ratio of interest does not matched")
                print("    Expect: ", ratio_interest_expect)
                print("    Actual: ", ratio_interest_actual)
                self.result = False
            ratio_interest_total_feed = self.common.division_percentage(len(list_article_frontend_interest), len(list_article_frontend))
            print("Ratio of interest in total feeds  : ", ratio_interest_total_feed, "%")
            total_feed_category = len(list_article_frontend_category_interest)+ len(list_article_frontend_category_editor) + len(list_article_frontend_category_popular) + len(list_article_frontend_category_sample)
            ratio_categories_actual = self.common.division_percentage(total_feed_category, len(list_article_frontend))
            print("Ratio of category in total feeds", category_id, " in total feeds  : ", ratio_categories_actual, "%")
        assert self.result == True

    # User like 2 interest
    def test_get_user_feed_with_2_interest(self, binary_path, default_directory):
        filename = self.set_filename("Userfeed")
        list_vid = self.list_vid
        ratio_interest_expect = 80   # 80%

        list_categories = [ "Kinh tế", "Xã hội"]
        list_category_id = [ 10000, 13000]
        list_ratio_interest = [ 70, 30 ]


        vid = list_vid[0]    # Check for 1 vid
        for j in range(5):
            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=51000)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            self.common.append_to_file(filename, self.newsfeed_api.full_api_url, type="string")
            api_data_articles = api_data["news"]
            print("Number of articles: ", len(api_data_articles))

            list_article_frontend = []
            list_article_frontend_interest = []
            list_article_frontend_category_0 = []
            list_article_frontend_category_1 = []
            for i in range(len(api_data_articles)):
                article_id = api_data_articles[i]["id"]
                title = api_data_articles[i]["title"]
                type = api_data_articles[i]["type"]
                category_id_api = api_data_articles[i]["category_id"]
                if type == "interest" or (type == "popular" and category_id_api in list_category_id):
                    list_article_frontend_interest.append(article_id + ": " + title)
                    if category_id_api == list_category_id[0]:
                        list_article_frontend_category_0.append(article_id + ": " + title)
                    elif category_id_api == list_category_id[1]:
                        list_article_frontend_category_1.append(article_id + ": " + title)
                list_article_frontend.append(article_id + ": " + title)

            ratio_interest_actual = len(list_article_frontend_interest) / len(list_article_frontend) * 100
            print("Ratio of interest in total feeds  : ", ratio_interest_actual, "%")
            if ratio_interest_actual != ratio_interest_expect:
                print("ERROR: Ratio of interest does not matched")
                print("    Expect: ", ratio_interest_expect)
                print("    Actual: ", ratio_interest_actual)
                self.result = False
            ratio_categories_actual_0 = len(list_article_frontend_category_0) / len(list_article_frontend_interest) * 100
            print("Ratio of category ", list_category_id[0], " in total feeds  : ", ratio_categories_actual_0, "%")
            if ratio_categories_actual_0 != list_ratio_interest[0]:
                print("ERROR: Ratio of categories does not matched")
                print("    Expect: ", list_ratio_interest[0])
                print("    Actual: ", ratio_categories_actual_0)
            ratio_categories_actual_1 = len(list_article_frontend_category_1) / len(list_article_frontend_interest) * 100
            print("Ratio of category ", list_category_id[1], " in total feeds  : ", ratio_categories_actual_1, "%")
            if ratio_categories_actual_1 != list_ratio_interest[1]:
                print("ERROR: Ratio of categories does not matched")
                print("    Expect: ", list_ratio_interest[1])
                print("    Actual: ", ratio_categories_actual_1)
        assert self.result == True

    # Open list of urls in browser
    def open_list_webpage(self, binary_file, default_dir, list_url):
        browser = self.open_webpage(binary_file, default_dir)
        for url in list_url:
            LOGGER.info(url)
            browser.get(url)
            time.sleep(1)
        browser.close()

    def open_webpage(self, binary_file, default_dir):
        prog = subprocess.Popen("taskkill /im chromedriver.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog = subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()

        global startBrowser

        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        opts.add_argument('user-data-dir=' + default_dir)
        # opts.add_argument("--headless --disable-gpu")
        # opts.add_argument("--window-size=1920,1080")
        # opts.add_argument("--proxy-server='direct://'")
        # opts.add_argument("--proxy-bypass-list=*")
        # opts.add_argument("--start-maximized")
        # opts.add_argument('--disable-gpu')
        # opts.add_argument('--disable-dev-shm-usage')
        # opts.add_argument('--no-sandbox')
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--allow-insecure-localhost")

        caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = "normal"  # complete
        # caps["pageLoadStrategy"] = "eager"
        startBrowser = int(round(time.time() * 1000))
        driver = webdriver.Chrome(chrome_options=opts, desired_capabilities=caps)
        # driver.get(source)
        return driver

    # NF-297: [Frontend] Integrate frontend api block list domains & single api for user settings
    def test_frontend_user_actions_block_sources(self):
        # Get list vid
        # my vid : 693y6GJ61CGT91oTSu1u9GV1J9J6Gu996TuoW2nBb9rofPtd8jQneKDZZdOWW

        for vid in self.list_vid:
            list_block_source_db = self.common.get_list_newsfeed_db(f"SELECT domain FROM coccoc_news_feed.user_block_sources where vid = '{vid}';")
            params = self.newsfeed_api.set_vid_data(vid)
            api_user_setting = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_SETTING, params=params)
            list_domain_api = []
            for i in range(len(api_user_setting["block_sources"])):
                list_domain_api.append(api_user_setting["block_sources"][i]["domain"])

            self.result = self.common.check_if_lists_are_different(list_domain_api, list_block_source_db)
        assert self.result == True

    # NF-318: Full-flow test for NewsFeed (20%) release
    # I want read only updated news (last 3 days) and as soon as possible after it is published (less than 1 hours)
    def test_check_user_feed_news_in_last_3_days(self, binary_path, default_directory):
        vid = self.list_vid[0]
        current_time = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
        print(current_time)

        expired_time = 3

        params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=None, size=1000)
        api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
        api_data_articles = api_data["news"]
        print("Number of articles: ", len(api_data_articles))

        for i in range(len(api_data_articles)):
            article_id = api_data_articles[i]["id"]
            title = api_data_articles[i]["title"]
            url = api_data_articles[i]["url"]
            event_time = api_data_articles[i]["event_time"]
            print("    event_time    : ", event_time)
            threshold = self.common.subtraction_days(current_time, event_time)
            # published_time = self.common.get_parse_news_fetch(url, "published_time")
            # threshold = self.common.subtraction_days(current_time, published_time)

            if threshold > expired_time:
                print("ERROR: Article is too late:")
                print("    article       : ", article_id, " : ", title)
                print("    url           : ", url)
                print("    event_time    : ", event_time)
                # print("    published_time: ", published_time)
                print("    threshold     : ", threshold)
                self.result = False

        assert self.result == True

    # NF-316: [Frontend Api] Improve pattern data for each page
    def test_pattern_data(self):
        vid = self.list_vid[0]
        # sid = "ke0zz18gmji7swpd5"
        sid = None
        # Small page
        number_of_pages = 1
        page_size = 1200
        number_of_editor_expect = 3
        number_of_popular_expect = 17
        number_of_interest_expect = 7
        number_of_sample_expect = 3

        # Total pages
        # number_of_pages = 1
        # page_size = 2000
        # number_of_editor_expect = 200
        # number_of_popular_expect = 921
        # number_of_interest_expect = 412
        # number_of_sample_expect = 204

        ratio_of_editor_expect = 11.52
        ratio_of_popular_expect = 53.02
        ratio_of_interest_expect = 23.72
        ratio_of_sample_expect = 11.74

        for i in range(number_of_pages):
            LOGGER.info("Page %s" %i)
            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=sid, page=i, size=page_size)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            api_data_articles = api_data["news"]
            print("Number of articles: ", len(api_data_articles))

            list_editor_articles = []
            list_popular_articles = []
            list_interest_articles = []
            list_sample_articles = []
            for i in range(len(api_data_articles)):
                article_id = api_data_articles[i]["id"]
                type = api_data_articles[i]["type"]
                title = api_data_articles[i]["title"]
                if type == "editor":
                    list_editor_articles.append(article_id)
                elif type == "popular":
                    list_popular_articles.append(article_id)
                elif type == "interest":
                    list_interest_articles.append(article_id)
                elif type == "sample":
                    list_sample_articles.append(article_id)
            self.assert_equals(number_of_editor_expect, len(list_editor_articles), "Number editor")
            self.assert_equals(number_of_popular_expect, len(list_popular_articles), "Number popular")
            self.assert_equals(number_of_interest_expect, len(list_interest_articles), "Number interest")
            self.assert_equals(number_of_sample_expect, len(list_sample_articles), "Number sample")

            ratio_of_editor_actual = self.common.division_percentage(len(list_editor_articles), len(api_data_articles))
            ratio_of_popular_actual = self.common.division_percentage(len(list_popular_articles), len(api_data_articles))
            ratio_of_interest_actual = self.common.division_percentage(len(list_interest_articles), len(api_data_articles))
            ratio_of_sample_actual = self.common.division_percentage(len(list_sample_articles), len(api_data_articles))

            self.assert_equals(ratio_of_editor_expect, ratio_of_editor_actual, "Ratio editor")
            self.assert_equals(ratio_of_popular_expect, ratio_of_popular_actual, "Ratio popular")
            self.assert_equals(ratio_of_interest_expect, ratio_of_interest_actual, "Ratio interest")
            self.assert_equals(ratio_of_sample_expect, ratio_of_sample_actual, "Ratio sample")

        assert self.result == False

    # NF-260: User have click on feed with get update articles after 10 minutes, feed need filter articles shown more than 3 times or already clicked by this user
    def test_interest_articles_appear_3_times(self):
        vid = self.list_vid[0]
        # sid = "ke0zz18gmji7swpd5"
        sid = None
        article_title = "Cựu Chủ tịch Petroland Bùi Minh Chính làm thất thoát 50 tỷ"
        # Small page
        loop = 5
        wait_time_update = 1200 # Wait for 20 minutes

        for i in range(loop):
            LOGGER.info("Page %s" %i)
            params = self.newsfeed_api.set_user_feed_data(vid=vid, sid=sid, page=0, size=1200)
            api_data = self.newsfeed_api.request_get_new_feeds(COCCOC_NEW_FEED_API_FE_USER_FEED, params=params)
            api_data_articles = api_data["news"]
            print("Number of articles: ", len(api_data_articles))

            if i > 3:
                time.sleep(wait_time_update)    # Wait update cache
            for j in range(len(api_data_articles)):
                title = api_data_articles[j]["title"]
                if title == article_title:
                    LOGGER.info("Found: %s : %s" % (j, title))
                    self.result = False
                    time.sleep(60)
        assert self.result == True

    def assert_equals(self, expect, actual, fail_message = None):
        global result
        if expect != actual:
            if fail_message is not None:
                LOGGER.info("ERROR: %s are not equal: expect %s != actual %s" % (fail_message, expect, actual))
                # print("ERROR: %s are not equal: expect %s != actual %s" % (fail_message, expect, actual))
            result = False







