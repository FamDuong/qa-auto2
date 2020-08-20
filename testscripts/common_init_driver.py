from utils_automation.common import FilesHandle
from selenium import webdriver

file_handle = FilesHandle()


def init_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {'safebrowsing.enabled': 'true'})
    binary_path_temp = file_handle.get_absolute_filename("\\webdriver\\chromedriver.exe")
    binary_path = binary_path_temp.replace('\\utils_automation', '\\resources')
    print(binary_path+"hello"+binary_path_temp)
    driver = webdriver.Chrome(options=chrome_options, executable_path=binary_path)
    return driver
