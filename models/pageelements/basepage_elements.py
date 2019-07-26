from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePageElement(object):

    @staticmethod
    def select_shadow_element_by_css_selector(browser, selector):
        element = browser.execute_script('return arguments[0].shadowRoot', selector)
        return element

    def find_shadow_element(self, driver, *string_text):

        wait = WebDriverWait(driver, 5)
        i = 0
        root = wait.until(ec.presence_of_element_located((By.TAG_NAME, string_text[i])))
        # root = driver.find_element_by_tag_name(string_text[i])
        while len(string_text) > (i+1):
            i = i+1
            shadow_root = self.select_shadow_element_by_css_selector(driver, root)
            root = shadow_root.find_element_by_css_selector(string_text[i])
        return root
