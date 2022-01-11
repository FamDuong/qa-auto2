from utils_automation.database import MySQL

mysql_drive = MySQL()


class shoppingDB:
    def coccoc_shopping_db_interact(self):
        from config.environment import COCCOC_SHOPPING_DB_SERVER
        from config.environment import COCCOC_SHOPPING_DB_NAME
        from config.environment import COCCOC_SHOPPING_DB_USERNAME
        from config.environment import COCCOC_SHOPPING_DB_PASSWORD
        connection = mysql_drive.connect(host_name=COCCOC_SHOPPING_DB_SERVER,
                                         database_name=COCCOC_SHOPPING_DB_NAME
                                         , user_name=COCCOC_SHOPPING_DB_USERNAME
                                         , password=COCCOC_SHOPPING_DB_PASSWORD)
        return connection

    def coccoc_shopping_db_close(self):
        connection = self.coccoc_shopping_db_interact()
        mysql_drive.close(connection)

    def get_merchant_rules_db(self, domain):
        import logging
        sql_query = f'SELECT name, value FROM shopping.merchant_rules where domain = "{domain}";'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows


