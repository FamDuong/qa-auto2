from pytest_testrail.plugin import pytestrail

from utils_automation.database import CocCocMusicCrawler

cococ_music_crawler = CocCocMusicCrawler()


@pytestrail.case('C131161')
def test_playlist_id(cococ_music_crawler_db_interact):
    rows = cococ_music_crawler.check_if_duplicate_value_in_column(cococ_music_crawler_db_interact, 'playlist_id'
                                                                  , 'playlists')
    row_one_result_playlists = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact, 'playlists')
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
    row = cococ_music_crawler.check_if_value_null_or_empty_in_column(cococ_music_crawler_db_interact
                                                                     , 'url', 'playlists')
    one_result = cococ_music_crawler.get_one_result_from_table(cococ_music_crawler_db_interact
                                                               , 'playlists')
    image_url = one_result['url']
    import requests
    response = requests.get(image_url)
    from delayed_assert import expect
    expect(row[0] == 0)
    expect(200 <= response.status_code < 300)
    from delayed_assert import assert_expectations
    assert_expectations()





