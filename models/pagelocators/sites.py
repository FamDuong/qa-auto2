from selenium.webdriver.common.by import By


class YoutubePageLocators(object):

    @staticmethod
    def any_video_item(text):
        return By.XPATH, '//a[contains(text(), "%s")][@id="video-title"]' % text

    VIDEO_PLAYER_ITEM = (By.ID, 'movie_player')

    SEARCH_BOX = (By.ID, 'search')

    SEARCH_BTN = (By.ID, 'search-icon-legacy')


class GooglePageLocators(object):

    SEARCH_FIELD = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="VlcLAe"]/input[@class="gNO89b"]')
    VIDEO_SEARCH_BTN = (By.XPATH, '//a[contains(text(),"Videos")]')

    SHADOW_ROOT_CONTENT = (By.XPATH, '(//div[starts-with(@data-hveid, "4")]//div[@class="s"]//div)[6]')
    SAVIOR_ICON = '[class="button-block shown"]'


class AnySite(object):
    TWENTY_FOUR_H_VIDEO_ITEM = (By.ID, 'zoneViewVideoPlay')


