#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Manufactura Independente'
SITENAME = u'Manufactura Independente'
SITESUBTITLE = "Libre Graphics & Design research studio"
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
DRAFT_URL = 'private/{slug}/'
DRAFT_SAVE_AS = 'private/{slug}/index.html'
DRAFT_LANG_URL = 'private/{slug}-{lang}/'
DRAFT_LANG_SAVE_AS = 'private/{slug}-{lang}/index.html'

STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'
STATIC_PATHS = [
    'images',
    'extra/htaccess',
    'files',
]
EXTRA_PATH_METADATA = {
    'extra/htaccess': {'path': '.htaccess'},
    'files': {'path': 'files'},
}

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_PATH = "output/"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["gallery"]

# Gallery plug-in
GALLERY_FOLDER = "galleries"
GALLERY_SRC_PATH = "%s%s" % (BASE_PATH, "gallery_src")
GALLERY_OUTPUT_PATH = "%s%s%s" % (BASE_PATH, OUTPUT_PATH, GALLERY_FOLDER)
GALLERY_REGENERATE_EXISTING = False
GALLERY_PRESETS = [
    {"name": "thumb", "actions": [{"type": "fit", "height": 100, "width": 100, "from": (0.5, 0.5)}]},
    {"name": "slider", "actions": [{"type": "fit", "height": 300, "width": 900, "from": (0.5, 0.5)}]},
    {"name": "large", "actions": [{"type": "resize", "height": 640, "width": 850, "from": (0.5, 0.5)}]},
    {"name": "thumb_greyscale",
        "actions": [
            {"type": "fit", "height": 100, "width": 100, "from": (0.5, 0.5)},
            {"type": "greyscale"}
        ]},
]
# This setting is optional, used for thumbnails in bootstrap
# THUMBNAIL_GALLERY_CLASS = "span2"


# COVER_IMG_URL = 'theme/images/cover.jpg'
# PROFILE_IMAGE_URL =  'theme/images/profile.jpg'
# TAGLINE = 'Olá!'
# SOCIAL = (
#            ('github', 'https://github.com/manufacturaind/'),
#            ('twitter-square', 'https://twitter.com/manufacturaind'),
#         )
