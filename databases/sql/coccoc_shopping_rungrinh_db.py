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

    def get_products_list_db(self, product_api_url):
        import logging
        sql_query = f'SELECT merchant_shop_id, merchant_product_id, name FROM shopping.products where product_api_url = "{product_api_url}";'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows

    def get_product_review_db(self):
        import logging
        sql_query = f'select product_id, product_review_api_url from shopping.products where review_crawl_status = "crawled" and product_review_api_url is not null;'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows

    def get_review_db(self, product_id):
        import logging
        sql_query = f'SELECT product_review_id, user_name, rating, comment  FROM shopping.product_reviews where product_id = "{product_id}";'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows


