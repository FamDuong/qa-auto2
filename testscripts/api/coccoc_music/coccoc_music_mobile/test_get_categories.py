from api.coccoc_music.coccoc_music_mobile.categories_api import CategoriesAPI
from models.api.coccoc_music.category_schema import ResultsCategorySchema
from utils_automation.database import CocCocMusicCrawler


class TestGetCategories:

    categories_api = CategoriesAPI()
    results_category_schema = ResultsCategorySchema()
    coccoc_music_crawler = CocCocMusicCrawler()

    def test_verify_number_of_categories(self, coccoc_music_crawler_db_interact):
        response_categories_api = self.categories_api.get_categories()
        list_playlists = response_categories_api.json()
        number_of_categories = self.results_category_schema.load(list_playlists).get('results')
        rows = self.coccoc_music_crawler.get_all_rows_from_table(coccoc_music_crawler_db_interact, 'categories')
        print(len(rows))
        assert 0 < len(number_of_categories) <= 60
        assert len(rows) >= len(number_of_categories)
