from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement(object):

    @staticmethod
    def select_shadow_element_by_css_selector(browser, selector):
        element = browser.execute_script('return arguments[0].shadowRoot', selector)
        return element

    def find_shadow_element(self, driver, *string_text):

        i = 0
        root = driver.find_element_by_tag_name(string_text[i])
        print (0 + len(string_text))
        while len(string_text) > (i+1):
            i = i+1
            shadow_root = self.select_shadow_element_by_css_selector(driver, root)
            root = shadow_root.find_element_by_css_selector(string_text[i])
        return root
