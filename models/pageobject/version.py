from models.pageelements.version import VersionPageElements
from models.pageobject.basepage_object import BasePageObject


class VersionPageObject(BasePageObject):
    version_element = VersionPageElements()

    def get_profile_path(self, driver):
        profile_path_elem = self.version_element.find_profile_path_element(driver)
        return profile_path_elem.text


