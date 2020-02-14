import os
import time
from utils_automation.const import Urls
from models.pageobject.basepage_object import BasePageObject
from models.pageelements.coccocpage import CocCocPageElement
from models.pageobject.downloads import DownloadsPageObject


def verify_download_successfully(download_folder, language="en"):
    download_file = download_folder + '/coccoc_' + language + '.exe'
    os.path.isfile(download_file)
    return download_file


class CocCocPageObjects(BasePageObject):
    coccocpage_elem = CocCocPageElement()
    download_elem = DownloadsPageObject()

    def download_coccoc_from_dev(self, browser, download_folder, os="win", language="en"):
        browser.get(Urls.COCCOC_DEV_URL)
        return self.download_latest_version(browser, download_folder, os, language)

    def download_coccoc_from_production(self, browser, download_folder, os="win", language="vi"):
        browser.get(Urls.COCCOC_URL)
        return self.download_latest_version(browser, download_folder, os, language)

    def download_latest_version(self, driver, download_folder, os="win", language="en"):
        self.coccocpage_elem.find_download_element(driver, os, language).click()
        self.coccocpage_elem.find_privacy_button(driver).click()
        time.sleep(20)
        return verify_download_successfully(download_folder, language)
