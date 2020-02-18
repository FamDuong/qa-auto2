from pytest_testrail.plugin import pytestrail


class TestImportDataWhileInstalling:

    """
    browser_name = 'chrome', 'firefox', 'microsoft-edge:', 'iexplore'
    """

    def open_browser_from_command(self, browser_name='chrome'):
        import subprocess
        subprocess.Popen(["powershell.exe",
                          f"start {browser_name}"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    @pytestrail.case('C44825')
    def test_import_data_from_chrome(self):
        from testscripts.smoketest.common import change_default_browser
        change_default_browser('Google Chrome')
        self.open_browser_from_command(browser_name='chrome')
        from testscripts.smoketest.common import install_coccoc_with_default
        install_coccoc_with_default(is_needed_clean_up=False, is_needed_clear_user_data=True)
        a = 5





