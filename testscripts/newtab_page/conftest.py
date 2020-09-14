import pytest


def pytest_addoption(parser):
    parser.addoption('--newtab-url', action='store', default='Sheet2')


@pytest.fixture(scope='class')
def get_newtab_url(request):
    newtab_url = request.config.getoption("--newtab-url")
    if newtab_url is None:
        raise Exception
    return newtab_url