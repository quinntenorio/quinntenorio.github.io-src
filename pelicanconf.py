#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Quinn Tenorio'
SITENAME = 'Quinn Tenorio'
SITETITLE = 'Quinn Tenorio'
SITESUBTITLE = 'Senior in Computer Science @ CO School of Mines\nHuge computer nerd and a native'
SITELOGO = '/images/quinn.jpg'
FAVICON = '/images/favicon.ico'
INDEX_SAVE_AS = 'blog.html'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

STATIC_PATHS = ["images", "pages", "static"]

COPYRIGHT_YEAR = '2018'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa',
}

ARTICLE_URL = 'blog/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{category}/{slug}.html'
DISABLE_URL_HASH = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGES_SORT_ATTRIBUTE = 'date'

# Blogroll
LINKS = (('blog', '/blog.html'),
        )

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/qktenorio'),
          ('github', 'https://github.com/quinntenorio'),
          ('instagram', 'https://instagram.com/quinntenorio'),
          ('facebook', 'https://www.facebook.com/quinnktenorio')
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "../pelican-themes/Flex"
