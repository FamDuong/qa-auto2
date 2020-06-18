import  json
import string
from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import DatafeedAPI;
from databases.sql.coccoc_new_feeds_db import NewFeedsDB;

from config.environment import COCCOC_NEW_FEED_DATA_URL

class TestDataCrawler:
    new_feed_api = DatafeedAPI()
    new_feed_db = NewFeedsDB()

    # Test data crawler
    def test_data_crawler(self, coccoc_new_feeds_db_interact):
        result = True
        api_data = self.new_feed_api.request_get_new_feeds(COCCOC_NEW_FEED_DATA_URL)
        api_data = api_data['sample']
        list_api_hostname = self.new_feed_api.get_list_json_level_1(api_data, 'host')
        db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(hostname) from hosts;')
        list_db_hostname = self.new_feed_db.get_list_db(db_data, 0)

        # Check if duplicated hostname
        result = self.new_feed_api.check_if_element_duplicated(list_api_hostname)
        if result is False:
            print("ERROR: Duplicated hostname")

        # Check if api host name is not same db hostname
        result = self.new_feed_api.check_if_element_different_in_lists(list_db_hostname, list_db_hostname)
        if result is False:
            print("ERROR: hostname in hosts table")

        for hostname in list_api_hostname:
            print("hostname: ", hostname)
            list_api_urls = self.new_feed_api.get_list_json_level_2(api_data, 'host', hostname, 'urls')
            # db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select url from urls where host_id in (select id from hosts where hostname ="{hostname}");')
            db_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select distinct(url) from urls where id not in (select distinct(url_id) from assessed_data) and date(create_time) = curdate() and host_id in (select distinct(id) from hosts where hostname="{hostname}");')
            list_db_urls = self.new_feed_db.get_list_db(db_data, 0)

            # For each host we will have 50 new urls everyday
            if len(list_api_urls) != 50:
                print("    ERROR: Host has not enough urls", " : ", len(list_api_urls))
                result = False

            # Check if duplicated url for each hostname
            result_tmp = self.new_feed_api.check_if_element_duplicated(list_api_urls)
            if result_tmp is False:
                print("    ERROR: Duplicated url")
                result = False

            # Check if url belong the hostname
            result_tmp = self.new_feed_api.check_if_elements_in_lists_contains_string(list_api_urls, hostname)
            if result_tmp is False:
                print("    ERROR: url NOT belong the hostname")
                result = False

            # (T.B.D) Check if url in DB if not in assessed_data table
            # result_tmp = self.new_feed_api.check_if_element_different_in_lists(list_db_urls, list_api_urls)
            # if result_tmp is False:
            #    print("    ERROR: url in urls table")
            #    result = False

            # Check if data in assessed_data table are not clear
            # Must do by manual

        assert result == True



    # For each host: We will remove old urls which belong to this host and NOT IN assessed_data table (We need to keep old version)
    def test_urls_in_db(self, coccoc_new_feeds_db_interact):
        # Get from crawler
        result = True
        api_get_data = self.new_feed_api.get_data_crawler()

        number_of_hosts = len(api_get_data['sample'])
        for i in range(number_of_hosts):
            api_hostname = api_get_data['sample'][i]['host']
            # Maximum 50 urls are added
            db_get_url = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact,
                                                          f'select distinct(url) from urls where id not in (select distinct(url_id) from assessed_data) and date(create_time) = curdate() and host_id in (select distinct(id) from hosts where hostname="{api_hostname}");')
            print(api_hostname, ": ", len(db_get_url))
            if len(db_get_url) > 50:
                print("ERROR: There are more than 50 urls are saved for ", api_hostname)
                result = False
            api_number_urls = len(api_get_data['sample'][i]['urls'])
            db_get_url_assess_data = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact,
                                                                      f'select url from urls where id in (select distinct(url_id) from assessed_data) and host_id in (select id from hosts where hostname ="{api_hostname}") and date(create_time) != curdate();')
            total_url = len(db_get_url_assess_data) + api_number_urls
            # Check total url
            db_get_url = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact,
                                                          f'select url from urls where host_id in (select id from hosts where hostname ="{api_hostname}");')
            if len(db_get_url) != total_url:
                print("ERROR: Total URL are not correct: ", api_hostname, ": ", total_url, " - ", len(db_get_url))
                result = False

        # Check there is no url which is not in assess_data, and create date is not today
        db_get_url = self.new_feed_db.get_newfeeds_db(coccoc_new_feeds_db_interact, f'select * from urls where id not in (select distinct(url_id) from assessed_data) and date(create_time) != curdate();')
        if len(db_get_url) != 0:
            print("ERROR: There are some urls which is not in assess_date and create date is not today")
            result = False

        assert result == True






