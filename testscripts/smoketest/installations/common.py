def open_browser_from_command(browser_name='chrome'):
    """
        browser_name = 'chrome', 'firefox', 'microsoft-edge:', 'iexplore'
        """
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"start {browser_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def check_task_scheduler(task_name):
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"Get-ScheduledTask -TaskName {task_name} | Get-ScheduledTaskInfo"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    tasks = str(p.communicate()[0])
    return tasks