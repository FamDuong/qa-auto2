import pytest

username = None


@pytest.fixture(scope='session', autouse=True)
def get_username(request):
    global username
    username = request.config.getoption("--user")
    return username


@pytest.fixture(scope='session')
def binary_path():
    return f'C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe'


@pytest.fixture(scope='session')
def default_directory():
    return f'C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\User Data'


@pytest.fixture(scope='session')
def application_path():
    return f"C:\\Users\\{username}\\AppData\\Local\\CocCoc\\Browser\\Application"




