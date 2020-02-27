import time
from datetime import datetime
from models.pageobject.basepage_object import BasePageObject
from models.pageelements.coccocpage import CocCocPageElement
from models.pageobject.downloads import DownloadsPageObject


def sleep_with_timeout(default_download_folder, language):
    download_folder_powershell = default_download_folder.replace("\\", "\\\\") + "\\\\"
    from testscripts.smoketest.common import check_if_installer_is_downloaded
    start_time = datetime.now()
    while check_if_installer_is_downloaded(download_folder_powershell, language) is False:
        time.sleep(2)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 10:
            break


class CocCocPageObjects(BasePageObject):
    coccocpage_elem = CocCocPageElement()
    download_elem = DownloadsPageObject()

    def download_coccoc(self, browser, base_url, default_download_folder, os, language):
        browser.get(base_url)
        self.coccocpage_elem.find_download_element(browser, os, language).click()
        self.coccocpage_elem.find_privacy_button(browser).click()
        sleep_with_timeout(default_download_folder, language)

    def get_path_installer(self, browser, base_url, default_download_folder, os="win", language="en"):
        self.download_coccoc(browser, base_url, default_download_folder, os, language)
        path_downloaded = default_download_folder + '/coccoc_' + language + '.exe'
        return path_downloaded
