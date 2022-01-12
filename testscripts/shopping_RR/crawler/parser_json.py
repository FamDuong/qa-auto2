import json

from databases.sql.coccoc_shopping_rungrinh_db import shoppingDB
import requests
import csv

class TestShoppingCrawler:
    shopping_db = shoppingDB()

    # get json data from source
    def get_product_json_data_from_source(self, url):
        r = requests.get(url)
        data_json = r.json()
        data = data_json['data']
        shopid = data['shopid']
        itemid = data['itemid']
        name = data['name']
        lstData_array = [shopid, itemid, name]
        return lstData_array

    # get product from db
    def get_product_data_from_db(self, product_api_url):
        list_products = self.shopping_db.get_products_list_db(product_api_url)
        lstProduct_array = []
        for product in list_products:
            # print("=========merchant_shop_id", product[0])
            merchant_shop_id = product[0]
            merchant_product_id = product[1]
            name = product[2]
            lstProduct_array = [merchant_shop_id, merchant_product_id, name]
        return lstProduct_array

    def get_list_review_json_from_source(self):
        list_url_api_of_products_review = self.shopping_db.get_product_review_db()
        for url in list_url_api_of_products_review:
            url_api = url[1]
            r = requests.get(url_api)
            data_json = r.json()
            data = data_json['data']['ratings']
            product_review_id = data['cmtid']
            user_name = data['author_username']

    def get_list_review_data_from_db(self):
        list_id_of_products_review = self.shopping_db.get_product_review_db()
        lst_review_array = []
        for id in list_id_of_products_review:
            product_id = id[0]
            lst_review = self.shopping_db.get_review_db(product_id)
            for review in lst_review:
                product_id = review[0]
                product_review_id = review[1]
                user_name = review[2]
                rating = review[3]
                comment = review[4]
                review_time = review[5]
                lst_review_array = [product_id, product_review_id, user_name, rating, comment, review_time]
                print("========", lst_review_array)
        return lst_review_array

    def test_crawler_product_detail_type_json(self):
        # read csv file
        with open('data/product_api_url_data_csv.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                print(f'\t{row["url"]}')
                url = row["url"]
                jsonData = self.get_product_json_data_from_source(url)
                dbData = self.get_product_data_from_db(url)
                line_count += 1
                print("++++", jsonData)
                print("++++", dbData)
                if jsonData == dbData:
                    print("OK")
                else:
                    print("NOK")

    def test_crawler_product_review_type_json(self):

