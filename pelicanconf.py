#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Quinn Tenorio'
SITENAME = 'Quinn Tenorio'
SITETITLE = 'Quinn Tenorio'
SITESUBTITLE = 'Portfolio'
SITELOGO = '/images/quinn.jpg'
INDEX_SAVE_AS = 'blog.html'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

STATIC_PATHS = ["images", "pages"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('about', 'http://getpelican.com/'),
         ('contact', 'http://python.org/'),
         ('resume', 'http://jinja.pocoo.org/'),
         ('projects', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/qktenorio'),
          ('github', 'http://github.com/quinntenorio'),
          ('instagram', 'http://instagram.com/quinntenorio'),
          ('facebook', 'https://www.facebook.com/quinnktenorio')
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "../pelican-themes/Flex"
