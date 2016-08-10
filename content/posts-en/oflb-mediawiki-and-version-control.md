Title: OFLB: MediaWiki and Version Control
Date: 2011-08-02 17:01
Author: manufactura
Status: draft
Category: Post
Tags: oflb
Slug: oflb-mediawiki-and-version-control
Lang: en

[![Media Wiki install screenshot]({filename}/media/IMAG0170-1024x495.jpg "IMAG0170")]({filename}/media/IMAG0170.jpg)

We’re now busy getting [MediaWiki](http://www.mediawiki.org/) up and
running for Open Font Library, as it will be the backend for the OFLB
Guidebook — the place for documentation about open fonts and open
typography.

Since we’re using version control — [Git](http://git-scm.com/) — for
this project, we’d like the MediaWiki install to be able to work with
this. The ‘traditional’ configuration involves MySQL, which is not the
best choice for this purpose, since we’d have to jump through a few
hoops for keeping the database under Git.

Fortunately, there’s [SQLite](http://www.sqlite.org/), which is a
database format that keeps everything in simple files, and we’re able to
keep track and update them through Git since the database is part of the
file system.

We got a pleasant surprise while revisiting MediaWiki in order to create
our local install — the installation steps are clear and helpful (with
pretty Javascript collapsing panels) and, best of all, SQLite support
for MediaWiki is already production-level. We just selected the SQLite
option, created the database directory under our project with the
appropriate permissions, and everything was running smooth.

We’ll just have to fiddle a bit with the MediaWiki config so that we can
have a little file that can specify local directories — for instance,
each computer might have different places for the project, and the
MediaWiki config needs to be pointed that way. But it’s already [up on
Gitorious](https://gitorious.org/oflb/guidebook) and ready for our
skinning hacks.

