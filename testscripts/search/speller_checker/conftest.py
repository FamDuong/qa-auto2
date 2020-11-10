import pytest


def pytest_addoption(parser):
    parser.addoption('--sheet-range-input', action='store', default='A2:C44')


@pytest.fixture
def get_sheet_range_input(request):
    sheet_range = request.config.getoption("--sheet-range-input")
    if sheet_range is None:
        raise Exception
    return sheet_range
