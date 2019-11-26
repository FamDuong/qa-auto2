from pytest_testrail.plugin import pytestrail
from models.pageobject.newtab import NewTabZenPageObject
from utils_automation.const import Urls
from utils_automation.setup import WaitAfterEach

new_tab_zen_page_object = NewTabZenPageObject()


@pytestrail.case('C54986')
def test_redirect_after_click_zen_news(browser):
    browser.get(Urls.NEW_TAB_URL)
    new_tab_zen_page_object.move_to_any_zen_element(browser)
    new_tab_zen_page_object.click_on_any_zen_element(browser)
    element_href = new_tab_zen_page_object.get_attribute_any_zen_element(browser, 'href')
    windows_handles = browser.window_handles
    if len(windows_handles) == 3:
        browser.switch_to.window(windows_handles[2])
    elif len(windows_handles) == 2:
        browser.switch_to.window(windows_handles[1])
    current_url = browser.current_url
    browser.close()
    browser.switch_to.window(windows_handles[0])
    assert element_href == current_url


@pytestrail.case('C55001')
def test_check_allow_scroll_down(browser):
    browser.get(Urls.NEW_TAB_URL)
    for x in range(0, 5):
        before_scroll_total_elems = new_tab_zen_page_object.get_number_of_all_current_zen_elements(browser)
        new_tab_zen_page_object.scroll_to_with_scroll_height(browser)
        WaitAfterEach.sleep_timer_after_each_step()
        after_scroll_total_elems = new_tab_zen_page_object.get_number_of_all_current_zen_elements(browser)
        assert after_scroll_total_elems > before_scroll_total_elems


@pytestrail.case('C127500')
def test_check_no_duplicate_news_on_zen(browser):
    from utils_automation.common import check_if_duplicates_list
    browser.get(Urls.NEW_TAB_URL)
    for x in range(0, 20):
        new_tab_zen_page_object.scroll_to_with_scroll_height(browser)
        WaitAfterEach.sleep_timer_after_each_step()
    url_list = new_tab_zen_page_object.get_attribute_all_zen_element(browser, 'href')
    print(f'List of urls is : {url_list}')
    assert check_if_duplicates_list(url_list)




