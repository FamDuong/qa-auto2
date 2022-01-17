import requests
from bs4 import BeautifulSoup
from lxml import etree

from databases.sql.coccoc_shopping_rungrinh_db import shoppingDB


class TestShoppingCrawlerHTML:
    shopping_db = shoppingDB()

    # get source url
    def get_source_url(self, domain):
        lst_source_url = []
        source_urls = self.shopping_db.get_product_api_url(domain)
        for source_url in source_urls:
            lst_source_url.append(source_url[0])
        return lst_source_url

    # get html data from source
    def get_product_html_data_from_source(self, url):
        url = 'https://' + url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="iso-8859-1")
        dom = etree.HTML(str(soup))
        title = soup.find('h1').text
        category_name = dom.xpath('//ul[@class="breadcrumb"]/li[last()]/a')[0].text
        price = dom.xpath('//p[contains(@class,"box-price-present")]')[0].text.strip("₫ *").replace(".", "")
        discount_rate = 0
        list_price = 0
        if dom.xpath('//p[contains(@class,"price-old")]'):
            element = dom.xpath('//p[contains(@class,"price-old")]')[0]
            list_price = element.text.strip("₫ *").replace(".", "")
            discount_rate = str(round((int(list_price) - int(price)) / int(list_price), 6))
            print('list_price---------', list_price)
            print('discount_rate---------', discount_rate)
        lstData_array = [title, category_name, price, list_price, discount_rate]
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

    def test_crawler_product_detail_type_html(self):
        lst_source = self.get_source_url("thegioididong.com")
        for source in lst_source:
            htmlData = self.get_product_html_data_from_source(source)
            dbData = self.get_product_data_from_db(source)
            print("++++", htmlData)
            print("++++", dbData)
            if htmlData == dbData:
                print("OK")
            else:
                print("NOK")