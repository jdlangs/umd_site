#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Josh Langsfeld'
SITENAME = 'Josh Langsfeld'
SITEURL = ''
THEME = 'themes/pelican-sober'

PATH = 'content'
RELATIVE_URLS = True

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Sidebar info
PELICAN_SOBER_ABOUT = """
jdlangs&#64;<span style="display:none">unknown</span>umd&#46;edu<br>
<br>2181 Glenn L. Martin Hall, Building 088<br>
University of Maryland<br>
College Park, MD 20742<br>
<br>301-405-6572<br>
"""
PELICAN_SOBER_STICKY_SIDEBAR = True

SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/pub/josh-langsfeld/31/287/807'),
    ('github', 'https://github.com/jdlangs'),
    ('google+', 'https://plus.google.com/+JoshLangsfeld'),
)
LINKS = (
    ('UMD', 'http://www.umd.edu/'),
    ('Maryland Robotics Center', 'http://www.robotics.umd.edu/'),
)

DEFAULT_PAGINATION = False
STATIC_PATHS = ['images', 'files']
