#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Yodiwo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'enum34==1.1.6',
        'paho-mqtt==1.3.1'
    ]
)