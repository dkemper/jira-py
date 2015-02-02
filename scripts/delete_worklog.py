import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import lib.jira as jira


def main(issue_key, worklog_id):
    try:
        jira.Worklog.get(issue_key, worklog_id).delete()
    except jira.APIException, e:
        print e.response.status, e.response.reason
        print e.response.read()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print 'Usage: python %s [issueKey]' % __file__
        sys.exit(0)
    issueKey = sys.argv[1]
    worklog_id = raw_input('Worklog ID: ')
    main(issueKey, worklog_id)
