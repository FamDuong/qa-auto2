import time
class NewFeedsDB:

    def get_newfeeds_db(self, connection, sql_query):
        import logging
        # sql_query = f'select * from urls;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        # print("  DB: ", rows)
        return rows

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

