#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Josh Langsfeld'
SITENAME = 'Josh Langsfeld - UMD'
SITEURL = 'http://terpconnect.umd.edu/~jdlangs'
THEME = 'themes/pelican-sober'

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Sidebar info
PELICAN_SOBER_ABOUT = 'Site of Josh Langsfeld'
SOCIAL = (
    ('github/phobon', 'https://github.com/phobon'),
)
LINKS = (
    ('UMD', 'http://www.umd.edu/'),
    ('Maryland Robotics Center', 'http://www.robotics.umd.edu/'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
