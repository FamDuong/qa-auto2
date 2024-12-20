from utils_automation.database import MySQL
mysql_drive = MySQL()

class NewFeedDB:
    def coccoc_new_feeds_db_interact(self):
        from config.environment import COCCOC_NEW_FEED_DATA_DB_SERVER
        from config.environment import COCCOC_NEW_FEED_DATA_DB_NAME
        from config.environment import COCCOC_NEW_FEED_DATA_DB_USERNAME
        from config.environment import COCCOC_NEW_FEED_DATA_DB_PASSWORD
        connection = mysql_drive.connect(host_name=COCCOC_NEW_FEED_DATA_DB_SERVER,
                                         database_name=COCCOC_NEW_FEED_DATA_DB_NAME
                                         , user_name=COCCOC_NEW_FEED_DATA_DB_USERNAME
                                         , password=COCCOC_NEW_FEED_DATA_DB_PASSWORD)
        return connection

    def coccoc_new_feeds_db_close(self, connection):
        mysql_drive.close(connection)

    def get_newfeeds_db_connection(self, connection, sql_query):
        import logging
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        # print("  DB: ", rows)
        return rows

    def select_newfeeds_db(self, sql_query, data_query = None):
        import logging
        # sql_query = f'select * from urls;'
        connection = self.coccoc_new_feeds_db_interact()
        cursor = connection.cursor()
        if data_query is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, data_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        self.coccoc_new_feeds_db_close(connection)
        # print("  DB: ", rows)
        return rows

    def update_newfeeds_db(self, sql_query, data_query = None):
        import logging
        connection = self.coccoc_new_feeds_db_interact()
        cursor = connection.cursor()
        if data_query is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, data_query)
        connection.commit()
        self.coccoc_new_feeds_db_close(connection)
        print(cursor.rowcount, "Record(s) affected")


    def check_urls_of_hostname(self, connection, hostname):
        import logging
        sql_query = f'select url from urls where host_id in (select id from hosts where hostname = "{hostname}");'
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        return rows

    def check_if_urls_of_hostname_exist(self, connection, hostname, url):
        import logging
        sql_query = f'select url from urls where host_id in (select id from hosts where hostname = "{hostname}") and url = "{url}";'
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        if results:
            return True
        else:
            print(hostname, ": ", url)
            return False

    def check_if_url_in_assessed_data(self, connection, hostname, url):
        import logging
        sql_query = f'select url from urls where id in (select distinct(url_id) from assessed_data) and host_id in (select id from hosts where hostname ="{hostname}") and url = "{url}";'
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        if results:
            return True
        else:
            print(hostname, ": ", url)
            return False

    def get_number_of_urls_host_name_in_assessed_data(self, connection, hostname):
        import logging
        sql_query = f'select url from urls where id in (select distinct(url_id) from assessed_data) and host_id in (select id from hosts where hostname ="{hostname}");'
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results

    def check_is_hostname_in_db(self, connection, hostname):
        import logging
        sql_query = f'select * from hosts where hostname = "{hostname}";'
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        return rows

    def get_list_db(self, db, col_index = 0):
        list_groups = []
        for row in db:
            list_groups.append(row[col_index])
        return list_groups

