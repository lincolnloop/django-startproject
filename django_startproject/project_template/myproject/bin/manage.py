#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line

# Work out the project module name and root directory, assuming that this file
# is located at [project]/bin/manage.py
PROJECT_ROOT, PROJECT_MODULE_NAME = os.path.split(
                os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Check that the project module can be imported.
try:
    __import__(PROJECT_MODULE_NAME)
except ImportError:
    # Couldn't import the project, place it on the Python path and try again.
    sys.path.append(PROJECT_ROOT)
    try:
        __import__(PROJECT_MODULE_NAME)
    except ImportError:
        sys.stderr.write("Error: Can't import the \"%s\" project module." %
                         PROJECT_MODULE_NAME)
        sys.exit(1)

# If DJANGO_SETTINGS_MODULE doesn't exist, try to use ``[project].conf.local.settings``
# This gets overridden if settings are passed in to manage.py 
if not 'DJANGO_SETTINGS_MODULE' in os.environ:
    settings_module = '%s.conf.local.settings' % PROJECT_MODULE_NAME
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

execute_from_command_line()
