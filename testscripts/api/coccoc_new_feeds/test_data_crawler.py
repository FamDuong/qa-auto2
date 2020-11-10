import  json
import logging

from api.coccoc_new_feeds.coccoc_new_feeds_crawler.coccoc_new_feeds_api import NewFeedAPI;

LOGGER = logging.getLogger(__name__)

new_feed_data = NewFeedAPI()

class TestDataCrawler:

    def test_get_data_crawler(self):
        response_api_get_data = new_feed_data.get_data_crawler()
        api_get_data = json.loads(response_api_get_data.content)

        number_of_hosts = len(api_get_data['sample'])
        for i in range(number_of_hosts):
            LOGGER.info(api_get_data['sample'][i]['host'])
            number_of_urls = len(api_get_data['sample'][i]['urls'])
            for j in range(number_of_urls):
                LOGGER.info(api_get_data['sample'][i]['urls'][j])


