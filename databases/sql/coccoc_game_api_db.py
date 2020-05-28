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

    def get_games_hightlighted_ntp_games_db(self, connection,):
        sql_query = "select * from games where status = 'publish' and for_mobile = 1 and mobile_ready = 1 and feature_game =1 order by priority desc limit 5;"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_game_events_public_events_all_games_db(self, connection,):
        sql_query = "select a.*, b.game_name, b.thumb_image_url, b.game_url " \
                    "from game_events a inner join games b on a.game_id = b.game_id " \
                    "where a.status = 'active' and a.event_type = 'public' and a.from_time <= now() " \
                    "and a.to_time >= now() and b.status = 'publish' and b.for_mobile = 1 and b.mobile_ready = 1 " \
                    "order by a.from_time desc ;"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_iframe_by_game_id(self, connection, game_id):
        sql_query = f"select iframe from games where game_id = {game_id};"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchone()

    def get_games_by_condition(self, connection, condition):
        sql_query = f"select game_id from games where {condition} ;"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows



