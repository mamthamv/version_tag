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
    version='0.0.3',
    description='Tool to manage AWS Backups', 
    long_description_content_type="text/markdown",
    author='Nuvola',
    author_email='DataServicesTeam1@thomson.com',
    url='https://github.com/tr/nuvola_aws-backup-infra-cdk/',
    packages=find_packages(),
    package_data={'': ['*.config', '*.json', '*.cfg', '*.yaml']},
    include_package_data=True,
    install_requires=[
        'aws-cdk-lib==2.19.0', 
        'constructs',   
        'pyyaml',   
        'tr-aws-cdk.core==2.0.2'
    ],
    setup_requires=[
        'flake8',
        'sphinx',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
