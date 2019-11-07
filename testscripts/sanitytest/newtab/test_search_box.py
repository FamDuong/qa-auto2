from pytest_testrail.plugin import pytestrail
from selenium.webdriver.common.keys import Keys
from models.pageobject.newtab import NewTabSearchPageObject
from utils_automation.const import Urls


new_tab_search_page_object = NewTabSearchPageObject()
COCCOC_SEARCH_RELATIVE_URL = 'coccoc.com/search'


@pytestrail.case('C54967')
def test_check_display_search_box(browser):
    browser.get(Urls.NEW_TAB_URL)
    font_size_search_string_value = new_tab_search_page_object.get_css_value_search_string_element(browser, 'font-size')
    color_search_button_value = new_tab_search_page_object.get_css_value_search_button_element(browser, 'background')
    assert font_size_search_string_value == '16px'
    assert 'data:image/svg+xml;base64' in color_search_button_value


@pytestrail.case('C54971')
def test_check_redirect_coccoc_search_page_by_click_search_btn(browser):
    browser.get(Urls.NEW_TAB_URL)
    new_tab_search_page_object.send_key_string_to_search_string_element(browser, 'google.com')
    new_tab_search_page_object.click_search_button_element(browser)
    assert COCCOC_SEARCH_RELATIVE_URL in browser.current_url


@pytestrail.case('C54972')
def test_check_redirect_coccoc_search_page_hit_enter(browser):
    browser.get(Urls.NEW_TAB_URL)
    new_tab_search_page_object.send_key_string_to_search_string_element(browser, 'google.com')
    new_tab_search_page_object.send_key_string_to_search_string_element(browser, Keys.RETURN)
    assert COCCOC_SEARCH_RELATIVE_URL in browser.current_url







