from bs4 import BeautifulSoup, SoupStrainer


class WebScrapingTime:

    def get_published_time_of_web_page(self, response_text):
        published_time = None
        soup_instance = BeautifulSoup(response_text, features='html.parser', parse_only=SoupStrainer("head"))
        meta_tags = soup_instance.find_all(name="meta")
        for item in meta_tags:
            property_value = item.get('property')
            if property_value == 'article:published_time':
                published_time = item.get('content')
        if published_time is None:
            soup_instance = BeautifulSoup(response_text, features='html.parser', parse_only=SoupStrainer('script',
                                                                                                         attrs={
                                                                                                             "type": "application/ld+json"}))
            list_json = soup_instance.findAll('script')
            for each_json in list_json:
                if 'datePublished' in each_json.text.strip():
                    import json
                    from json import JSONDecodeError
                    try:
                        json_parse = json.loads(each_json.text.strip(), strict=False)
                        published_time = json_parse['datePublished']
                    except JSONDecodeError as e:
                        print(e)
        return published_time











