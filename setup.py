#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages


def read_requirements(filename):
    """Returns requirements specs from file with given 'filename'
    as list."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


setup(
    name="python_project_template",
    author="Andrei Pashkin",
    author_email="andrew.pashkin@gmx.co.uk",
    packages=find_packages(where='src', include=[]),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=read_requirements('requirements.txt'),
)
