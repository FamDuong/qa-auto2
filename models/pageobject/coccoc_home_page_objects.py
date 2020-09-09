from models.pageobject.coccocpage import sleep_with_timeout
from utils_automation.const import Urls


class CocCocHomePageActions:
    def download_coccoc_installer_from_thanks_url(self, driver, test_environment):
        if test_environment in 'dev':
            driver.get(Urls.COCCOC_THANK_YOU_URL_EN)
        else:
            driver.get(Urls.COCCOC_THANK_YOU_URL_EN_PRO)

    def waiting_until_finish_download_coccoc_installer(self, download_folder, language):
        sleep_with_timeout(download_folder, language)
