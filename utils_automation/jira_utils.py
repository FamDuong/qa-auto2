from jira import JIRA


class JiraUtils:

    @staticmethod
    def access_jira():
        options = {'server': 'https://coccoc.atlassian.net'}
        return JIRA(options=options, basic_auth=('cuongld@coccoc.com', 'R6AX8lkxgzyhxCua94S2C9F8'))

    def add_comment(self, jira_issue, comment_content):
        self.access_jira().add_comment(jira_issue, comment_content)

