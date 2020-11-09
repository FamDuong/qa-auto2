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


class NewTabLogAdsLocators:
    BANNER_ADS_IFRAME = (By.ID, 'ntrb-5')
    BANNER_ADS_LINK = (By.ID, 'link')
    SKIN_ADS_LINK = (By.ID, 'canvas')
    VIDEO_ADS_CLOSE_FLOAT_BUTTON = (By.XPATH, '//button[@class="close"]')
    VIDEO_ADS_CLOSE_FLOAT_BUTTON_XPATH = '//button[@class="close"]'
    VIDEO_ADS_IFRAME = (By.ID, 'ntrb-vast')
    VIDEO_ADS_VIDEO = (By.XPATH, '//video[@webkit-playsinline="true"]')
    NEWS_FIRST_NEWS_BY_PARAM_XPATH = '(//div[@data-ga-label="{param1}"]//a)[1]'
    # NEWS_FIRST_SMALL_NEWS = (By.XPATH, '(//div[@data-ga-label="small"]//a)[1]')
    # NEWS_FIRST_BIG_NEWS = (By.XPATH, '(//div[@data-ga-label="big"]//a)[1]')
    NEWS_FIRST_NEWS_BY_PARAM_LIKE_BUTTON_XPATH = '(//div[@data-ga-label="{param1}"]//div[@data-ga-label="likeButton"]//button)[1]'
    NEWS_FIRST_NEWS_BY_PARAM_DISLIKE_BUTTON_XPATH = '(//div[@data-ga-label="{param1}"]//div[@data-ga-label="likeButton"]//button[contains(@class,"liked")])[1]'
    NEWS_FIRST_NEWS_BY_PARAM_CUSTOMS_BUTTON_XPATH = '(//div[@data-ga-label="{param1}"]//div[@data-ga-label="likeButton"]//button[@data-ga-label="disLikeMenuButton"])[1]'
    NEWS_FIRST_NEWS_BY_PARAM_CUSTOMS_HIDE_ARTICLE_XPATH = '(//div[@data-ga-label="{param1}"]//div[@data-ga-label="likeButton"]//div[@data-ga-label="dislikeMenu-hideArticle"])[1]'
    NEWS_FIRST_NEWS_BY_PARAM_CUSTOMS_HIDE_SOURCE_XPATH = '(//div[@data-ga-label="{param1}"]//div[@data-ga-label="likeButton"]//div[@data-ga-label="dislikeMenu-hideSource"])[1]'
    NEWS_FIRST_NEWS_BY_PARAM_CUSTOMS_REPORT_XPATH = '(//div[@data-ga-label="{param1}"]//div[@data-ga-label="likeButton"]//div[@data-ga-label="dislikeMenu-report"])[1]'

    # NEWS_FIRST_BIG_NEWS_LIKE_BUTTON = (By.XPATH, '(//div[@data-ga-label="big"]//div[@data-ga-label="likeButton"]//button)[1]')
    # NEWS_FIRST_BIG_NEWS_DISLIKE_BUTTON = (By.XPATH, '(//div[@data-ga-label="big"]//div[@data-ga-label="likeButton"]//button[contains(@class,"liked")])[1]')
    # NEWS_FIRST_BIG_NEWS_CUSTOMS_BUTTON = (By.XPATH, '(//div[@data-ga-label="big"]//div[@data-ga-label="likeButton"]//button[@data-ga-label="disLikeMenuButton"])[1]')
    NEWS_FIRST_ADS_BY_PARAM_XPATH = '(//div[@data-ga-label="{param1}:ad"]//a[2])[1]'
    # NEWS_FIRST_SMALL_ADS = (By.XPATH, '(//div[@data-ga-label="small:ad"]//a[2])[1]')
    # NEWS_FIRST_BIG_ADS = (By.XPATH, '(//div[@data-ga-label="big:ad"]//a[2])[1]')

