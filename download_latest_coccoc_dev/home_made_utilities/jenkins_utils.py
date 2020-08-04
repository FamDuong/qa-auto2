import jenkins


class JenkinsCommon:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(JenkinsCommon, cls).__new__(cls)

        return cls.instance

    def jenkins_access(self):
        from configs.yaml_configs import JenkinsConfigs
        return jenkins.Jenkins(JenkinsConfigs.JENKINS_DOMAIN, JenkinsConfigs.JENKINS_ADMIN_USERNAME
                               , JenkinsConfigs.JENKINS_ADMIN_PASSWORD)