import json

from databases.sql.coccoc_shopping_rungrinh_db import shoppingDB
import requests

class TestShoppingCrawler:
    shopping_db = shoppingDB()

    def test_crawler_type_json(self):
        # get rule from db
        # domain = 'shopee.vn'
        # list_merchant_rules = self.shopping_db.get_merchant_rules_db(domain)
        # for merchant_rule in list_merchant_rules:
        #     print("===0", merchant_rule[0])
        #     print("===1", merchant_rule[1])

        # get json data from source
        url = 'https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id=11036102&newest=0&order=desc'
        r = requests.get(url)
        data = r.json()
        items = data['items']
        for item in items:
            print("==========", item['item_basic']['shopid'])
            print("==========", item['item_basic']['itemid'])
            print("==========", item['item_basic']['name'])
            print("==========", item['item_basic']['image'])
            print("==========", item['item_basic']['image'])
            print("==========", item['item_basic']['price'])
            print("==========", item['item_basic']['price_before_discount'])
            print("==========", item['item_basic']['stock'])
            print("==========", item['item_basic']['sold'])

