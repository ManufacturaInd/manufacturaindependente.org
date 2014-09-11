#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Manufactura Independente'
SITENAME = u'Manufactura Independente'
SITEURL = 'http://manufacturaindependente.org'

PATH = 'content'

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

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Specify a customized theme, via path relative to the settings file
THEME = 'themes/pure-single'

COVER_IMG_URL = 'themes/pure-single/static/img/cutis.jpg'
PROFILE_IMAGE_URL =  'themes/pure-single/static/img/cutis.jpg'
TAGLINE = 'A Manufactura é que é.'
SOCIAL = (
            ('github', 'https://github.com/manufacturaind/'),
            ('twitter-square', 'https://twitter.com/manufacturaind'),
         )

