from utils_automation.testrail_utils import TestrailUtils

test_rail_utils = TestrailUtils()


def get_test_plan_name(plan_id):
    return test_rail_utils.get_test_plan_info(plan_id).get('name')


def get_test_run_config(run_id):
    return test_rail_utils.get_test_run_info(run_id).get('config')


def get_test_run_config(run_id):
    return test_rail_utils.get_test_run_info(run_id).get('config')


def get_test_run_passed_count(run_id):
    return test_rail_utils.get_test_run_info(run_id).get('passed_count')


def get_test_run_untested_count(run_id):
    return test_rail_utils.get_test_run_info(run_id).get('untested_count')


def get_test_run_failed_count(run_id):
    return test_rail_utils.get_test_run_info(run_id).get('failed_count')


def define_messsage_content(plan_id, plan_name, run_id, test_run_config, failed_count, passed_count,
                            untested_count, total_cases):
    message_content_to_send = f"(hearteyesrobot)(hearteyesrobot)(hearteyesrobot) SMOKE TEST RESULT (hearteyesrobot)(" \
                              f"hearteyesrobot)(hearteyesrobot)" \
                              f"\nhttp://testrail.coccoc.com/index.php?/plans/view/{plan_id} - {plan_name}" \
                              f"\n\thttp://testrail.coccoc.com/index.php?/runs/view/{run_id} - {test_run_config}:" \
                              f"\n\t\t(crossmark) {failed_count} failed/ {total_cases} cases" \
                              f"\n\t\t(checkmark) {passed_count} passed/ {total_cases} cases" \
                              f"\n\t\t(heartblack) {untested_count} untested/ {total_cases} cases \n"
    return message_content_to_send


def noti_smoke_test_result(run_id):
    plan_id = test_rail_utils.get_test_run_info(run_id).get('plan_id')
    plan_name = get_test_plan_name(plan_id)
    list_of_test_ids = test_rail_utils.get_test_ids_from_run_id(run_id=run_id)
    total_cases = str(len(list_of_test_ids))
    test_run_config = get_test_run_config(run_id)
    passed_count = get_test_run_passed_count(run_id)
    untested_count = get_test_run_untested_count(run_id)
    failed_count = get_test_run_failed_count(run_id)
    message_content_to_send = define_messsage_content(plan_id, plan_name, run_id, test_run_config,
                                                      failed_count, passed_count,
                                                      untested_count, total_cases)
    from testscripts.jobs.noti_test_result_change import send_message_skype
    send_message_skype(message_content_to_send)


def test_noti_smoke_test_result(run_id_testrail):
    run_id_list = run_id_testrail
    for run_id in run_id_list:
        noti_smoke_test_result(run_id)
