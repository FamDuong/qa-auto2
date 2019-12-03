from pytest_testrail.plugin import pytestrail

from utils_automation.database import CocCocMusicCrawler

cococ_music_crawler = CocCocMusicCrawler()


@pytestrail.case('C131161')
def test_playlist_id(cococ_music_crawler_db_interact):
    rows = cococ_music_crawler.check_if_duplicate_value_in_column(cococ_music_crawler_db_interact, 'playlist_id'
                                                                  , 'playlists')
    row_one_result_playlists = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact,
                                                                             'playlists')
    playlist_id_value = row_one_result_playlists['playlist_id']
    rows_all_playlist_category = cococ_music_crawler.get_all_rows_from_table_where_column_has_value(
        cococ_music_crawler_db_interact, 'playlist_id', playlist_id_value, 'playlists')
    rows_all_playlist_songs = cococ_music_crawler.get_all_rows_from_table_where_column_has_value(
        cococ_music_crawler_db_interact, 'playlist_id', playlist_id_value, 'playlists'
    )
    assert len(rows_all_playlist_songs) > 0
    assert len(rows_all_playlist_category) > 0
    assert len(rows) == 0


@pytestrail.case('C131162')
def test_source_id(cococ_music_crawler_db_interact):
    rows = cococ_music_crawler.get_all_distinct_value_from_column_in_table(cococ_music_crawler_db_interact, 'source_id'
                                                                           , 'playlists')
    assert len(rows) == 2
    for each_row in rows:
        assert each_row[0] in ('nhaccuatui', 'zingmp3')


@pytestrail.case('C131163')
def test_playlist_type(cococ_music_crawler_db_interact):
    rows = cococ_music_crawler.get_all_distinct_value_from_column_in_table(cococ_music_crawler_db_interact
                                                                           , 'playlist_type', 'playlists')
    assert len(rows) <= 2
    for each_row in rows:
        assert each_row[0] in ('manual', 'crawl')


@pytestrail.case('C131164')
def test_playlist_title(cococ_music_crawler_db_interact):
    row = cococ_music_crawler.check_if_value_null_or_empty_in_column(cococ_music_crawler_db_interact
                                                                     , 'title', 'playlists')
    assert row[0] == 0


@pytestrail.case('C131165')
def test_image_url(cococ_music_crawler_db_interact):
    row = cococ_music_crawler.check_if_value_null_or_empty_in_column(cococ_music_crawler_db_interact
                                                                     , 'image_url', 'playlists')
    one_result = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact
                                                               , 'playlists')
    image_url = one_result['image_url']
    import requests
    response = requests.get(image_url)
    from delayed_assert import expect
    expect(row[0] == 0)
    expect(200 <= response.status_code < 300)
    from delayed_assert import assert_expectations
    assert_expectations()


@pytestrail.case('C131166')
def test_image_thumbnail_url(cococ_music_crawler_db_interact):
    row = cococ_music_crawler.check_if_value_null_or_empty_in_column(cococ_music_crawler_db_interact
                                                                     , 'image_thumbnail_url', 'playlists')
    one_result = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact
                                                               , 'playlists')
    image_url = one_result['image_thumbnail_url']
    import requests
    response = requests.get(image_url)
    from delayed_assert import expect
    expect(row[0] == 0)
    expect(200 <= response.status_code < 300)
    from delayed_assert import assert_expectations
    assert_expectations()


@pytestrail.case('C131167')
def test_playlist_url(cococ_music_crawler_db_interact):
    from utils_automation.web_scraping_utils import WebScrapingCocCocCrawler
    web_scrape_coccoc_crawler = WebScrapingCocCocCrawler()
    number_of_songs = None
    row = cococ_music_crawler.check_if_value_null_or_empty_in_column(cococ_music_crawler_db_interact
                                                                     , 'url', 'playlists')
    one_result = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact
                                                               , 'playlists')
    playlist_url = one_result['url']
    playlist_id = one_result['playlist_id']
    source_id = one_result['source_id']
    import requests
    response = requests.get(playlist_url)
    if source_id == 'zingmp3':
        number_of_songs = web_scrape_coccoc_crawler.get_number_of_songs_in_zingmp3(response.text)
    elif source_id == 'nhaccuatui':
        number_of_songs = web_scrape_coccoc_crawler.get_number_of_songs_in_nhac_cua_tui(response.text)
    else:
        raise Exception
    number_of_songs_in_playlist_song = len(cococ_music_crawler.get_all_rows_from_table_where_column_has_value(
        cococ_music_crawler_db_interact, 'playlist_id', playlist_id, 'playlist_song'))
    from delayed_assert import expect
    expect(row[0] == 0)
    expect(200 <= response.status_code < 300)
    expect(number_of_songs == number_of_songs_in_playlist_song)
    from delayed_assert import assert_expectations
    assert_expectations()


@pytestrail.case('C131168')
def test_playlist_api(cococ_music_crawler_db_interact):
    # Check playlist_api for source_id is nhaccuatui
    result_nhac_cua_tui = cococ_music_crawler.get_one_result_from_table_with_condition(cococ_music_crawler_db_interact
                                                                                       , 'source_id', 'nhaccuatui'
                                                                                       , 'playlists')
    assert result_nhac_cua_tui['playlist_api'] is None
    # Check playlist_api for source_id is zingmp3

    result_zingmp3 = cococ_music_crawler.get_one_result_from_table_with_condition(cococ_music_crawler_db_interact
                                                                                  , 'source_id', 'zingmp3', 'playlists')
    assert result_zingmp3['playlist_api'] is not None
    import re
    text_found = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                           , result_zingmp3['playlist_api'])
    assert text_found is not None


@pytestrail.case('C131169')
def test_status(cococ_music_crawler_db_interact):
    status_tuple = cococ_music_crawler.get_all_distinct_value_from_column_in_table(cococ_music_crawler_db_interact
                                                                                   , 'status', 'playlists')
    for each_status in status_tuple:
        assert each_status[0] in ['new', 'ready for review', 'published', 'rejected', 'unlisted', 'error']


@pytestrail.case('C131170')
def test_raw_views(cococ_music_crawler_db_interact):
    one_row_result = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact
                                                                   , 'playlists')
    raw_views = one_row_result['raw_views']
    views = one_row_result['views']
    if raw_views is not None and views is not None:
        assert raw_views <= views
    else:
        pass


@pytestrail.case('C131171')
def test_raw_likes(cococ_music_crawler_db_interact):
    one_row_result = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact
                                                                   , 'playlists')
    raw_views = one_row_result['raw_likes']
    views = one_row_result['likes']
    if raw_views is not None and views is not None:
        assert raw_views <= views
    else:
        pass


@pytestrail.case('C131174')
def test_create_time(cococ_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact, 'playlists')
    create_time = row['create_time']
    from utils_automation.date_time_utils import how_many_days_til_now
    import datetime
    # Validate format of time
    datetime.datetime.strptime(str(create_time), '%Y-%m-%d %H:%M:%S')
    assert how_many_days_til_now(create_time) >= 0


@pytestrail.case('C131175')
def test_update_time(cococ_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact, 'playlists')
    create_time = row['create_time']
    update_time = row['update_time']
    from utils_automation.date_time_utils import how_many_seconds_between_times
    assert how_many_seconds_between_times(update_time, create_time) >= 0

