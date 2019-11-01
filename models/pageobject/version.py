import os
from models.pageelements.version import VersionPageElements
from models.pageobject.basepage_object import BasePageObject
from os import path
import pytest


class VersionPageObject(BasePageObject):
    version_element = VersionPageElements()

    def get_profile_path(self, driver):
        profile_path_elem = self.version_element.find_profile_path_element(driver)
        return profile_path_elem.text

    def get_flash_path(self, driver):
        flash_path = self.version_element.find_flash_path_element(driver)
        return flash_path.text

    def verify_version_is_correct(self, expect_version):
        localappdata = path.expandvars(r'%LOCALAPPDATA%\CocCoc\Browser\Application\\')
        assert str(os.path.isdir(localappdata + expect_version)) == "True"



