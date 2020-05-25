from databases.sql.coccoc_game_crawler_db import CocCocGameCrawler


class TestNumberGame:
    coccoc_game_crawler_db = CocCocGameCrawler()

    def test_game_number(self, coccoc_music_crawler_db_interact):
        rows = self.coccoc_game_crawler_db.get_all_games_by_category(connection=coccoc_music_crawler_db_interact
                                                                     , category_id=4)
        print(len(rows))
