import pytest
from config.environment import COCCOC_MUSIC_CMS_DOMAIN_URL, COCCOC_MUSIC_CMS_ADMIN_EMAIL, \
    COCCOC_MUSIC_CMS_ADMIN_PASSWORD
from models.pageobject.coccoc_music.coccoc_music_cms.dash_board_page import CMSDashBoardPageObjects
from models.pageobject.coccoc_music.coccoc_music_cms.login_page import CMSLoginPagePageObject

cms_login_page_object = CMSLoginPagePageObject()
cms_dash_board_object = CMSDashBoardPageObjects()


@pytest.fixture()
def set_up_login_then_log_out_after_finish(browser):
    browser.get(COCCOC_MUSIC_CMS_DOMAIN_URL)
    cms_login_page_object.login(browser, COCCOC_MUSIC_CMS_ADMIN_EMAIL, COCCOC_MUSIC_CMS_ADMIN_PASSWORD)
    yield browser
    browser.get(COCCOC_MUSIC_CMS_DOMAIN_URL)
    cms_dash_board_object.sign_out(browser)






