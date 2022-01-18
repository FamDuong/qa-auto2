import json
import urllib
from urllib.request import Request

from bs4 import BeautifulSoup
from lxml import etree

from databases.sql.coccoc_shopping_rungrinh_db import shoppingDB
import requests
import csv

class TestShoppingCrawler:
    shopping_db = shoppingDB()

    # get source url
    def get_source_url(self, type):
        lst_source_url = []
        source_urls = self.shopping_db.get_product_api_url(type)
        for source_url in source_urls:
            lst_source_url.append(source_url[0])
        return lst_source_url

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

    # get html data from source
    def get_product_html_data_from_source(self):
        # url = 'https://vnexpress.net'
        url = 'https://thegioididong.com/laptop/acer-predator-triton-300-pt315-53-71dj-i7'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="iso-8859-1")
        dom = etree.HTML(str(soup))
        title = soup.find('h1')
        price = soup.find("p", class_= "box-price-present")
        category_name = dom.xpath('//ul[@class="breadcrumb"]/li[last()]/a')[0]
        print('title---------', title.text)
        print('price---------', price.text)
        print('category_name---------', category_name.text)

    # get product from db
    def get_product_data_from_db(self, product_api_url):
        list_products = self.shopping_db.get_products_list_db(product_api_url)
        lstProduct_array = []
        for product in list_products:
            merchant_shop_id = product[0]
            merchant_product_id = product[1]
            name = product[2]
            lstProduct_array = [merchant_shop_id, merchant_product_id, name]
        return lstProduct_array

    def get_product_data_from_db_html(self, product_url):
        list_products = self.shopping_db.get_products_list_db_all(product_url)
        lstProduct_array = []
        for product in list_products:
            merchant_shop_id = product[1]
            merchant_product_id = product[0]
            name = product[6]
            price = product[11]
            category = product[4]
            lstProduct_array = [name, price, category]
        return lstProduct_array


    # get json list product review from source
    def get_list_review_json_from_source(self):
        list_url_api_of_products_review = self.shopping_db.get_product_review_db()
        lstData_array = []
        for url in list_url_api_of_products_review:
            url_api = url[1]
            # print("===url: ", url_api)
            r = requests.get(url_api)
            data_json = r.json()
            data = data_json['data']['ratings']
            for item in data:
                product_review_id = item['cmtid']
                user_name = item['author_username']
                rating = item['rating_star']
                comment = item['comment']
                lstData_array.append([product_review_id, user_name, rating, comment])
        return lstData_array

    # get list product review from db
    def get_list_review_data_from_db(self):
        list_id_of_products_review = self.shopping_db.get_product_review_db()
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

    def test(self):
        self.get_product_html_data_from_source()

    def test_crawler_product_detail_type_json(self):
        lst_source = self.get_source_url("json")
        for source in lst_source:
            jsonData = self.get_product_json_data_from_source(source)
            dbData = self.get_product_data_from_db(source)
            print("++++", jsonData)
            print("++++", dbData)
            if jsonData == dbData:
                print("OK")
            else:
                print("NOK")

    def test_crawler_product_review_type_json(self):
        # assert len(self.get_list_review_json_from_source()) == len(self.get_list_review_data_from_db())
        if len(self.get_list_review_json_from_source()) == len(self.get_list_review_data_from_db()):
            print("OK")
        else:
            print("NOK")

