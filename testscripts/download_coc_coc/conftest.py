import pytest


def pytest_addoption(parser):
    parser.addoption('--browsers', action='store', )
    parser.addoption('--domains', action='store', )

@pytest.fixture
def browsers(request):
    browsers = request.config.getoption('--browsers')
    if browsers is None:
        raise Exception
    browser_list = browsers.split(',')
    browser_list_return = []
    for i in browser_list:
        browser_list_return.append(i)
    return browser_list_return


@pytest.fixture
def domains(request):
    domains =request.config.getoption('--domains')
    if domains is None:
        raise Exception
    domain_list = domains.split(',')
    domain_list_return = []
    for i in domain_list:
        domain_list_return.append(i)
    return domain_list_return
