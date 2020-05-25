class CocCocGameCrawler:

    def get_all_games_by_category(self, connection, category_id=0):
        sql_query = f'select distinct (game_id) from game_category where category_id ={category_id};'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows



