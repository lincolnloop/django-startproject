#!/usr/bin/env python

"""
Shows boilerplate code in the project.
TODO: Prompt so this replaces the boilerplate automatically.

"""

import os
import re

ROOT = os.path.dirname(os.path.realpath(__file__))
EXCLUDE = ['show_boilerplate.py']
BOILERPLATE = ['myproject', 'mydevhost', 'myrepohost']

print "\nThe following files contain boilerplate code and should be edited."
print "=================================================================="

for word in BOILERPLATE:
    print "\nOccurences of '%s' in startproject" % word
    print '-' * (32 + len(word)) + '\n'
    
    for path, dirs, files in os.walk(ROOT):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            if f not in EXCLUDE:
                file_path = os.path.join(path, f)
                contents = open(file_path, 'rb').read()
                bp = re.findall(word, contents)
                if bp:
                    print len(bp), file_path.replace(ROOT, '.')
