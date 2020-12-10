import requests
import lxml
import re
import urllib
import requests
import colorama
import random
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
from urllib import parse
from utils_automation.setup import WaitAfterEach

import logging

LOGGER = logging.getLogger(__name__)


class URLUtils:
    # initialize the set of links (unique links)
    internal_urls = set()
    external_urls = set()
    total_urls_visited = 0
    colorama.init()

    GREEN = colorama.Fore.GREEN
    GRAY = colorama.Fore.LIGHTBLACK_EX
    RESET = colorama.Fore.RESET

    def set_user_agent(self):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent': user_agent, }
        return headers

    def is_url_exits(self, url):
        is_exist = True
        # headers = self.set_user_agent()
        try:
            response = requests.get(url)
            # response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError as er:
            is_exist = False
            LOGGER.info("%s is not reachable!!!: %s" % (url, er))
            LOGGER.info("Connection refused by the server..")
            LOGGER.info("Let me sleep for 5 seconds")
            import time
            time.sleep(5)
            LOGGER.info("Was a nice sleep, now let me continue...")
        # except requests.exceptions.InvalidSchema as er:
        #    is_exist = False
        #    LOGGER.info("%s is not reachable!!!: %s" % (url, er))
        LOGGER.info("%s is existed: %s" % (url, str(is_exist)))
        return is_exist

    def is_url_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def wait_for_page_to_load(self, browser, url):
        LOGGER.info(url)
        browser.get(url)
        browser.execute_script("return window.performance.timing.loadEventEnd")
        WaitAfterEach.sleep_timer_after_each_step()

    # Get all sub links in an url which data-linktype="newsdetail"
    def get_newest_link_in_newsfeed(self, url, no_of_urls=2):
        headers = self.set_user_agent()
        sublinks = []
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
                    LOGGER.info("Sub links: %s" % url)
                    found = True
                if found and sublinks.append(link) > no_of_urls:
                    break
        except:
            LOGGER.info("Stop find sub links!")
        return sublinks

    def get_all_website_links(self, url):
        """
        Returns all URLs that is found on `url` in which it belongs to the same website
        """
        # all URLs of `url`
        urls = set()
        # domain name of the URL without the protocol
        try:
            domain_name = urlparse(url).netloc
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
        except requests.exceptions.ConnectionError as r:
            r.status_code = "Connection refused"
            return None
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # href empty tag
                continue
            # join the URL if it's relative (not absolute link)
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not self.is_url_valid(href):
                # not a valid URL
                continue
            if href in self.internal_urls:
                # already in the set
                continue
            if domain_name not in href:
                # external link
                if href not in self.external_urls:
                    # print(f"{self.GRAY}[!] External link: {href}{self.RESET}")
                    self.external_urls.add(href)
                continue
            # print(f"{self.GREEN}[*] Internal link: {href}{self.RESET}")
            urls.add(href)
            self.internal_urls.add(href)
        return urls

    # Check url is live
    def check_link_is_alive(self, url):
        live = True
        headers = self.set_user_agent()
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            LOGGER.info("URL %s not reachable" % url)
            live = False
        return live

    # Check all urls in files are live
    def get_all_links_in_file_are_not_alive(self, filename):
        urls_not_live = set()

        with open(filename, "r+", encoding="utf-8") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                i = i.rstrip('\n')
                live = self.is_url_exits(i)
                if not live:
                    # LOGGER.info("URL %s not reachable!!" % i)
                    urls_not_live.add(i)
            # f.truncate()
        return urls_not_live

    # Remove invalid links
    def remove_invalid_links_in_list(self, urls, urls_not_live):
        # for i in urls_not_live:
        #    urls_live = [ x for x in urls if i not in x ]
        urls_live = [i for i in urls if i not in urls_not_live]
        return urls_live

    # Get sublinks valid
    def get_random_valid_links(self, child_urls, parent_url, number_sublinks = 1):
        result = False
        LOGGER.info("Parent url: " + parent_url)
        LOGGER.info("Child url: " + str(child_urls))
        while not result:
            sub_urls = random.sample(tuple(child_urls), number_sublinks)
            for url in sub_urls:
                sub_url_is_same_root_url = self.is_same_domain(url, parent_url)
                result = self.is_url_exits(url)
                if sub_url_is_same_root_url and url != parent_url and result:
                    break
        LOGGER.info("Child url that selected: " + str(sub_urls))
        LOGGER.info("=================================================================")
        return sub_urls

    # Check if same domain
    def is_same_domain(self, url_1, url_2):
        LOGGER.info("Verify child domain % s is/not same parent domain %s " % (url_1, url_2))
        result = False
        search_domain = parse.urlparse(url_1).hostname
        if search_domain in url_2:
            result = True
        return result
