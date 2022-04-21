from bs4 import BeautifulSoup
import urllib.request
import re


def not_relative_uri(href):
    return re.compile('^https://').search(href) is not None


url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser', from_encoding="iso-8859-1")

new_feeds = soup.find('section', class_='section section_topstory').find('a')
print('newfeeds---------', new_feeds['href'])
for feed in new_feeds:
    print(feed)
    # title = feed['title']
    # link = feed.get('href')
    # print('Title: {} - Link: {}'.format(title, link))
    # print('title', title)
    # link_url = feed["href"]
    # print(f"Apply here: {link_url}\n")
