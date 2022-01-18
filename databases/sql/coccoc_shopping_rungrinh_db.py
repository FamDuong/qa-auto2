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

    def get_product_api_url(self, domain):
        import logging
        sql_query = f'SELECT CASE WHEN products.product_api_url IS NULL THEN products.url ELSE products.product_api_url END AS product_url ' \
                    f'FROM shopping.products ' \
                    f'where status = "crawled" and domain = "{domain}";'
        # sql_query = f'SELECT url FROM shopping.products p WHERE p.domain in (SELECT distinct domain FROM shopping.merchant_datafeeds WHERE merchant_datafeeds.type = "{type}") and p.status = "crawled";'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows

    def get_products_list_db(self, product_api_url):
        import logging
        # sql_query = f'SELECT merchant_shop_id, merchant_product_id, name FROM shopping.products where product_api_url = "{product_api_url}" OR url = "{product_api_url}";'
        sql_query = f'SELECT name, category_name, price, list_price, discount_rate FROM shopping.products where product_api_url = "{product_api_url}" OR url = "{product_api_url}";'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows

    def get_product_review_db(self, domain):
        import logging
        sql_query = f'SELECT product_id, CASE WHEN products.product_review_api_url IS NULL THEN products.url ELSE products.product_review_api_url END AS product_url ' \
                    f'from shopping.products where review_crawl_status = "crawled" and domain = "{domain}"'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows

    def get_review_db(self, product_id):
        import logging
        sql_query = f'SELECT product_review_id, user_name, rating, comment  FROM shopping.product_reviews where product_id = "{product_id}"; '
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        return rows

    def get_product_api_url_html(self, type, domain):
        import logging
        sql_query = f'select url from products p where p.domain in (select distinct domain from merchant_datafeeds ' \
                    f'where  merchant_datafeeds.type = "{type}") and p.status = "crawled" and p.domain= "{domain}";'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        #print(rows)
        connection.commit()
        return rows

    def get_products_list_db_all(self, product_api_url):
        import logging
        sql_query = f'SELECT * FROM shopping.products where product_api_url LIKE \'%{product_api_url}%\' OR url LIKE \'%{product_api_url}%\';'
        connection = self.coccoc_shopping_db_interact()
        cursor = connection.cursor()
        # print(sql_query)
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        logging.debug(f"Duplicate rows are : {rows}")
        connection.commit()
        # print(rows)
        return rows




