import pytest

username = None
browser_type = None

@pytest.fixture(scope='session', autouse=True)
def get_username(request):
    global username
    username = request.config.getoption("--user")
    return username


@pytest.fixture(scope='session')
def binary_path(get_browser_type):
    if get_browser_type == "CocCoc":
        #return f"C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
        return f"C:\\Program Files (x86)\\CocCoc\\Browser\\Application\\browser.exe"
    elif get_browser_type == "Chrome":
        return f"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


@pytest.fixture(scope='session')
def default_directory(get_browser_type):
    if get_browser_type == "CocCoc":
        return f'C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\User Data'
    elif get_browser_type == "Chrome":
        return f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data'


@pytest.fixture(scope='session')
def application_path(get_browser_type):
    if get_browser_type == "CocCoc":
        #return f"C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application"   #User mode
        return f"C:\\Program Files (x86)\\CocCoc\\Browser\\Application"
    elif get_browser_type == "Chrome":
        return f"C:\\Program Files\\Google\\Chrome\\Application\\"


@pytest.fixture(scope='session')
def get_enabled_adblock_extension(request):
    return request.config.getoption("--enabled-adblock-extension", default=True)

@pytest.fixture(scope='session')
def get_browser_type(request):
    return request.config.getoption("--browser-type", default="CocCoc")

