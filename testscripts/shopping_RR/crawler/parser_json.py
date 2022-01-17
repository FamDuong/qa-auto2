import json
import urllib
from urllib.request import Request

from databases.sql.coccoc_shopping_rungrinh_db import shoppingDB
import requests
import csv


class TestShoppingCrawler:
    shopping_db = shoppingDB()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # get source url
    def get_source_url(self, domain):
        lst_source_url = []
        source_urls = self.shopping_db.get_product_api_url(domain)
        for source_url in source_urls:
            lst_source_url.append(source_url[0])
        return lst_source_url

    # get json data from source
    def get_product_json_data_from_source_shopee(self, url):
        r = requests.get(url, headers=self.headers)
        data_json = r.json()
        data = data_json['data']
        name = data['name']
        price = data['price'] / 100000
        list_price = data['price_before_discount']
        discount = data['discount']
        categories = data['categories']
        for category in categories:
            category_name = category['display_name']
        lstData_array = [name, category_name, price, list_price, discount]
        return lstData_array

    def get_product_json_data_from_source_tiki(self, url):
        r = requests.get(url, headers=self.headers)
        data_json = r.json()
        name = data_json['name']
        price = data_json['price']
        list_price = data_json['list_price']
        discount = data_json['discount_rate']
        categories = data_json['breadcrumbs']
        for category in categories:
            category_name = category['name']
        lstData_array = [name, category_name, price, list_price, discount]
        return lstData_array

    def get_product_json_data_from_source_sendo(self, url):
        r = requests.get(url, headers=self.headers)
        data_json = r.json()
        data = data_json['data']
        name = data['name']
        price = data['price']
        list_price = data['final_price_max']
        discount = data['discount']
        categories = data['category_info']
        for category in categories:
            category_name = category['title']
        lstData_array = [name, category_name, price, list_price, discount]
        return lstData_array

    # get product from db
    def get_product_data_from_db(self, product_api_url):
        list_products = self.shopping_db.get_products_list_db(product_api_url)
        lstProduct_array = []
        for product in list_products:
            name = product[0]
            category_name = product[1]
            price = product[2]
            list_price = product[3]
            discount_rate = product[4]
            lstProduct_array = [name, category_name, price, list_price, discount_rate]
        return lstProduct_array

    # get json list product review from source
    def get_list_review_json_from_source(self, domain):
        list_url_api_of_products_review = self.shopping_db.get_product_review_db(domain)
        lstData_array = []
        for url in list_url_api_of_products_review:
            url_api = url[1]
            # print("===url: ", url_api)
            r = requests.get(url_api)
            data_json = r.json()
            if domain == 'shopee.vn':
                data = data_json['data']['ratings']
                for item in data:
                    product_review_id = item['cmtid']
                    user_name = item['author_username']
                    rating = item['rating_star']
                    comment = item['comment']
                    lstData_array.append([product_review_id, user_name, rating, comment])
            elif domain == 'tiki.vn':
                data = data_json['data']
                for item in data:
                    product_review_id = item['product_id']
                    user_name = item['created_by']['full_name']
                    rating = item['rating']
                    comment = item['content']
                    lstData_array.append([product_review_id, user_name, rating, comment])
        return lstData_array

    # get list product review from db
    def get_list_review_data_from_db(self, domain):
        list_id_of_products_review = self.shopping_db.get_product_review_db(domain)
        lst_review_array = []
        for id in list_id_of_products_review:
            product_id = id[0]
            lst_review = self.shopping_db.get_review_db(product_id)
            for review in lst_review:
                product_review_id = review[0]
                user_name = review[1]
                rating = review[2]
                comment = review[3]
                lst_review_array.append([product_review_id, user_name, rating, comment])
        return lst_review_array

    def test_crawler_product_detail_type_json_shopee(self):
        lst_source = self.get_source_url("shopee.vn")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source_shopee(source)
            dbData = self.get_product_data_from_db(source)
            print("fromsource++++", jsonData)
            print("fromDB++++", dbData)
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("OK")
            else:
                print("NOK")

    def test_crawler_product_detail_type_json_sendo(self):
        lst_source = self.get_source_url("sendo.vn")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source_sendo(source)
            dbData = self.get_product_data_from_db(source)
            print("fromsource++++", jsonData)
            print("fromDB++++", dbData)
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("OK")
            else:
                print("NOK")

    def test_crawler_product_detail_type_json_tiki(self):
        lst_source = self.get_source_url("tiki.vn")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source_tiki(source)
            dbData = self.get_product_data_from_db(source)
            print("fromsource++++", jsonData)
            print("fromDB++++", dbData)
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("OK")
            else:
                print("NOK")

    def test_crawler_product_review_type_json_tiki(self):
        jsonData = self.get_list_review_json_from_source("tiki.vn")
        dbData = self.get_list_review_data_from_db()
        print("fromsource++++", jsonData)
        print("fromDB++++", dbData)
        res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
        if not res:
            print("OK")
        else:
            print("NOK")

    def test_crawler_product_review_type_json_shopee(self):
        jsonData = self.get_list_review_json_from_source("shopee.vn")
        dbData = self.get_list_review_data_from_db()
        print("fromsource++++", jsonData)
        print("fromDB++++", dbData)
        res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
        if not res:
            print("OK")
        else:
            print("NOK")
