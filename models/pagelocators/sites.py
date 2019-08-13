from selenium.webdriver.common.by import By


class YoutubePageLocators(object):
    ANY_VIDEO_ITEM = (By.XPATH, '(//a[not(contains(text(), "Live"))][@id="video-title"])[10]')

    VIDEO_PLAYER_ITEM = (By.ID, 'player')


class GooglePageLocators(object):

    SEARCH_FIELD = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="VlcLAe"]/input[@class="gNO89b"]')
    VIDEO_SEARCH_BTN = (By.XPATH, '//a[contains(text(),"Videos")]')

    SHADOW_ROOT_CONTENT = (By.XPATH, '(//div[starts-with(@data-hveid, "4")]//div[@class="s"]//div)[6]')
    SAVIOR_ICON = '[class="button-block shown"]'
