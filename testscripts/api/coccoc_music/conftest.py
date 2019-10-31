import pytest

from utils_automation.const import SkypeGroupIds
from utils_automation.jira_utils import JiraUtils
from utils_automation.skype_utils import SkypeLocalUtils

jira_utils = JiraUtils()
skype_utils = SkypeLocalUtils()


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    total_test_failed = 0

    def comment_for_jira_skype():
        general_comment = "\nThis is result for checking CocCoc Music API to return list of playlists"
        if total_test_failed > 0:
            failed_comment = f"\nTest result is FAILED\nTotal test failed is :{total_test_failed}" \
                             f"\nPlease check test run with ID=2358 in test rail" \
                             f"and jenkins job for api test for details"
            return general_comment + failed_comment
        elif total_test_failed == 0:
            success_comment = "\nTest result is SUCCESS"
            return general_comment + success_comment

    if report.when == 'call' and report.failed:
        total_test_failed += 1
    if total_test_failed > 0:
        jira_utils.add_comment('QA-469', comment_for_jira_skype())
        skype_utils.send_message_group_skype(SkypeGroupIds.COCCOC_MUSIC_GROUP_ID,comment_for_jira_skype())
    else:
        jira_utils.add_comment('QA-469', comment_for_jira_skype())

