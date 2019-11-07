from selenium.webdriver.common.by import By


class NewTabSearchLocators:
    MOST_VISITED_TITLES_CSS_SELECTOR = 'a[data-ga-label*="tile"]'
    SEARCH_STRING = (By.ID, 'search-string')
    SEARCH_BUTTON = (By.ID, 'search-button')
    MOST_VISITED_TITLES = (By.CSS_SELECTOR, MOST_VISITED_TITLES_CSS_SELECTOR)







