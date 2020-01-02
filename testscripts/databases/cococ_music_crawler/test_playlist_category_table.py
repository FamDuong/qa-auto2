from pytest_testrail.plugin import pytestrail
from utils_automation.database import CocCocMusicCrawler

cococ_music_crawler = CocCocMusicCrawler()


@pytestrail.case('C131181')
def test_playlist_id(coccoc_music_crawler_db_interact):
    row_one_result_playlist_category = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact,
                                                                                     'playlist_category')
    playlist_id_value = row_one_result_playlist_category['playlist_id']
    rows_all_playlist_songs = cococ_music_crawler.get_all_rows_from_table_where_column_has_value(
        coccoc_music_crawler_db_interact, 'playlist_id', playlist_id_value, 'playlist_song'
    )
    rows_all_playlist_artist = cococ_music_crawler.get_all_rows_from_table_where_column_has_value(
        coccoc_music_crawler_db_interact, 'playlist_id', playlist_id_value, 'playlist_artist'
    )
    rows_all_playlists = cococ_music_crawler.get_all_rows_from_table_where_column_has_value(
        coccoc_music_crawler_db_interact, 'playlist_id', playlist_id_value, 'playlists'
    )
    assert len(rows_all_playlist_songs) > 0
    assert len(rows_all_playlist_artist) > 0
    assert len(rows_all_playlists) > 0


@pytestrail.case('C131182')
def test_category_id(coccoc_music_crawler_db_interact):
    null_or_empty_result = cococ_music_crawler.check_if_value_null_or_empty_in_column(
        coccoc_music_crawler_db_interact, 'category_id', 'playlist_category')
    one_result_playist_category = cococ_music_crawler.get_one_result_from_table(
        coccoc_music_crawler_db_interact, 'playlist_category'
    )
    category_id = one_result_playist_category['category_id']
    one_result_condition_categories = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'category_id', category_id, 'categories'
    )
    one_result_condition_source_datafeeds = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'category_id', category_id, 'source_datafeeds'
    )
    assert null_or_empty_result[0] == 0
    assert one_result_condition_categories is not None
    assert one_result_condition_source_datafeeds is not None


@pytestrail.case('C131183')
def test_create_time(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'playlist_category')
    create_time = row['create_time']
    from utils_automation.date_time_utils import how_many_days_til_now
    import datetime
    # Validate format of time
    datetime.datetime.strptime(str(create_time), '%Y-%m-%d %H:%M:%S')
    assert how_many_days_til_now(create_time) >= 0


@pytestrail.case('C131184')
def test_update_time(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'playlist_category')
    create_time = row['create_time']
    update_time = row['update_time']
    from utils_automation.date_time_utils import how_many_seconds_between_times
    assert how_many_seconds_between_times(update_time, create_time) >= 0



