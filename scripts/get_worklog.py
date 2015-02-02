import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import lib.jira as jira
import json
from termcolor import colored

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print 'Usage: python %s [issue_key]' % __file__
        sys.exit(0)
    issue_key = sys.argv[1]
    try:
        worklogs = jira.Worklog.get_by_issue(issue_key)
    except jira.APIException, e:
        print e.response.status, e.response.reason
        print e.response.read()
    for worklog in worklogs:
        print '%s %s:\n  %s' % (
        colored('#%s' % worklog.id, 'cyan'), colored(worklog.author, 'magenta'), worklog.comment.replace('\n', '\n  '))

