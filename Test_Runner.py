
import time


class TestBrowser:

    def select_shadow_element_by_css_selector(self, browser, selector):
        element = browser.execute_script('return arguments[0].shadowRoot', selector)
        return element

    def test_click_on_open_a_set_of_pages(self, browser):
        browser.maximize_window()
        browser.get("coccoc://settings")
        root1 = browser.find_element_by_tag_name('settings-ui')
        shadow_root1 = self.select_shadow_element_by_css_selector(browser, root1)

        root2 = shadow_root1.find_element_by_css_selector('settings-main')
        shadow_root2 = self.select_shadow_element_by_css_selector(browser, root2)

        root3 = shadow_root2.find_element_by_css_selector('settings-basic-page')
        shadow_root3 = self.select_shadow_element_by_css_selector(browser, root3)

        root4 = shadow_root3.find_element_by_css_selector('settings-on-startup-page')
        shadow_root4 = self.select_shadow_element_by_css_selector(browser, root4)

        root5 = shadow_root4.find_element_by_css_selector('[label="Open a specific page or set of pages"]')
        root5.click()

        time.sleep(2)

    def test_click_on_continue_where_left_off(self,browser):
        browser.maximize_window()
        browser.get("coccoc://settings")
        root1 = browser.find_element_by_tag_name('settings-ui')
        shadow_root1 = self.select_shadow_element_by_css_selector(browser, root1)

        root2 = shadow_root1.find_element_by_css_selector('settings-main')
        shadow_root2 = self.select_shadow_element_by_css_selector(browser,root2)

        root3 = shadow_root2.find_element_by_css_selector('settings-basic-page')
        shadow_root3 = self.select_shadow_element_by_css_selector(browser,root3)

        root4 = shadow_root3.find_element_by_css_selector('settings-on-startup-page')
        shadow_root4 = self.select_shadow_element_by_css_selector(browser,root4)

        root5 = shadow_root4.find_element_by_css_selector('[label="Continue where you left off"]')
        root5.click()

        time.sleep(2)

    def test_click_on_show_language_option(self, browser):
        browser.maximize_window()
        browser.get("coccoc://settings")
        root1 = browser.find_element_by_tag_name('settings-ui')
        shadow_root1 = self.select_shadow_element_by_css_selector(browser,root1)

        root2 = shadow_root1.find_element_by_css_selector('settings-main')
        shadow_root2 = self.select_shadow_element_by_css_selector(browser,root2)

        root3 = shadow_root2.find_element_by_css_selector('settings-basic-page')
        shadow_root3 = self.select_shadow_element_by_css_selector(browser,root3)

        root5 = shadow_root3.find_element_by_css_selector('settings-languages-page')
        time.sleep(1)
        shadow_root5 = self.select_shadow_element_by_css_selector(browser,root5)
        time.sleep(1)

        root7 = shadow_root5.find_element_by_css_selector('[alt="Show language options"]')

        root7.click()
        time.sleep(2)

    # def test_facebook(self,browser):
    #     Value = "Under 20"
    #     browser.get("http://www.facebook.com/")
    #     # browser.save_screenshot("Test2.png")
    #     assert "xyy" in browser.title
    #
    # def test_google(self,browser):
    #     Value = "Under 20"
    #     browser.get("http://www.google.com/")
    #     # browser.save_screenshot("Test2.png")
    #     assert "xyy" in browser.title
    #     assert True