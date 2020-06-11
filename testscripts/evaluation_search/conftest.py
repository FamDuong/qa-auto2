import pytest


def pytest_addoption(parser):
    parser.addoption('--spreed-sheet-id', action='store', )
    parser.addoption('--sheet-name', action='store', )
    parser.addoption('--sheet-range', action='store', )
    parser.addoption('--string-verify', action='store', )
    parser.addoption('--result-col-coccoc', action='store', )
    parser.addoption('--result-col-google', action='store', )


@pytest.fixture
def spreed_sheet_id(request):
    spreed_sheet_id = request.config.getoption("--spreed-sheet-id")
    if spreed_sheet_id is None:
        raise Exception
    return spreed_sheet_id


@pytest.fixture
def sheet_name(request):
    sheet_name = request.config.getoption("--sheet-name")
    if sheet_name is None:
        raise Exception
    return sheet_name


@pytest.fixture
def sheet_range(request):
    sheet_range = request.config.getoption("--sheet-range")
    if sheet_range is None:
        raise Exception
    return sheet_range


@pytest.fixture
def string_verify(request):
    string_verify = request.config.getoption("--string-verify")
    if string_verify is None:
        raise Exception
    string_verify_values = string_verify.split(",")
    string_verify_list = []
    for each_string in string_verify_values:
        string_verify_list.append(each_string)
    return string_verify_list


@pytest.fixture
def result_col_coccoc(request):
    result_col_coccoc = request.config.getoption("--result-col-coccoc")
    if result_col_coccoc is None:
        raise Exception
    return result_col_coccoc


@pytest.fixture
def result_col_google(request):
    result_col_google = request.config.getoption("--result-col-google")
    if result_col_google is None:
        raise Exception
    return result_col_google
