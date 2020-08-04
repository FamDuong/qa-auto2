import os

from home_made_utilities.file_utils import YamlUtils

yaml_made_utils = YamlUtils()
configuration_info = None
configuration_path = '/resources/configurations.yaml'


def get_configurations_info():
    if configuration_info is None:
        return yaml_made_utils.read_data_from_file(os.getcwd() + configuration_path)
    else:
        return configuration_info


class JenkinsConfigs:

    JENKINS_DOMAIN = get_configurations_info()['jenkins']['domain']
    JENKINS_ADMIN_USERNAME = get_configurations_info()['jenkins']['admin_username']
    JENKINS_ADMIN_PASSWORD = get_configurations_info()['jenkins']['admin_password']


class CocCocConfigs:
    COCCOC_DEV_VERSION = get_configurations_info()['coccoc_dev_version']

    @staticmethod
    def update_coccoc_dev_version(coccoc_version):
        data = get_configurations_info()
        data['coccoc_dev_version'] = coccoc_version
        return yaml_made_utils.write_data_to_file(data, os.getcwd() + configuration_path)



