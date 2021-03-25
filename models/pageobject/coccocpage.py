import time
from datetime import datetime

from models.pagelocators.coccocpage import CocCocPageLocators
from models.pageobject.basepage_object import BasePageObject
from models.pageelements.coccocpage import CocCocPageElement
from models.pageobject.downloads import DownloadsPageObject
from utils_automation.common import WebElements


def get_timeout_by_extension(extension):
    if extension in '.exe':
        return 10
    elif extension in '.dmg':
        return 120


def sleep_with_timeout(default_download_folder, language='', installer_name='CocCocSetup', extension='.exe'):
    download_folder_powershell = default_download_folder.replace("\\", "\\\\") + "\\\\"
    from testscripts.smoketest.common import check_if_installer_is_downloaded
    start_time = datetime.now()
    while check_if_installer_is_downloaded(download_folder_powershell, language, installer_name, extension) is False:
        time.sleep(2)
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= get_timeout_by_extension(extension):
            break


class CocCocPageObjects(BasePageObject):
    coccocpage_elem = CocCocPageElement()
    download_elem = DownloadsPageObject()

    def download_coccoc(self, browser, base_url, default_download_folder, os, language):
        browser.get(base_url)
        if "dev" in base_url:
            self.coccocpage_elem.find_download_element(browser, os, language).click()
            self.coccocpage_elem.find_privacy_button(browser).click()
        else:
            self.coccocpage_elem.find_download_element_production(browser, language).click()
            self.click_privacy_button_by_javascript(browser)
        sleep_with_timeout(default_download_folder, language)

    def get_path_installer(self, browser, base_url, default_download_folder, os="win", language="en"):
        self.download_coccoc(browser, base_url, default_download_folder, os, language)
        path_downloaded = default_download_folder + '/CocCocSetup.exe'
        return path_downloaded

    def click_privacy_button_by_javascript(self, browser):
        WebElements.click_element_by_javascript(browser, CocCocPageLocators.PRO_TOI_DA_HIEU_VA_DONG_Y_CSS)