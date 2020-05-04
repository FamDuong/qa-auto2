import pytest


def pytest_addoption(parser):
    parser.addoption('--spreed-sheet-id', action='store',)
    parser.addoption('--sheet-name', action='store',)
    parser.addoption('--sheet-range', action='store', )
    parser.addoption('--string-verify', action='store', )
    parser.addoption('--result-range', action='store', )


@pytest.fixture
def spreed_sheet_id(request):
    spreed_sheet_id = "1SVToMOq4r4esiAP_66xjeu5ZPJsBm2E4BQz88-Srlvs"
    ##request.config.getoption("--spreed-sheet-id")
    if spreed_sheet_id is None:
        raise Exception
    return spreed_sheet_id

@pytest.fixture
def sheet_name(request):
    sheet_name = "SERP Evaluation_Mar2020"
    #request.config.getoption("--sheet-name")
    if sheet_name is None:
        raise Exception
    return sheet_name

@pytest.fixture
def sheet_range(request):
    sheet_range = "B31:B32"
        #request.config.getoption("--sheet-range")
    if sheet_range is None:
        raise Exception
    return sheet_range

@pytest.fixture
def string_verify(request):
    string_verify = "This page isn’t working,This site can’t be reached,404 Page,Lỗi 404"
        #request.config.getoption("--string-verify")
    if string_verify is None:
        raise Exception
    string_verify_values = string_verify.split(",")
    string_verify_list = []
    for each_string in string_verify_values:
        string_verify_list.append(each_string)
    return string_verify_list

@pytest.fixture
def result_col(request):
    result_col = "J"
        #request.config.getoption("--result-range")
    if result_col is None:
        raise Exception
    return result_col


