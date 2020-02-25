def open_browser_from_command(browser_name='chrome'):
    """
        browser_name = 'chrome', 'firefox', 'microsoft-edge:', 'iexplore'
        """
    import subprocess
    subprocess.Popen(["powershell.exe",
                      f"start {browser_name}"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)