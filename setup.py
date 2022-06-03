#!/usr/bin/env python
"""
backup cdk Tool Installation
"""

import sys 

try:
    from setuptools import setup, find_packages
except ImportError:
    setup = None
    find_packages = None
    print('You need to install setuptools.')
    print('Go to https://pypi.python.org/pypi/setuptools for instructions.')
    sys.exit(1)

setup(
    name='tr-awsbackup-infra',
    version='0.0.1',
    url='https://github.com/mamthamv/version_tag.git'
)