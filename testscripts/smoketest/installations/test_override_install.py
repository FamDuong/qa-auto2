from pytest_testrail.plugin import pytestrail


class TestOverrideInstall:

    @pytestrail.case('C44773')
    def test_check_install_new_version_above_old_version(self):
        from testscripts.smoketest.common import install_old_coccoc_version
        install_old_coccoc_version()
        from testscripts.smoketest.common import get_list_coccoc_version_folder_name
        old_version = get_list_coccoc_version_folder_name()[0]
        from testscripts.smoketest.common import install_coccoc_with_default
        install_coccoc_with_default()
        new_version = get_list_coccoc_version_folder_name()[0]
        from utils_automation.version import is_version_greater
        assert is_version_greater(new_version, old_version) is True





