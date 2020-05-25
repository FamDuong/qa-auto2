class CocCocGameApiDb:

    def get_games_hightlighted_home_api_db(self, connection,):
        sql_query = 'select * from games where for_mobile = 1 and feature_game = 1 order by priority desc limit 20;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_games_categories_db(self, connection,):
        sql_query = 'select * from games inner join game_category gc on games.game_id = gc.game_id where for_mobile = 1 and category_id in (select category_id from game_category) order by priority desc limit 20;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_game_ids_for_hightlighted_home_api_db(self, connection):
        sql_query = 'select game_id from games where for_mobile = 1 and feature_game = 1 order by priority desc limit 20;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_game_recommended_home_api_db(self, connection, exclude_game_id=()):
        sql_query = f'select * from games where for_mobile = 1 and hot_game = 1 and game_id not in {exclude_game_id} order by priority desc limit 20;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows



