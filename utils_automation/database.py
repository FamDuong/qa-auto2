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





