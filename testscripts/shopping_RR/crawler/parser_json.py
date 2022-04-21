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
        list_price = data['price_before_discount'] / 100000
        if list_price > 0:
            discount = round((int(list_price) - int(price)) / int(list_price), 6)
        else:
            discount = None
        categories = data['categories']
        for category in categories:
            category_name = category['display_name']
        description = data['description']
        sold_count = data['sold']
        sku = ""
        rating_average = data['item_rating']['rating_star']
        review_count = data['item_rating']['rating_count'][0]
        brand_name = data['brand']
        lstData_array = [name, category_name, price, list_price, discount, sold_count, sku, rating_average,
                         review_count, brand_name, description]
        return lstData_array

    def get_product_json_data_from_source_tiki(self, url):
        r = requests.get(url, headers=self.headers)
        data_json = r.json()
        name = data_json['name']
        price = data_json['price']
        list_price = data_json['list_price']
        if list_price > 0:
            discount = round((int(list_price) - int(price)) / int(list_price), 6)
        else:
            discount = None
        categories = data_json['breadcrumbs']
        for category in categories:
            category_name = category['name']
        description = data_json['description']
        if "all_time_quantity_sold" in data_json:
            sold_count = data_json['all_time_quantity_sold']
        else:
            sold_count = 0
        sku = data_json['sku']
        rating_average = data_json['rating_average']
        review_count = data_json['review_count']
        brand_name = data_json['brand']['name']
        lstData_array = [name, category_name, price, list_price, discount, sold_count, sku, rating_average,
                         review_count, brand_name, description]
        return lstData_array

    def get_product_json_data_from_source_sendo(self, url):
        r = requests.get(url, headers=self.headers)
        data_json = r.json()
        data = data_json['data']
        name = data['name']
        price = data['final_price']
        list_price = data['price']
        if list_price > 0:
            discount = round((int(list_price) - int(price)) / int(list_price), 6)
        else:
            discount = None
        categories = data['category_info']
        for category in categories:
            category_name = category['title']
        description = data['description_info']['description']
        sold_count = data['order_count']
        sku = data['sku_user']
        rating_average = data['rating_info']['percent_star']
        review_count = data['rating_info']['total_rated']
        brand_info = data['brand_info']
        if "name" in brand_info:
            brand_name = data['brand_info']['name']
        else:
            brand_name = ''
        lstData_array = [name, category_name, price, list_price, discount, sold_count, sku, rating_average, review_count, brand_name, description]
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
            sold_count = product[5]
            sku = product[6]
            rating_average = product[7]
            review_count = product[8]
            brand_name = product[9]
            description = product[10]
            lstProduct_array = [name, category_name, price, list_price, discount_rate, sold_count, sku, rating_average, review_count, brand_name, description]
        return lstProduct_array

    # get source url
    def get_review_source_url(self, domain):
        lst_source_url = []
        source_urls = self.shopping_db.get_product_review_db(domain)
        for source_url in source_urls:
            lst_source_url.append([source_url[0], source_url[1]])
        return lst_source_url

    # get json list product review from source
    def get_list_review_json_from_source(self, domain, url):
        lstData_array = []
        r = requests.get(url, headers=self.headers)
        data_json = r.json()
        if domain == 'shopee.vn':
            data = data_json['data']['ratings']
            for item in data:
                product_review_id = item['cmtid']
                user_name = item['author_username']
                if user_name is not None:
                    user_name = user_name.strip()
                elif user_name is None:
                    user_name = ""
                rating = item['rating_star']
                comment = item['comment']
                if comment is not None:
                    comment = comment.strip()
                elif comment is None:
                    comment = ""
                lstData_array.append([product_review_id, user_name, rating, comment])
        elif domain == 'tiki.vn':
            data = data_json['data']
            for item in data:
                product_review_id = item['id']
                if 'full_name' in item:
                    user_name = item['created_by']['full_name']
                    if user_name is not None:
                        user_name = user_name.strip()
                    elif user_name is None:
                        user_name = ""
                else:
                    user_name = ""
                rating = item['rating']
                comment = item['content']
                if comment is not None:
                    comment = comment.strip()
                elif comment is None:
                    comment = ""
                lstData_array.append([product_review_id, user_name, rating, comment])
        return lstData_array

    # get list product review from db
    def get_list_review_data_from_db(self, id):
        lst_review_array = []
        lst_review = self.shopping_db.get_review_db(id)
        for review in lst_review:
            product_review_id = review[0]
            user_name = review[1]
            if user_name is not None:
                user_name = user_name.strip()
            rating = review[2]
            comment = review[3]
            if comment is not None:
                comment = comment.strip()
            lst_review_array.append([product_review_id, user_name, rating, comment])
        return lst_review_array

    def test_crawler_product_detail_type_json_shopee(self):
        lst_source = self.get_source_url("shopee.vn")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source_shopee(source)
            dbData = self.get_product_data_from_db(source)
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("")
            else:
                print("name, category_name, price, list_price, discount_rate, sold_count, sku, rating_average, review_count, brand_name, description")
                print("fromsource++", jsonData)
                print("fromDB++++++", dbData)
                print("NOK")

    def test_crawler_product_detail_type_json_sendo(self):
        lst_source = self.get_source_url("sendo.vn")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source_sendo(source)
            dbData = self.get_product_data_from_db(source)
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("")
            else:
                print("name, category_name, price, list_price, discount_rate, sold_count, sku, rating_average, review_count, brand_name, description")
                print("fromsource++", jsonData)
                print("fromDB++++++", dbData)
                print("NOK")

    def test_crawler_product_detail_type_json_tiki(self):
        lst_source = self.get_source_url("tiki.vn")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source_tiki(source)
            dbData = self.get_product_data_from_db(source)
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("")
            else:
                print("name, category_name, price, list_price, discount_rate, sold_count, sku, rating_average, review_count, brand_name, description")
                print("fromsource++", jsonData)
                print("fromDB++++++", dbData)
                print("NOK")

    def test_crawler_product_review_type_json_tiki(self):
        lst_source = self.get_review_source_url("tiki.vn")
        for source in lst_source:
            jsonData = self.get_list_review_json_from_source("tiki.vn", source[1])
            dbData = self.get_list_review_data_from_db(source[0])
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("")
            else:
                print("fromsource++", jsonData)
                print("fromDB++++++", dbData)
                for i in jsonData:
                    print("", i[0])
                    print("", i[1])
                    print("", i[2])
                    print("", i[3])
                print("-------")
                for j in dbData:
                    print("", j[0])
                    print("", j[1])
                    print("", j[2])
                    print("", j[3])
                print("NOK")

    def test_crawler_product_review_type_json_shopee(self):
        lst_source = self.get_review_source_url("shopee.vn")
        for source in lst_source:
            jsonData = self.get_list_review_json_from_source("shopee.vn", source[1])
            dbData = self.get_list_review_data_from_db(source[0])
            res = [x for x in jsonData + dbData if x not in jsonData or x not in dbData]
            if not res:
                print("")
            else:
                print("fromsource++", jsonData)
                print("fromDB++++++", dbData)
                for i in jsonData:
                    print("", i[0])
                    print("", i[1])
                    print("", i[2])
                    print("", i[3])
                print("-------")
                for j in dbData:
                    print("", j[0])
                    print("", j[1])
                    print("", j[2])
                    print("", j[3])
                print("NOK")

    def test_crawler_list_product_from_source(self):
        headers_test = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Referer': 'sendo.vn'}
        url = 'https://searchlist-api.sendo.vn/web/categories/1954/products?listing_algo=algo13&page=1&platform=web&size=60&sortType=listing_v2_desc'
        r = requests.get(url, headers=headers_test)
        data_json = r.json()
        # data = data_json['items']
        # for item in data:
        #     name = item['item_basic']['name']
        #     print("", name)
        data = data_json['data']
        for item in data:
            name = item['name']
            print("", name)
