from selenium.webdriver.common.by import By


class CCSearchPageLocators:
    GOOGLE_SEARCH_RESULTS_XPATH = "//*[@id='search']//div[@class='r']/a//@href"

class CCSpellerCheckerLocators:
    SPELLER_BOX = (By.XPATH, "//div[@contenteditable='true']")
    SPELLER_BOX_CSS = "div[contenteditable='true']"
    KIEM_TRA_BTN = (By.XPATH, "//div[text()='Kiểm tra']")
    LOI_LBL = (By.XPATH, "//div[@class='_26vd5']/span[1]")
    SUA_TAT_CA_LOI_BTN = (By.XPATH, "//div[text()='Sửa tất cả lỗi']")
    SPELLER_CHECKER_DEV_URL = "http://dev4.coccoc.com/search?query=chinh%20ta"