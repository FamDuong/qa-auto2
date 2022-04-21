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
        # url = 'https://' + url
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
        if dom.xpath('//p[contains(@class,"box-price-old")]'):
            element = dom.xpath('//p[contains(@class,"box-price-old")]')[0]
            list_price = element.text.strip("₫ *").replace(".", "")
            discount_rate = round((int(list_price) - int(price)) / int(list_price), 6)
        sold_count = ""
        sku = ""
        description = ""
        rating_average = 0
        if dom.xpath('//p[@class="point"]'):
            rating_average = dom.xpath('//p[@class="point"]')[0].text
        review_count = 0
        if dom.xpath('//*[@class="rating-total"]'):
            review_count = dom.xpath('//*[@class="rating-total"]')[0].text.strip(" Ä\x91Ã¡nh giÃ¡")
        brand_name = ""
        if dom.xpath('//p[@class="manu-info-popup__content__title"]'):
            brand_name = dom.xpath('//p[@class="manu-info-popup__content__title"]/img/@alt')[0]
        lstData_array = [title, category_name, price, list_price, discount_rate, sold_count, sku, rating_average,
                         review_count, brand_name, description]
        return lstData_array

    # get product from db
    def get_product_data_from_db(self, product_api_url):
        list_products = self.shopping_db.get_products_list_db(product_api_url)
        lstProduct_array = []
        for product in list_products:
            name = product[0]
            category_name = product[1]
            price = int(product[2])
            list_price = int(product[3])
            discount_rate = int(product[4])
            sold_count = product[5]
            sku = product[6]
            rating_average = int(product[7])
            review_count = int(product[8])
            brand_name = product[9]
            description = product[10]
            lstProduct_array = [name, category_name, price, list_price, discount_rate, sold_count, sku, rating_average,
                                review_count, brand_name, description]
        return lstProduct_array

    def test_crawler_product_detail_type_html_thegioididong(self):
        lst_source = self.get_source_url("thegioididong.com")
        for source in lst_source:
            htmlData = self.get_product_html_data_from_source(source)
            dbData = self.get_product_data_from_db(source)
            res = [x for x in htmlData + dbData if x not in htmlData or x not in dbData]
            if not res:
                print("")
            else:
                print("name, category_name, price, list_price, discount_rate, sold_count, sku, rating_average, review_count, brand_name, description")
                print("fromsource++", htmlData)
                print("fromDB++++++", dbData)
                print("NOK")
