
# Jira-py

A lightweight python client for the [Jira REST API](http://docs.atlassian.com/jira/REST/latest/). 

# Prerequisites

You'll need python 2.7 and [pip](http://pypi.python.org/pypi/pip/) installed.

# Try it out

Clone the repo, and run:

	pip install -r requirements.txt

This will pull in the dependencies for the library. Once this is done, run:

	scripts/mine

This will prompt for your username, password and jira host, and list all the issues currently assigned to you, in order that they were last updated. If you'd rather override this with a custom query, just add it as the argument onto the script:

	scripts/mine "assignee = currentUser() and status = Open"

Choose an issue key and run:

	scripts/comments [issueKey]

This will list all the comments on that issue. To add a comment, use:

	scripts/add_comment [issueKey]

Your `$EDITOR` will be opened to create the comment. If you save and close the temp file, the comment will be added. If not, the addition will be skipped.

To jump to the issue in a web browser, run:

	scripts/jumpto [issueKey]

This will open the issue in your default browser. You might need to log in again.

There's also `scripts/search`, `scripts/edit_comment`, `scripts/delete_comment`, and `scripts/transition` for you to try out, they should be self-explanatory. Run them without any arguments to get usage details. Have a look at the API and you can probably easily extend it to do other things.

# Credentials

Credentials are stored in a plain-text config file in `.jira.cfg` with `600` permissions, so they can only be read by you (similar to the approach that the `svn` command line client takes).

If you need to change the credentials or API details, just remove the `.jira.cfg` file and next time you run a query you will be prompted to update it.

If you need to connect to multiple jira instances, it's probably easiest just to copy the cloned repo to another directory and run the second copy with your different credentials. 

# Color-coding statuses

You can add a `colors` section in your `.jira.cfg` containing a mapping of statuses to colors. Any of the available [termcolor](http://pypi.python.org/pypi/termcolor/) colors is valid. A default color coding will be generated when the `.jira.cfg` is first created, which you can add to to customise the colors.

# API

The main API is in `lib/jira.py`. You can read the [annotated source code](http://pranavraja.github.com/jira-py/docs/jira.html). Note that the API will probably change around a lot as I just started this.

# Running the tests

To run the tests, you'll need to install [nose](http://pypi.python.org/pypi/nose) and [mock](http://pypi.python.org/pypi/mock). Easiest way to do this is through pip, e.g. `sudo pip install mock nose`

After installing the prerequisites, clone the repo and run:

	nosetests
