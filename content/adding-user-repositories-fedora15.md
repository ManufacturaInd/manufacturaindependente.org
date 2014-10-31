Title: Adding user repositories in Fedora 15
Summary: Transitioning to Fedora
Date: 2011-07-17 13:54
Author: manufactura
Category: Post
Slug: adding-user-repositories-in-fedora-15
Lang: en

We are now taking our first steps with **Fedora 15** after
having decided to move on from Ubuntu.

Most of the stuff is familiar, with some different applications showing
up in place of the usual Ubuntu/Debian ones. One such case is the Fedora
package manager, **yum**, which is used instead of **apt**.

Migrating from apt to yum is a smooth process -- we were easily
installing and reviewing packages after a couple of minutes. However, we
were wondering if there was any equivalent to Ubuntu PPA’s -- a way to
host custom repositories where the most cutting-edge software versions
live.

Our workflow grew dependent on the development versions of a few
programs, most important of which are **Gimp** and **Scribus**. The
version of Gimp in the Fedora repos comes from the stable 2.6 series,
and we immediately missed the single-window mode in the Gimp 2.7
development branch. Same with Scribus: the stable, included version is
1.3.9, whereas we work almost exclusively with the 1.4.0 series
(particularly in [Libre Graphics
Magazine](http://libregraphicsmag.com)).

Thankfully, there is a way! All the information on the repositories to
use are inside the `/etc/yum.repos.d` directory. If we want to add one,
we just need to place a special .repo file inside that directory, which
is a simple file pointing to the place where the actual package files
can be fetched. Here's an example of mrdocs's Scribus repo file:

> `[home_mrdocs] name=mrdocs's Home Project (Fedora_15) type=rpm-md baseurl=http://download.opensuse.org/repositories/home:/mrdocs/Fedora_15/ gpgcheck=1 gpgkey=http://download.opensuse.org/repositories/home:/mrdocs/Fedora_15/repodata/repomd.xml.key enabled=1`

Here are links to the .repo files that we currently use for various
kinds of software. We are running this on Fedora 15, your mileage may
vary.

- **Gimp 2.7 series** ([repo
file](http://repos.fedorapeople.org/repos/luya/gimp/fedora-gimp.repo))
This one gave us a little trouble -- we replaced `$basearch` for `i386`
inside the file, and all was good.  
- **Scribus 1.4.0 series** ([repo
file](http://download.opensuse.org/repositories/home:/mrdocs/Fedora_15/home:mrdocs.repo))  
- **Gpick**, an awesome palette manager ([repo
file](http://download.opensuse.org/repositories/home:/ketheriel:/gpick/Fedora_15/home:ketheriel:gpick.repo))  
- **Google Chrome** ([page with repo
file](http://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/))

Once you have downloaded all the files, move them to `/etc/yum.repos.d`,
and feel free to rename them -- we named ours `gimp.repo`,
`scribus.repo`, etc. for clarity.

All that’s left is playing around with yum install now.
