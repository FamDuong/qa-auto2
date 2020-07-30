import lxml.html
import urllib.request
import urllib
import lxml.html
from urllib.parse import urlsplit
import re
import requests
import feedparser
from PIL import Image
from io import BytesIO
import os
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from urllib import request
from bs4 import BeautifulSoup

class NewFeedCommon:
    newfeed_db = NewFeedDB()
    # Check url is live
    def check_link_is_alive(self, url):
        live = True
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print(f"URL {url} not reachable")
            live = False
        return live

    # Check all urls in files are live
    def get_all_links_in_file_are_not_alive(self, filename):
        urls_not_live = set()

        with open(filename, "r+", encoding="utf-8") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                live = self.check_link_is_alive(i)
                if not live:
                    urls_not_live.add(i)
            # f.truncate()
        return urls_not_live

    # Get all sub links in an url which data-linktype="newsdetail"
    def get_sub_links_are_article(self, url):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        # user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/87.0.148 Chrome/81.0.4044.148 Safari/537.36'
        headers = {'User-Agent': user_agent, }
        sublinks = []
        request = urllib.request.Request(url, None, headers)
        connection = urllib.request.urlopen(request)
        dom = lxml.html.fromstring(connection.read())
        # for link in dom.xpath('//a/@href'):
        # for element in dom.xpath('//a[@href and @data-linktype]'):
        # title = element.text
        # link = element.get('href')
        for link in dom.xpath('//a/@href'):
            #if (any(chr.isdigit() for chr in link)):
            if (bool(re.search('[0-9]{5}', link))):
                if not link.startswith('http'):
                    sublinks.append(url + link)
                else:
                    sublinks.append(link)
        return sublinks

    # Extract title
    def get_attribute_from_url(self, url, attribute):
        description_selectors = [
            {"name": "description"},
             {"name": "og:description"},
            {"property": "description"}
        ]
        # html = request.urlopen(url).read()
        # html[:60]
        # soup = BeautifulSoup(html, 'html.parser')
        title = ''
        try:
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers = {'User-Agent': user_agent, }
            request = urllib.request.Request(url, None, headers)
            connection = urllib.request.urlopen(request)
            soup = BeautifulSoup(connection.read(), 'html.parser')
            # title = soup.find('title').content
            title = soup.title.string
            # metas = soup.find_all('meta')
            # title = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == attribute ]
            # return content
            #for selector in description_selectors:
            #    description_tag = soup.find(attrs=selector)
            #    if description_tag and description_tag.get('content'):
            #        title = description_tag['content']
            #        break
        except:
            title = ''
        finally:
            return title

    # Get all sub links in a rss feed
    def get_sub_links_in_rss_feed(self, url):
        sublinks = []
        news_feed = feedparser.parse(url)
        for i in range(len(news_feed.entries)):
            try:
                entry = news_feed.entries[i]
                sublinks.append(entry.link)
            except:
                continue
        return sublinks


    # Remove links not same domain
    def remove_not_sub_links_in_list(self, domain, sublinks):
        return [ x for x in sublinks if domain in x ]


    # Remove invalid links
    def remove_invalid_links_in_list(self, sublinks, list_invalid_strings):
        for i in list_invalid_strings:
            sublinks = [ x for x in sublinks if i not in x ]
        return sublinks

    # Replace string in list
    def replace_string_in_list(self, list, original, replacement):
        replace_list = []
        for i in list:
            replace_list = [ sub.replace(original, replacement) for sub in list ]
        return replace_list


    # Print list
    def print_list(self, my_list):
        for i in my_list:
            print(i, sep = "\n")

    # Print line by line in file
    def print_file(self, filename):
        file = open(filename)
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()

    # Remove duplicated items in list
    def remove_duplicated_items_in_list(self, my_list):
        return list(dict.fromkeys(my_list))

    # Write list to new text file
    def write_to_file(self, filename, input_lists):
        file = open(filename, 'w+', encoding="utf-8")
        for i in input_lists:
            file.write("%s\n" % (i))
        file.close()

    # Append list to a file
    def append_to_file(self, filename, input_lists):
        if os.path.exists(filename):
            file = open(filename, 'a', encoding="utf-8")
        else:
            file = open(filename, 'w+', encoding="utf-8")
        for i in input_lists:
            file.write("%s\n" % (i))
        file.close()

    # Remove a file
    def remove_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print('File does not exists')

    # Remove duplicated lines in text files
    def remove_duplicated_items_in_file(self, filename):
        lines_seen = set()  # holds lines already seen

        with open(filename, "r+", encoding="utf-8") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i not in lines_seen:
                    f.write(i)
                    lines_seen.add(i)
            f.truncate()

    # Remove duplicated lines in text files
    def get_duplicated_items_in_file(self, filename):
        lines_seen = set()  # holds lines already seen
        lines_duplicated = set()

        with open(filename, "r+", encoding="utf-8") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i in lines_seen:
                    lines_duplicated.add(i)
                else:
                    lines_seen.add(i)
            # f.truncate()
        return lines_duplicated

    # Remove duplicated lines in text files
    def get_items_in_file_not_contains(self, filename, string):
        lines_not_contains = set()

        with open(filename, "r+", encoding="utf-8") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if string not in i:
                    lines_not_contains.add(i)
            # f.truncate()
        return lines_not_contains

    # Get different value between files
    def get_different_elements_between_files(self, filename_1, filename_2, diff_filename):
        with open(filename_1, 'r', encoding="utf-8") as file1:
            with open(filename_2, 'r', encoding="utf-8") as file2:
                difference = set(file1).difference(file2)

        difference.discard('\n')

        with open(diff_filename, 'w', encoding="utf-8") as file_out:
            for line in difference:
                file_out.write(line)
                # print(line)

    # Get different value between files
    def get_common_value_between_files(self, filename_1, filename_2, common_filename):
        with open(filename_1, 'r', encoding="utf-8") as file1:
            with open(filename_2, 'r', encoding="utf-8") as file2:
                same = set(file1).intersection(file2)

        same.discard('\n')

        with open(common_filename, 'w', encoding="utf-8") as file_out:
            for line in same:
                file_out.write(line)
                # print(line)

    # Get number of lines in file
    def get_number_of_lines(self, filename):
        return sum(1 for line in open(filename, "r",encoding='utf-8'))

    def get_domain_from_url(self, url):
        base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
        print(base_url)
        return base_url

    # Check if all items in list contains a string
    # Return items which do not contains string
    def get_items_in_list_not_contains(self, list, string):
        return [item for item in list if string not in item]


    # Get different elements in 2 lists
    def get_different_elements_between_lists(self, list_1, list_2):
        return [item for item in list_1 if str(item) not in list_2]


    # Check list of keywords which are not in string
    def get_keywords_not_in_strings(self, string, list_keyword):
        return [item for item in list_keyword if item in string]

    # Compare two images
    def compare_images_from_url(self, first_image_url, second_image_url):
        """
        - Compare two images and return the threshold
        - Input: First image dir, Second image dir
        """
        # print(first_image_url)
        # print(second_image_url)
        try:
            response = requests.get(first_image_url)
            i1 = Image.open(BytesIO(response.content))
            response = requests.get(second_image_url)
            i2 = Image.open(BytesIO(response.content))
            if i1.mode != i2.mode:
                print(first_image_url)
                print(second_image_url)
                print("ERROR: Different kinds of images: ", i1.mode, " != ", i2.mode)
            if i1.size != i2.size:
                print(first_image_url)
                print(second_image_url)
                print("ERROR: Different sizes: ", i1.size, " != ", i2.size)

            pairs = zip(i1.getdata(), i2.getdata())

            if len(i1.getbands()) == 1:
                # for gray-scale jpegs
                dif = sum(abs(p1 - p2) for p1, p2 in pairs)
            else:
                dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
            ncomponents = i1.size[0] * i1.size[1] * 3
            threshold = (dif / 255.0 * 100) / ncomponents
        except:
            print("ERROR: Cannot calculate")
            threshold = 100
        print("Difference (percentage):", threshold)
        return threshold

    # Get color text in DB
    def get_list_article_db(self, query, index = 0):
        db_article = self.newfeed_db.get_newfeeds_db(query)
        list_article = self.newfeed_db.get_list_db(db_article, index)
        return list_article;


    # Convert all items in list to string
    def convert_byte_to_string(self, list):
        encoding = 'utf-8'
        convert_list = [i.decode(encoding) for i in list]
        return convert_list

    def division_percentage(self, x, y):
        try:
            return (x / y) * 100
        except ZeroDivisionError:
            return 0