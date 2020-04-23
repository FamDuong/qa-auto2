import mysql.connector
from mysql.connector import Error


class MySQL:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(MySQL, cls).__new__(cls)

        return cls.instance

    def connect(self, host_name, database_name, user_name, password):
        try:
            connection = mysql.connector.connect(host=host_name,
                                                 database=database_name,
                                                 user=user_name,
                                                 password=password,)

            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Your connected to database: ", record)
                return connection

        except Error as e:
            print("Error while connecting to MySQL", e)

    def close(self, connection):
        if connection.is_connected():
            connection.cursor().close()
            connection.close()
            print("MySQL connection is closed")


class CocCocMusicCrawler:

    def check_if_duplicate_value_in_column(self, connection, column_check, table_name):
        import logging
        sql_query = f'select count({column_check}) from {table_name} group by {column_check}' \
                    f' having count({column_check}) >1;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        return rows

    def check_if_value_null_or_empty_in_column(self, connection, column_check, table_name):
        sql_query = f'select count(*) from {table_name} where {column_check} is null or {column_check} = "";'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return cursor.fetchone()

    def get_one_result_from_table(self, connection, table_name):
        import logging
        sql_query = f'select * from {table_name} limit 1;'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        row = dict(zip(cursor.column_names, cursor.fetchone()))
        logging.debug(f"One result from table {table_name} is : {row}")
        return row

    def get_one_result_from_table_with_condition(self, connection, column_check, column_value, table_name):
        sql_query = f'select * from {table_name} where {column_check} = "{column_value}"'
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_query)
        row = dict(zip(cursor.column_names, cursor.fetchone()))
        return row

    def get_all_distinct_value_from_column_in_table(self, connection, column_check, table_name):
        sql_query = f'select distinct {column_check} from {table_name};'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_all_rows_from_table_where_column_has_value(self, connection, column_check, column_value, table_name):
        sql_query = f'select * from {table_name} where {column_check} = "{column_value}";'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows

    def get_all_rows_from_table(self, connection, table_name):
        sql_query = f'select * from {table_name};'
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows




