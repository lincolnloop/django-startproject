#!/usr/bin/env python

"""
Shows boilerplate code in the project.
TODO: Prompt so this replaces the boilerplate automatically.

"""

import os
import re

ROOT = os.path.dirname(os.path.realpath(__file__))
EXCLUDE_FILES = ['show_boilerplate.py']
EXCLUDE_DIRS = ['.git', '_build']
BOILERPLATE = ['myproject', 'myauthor', 'mydevhost', 'myrepohost']

print "\nThe following files contain boilerplate code and should be edited."
print "=================================================================="

for word in BOILERPLATE:
    print "\nOccurences of '%s' in startproject" % word
    print '-' * (32 + len(word)) + '\n'
    
    for path, dirs, files in os.walk(ROOT):
        for d in dirs:
            if d in EXCLUDE_DIRS:
                dirs.remove(d)
        for f in files:
            if f not in EXCLUDE_FILES:
                file_path = os.path.join(path, f)
                contents = open(file_path, 'rb').read()
                bp = re.findall(word, contents)
                if bp:
                    print len(bp), file_path.replace(ROOT, '.')
