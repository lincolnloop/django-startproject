#!/usr/bin/env python

"""
Shows boilerplate code in the project.
TODO: Prompt so this replaces the boilerplate automatically.

"""

import os
import re
from django_startproject import settings


EXCLUDE_FILES = []
EXCLUDE_DIRS = []
BOILERPLATE = ['myproject', 'myauthor', 'mydevhost', 'myrepohost']

print "\nThe following files contain boilerplate code and should be edited."
print "=================================================================="

for word in BOILERPLATE:
    title = "Occurrences of '%s' in project_template" % word
    print
    print title
    print '-' * len(title)
    print
    
    for path, dirs, files in os.walk(settings.TEMPLATE_DIR):
        for d in dirs:
            if d in EXCLUDE_DIRS:
                dirs.remove(d)
        for f in files:
            if f in EXCLUDE_FILES:
                continue
            file_path = os.path.join(path, f)
            contents = open(file_path, 'r').read()
            bp = re.findall(word, contents)
            if bp:
                print '%2d .%s' % (len(bp),
                                   file_path[len(settings.TEMPLATE_DIR):])
