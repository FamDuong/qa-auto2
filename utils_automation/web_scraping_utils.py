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
        return published_time











