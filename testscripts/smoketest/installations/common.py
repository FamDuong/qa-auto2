import utils_automation.common
import utils_automation.common_browser
from utils_automation.common import WindowsCMD
import testscripts.smoketest.common as common


def open_browser_from_command(browser_name='chrome'):
    """
        browser_name = 'chrome', 'firefox', 'microsoft-edge:', 'iexplore'
        """
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"start {browser_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def check_task_scheduler(task_name):
    list_start_up_apps = WindowsCMD.execute_cmd("schtasks /query /fo CSV | findstr " + task_name)
    return str(list_start_up_apps)


def install_coc_coc(coc_coc_installer, language, is_needed_clean_up=True):
    if is_needed_clean_up is True:
        utils_automation.common_browser.cleanup()
    else:
        pass
    common.uninstall_old_version_remove_local_app()
    common.install_coccoc_installer_from_path(coc_coc_installer, language)
