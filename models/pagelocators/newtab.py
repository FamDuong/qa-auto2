from selenium.webdriver.common.by import By


class NewTabSearchLocators:
    SEARCH_STRING = (By.ID, 'search-string')
    SEARCH_BUTTON = (By.ID, 'search-button')


class NewTabIconSitesLocators:
    MOST_VISITED_TITLES_CSS_SELECTOR = 'a[data-ga-label*="tile"]'
    MOST_VISITED_ICONS_CSS_SELECTOR = 'a[data-ga-label*="icon"]'
    MOST_VISITED_TITLES = (By.CSS_SELECTOR, MOST_VISITED_TITLES_CSS_SELECTOR)
    MOST_VISITED_ICONS = (By.CSS_SELECTOR, MOST_VISITED_ICONS_CSS_SELECTOR)


class NewTabZenLocators:
    ZEN_NEWS_ITEM_CSS_SELECTOR = 'div[class] > a:not(.qc-link)[href]:not(.context-content)'
    ZEN_NEWS_ITEM = (By.CSS_SELECTOR, ZEN_NEWS_ITEM_CSS_SELECTOR)
    ZEN_NEWS_NOT_CONTAINS_ADS_ITEM_CSS_SELECTOR = 'div[class] > a:not(.qc-link)[href]:not(.context-content)' \
                                                  ':not(.zen-ads__context):not([href*="utm"])' \
                                                  ':not([data-click-url*="click"])'
    ZEN_NEWS_NOT_CONTAINS_ADS_ITEM = (By.CSS_SELECTOR, ZEN_NEWS_NOT_CONTAINS_ADS_ITEM_CSS_SELECTOR)

class NewTabWidgetLocators:
    EDIT_WIDGET_BUTTON = (By.XPATH, '//div[@class="widget-customize-button minimal"]')
    # EDIT_WIDGET_BUTTON = (By.XPATH, '// span[text() = "Customize page"]')
    # SELECTED_WIDGET = (By.XPATH, "//div[@class='bg-item'][@data-index]")
    SELECTED_WIDGET = (By.XPATH, "//div[@class='bg-item'][contains(@style, '68abee5573567d1a6c8a413196cbb0b4')]")
    SELECTED_BACKGROUND_IMAGE = (By.XPATH, "//div[@class='bg-item active']")
    DONE_BUTTON = (By.XPATH, '//button[text()="Done"]')
    RESET_DEFAULT_BUTTON = (By.XPATH, '//button[@class="btn btn-600 reset"]')

class NewTabMostVisitedLocators:
    TOTAL_MOST_VISITED_QC = (By.XPATH, "//li[contains(@class,'most-visited-tile mv-qc')]")
    TOTAL_MOST_VISITED_QC_XPATH = "//li[contains(@class,'most-visited-tile mv-qc')]"
    MOST_VISITED_QC_BY_INDEX_XPATH = "(//li[contains(@class,'most-visited-tile mv-qc')]//a)[{param1}]"
    TOTAL_NEWS_XPATH = "//div[contains(@class,'feedRow')]//div[contains(@class,'nf-card')]"
    TOTAL_NEWS_ADS_XPATH = "//div[contains(@class,'feedRow')]//div[contains(@class,'-ad nf-card')]"
    NEWS_ADS_BY_INDEX_XPATH = "(//div[contains(@class,'feedRow')]//div[contains(@class,'-ad nf-card')])[{param1}]"




