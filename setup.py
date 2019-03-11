#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "cave-dianping",
    version = "0.0.1",
    keywords = ("pip", "dianping","大众点评","爬虫"),
    description = "dianping base class. 大众点评 爬虫 基础",
    long_description = "dianping base class. 大众点评 爬虫 基础",
    license = "MIT Licence",

    url = "https://github.com/lastcaveman/dianping",     
    author = "lastcaveman",
    author_email = "caveman.last@gmail.com",

    py_modules=['dianping'],
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests","configparser"]
)
