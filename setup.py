#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 18:20
# @Author  : Tony Tian
# @Email   : tiantangtl@foxmail.com
# @File    : setup.py

from setuptools import setup, find_packages

setup(
    name='logutils',
    version='1.0',
    description='some utils to deal with log files.',
    author='Tony Tian',
    author_email='tiantangtl@foxmail.com',
    platforms='python 3.6',
    url='www.devsave.com',
    install_requires=[
        'PyQt5>=5.11.1'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    package_data={
        '': ['/commands/*.bat'],
    }
)
