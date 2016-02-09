from lib.base import BaseJiraAction
from lib.formatters import to_comment_dict
import re
 
__all__ = [
    'SearchJiraAction'
]
 
 
class SearchJiraAction(BaseJiraAction):
 
    def run(self, issue_type):

     jql_query = 'project="TT" AND issuetype="Task"'
     all_issues = self._client.search_issues(jql_query, maxResults=None)

     for issue_key in all_issues:
       print issue_key.key
