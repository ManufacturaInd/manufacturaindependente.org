#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Manufactura Independente'
SITENAME = u'Manufactura Independente'
SITESUBTITLE = "Libre Graphics & Design research studio"
SITEURL = 'http://manufacturaindependente.org'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Specify a customized theme, via path relative to the settings file
THEME = 'theme/manufactura'

SITE_DESCRIPTION = 'Manufactura, Libre Graphics Design & Research Studio.'

SITE_LOGO = '/theme/images/manufactura.png'


ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'


#COVER_IMG_URL = 'theme/images/cutis.jpg'
#PROFILE_IMAGE_URL =  'theme/images/cutis.jpg'
#TAGLINE = 'A Manufactura é que é.'
#SOCIAL = (
#            ('github', 'https://github.com/manufacturaind/'),
#            ('twitter-square', 'https://twitter.com/manufacturaind'),
#         )
