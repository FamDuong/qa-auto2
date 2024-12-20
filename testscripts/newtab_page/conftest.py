import pytest


def pytest_addoption(parser):
    parser.addoption('--newtab-url', action='store', )


@pytest.fixture(scope='class')
def get_newtab_url(request):
    newtab_url = request.config.getoption("--newtab-url")
    if newtab_url is not None:
        newtab_url_values = newtab_url.split(",")
        newtab_url_list = []
        for each_url in newtab_url_values:
            newtab_url_list.append(each_url)
        return newtab_url_list
    else:
        return None
