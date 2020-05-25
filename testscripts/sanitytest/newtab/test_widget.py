import time

from pytest_testrail.plugin import pytestrail

from models.pageobject.newtab import NewTabWidgetActions
from utils_automation.const import Urls


@pytestrail.case('C65114')
def test_widget_new_tab(browser):
    new_tab_widget_action = NewTabWidgetActions()
    browser.get(Urls.NEW_TAB_URL)
    new_tab_widget_action.click_on_widget_button(browser)
    new_tab_widget_action.click_on_selected_widget(browser)
    selected_widget_attribute = new_tab_widget_action.get_attribute_selected_widget(browser)
    print(selected_widget_attribute)
    tag = selected_widget_attribute.rsplit('/', 1)[-1]
    print(tag)
    time.sleep(5)
    new_tab_widget_action.click_on_done_button(browser)
    time.sleep(10)
    image_background = browser.find_element_by_xpath(
        "//div[@class='fixedBackgroundImage'][contains(@style, 'background-image')]")
    image_background_attribute = image_background.get_attribute('style')
    print(image_background_attribute)
    time.sleep(5)
    assert tag in image_background_attribute
    # new_tab_widget_action.click_on_widget_button(browser)
    # new_tab_widget_action.click_on_reset_button()
    # time.sleep(5)


    # print(selected_widget_attribute)
    # selected_widget = browser.find_element_by_xpath("//div[@class='bg-item'][contains(@style, '0446fcf64751adc0cad2054bc13d719c')]")
    # selected_widget.click()
    # done_button = browser.find_element_by_xpath('//button[text()="Done"]')
    # done_button.click()
    # selected_widget_attribute = selected_widget.get_attribute('style')
    # print(selected_widget_attribute)
    # url = style_attribute.split(' url("')[1].replace('");', '')
    # tag = selected_widget_attribute.rsplit('/', 1)[-1]
    # print(tag)
    # time.sleep(10)
    # background_image = browser.find_element_by_xpath("//div[@class='fixedBackgroundImage'][contains(@style, 'background-image')]")
    # background_image_attribute = background_image.get_attribute('style')
    # print(background_image_attribute)
    # time.sleep(5)
    # assert tag in background_image_attribute



