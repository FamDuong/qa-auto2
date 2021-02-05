class CoccocHomePageLocators:
    TAI_CC_BTN_HEADER_XPATH = "//*[@id='menu']//a//li"
    TAI_CC_BTN_CENTER_HOME_XPATH = '//div[ contains(@class,"btn__download__coccoc")])[2]'
    TAI_CC_BTN_CENTER_OTHER_PAGE_XPATH = "//section[@class='section__mobile']//a[contains(@class,'js-show-modal-download')]"
    TAI_CC_BTN_FOOTER_XPATH = "//div[@class='section__download__app']//a[contains(@class,'js-show-modal-download')]"
    DONG_Y_BTN_CSS = "div.cc-modal-download-bottom.js-cc-download > a"
    DONG_Y_BTN_XPATH = "//a[text()='Tôi đã hiểu và đồng ý']"
    TRINH_DUYET_DI_DONG_TAB_XPATH = "//a[text()='Trình duyệt di động']"
    TAI_CC_MAC_BTN_XPATH = "//a[contains(@class,'js-show-modal-mac')]"
    ANDROID_BTN_XPATH = "//img[contains(@class,'ic_android')]"
    IOS_BTN_XPATH = "//img[contains(@class,'ic_apple')]"
    APP_STORE_BTN_CENTER_XPATH = "//div[contains(@class,'section__mobile')]//li[contains(@class,'btn-appstore')]//img[@class='appStore']/parent::a"
    APP_STORE_BTN_FOOTER_XPATH = "//div[contains(@class,'section__download__app')]//li[contains(@class,'btn-appstore')]//img[@class='appStore']/parent::a"
    GOODLE_PLAY_BTN_CENTER_XPATH = "//section[@class='section__mobile']//img[@class='google-play']/parent::a[@class='googlePlay']"
    GOODLE_PLAY_BTN_FOOTER_XPATH = "//div[contains(@class,'section__download__app')]//img[@class='google-play']/parent::a[@class='googlePlay']"
    GOODLE_PLAY_URL = "https://play.google.com/store/apps/details?id=com.coccoc.trinhduyet&hl=en/"
    APP_STORE_URL = "https://apps.apple.com/vn/app/tr%C3%ACnh-duy%E1%BB%87t-c%E1%BB%91c-c%E1%BB%91c/id1170593919?l=vi/"
    TITTLE_MOBILE_PAGE = 'Khám phá trình duyệt Cốc Cốc cho di động.'
