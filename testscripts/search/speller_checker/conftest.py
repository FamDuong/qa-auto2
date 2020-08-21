import pytest


def pytest_addoption(parser):
    parser.addoption('--sheet-range-input', action='store', default='A2:A44')
    parser.addoption('--sheet-range-expect', action='store', default='B2:B44')
    parser.addoption('--result-col-error', action='store', default='D')
    parser.addoption('--result-col-actual-string', action='store', default='E')
    parser.addoption('--result-col-expect-string-diff', action='store', default='H')
    parser.addoption('--result-col-actual-string-diff', action='store', default='I')


@pytest.fixture
def get_sheet_range_input(request):
    sheet_range = request.config.getoption("--sheet-range-input")
    if sheet_range is None:
        raise Exception
    return sheet_range


@pytest.fixture
def get_sheet_range_expect(request):
    sheet_range_expect = request.config.getoption("--sheet-range-expect")
    if sheet_range_expect is None:
        raise Exception
    return sheet_range_expect


@pytest.fixture
def get_result_col_error(request):
    result_col_error = request.config.getoption("--result-col-error")
    if result_col_error is None:
        raise Exception
    return result_col_error


@pytest.fixture
def get_result_col_actual_string(request):
    result_col_actual_string = request.config.getoption("--result-col-actual-string")
    if result_col_actual_string is None:
        raise Exception
    return result_col_actual_string


@pytest.fixture
def get_result_col_expect_string_diff(request):
    result_col_expect_string_diff = request.config.getoption("--result-col-expect-string-diff")
    if result_col_expect_string_diff is None:
        raise Exception
    return result_col_expect_string_diff


@pytest.fixture
def get_result_col_actual_string_diff(request):
    result_col_actual_string_diff = request.config.getoption("--result-col-actual-string-diff")
    if result_col_actual_string_diff is None:
        raise Exception
    return result_col_actual_string_diff
