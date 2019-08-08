from selenium import webdriver


class Browser:
    def browser_incognito(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        return webdriver.Chrome(options=chrome_options)
