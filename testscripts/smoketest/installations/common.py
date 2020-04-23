from utils_automation.common import WindowsCMD


def open_browser_from_command(browser_name='chrome'):
    """
        browser_name = 'chrome', 'firefox', 'microsoft-edge:', 'iexplore'
        """
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"start {browser_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def check_task_scheduler(task_name):
    list_start_up_apps = WindowsCMD.execute_cmd("schtasks /query /fo CSV | findstr "+task_name)
    return str(list_start_up_apps)
