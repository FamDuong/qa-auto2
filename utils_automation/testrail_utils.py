from testrail_api import TestRailAPI

from config.testrail import TESTRAIL_DOMAIN_URL, TESTRAIL_USERNAME, TESTRAIL_PASSWORD


class TestrailUtils:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(TestrailUtils, cls).__new__(cls)

        return cls.instance

    @staticmethod
    def access_testrail():
        return TestRailAPI(TESTRAIL_DOMAIN_URL, TESTRAIL_USERNAME, TESTRAIL_PASSWORD)

    def __init__(self):
        self.testrail = self.access_testrail()

    def get_test_ids_from_run_id(self, run_id):
        list_of_test_ids = []
        for each_test in self.testrail.tests.get_tests(run_id=run_id):
            list_of_test_ids.append(each_test.get('id'))
        return list_of_test_ids

    def get_test_run_info(self, run_id):
        return self.testrail.runs.get_run(run_id=run_id)

    def get_test_id_info(self, test_id):
        return self.testrail.tests.get_test(test_id=test_id)

    def get_status_id_from_test_id(self, test_id):
        results = self.testrail.results.get_results(test_id=test_id)
        results_status = []
        for each in results:
            results_status.append(each.get('status_id'))
        return results_status

    def check_if_any_result_change(self, run_id):
        list_of_test_ids = self.get_test_ids_from_run_id(run_id=run_id)
        for each_test_id in list_of_test_ids:
            results_status = self.get_status_id_from_test_id(each_test_id)
            if results_status[0] != results_status[1]:
                return True
        return False

    def get_test_id_has_result_change(self, run_id):
        test_id_result_change = []
        list_of_test_ids = self.get_test_ids_from_run_id(run_id=run_id)
        for each_test_id in list_of_test_ids:
            results_status_last_2_times = self.get_status_id_from_test_id(each_test_id)[0:2]
            if results_status_last_2_times[0] != results_status_last_2_times[1]:
                test_id_result_change.append(each_test_id)
        return test_id_result_change









