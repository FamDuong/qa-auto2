from selenium.webdriver.common.by import By


class CCSearchPageLocators:
    GOOGLE_SEARCH_RESULTS_XPATH = "//*[@id='search']//div[@class='r']/a//@href"
    AD_LINK_XPATH = '//div[@class="adsv"]//h3//a'
    AD_LINK = (By.XPATH, '//div[@class="adsv"]//h3//a')
    AD_LINK_BY_INDEX_XPATH = '(//div[@class="adsv"]//h3//a)[{param1}]'


class CCSpellerCheckerLocators:
    SPELLER_BOX = (By.XPATH, "//div[@contenteditable='true']")
    SPELLER_BOX_CSS = "div[contenteditable='true']"
    KIEM_TRA_BTN = (By.XPATH, "//div[text()='Kiểm tra']")
    LOI_LBL = (By.XPATH, "//div[text()='Sửa tất cả lỗi']//parent::div//span[1]")
    SUA_TAT_CA_LOI_BTN = (By.XPATH, "//div[text()='Sửa tất cả lỗi']")
    SPELLER_CHECKER_DEV_URL = "http://dev4.coccoc.com/search?query=chinh%20ta"
    DA_SUA_HET_LOI_LBL_XPATH = "//span[text()='Đã sửa hết lỗi']"
    BAN_LAM_DUNG_HET_ROI_NHE_LBL_XPATH = "//div[text()='Oh, bạn làm đúng hết rồi nhé!']"
