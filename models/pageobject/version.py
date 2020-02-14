import os
from models.pageelements.version import VersionPageElements
from models.pageobject.basepage_object import BasePageObject
from os import path
from models.pagelocators.version import VersionPageLocators
from utils_automation.const import Urls


class VersionPageObject(BasePageObject):
    version_element = VersionPageElements()

    def get_profile_path(self, driver):
        profile_path_elem = self.version_element.find_element(driver, VersionPageLocators.PROFILE_PATH_ELEMENT)
        return profile_path_elem.text

    def get_flash_path(self, driver):
        flash_path = self.version_element.find_element(driver, VersionPageLocators.FLASH_PATH_ELEMENT)
        return flash_path.text

    def get_user_agent(self, driver):
        user_agent = self.version_element.find_element(driver, VersionPageLocators.USER_AGENT_ELEMENT)
        return user_agent.text

    def verify_version_is_correct(self, expect_version):
        # Verify in local machine folder
        local_app_data = path.expandvars(r'%LOCALAPPDATA%\CocCoc\Browser\Application\\')
        assert str(os.path.isdir(local_app_data + expect_version)) == "True"

        # Verify in coccoc://version
        from testscripts.smoketest.common import coccoc_instance
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_VERSION_URL)
        assert expect_version in self.get_flash_path(driver)
        assert expect_version in self.get_user_agent(driver)
