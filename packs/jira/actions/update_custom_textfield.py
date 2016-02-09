from lib.base import BaseJiraAction
from lib.formatters import to_comment_dict
import re
 
__all__ = [
    'UpdateJiraiTextFieldAction'
]
 
 
class UpdateJiraTextFieldAction(BaseJiraAction):
 
    def run(self, issue_key, custom_field, comment_text, territory):
        custom_field_dict = {'Environment':'customfield_10105','Build Progress':'customfield_10200'}
        issue = self._client.issue(issue_key)
        
        current_comments = ""
        update_text = ""
        if (issue.fields.customfield_10200):
          current_comments = issue.fields.customfield_10200
        
        comment_text = territory + ": " + comment_text + chr(13) + chr(10)
        
        if (current_comments.find(territory) >= 0): 
#        need to use regular expression to replace whole territory comment
         match_string = territory + ".*?" + chr(10) 
         current_comments = re.sub(match_string,comment_text,current_comments)
        else: 
         current_comments = current_comments + comment_text

        result = issue.update(fields={custom_field_dict[custom_field]:current_comments})
        return result
