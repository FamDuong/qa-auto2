from selenium.webdriver.common.by import By


class YoutubePageLocators(object):
    ANY_VIDEO_ITEM = (By.ID, 'thumbnail')

    VIDEO_PLAYER_ITEM = (By.ID, 'player')
