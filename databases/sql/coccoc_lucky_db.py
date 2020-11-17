from utils_automation.database import MySQL
mysql_drive = MySQL()

class LuckyDB:
    def coccoc_lucky_db_interact(self):
        from config.environment import COCCOC_LUCKY_DB_SERVER
        from config.environment import COCCOC_LUCKY_DB_NAME
        from config.environment import COCCOC_LUCKY_DB_USERNAME
        from config.environment import COCCOC_LUCKY_DB_PASSWORD
        connection = mysql_drive.connect(host_name=COCCOC_LUCKY_DB_SERVER, database_name=COCCOC_LUCKY_DB_NAME
                                         , user_name=COCCOC_LUCKY_DB_USERNAME
                                         , password=COCCOC_LUCKY_DB_PASSWORD)
        return connection

    def coccoc_lucky_db_close(self, connection):
        mysql_drive.close(connection)

    def get_lucky_db_connection(self, connection, sql_query):
        import logging
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        # print("  DB: ", rows)
        return rows

    def get_lucky_db(self, sql_query):
        import logging
        connection = self.coccoc_lucky_db_interact()
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        self.coccoc_lucky_db_close(connection)
        # print("  DB: ", rows)
        return rows

    def update_lucky_db(self, sql_query, data_query = None):
        import logging
        connection = self.coccoc_lucky_db_interact()
        cursor = connection.cursor()
        if data_query is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, data_query)
        connection.commit()
        self.coccoc_lucky_db_close(connection)
        print(cursor.rowcount, "Record(s) affected")

    def get_list_db(self, db, col_index = 0):
        list_groups = []
        for row in db:
            list_groups.append(str(row[col_index]))
        return list_groups

    def select_lucky_db(self, sql_query, data_query = None):
        import logging
        # sql_query = f'select * from urls;'
        connection = self.coccoc_lucky_db_interact()
        cursor = connection.cursor()
        if data_query is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, data_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        self.coccoc_lucky_db_close(connection)
        return rows

    def get_list_lucky_db(self, sql_query, index = 0, data_query = None):
        db_lucky = self.select_lucky_db(sql_query, data_query)
        list_lucky = self.get_list_db(db_lucky, index)
        return list_lucky;