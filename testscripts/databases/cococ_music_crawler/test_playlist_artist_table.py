from pytest_testrail.plugin import pytestrail

from utils_automation.database import CocCocMusicCrawler

cococ_music_crawler = CocCocMusicCrawler()


@pytestrail.case('C131177')
def test_playlist_id(coccoc_music_crawler_db_interact):
    null_or_empty_value = cococ_music_crawler.check_if_value_null_or_empty_in_column(coccoc_music_crawler_db_interact
                                                                                     , 'playlist_id', 'playlist_artist')
    one_row_result = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'playlist_artist')
    playlist_id = one_row_result['playlist_id']
    one_row_result_table_playlists = cococ_music_crawler.get_one_result_from_table_with_condition \
        (coccoc_music_crawler_db_interact
         , 'playlist_id', playlist_id
         , 'playlists')
    one_row_result_table_playlist_category = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'playlist_id', playlist_id, 'playlist_category'
    )
    assert one_row_result_table_playlists is not None
    assert one_row_result_table_playlist_category is not None
    assert null_or_empty_value[0] == 0


@pytestrail.case('C131178')
def test_artist_id(coccoc_music_crawler_db_interact):
    null_or_empty_artist_id = cococ_music_crawler.check_if_value_null_or_empty_in_column(
        coccoc_music_crawler_db_interact, 'artist_id'
        , 'playlist_artist')
    one_row_result = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'playlist_artist')
    artist_id = one_row_result['artist_id']
    one_row_result_artists_table = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'artist_id', artist_id, 'artists'
    )
    one_row_result_song_artist_table = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'artist_id', artist_id, 'song_artist'
    )
    assert null_or_empty_artist_id[0] == 0
    assert one_row_result_artists_table is not None
    assert one_row_result_song_artist_table is not None


@pytestrail.case('C131179')
def test_create_time(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'playlist_artist')
    create_time = row['create_time']
    from utils_automation.date_time_utils import how_many_days_til_now
    import datetime
    # Validate format of time
    datetime.datetime.strptime(str(create_time), '%Y-%m-%d %H:%M:%S')
    assert how_many_days_til_now(create_time) >= 0


@pytestrail.case('C131180')
def test_update_time(coccoc_music_crawler_db_interact):
    row = cococ_music_crawler.get_one_result_from_table(coccoc_music_crawler_db_interact, 'playlist_artist')
    create_time = row['create_time']
    update_time = row['update_time']
    from utils_automation.date_time_utils import how_many_seconds_between_times
    assert how_many_seconds_between_times(update_time, create_time) >= 0



