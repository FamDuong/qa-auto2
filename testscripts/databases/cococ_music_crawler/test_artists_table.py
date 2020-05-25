from pytest_testrail.plugin import pytestrail

from databases.sql.coccoc_music_crawler_db import CocCocMusicCrawler

cococ_music_crawler = CocCocMusicCrawler()


@pytestrail.case('C131153')
def test_artist_id(coccoc_music_crawler_db_interact):
    rows = cococ_music_crawler.check_if_duplicate_value_in_column(coccoc_music_crawler_db_interact, 'artist_id', 'artists')
    assert len(rows) == 0


@pytestrail.case('C131154')
def test_artist_name(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.check_if_value_null_or_empty_in_column(coccoc_music_crawler_db_interact, 'name', 'artists')
    assert row[0] == 0


@pytestrail.case('C131155')
def test_image_url(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'artists')
    image_url = row['image_url']
    if image_url is not None:
        import re
        text_found = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                               , image_url)
        assert text_found is not None
    else:
        pass


@pytestrail.case('C131156')
def test_create_time(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'artists')
    create_time = row['create_time']
    from utils_automation.date_time_utils import how_many_days_til_now
    import datetime
    # Validate format of time
    datetime.datetime.strptime(str(create_time), '%Y-%m-%d %H:%M:%S')
    assert how_many_days_til_now(create_time) >= 0


@pytestrail.case('C131157')
def test_update_time(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'artists')
    create_time = row['create_time']
    update_time = row['update_time']
    from utils_automation.date_time_utils import how_many_seconds_between_times
    assert how_many_seconds_between_times(update_time, create_time) >= 0













