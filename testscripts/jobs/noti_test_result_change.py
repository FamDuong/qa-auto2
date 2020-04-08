from config.credentials import SKYPE_GROUP_AUTOMATION_ID
from enums.testrail import TestResultStatus
from utils_automation.jira_utils import JiraUtils
from utils_automation.skype_utils import SkypeLocalUtils
from utils_automation.testrail_utils import TestrailUtils

test_rail_utils = TestrailUtils()
jira_utils = JiraUtils()
skype_utils = SkypeLocalUtils()


def get_test_run_name(run_id):
    return test_rail_utils.get_test_run_info(run_id).get('name')


def define_message_content(run_id):
    # run_name = get_test_run_name(run_id)
    # message_intro = f"The test result for {run_name} has been changed as following: \n"
    test_id_result_change_list = test_rail_utils.get_test_id_has_result_change(run_id=run_id)
    message_content_to_send = ""
    for each_test_id in test_id_result_change_list:
        each_test_id_statuses = test_rail_utils.get_status_id_from_test_id(each_test_id)
        test_id_title = test_rail_utils.get_test_id_info(each_test_id).get('title')
        old_status = each_test_id_statuses[1]
        old_status_name = None
        new_status = each_test_id_statuses[0]
        new_status_name = None
        for each in TestResultStatus:
            if old_status == each.value:
                old_status_name = each.name
            if new_status == each.value:
                new_status_name = each.name
        message_content_to_send += f"Test case {test_id_title} has been changed from {old_status_name} to {new_status_name} \n"
    return message_content_to_send


def send_message_skype(message_skype_content):
    skype_utils.send_message_group_skype(SKYPE_GROUP_AUTOMATION_ID, message_skype_content)


def modify_jira_issue(issue_id, comment_jira_content):
    jira_utils.add_comment_jira(issue_id=issue_id, comment_content=comment_jira_content)


def test_run_noti_test_result_change(run_id_testrail, jira_issue_id,):
    run_id = run_id_testrail
    jira_issue_id = jira_issue_id
    is_result_changed = test_rail_utils.check_if_any_result_change(run_id)
    if is_result_changed is True:
        message_content_to_send = define_message_content(run_id)
        send_message_skype(message_content_to_send)
        modify_jira_issue(issue_id=jira_issue_id, comment_jira_content=message_content_to_send)
    else:
        pass


