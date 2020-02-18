import os
import time
from datetime import datetime

from utils_automation.const import Urls
from models.pageobject.basepage_object import BasePageObject
from models.pageelements.coccocpage import CocCocPageElement
from models.pageobject.downloads import DownloadsPageObject


def get_path_of_downloaded_coccoc_installer_from_dev(download_folder, language="en"):
    download_file = download_folder + '/coccoc_' + language + '.exe'
    os.path.isfile(download_file)
    return download_file


class CocCocPageObjects(BasePageObject):
    coccocpage_elem = CocCocPageElement()
    download_elem = DownloadsPageObject()

    def get_path_of_downloaded_coccoc_installer_from_dev(self, browser, download_folder, os="win", language="en"):
        browser.get(Urls.COCCOC_DEV_URL)
        self.coccocpage_elem.find_download_element(browser, os, language).click()
        self.coccocpage_elem.find_privacy_button(browser).click()
        path_downloaded = get_path_of_downloaded_coccoc_installer_from_dev(download_folder, language)
        start_time = datetime.now()
        while self.check_if_file_is_downloaded(language, path_downloaded) is False:
            time.sleep(3)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 120:
                break
        return path_downloaded

    def download_coccoc_from_production(self, browser, download_folder, os="win", language="vi"):
        browser.get(Urls.COCCOC_URL)
        return self.download_latest_version(browser, download_folder, os, language)

    def check_if_file_is_downloaded(self, language, path_downloaded):
        if '/coccoc_' + language + '.exe' in path_downloaded:
            return True
        else:
            return False
