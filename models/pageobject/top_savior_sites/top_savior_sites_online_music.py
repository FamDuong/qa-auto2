from models.pageelements.top_savior_sites.top_savior_sites_online_music import TopSaviorSitesOnlineMusicElements
from models.pageobject.basepage_object import BasePageObject


class TopSaviorSitesOnlineMusicActions(BasePageObject):
    online_music_element = TopSaviorSitesOnlineMusicElements()

    def click_on_nhac_cua_tui_marketing_popup(self, driver):
        if len(self.online_music_element.find_number_nhac_cua_tui_popup_btn(driver)) > 0:
            self.online_music_element.find_nhac_cua_tui_close_popup_btn(driver).click()
