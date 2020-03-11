import pytest
from pytest_testrail.plugin import pytestrail


class TestUnInstallations:

    @pytestrail.case('C9440')
    @pytestrail.defect('BR-1278')
    @pytest.mark.usefixtures('install_coccoc_after_finish_test')
    def test_uninstall_coccoc_browser_successfully_without_clear_user_data(self):
        from testscripts.smoketest.common import uninstall_coccoc_without_delete_user_data
        uninstall_coccoc_without_delete_user_data()
        from testscripts.smoketest.common import cleanup
        cleanup(firefox=False)
        # from testscripts.smoketest.installations.common import check_task_scheduler
        import time
        time.sleep(5)
        # coccoc_update_tasks = check_task_scheduler(task_name="CocCoc*")
        # import re
        from utils_automation.common import FilesHandle
        file = FilesHandle()
        # assert len(re.findall('CocCocUpdateTaskUser.*Core', coccoc_update_tasks)) == 0
        # assert len(re.findall('CocCocUpdateTaskUser.*UA', coccoc_update_tasks)) == 0
        assert file.is_subfolder_exist_in_folder(r'CrashReports', file.localappdata) is True
        assert file.is_subfolder_exist_in_folder(r'Browser\User Data', file.localappdata) is True
        assert file.is_file_exist_in_folder(r'uid', file.appdata) is True








