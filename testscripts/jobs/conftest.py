import pytest


def pytest_addoption(parser):
    parser.addoption('--testrail-run-id', action='store',)
    parser.addoption('--jira-issue-id', action='store',)


@pytest.fixture
def run_id_testrail(request):
    run_id = request.config.getoption("--testrail-run-id")
    if run_id is None:
        raise Exception
    run_id_list = run_id.split(',')
    run_id_list_int = []
    for each_id in run_id_list:
        run_id_list_int.append(int(each_id))
    return run_id_list_int


@pytest.fixture
def jira_issue_id(request):
    issue_id = request.config.getoption("--jira-issue-id")
    if issue_id is None:
        raise Exception
    return str(issue_id)



