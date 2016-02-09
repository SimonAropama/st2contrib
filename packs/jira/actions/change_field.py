from lib.base import BaseJiraAction
from lib.formatters import to_comment_dict

__all__ = [
    'ChangeJiraFieldAction'
]


class ChangeJiraFieldAction(BaseJiraAction):

    def run(self, issue_key):
        issue_update = self._client.issue(issue_key)
        update_str = str('new text for environment field')
        return issue_update.update(fields={'customfield_10105':update_str })
