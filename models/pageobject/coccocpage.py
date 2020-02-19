import time
from datetime import datetime

from utils_automation.const import Urls
from models.pageobject.basepage_object import BasePageObject
from models.pageelements.coccocpage import CocCocPageElement
from models.pageobject.downloads import DownloadsPageObject


def check_if_finished_with_timeout(download_folder, language):
    start_time = datetime.now()
    from testscripts.smoketest.common import check_if_installer_is_downloaded, break_if_timeout
    bool_value = check_if_installer_is_downloaded(download_folder, language)
    print("download_folder "+download_folder)
    print("Value "+str(bool_value))
    break_if_timeout(bool_value, False, 3, 60)


class CocCocPageObjects(BasePageObject):
    coccocpage_elem = CocCocPageElement()
    download_elem = DownloadsPageObject()

    def get_path_installer(self, browser, download_folder, os="win", language="en"):
        self.coccocpage_elem.find_download_element(browser, os, language).click()
        self.coccocpage_elem.find_privacy_button(browser).click()
        path_downloaded = download_folder + '/coccoc_' + language + '.exe'
        check_if_finished_with_timeout(download_folder, language)
        return path_downloaded

    def get_path_installer_that_download_from_dev(self, browser, download_folder, os="win", language="en"):
        browser.get(Urls.COCCOC_DEV_URL)
        return self.get_path_installer(browser, download_folder, os, language)

    def get_path_installer_that_download_from_production(self, browser, download_folder, os="win", language="vi"):
        browser.get(Urls.COCCOC_URL)
        return self.get_path_installer(browser, download_folder, os, language)
