import pytest


def pytest_addoption(parser):
    parser.addoption('--spreed-sheet-id', action='store', default='1n-D7VxSBuV55Ml8JUwTHi0Iczr9yBWy-2wCkyLAoZxU')
    parser.addoption('--sheet-name', action='store', default='Sheet2')


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

