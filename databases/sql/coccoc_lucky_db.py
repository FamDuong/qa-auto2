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

    def get_list_db(self, db, col_index = 0):
        list_groups = []
        for row in db:
            list_groups.append(row[col_index])
        return list_groups