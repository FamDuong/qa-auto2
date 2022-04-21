import urllib
from urllib.request import Request

from bs4 import BeautifulSoup
from lxml import etree
from databases.sql.coccoc_shopping_rungrinh_db import shoppingDB
import requests
import csv


class TestShoppingCrawler_html:
    shopping_db = shoppingDB()

    # get source url
    def get_source_url_html(self, type, domain):
        lst_source_url = []
        source_urls = self.shopping_db.get_product_api_url_html(type, domain)
        for source_url in source_urls:
            lst_source_url.append(source_url[0])
        return lst_source_url

    # def get_list_product_html_data_from_source_html(self, category_url):
    #     # URL = 'https://www.thegioididong.com/laptop?g=laptop-gaming#c=44&p=37699&o=9&pi=2'
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    #     page = requests.get(category_url, headers=headers)
    #     soup = BeautifulSoup(page.content, 'html.parser', from_encoding="iso-8859-1")
    #     dom = etree.HTML(str(soup))
    #     urls = []
    #     list_t = []
    #     u = soup.find('ul', class_='listproduct')
    #     for h in u.findAll('li'):
    #         a = h.find('a')
    #         try:
    #             if 'href' in a.attrs:
    #                     url = a.get('href')
    #                     urls.append(url)
    #         except:
    #             pass
    #     # for url in urls:
    #        # print(url)
    #         #urls.append(url)
    #     print(urls)
    #     return urls
    #         list_t = [url]
    #         return list_t

    # get html data from source
    def get_product_html_data_from_source_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="iso-8859-1")
        dom = etree.HTML(str(soup))
        title = soup.find('h1')
        price = soup.find("p", class_="box-price-present")
        category_name = dom.xpath('//ul[@class="breadcrumb"]/li[last()]/a')[0]
        lstData_array = [title.text]
        return lstData_array

    # get data of 1 product from DB, input product url
    def get_product_data_from_db_html(self, product_url):
        list_product = self.shopping_db.get_products_list_db_all(product_url)
        for product in list_product:
            name = product[6]
            price = product[11]
            category = product[4]
            product_array = [name]
            return product_array

    # compare for category url (multiple products)
    # def test_crawler_product_detail_type_html(self):
    #     lst_source = self.get_source_url_html("html", "thegioididong.com")
    #     #each source is a category link
    #     for source in lst_source:
    #         source = "https://" + source
    #         print (f"source: {source}")
    #         #lst_product_urls = self.get_list_product_html_data_from_source_html(source)
    #         for product_url in lst_product_urls:
    #             product_url_full = "https://thegioididong.com"+product_url
    #             htmlData = self.get_product_html_data_from_source_html(product_url_full)
    #             dbData = self.get_product_data_from_db_html(product_url_full)
    #             print(f"Comparing for product: {product_url} ")
    #             if htmlData == dbData:
    #                 print("OK")
    #             else:
    #                 print("NOK")

    def test_crawler_each_product_detail_type_html(self):
        #get all products type=html, domain=thegioididong.com:
        lst_source = self.get_source_url_html("html", "thegioididong.com")
        #each source is a product link
        count = 0;
        for product_url in lst_source:
            count +=1
            product_url_full = "https://" + product_url
            print(f'product url: {product_url}')
            htmlData = self.get_product_html_data_from_source_html(product_url_full)
            dbData = self.get_product_data_from_db_html(product_url)
            print(htmlData)
            print(dbData)
            if htmlData == dbData:
                print("OK")
            else:
                print("NOK")
            if count == 100:
                return

    # compare DB with HTML data for a URL
    # def test_crawler_product_detail_type_html_1(self):
    #     source_1 = 'https://www.thegioididong.com/dtdd/iphone-13-pro-max'
    #     source_2 = 'thegioididong.com/dtdd/iphone-13-pro-max'
    #     htmlData = self.get_product_html_data_from_source_html(source_1)
    #     dbData = self.get_product_data_from_db_html(source_2)
    #     print(htmlData)
    #     print(dbData)
    #     if htmlData == dbData:
    #         print("OK")
    #     else:
    #         print("NOK")

    # get html data review from source
    def get_product_html_data_review_from_source_html(self, url):
        # url = 'https://vnexpress.net'
        # url = 'https://thegioididong.com/laptop/acer-predator-triton-300-pt315-53-71dj-i7'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="iso-8859-1")
        dom = etree.HTML(str(soup))
        review_title = soup.find("p", class_="rating__title")
        point = soup.find("p", class_="point")
        lstData_array = [point.text]
        # print('title---------', point.text)
        return lstData_array

    # get data review of 1 product from DB, input product url
    def get_product_data_review_from_db_html(self, product_url):
        list_product = self.shopping_db.get_products_list_db_all(product_url)
        for product in list_product:
            rating_average = product[17]
            product_array = [rating_average]
            return product_array


    def test_crawler_each_review_detail_type_html(self):
        #get all products type=html, domain=thegioididong.com:
        lst_source = self.get_source_url_html("html", "thegioididong.com")
        #each source is a product link
        count = 0;
        for product_url in lst_source:
            count +=1
            product_url_full = "https://" + product_url
            print(f'product url: {product_url}')
            htmlData = self.get_product_html_data_review_from_source_html(product_url_full)
            dbData = self.get_product_data_review_from_db_html(product_url)
            print(htmlData)
            print(dbData)
            if htmlData == dbData:
                print("OK")
            else:
                print("NOK")
            if count == 2:
                return

