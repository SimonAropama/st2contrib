
from lib.base import BaseJiraAction
from lib.formatters import to_issue_dict
 
__all__ = [
    'DoJiraTransitionAction'
]
 
 
class DoJiraTransitionAction(BaseJiraAction):
 
    def run(self, type, issue_number=None):
 
        data = {
            'issuetype': {'name': type}
        }
 
        issue = self._client.issue(issue_number)
        self._client.transition_issue(issue.key, '21')
        result = to_issue_dict(issue)
        return result
