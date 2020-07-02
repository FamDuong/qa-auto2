class LuckyDB:

    def get_lucky_db(self, connection, sql_query):
        import logging
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        # print("  DB: ", rows)
        return rows

    def get_list_db(self, db, col_index = 0):
        list_groups = []
        for row in db:
            list_groups.append(row[col_index])
        return list_groups