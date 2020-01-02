from pytest_testrail.plugin import pytestrail
from utils_automation.database import CocCocMusicCrawler

cococ_music_crawler = CocCocMusicCrawler()


@pytestrail.case('C131185')
def test_playlist_id(coccoc_music_crawler_db_interact):
    null_or_empty = cococ_music_crawler.check_if_value_null_or_empty_in_column(
        coccoc_music_crawler_db_interact, 'playlist_id', 'playlist_song'
    )
    one_row_result_playlist_song = cococ_music_crawler.get_one_result_from_table(
        coccoc_music_crawler_db_interact, 'playlist_song'
    )
    playlist_id = one_row_result_playlist_song['playlist_id']
    one_row_result_playlists = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'playlist_id', playlist_id, 'playlists'
    )
    one_row_result_playlist_category = cococ_music_crawler.get_one_result_from_table_with_condition(
        coccoc_music_crawler_db_interact, 'playlist_id',playlist_id, 'playlist_category'
    )
    assert null_or_empty[0] == 0
    assert one_row_result_playlists is not None
    assert one_row_result_playlist_category is not None


@pytestrail.case('C131186')
def test_song_id(coccoc_music_crawler_db_interact):
    pass







