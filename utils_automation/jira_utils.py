from jira import JIRA

from config.credentials import ATLASSIAN_BOT_ACCOUNT_NAME, ATLASSIAN_BOT_PASSWORD
from config.path import COCCOC_ATLASSIAN_DOMAIN


class JiraUtils:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(JiraUtils, cls).__new__(cls)

        return cls.instance

    @staticmethod
    def access_jira():
        options = {'server': COCCOC_ATLASSIAN_DOMAIN}
        return JIRA(options=options, basic_auth=(ATLASSIAN_BOT_ACCOUNT_NAME, ATLASSIAN_BOT_PASSWORD))

    def __init__(self):
        self.jira = self.access_jira()

    def __enter__(self):
        yield self

    def add_comment_jira(self, issue_id, comment_content):
        self.jira.add_comment(issue_id,comment_content)

    """
    Status of the issue in jira
    [('11', 'Backlog'), ('21', 'Selected for Development'), ('31', 'In Progress'), ('41', 'Done')]
    """
    def change_status(self, issue_id, status=None):
        issue = self.jira.issue(issue_id)
        self.jira.transition_issue(issue, transition=status)

    def get_issue_info(self, issue_id):
        return self.jira.issue(id=issue_id).raw

    def get_issue_status(self, issue_id):
        raw_issue_dict = self.get_issue_info(issue_id=issue_id)
        return str(raw_issue_dict['fields']['status']['name']).upper()

    def get_all_projects(self):
        return self.jira.projects()

    def get_project_info(self, project_id):
        return self.jira.project(id=project_id)


