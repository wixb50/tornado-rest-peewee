#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from setuptools import (
    find_packages,
    setup,
)


setup(
    name='tornado_rest_peewee',
    version='1.0.0',
    description='tornado_rest_peewee',
    packages=find_packages(exclude=[]),
    author='wixb50',
    url='https://github.com/wixb50/tornado_rest_peewee.git',
    author_email='wixb50@gmail.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
    ],
)
