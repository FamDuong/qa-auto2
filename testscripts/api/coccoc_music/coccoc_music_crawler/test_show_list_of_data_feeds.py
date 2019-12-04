from pytest_testrail.plugin import pytestrail
from api.coccoc_music.coccoc_music_crawler.data_feeds import DataFeedsAPI

data_feeds_api = DataFeedsAPI()


@pytestrail.case('C137236')
def test_number_of_data_feeds():
    for source_id in ['nhaccuatui', 'zingmp3']:
        list_data_feeds_response = data_feeds_api.show_list_of_data_feeds(source_id)
        print(list_data_feeds_response)




