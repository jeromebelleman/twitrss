#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

setup(
    name='twitrss',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://jeromebelleman.gitlab.io',
    description="Tweet from RSS feeds",
    long_description="Tweet from RSS feeds and shorten posts if needs be.",
    scripts=['twitrss'],
)
