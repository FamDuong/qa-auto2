import random
import re

from pytest_testrail.plugin import pytestrail

from models.pageobject.newtab import NewTabSearchPageObject
from utils_automation.const import Urls


new_tab_search_page_object = NewTabSearchPageObject()


@pytestrail.case('C54976')
def test_check_redirect_after_click_on_most_visted(browser):
    browser.get(Urls.NEW_TAB_URL)
    total_number_most_visited = new_tab_search_page_object.get_total_number_most_visited_sites(browser)
    random_element_number = random.randrange(total_number_most_visited - 1)
    any_site_href_in_element = new_tab_search_page_object\
        .get_attribute_any_most_visited_site_element(browser, random_element_number, 'href')
    new_tab_search_page_object.click_any_most_visited_site_element(browser, random_element_number)
    assert_string_url = re.split(r'[A-Za-z]/', any_site_href_in_element)[1]
    assert 1 <= total_number_most_visited >= 5
    assert assert_string_url in browser.current_url







