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
from newspaper import Article
import metadata_parser
from bs4 import BeautifulSoup
from newsfetch.news import newspaper
from newsplease import NewsPlease
from databases.sql.coccoc_new_feeds_db import NewFeedDB;
from testscripts.api.coccoc_new_feeds.common import NewFeedCommon;
from datetime import datetime
import inspect

class NewFeedCommon(NewFeedCommon):
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
        # user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/87.0.148 Chrome/81.0.4044.148 Safari/537.36'
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

    # Get all sub links in an url which data-linktype="newsdetail"
    def get_newest_link_in_newsfeed(self, list_newsfeed):
        headers = self.set_user_agent()
        sublinks = []
        for url in list_newsfeed:
            try:
                found = False
                request = urllib.request.Request(url, None, headers)
                connection = urllib.request.urlopen(request)
                dom = lxml.html.fromstring(connection.read())
                # Get first article only
                for link in dom.xpath('//a/@href'):
                    if (bool(re.search('[0-9]{5}', link))) and ":" not in link and "www" not in link:
                        if not link.startswith('http'):
                            link = url + link
                        sublinks.append(link)
                        found = True
                    if found:
                        break
            except:
                continue
        return sublinks

    def set_user_agent(self):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent': user_agent, }
        return headers

    # Extract title
    def get_attribute_from_url(self, url, attribute):
        title = ''
        try:
            headers = self.set_user_agent()
            request = urllib.request.Request(url, None, headers)
            connection = urllib.request.urlopen(request)
            soup = BeautifulSoup(connection.read(), 'html.parser')
            title = soup.title.string
            # Get the correct title
            # title = title.split(" - ")[0]
            title = title.split(" | ")[0]
            title = title.replace("\r", "")
            title = title.replace("\n", "")
            title = title.strip()
        except:
            title = ''
        finally:
            return title

    # Use metadata parse
    def get_parse_metadata(self, url, attribute, list_parser, list_strip):
        content = ""
        try:
            page = metadata_parser.MetadataParser(url=url)
            for parser in list_parser:
                content = page.get_metadata(parser)
                if content is not None or content != "":
                    break
            for string in list_strip:
                content = content.split(string)[0]
            content = content.replace("  ", " ")
            # return page.get_metadata('og:title')
        finally:
            print(content)
            return content

    # Use newspaper parser
    def get_parse_newspaper(self, url, attribute, list_strip):
        content = ""
        try:
            article = Article(url)
            article.download()
            article.parse()
            if attribute == "title":
                content = article.title
            elif attribute == "description":
                content = article.meta_description
            elif attribute == "content":
                content = article.text[:50000]
                content = self.remove_newlines_string(content)
            elif attribute == "image_url":
                content = article.top_image
            elif attribute == "tags":
                content = article.meta_keywords
                content = ", ".join(map(str, content))
                if content is None:
                    content = "None"
        finally:
            content = self.strip_string(content, list_strip)
            return str(content)

    # Use newspaper parser
    def get_parse_news_fetch(self, url, attribute, list_strip = []):
        content = ""
        try:
            article = newspaper(url)
            if attribute == "published_time":
                content = article.date_publish
                content = content.strftime("%Y-%m-%d %H:%M:%S")
            elif attribute == "breadcumb_name":
                content = article.category
            elif attribute == "title":
                content = article.title
            elif attribute == "content":
                content = article.description
            elif attribute == "domain":
                content = article.source_domain
        finally:
            content = self.strip_string(content, list_strip)
            return str(content)

    # Use news release
    def get_parse_news_release(self, url, attribute, list_strip):
        content = ""
        try:
            article = NewsPlease.from_url(url)
            if attribute == "content":
                content = article.maintext
                content = self.remove_newlines_string(content)
                content = self.replace_string(content, article.description + ".", "")
        finally:
            content = self.strip_string(content, list_strip)
            return str(content)

    # Strip some unexpected keyword
    def strip_string(self, string, list_strip):
        try:
            for keyword in list_strip:
                string = string.split(keyword)[0]
        except:
            print("ERROR: Cannot strip string")
        return string

    # Remove new lines
    def remove_newlines_string(self, string):
        try:
            r_unwanted = re.compile("[\n\t\r]")
            return r_unwanted.sub("", string)
        except:
            return string

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
            replace_list = [ str(sub).replace(original, replacement) for sub in list ]
        return replace_list

    # Split string in list
    def split_string_in_list(self, list, string, index=0):
        list = [ str(sub).split(string)[index] for sub in list ]
        return list

    # Replace string in string
    def replace_string(self, string, original, replacement):
        try:
            string = str(string).replace(original, replacement)
        except:
            print("ERROR: Cannot replace")
        return string

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

    # Read from file
    def read_to_file(self, filename):
        file = open(filename, 'r+', encoding="utf-8")
        list_content = file.readlines()
        file.close()
        return list_content

    # Append list to a file
    def append_to_file(self, filename, input_lists, type="list"):
        if type == "string":
            input_lists = [ input_lists ]
        if os.path.exists(filename):
            file = open(filename, 'a', encoding="utf-8")
        else:
            file = open(filename, 'w+', encoding="utf-8")
        for i in input_lists:
            file.write("%s\n" % (i))
        file.close()

    # Check if file is exist
    def check_file_is_existed(self, filename):
        return os.path.exists(filename)

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
        list_1 = [ str(i) for i in list_1]
        list_2 = [ str(i) for i in list_2]
        diff_1 = [item for item in list_1 if str(item) not in list_2]
        diff_2 = [item for item in list_2 if str(item) not in list_1]
        return diff_1 + diff_2

    # Check if no common elements in two lists
    def check_if_lists_are_different(self, list_1, list_2):
        self.print_debug("List 1 length: %s" % len(list_1))
        self.print_debug("List 2 length: %s" % len(list_2))
        result = True
        diff = self.get_different_elements_between_lists(list_1, list_2)
        if len(diff):
            self.print_list(diff)
            result = False
        return result

    # Check list of keywords which are not in string
    def get_keywords_not_in_strings(self, string, list_keyword):
        return [item for item in list_keyword if item.lower() in string.lower()]

    # Compare two images
    def compare_images_from_url(self, first_image_url, second_image_url):
        compare_results = []
        mode = ""
        size = ""
        threshold = ""
        """
        - Compare two images and return the threshold
        - Input: First image dir, Second image dir
        - Output: Second image mode, second image size, threshold
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
            mode = str(i1.mode) + ", " + str(i2.mode)
            size = str(i1.size) + ", " + str(i2.size)

            pairs = zip(i1.getdata(), i2.getdata())

            if len(i1.getbands()) == 1:
                # for gray-scale jpegs
                dif = sum(abs(p1 - p2) for p1, p2 in pairs)
            else:
                dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
            ncomponents = i1.size[0] * i1.size[1] * 3
            threshold = (dif / 255.0 * 100) / ncomponents
        except:
            print("ERROR: Cannot calculate threshold")
            threshold = 100
        # print("Difference (percentage):", threshold)
        compare_results.append(mode)
        compare_results.append(size)
        compare_results.append(threshold)
        self.print_list(compare_results)
        return compare_results

    # Get color text in DB
    def get_list_newsfeed_db(self, sql_query, index = 0, data_query = None):
        db_article = self.newfeed_db.select_newfeeds_db(sql_query, data_query)
        list_article = self.newfeed_db.get_list_db(db_article, index)
        return list_article;


    # Convert all items in list to string
    def convert_byte_to_string(self, list):
        encoding = 'utf-8'
        convert_list = [i.decode(encoding) for i in list]
        return convert_list

    def convert_list_to_string(self, list, concentrate = ", "):
        convert_string = concentrate.join((map(str, list)))
        self.print_debug(convert_string)
        return convert_string

    def division_percentage(self, x, y):
        try:
            return (x / y) * 100
        except ZeroDivisionError:
            return 0

    # Need to fix the converter
    def subtraction_datetime(self, time_1, time_2, dateformat = "%Y-%m-%d %H:%M:%S", unit = "minutes"):
        sub = ""
        try:
            # time_1 = datetime.strptime(time_1, dateformat)
            time_2 = datetime.strptime(time_2, dateformat)
            threshold = time_1 - time_2
            if unit == "minutes":
                minutes = divmod(threshold.seconds, 60)
                sub = minutes[0]
        except:
            sub = ""
        return sub

    # Calculate different date
    def subtraction_days(self, date1, date2):
        format = "%Y-%m-%d %H:%M:%S"
        try:
            date1 = datetime.strptime(date1, format)
            date2 = datetime.strptime(date2, format)
            return abs((date2 - date1).days)
        except:
            self.print_debug("ERROR: Cannot calculate days")
            return 8888

    # Get data with reference index is
    def get_reference_data_in_list(self, list_1, list_2, reference):
        list_data = []
        temp = set(list_1)
        index = [i for i, val in enumerate(list_1) if (val in temp and val == reference)]
        for i in index:
            list_data.append(list_2[i])
        return list_data


    # Get data in dict
    def get_dict(self, dict, key):
        try:
            data = dict[key]
        except:
            data = None
        return data


    def print_debug(self, string):
        function_name = inspect.stack()[1].function
        print(function_name, ": ", string)


