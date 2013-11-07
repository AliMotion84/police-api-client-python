#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='police_api',
    version='0.1',
    description='Python client library for the Police API',
    author='Rock Kitchen Harris',
    packages=find_packages(),
    install_requires=[
        'requests==2.0.0',
    ],
)
