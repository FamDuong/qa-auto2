import pytest


def pytest_addoption(parser):
    parser.addoption('--spreed-sheet-id', action='store', default='1n-D7VxSBuV55Ml8JUwTHi0Iczr9yBWy-2wCkyLAoZxU')
    parser.addoption('--sheet-name', action='store', default='Sheet 2')
    parser.addoption('--test-url', action='store', default='https://coccoc.com/search?query=chinh%20ta')


@pytest.fixture
def get_spreed_sheet_id(request):
    spreed_sheet_id = request.config.getoption("--spreed-sheet-id")
    if spreed_sheet_id is None:
        raise Exception
    return spreed_sheet_id


@pytest.fixture
def get_sheet_name(request):
    sheet_name = request.config.getoption("--sheet-name")
    if sheet_name is None:
        raise Exception
    return sheet_name


@pytest.fixture
def get_test_url(request):
    test_url = request.config.getoption("--test-url")
    if test_url is None:
        raise Exception
    return test_url
