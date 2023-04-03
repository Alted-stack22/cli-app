#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from setuptools import setup


setup(
    name='pv',
    version='1.0',
    py_modules=['pv'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    '''
)
