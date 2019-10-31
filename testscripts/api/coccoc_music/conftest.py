import pytest

from utils_automation.const import SkypeGroupIds
from utils_automation.jira_utils import JiraUtils
from utils_automation.skype_utils import SkypeLocalUtils

jira_utils = JiraUtils()
skype_utils = SkypeLocalUtils()

total_test_failed = 0
jira_issue = 'QA-470'


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    global total_test_failed
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        total_test_failed += 1


@pytest.fixture(scope='session', autouse=True)
def update_result_jira_skype():
    yield
    jira_utils.add_comment(jira_issue, comment_for_jira_skype(total_test_failed))
    skype_utils.send_message_group_skype(SkypeGroupIds.TEST_GROUP_ID, comment_for_jira_skype(total_test_failed))


def comment_for_jira_skype(total_failed):
    general_comment = "\nThis is result for checking CocCoc Music API to return list of playlists"
    if total_failed > 0:
        failed_comment = f"\nTest result is FAILED\nTotal test failed is :{total_failed}" \
                             f"\nPlease check test run with ID=2358 in test rail" \
                             f"and jenkins job for api test for details"
        return general_comment + failed_comment
    elif total_failed == 0:
        success_comment = "\nTest result is SUCCESS"
        return general_comment + success_comment
    #
    # elif total_test_failed == 0:
    #     jira_utils.add_comment(jira_issue, comment_for_jira_skype(total_test_failed))

