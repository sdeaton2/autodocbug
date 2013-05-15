#!/usr/bin/env python

import os
import sys

# For debugging output, both of these lines are needed:
#import httplib2
#httplib2.debuglevel = 1

#import launchpadlib
# ..not sure why, but this print only works if you import as above.
#print launchpadlib.__version__
from launchpadlib.launchpad import Launchpad

# vars for later use
homedir = os.getenv("HOME")
#print "User home directory: %s" % homedir
cachedir = homedir + "/.launchpadlib/cache/"
#print "Cache directory: %s" % cachedir

# connect to launchpad (auth, etc.)
launchpad = Launchpad.login_with('autodocbug', 'staging')
#launchpad = Launchpad.login_with('autodocbug', 'production')

# get list of bugs on page

# loop through list of bugs, checking for #DocImpact flag

# operate on #DocImpact flag, creating new doc bug.
