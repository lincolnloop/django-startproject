#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='myproject',
      version='0.1',
      packages=find_packages(),
      package_data={'myproject': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'myproject': ['bin/*.pyc']},
      scripts=['myproject/bin/manage.py'])
