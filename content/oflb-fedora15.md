Title: Installing your local version of Open Font Library
Summary: Documentation to get your own OFLB on Fedora 15
Date: 2011-07-24 16:08
Author: manufactura
Category: Post
Slug: installing-your-local-version-of-open-font-library-on-fedora-15
Lang: en

Christopher Adams posted a [set of
instructions](https://blueprints.launchpad.net/openfontlibrary/+spec/oflb-live-dev)
for installing a local version of OFLB. This means you can have your own
Open Font Library running locally on a server or your own computer. This
is handy for us in order to test the new design on a development copy,
instead of doing things on a remote server.

We found a few hitches along the way, so we document here the whole
process to have your own OFLB on a Fedora 15 system.

Install the LAMP stack
----------------------

First, we’ll install Apache, MySQL and PHP. You’ll find complete
directions for this in this [Howtoforge
link](http://www.howtoforge.com/installing-apache2-with-php5-and-mysql-support-on-fedora-14-lamp).

Now, let’s set up MySQL for the Aiki database, following the
instructions on the [Aiki wiki
page](http://www.aikiframework.org/wiki/Create_SQL_User).

For our purposes, we’re running all the commands as root. This is fine
for our testing purposes, but be careful when doing this on a server you
don’t own or have with you (rule of thumb: check with the systems
administrator!)

[Download Aiki](http://www.aikiframework.org/wiki/Downloading_Aiki) and
copy it over to the Apache root, making the aiki/ dir world writable
during the installation process (don't forget to set this back in the
end!):

    cp aiki-rev-507.tar.gz /var/www/html
    cd /var/www/html
    tar xvzf aiki-rev-507.tar.gz
    chmod 777 -v aiki

Now, we need to tweak some things before we proceed to installing Aiki.

There’s a little detail that’s worth knowing about, since it left us
scratching our heads for a full afternoon before figuring out what was
missing. It turns out that Fedora comes with SELinux activated. SELinux
doesn’t really like Apache running scripts that create files on the
local filesystem. So, we just went on and deactivated SELinux:

      echo 0 > /selinux/enforce

In order to make this permanent, we’ll need to edit
/etc/sysconfig/selinux, and change the line

      SELINUX=enforcing

to

      SELINUX=permissive

Keep in mind that this will switch off all the protection provided by
SELinux. We’d love to know a way to specifically tell SELinux to not
care about Apache but keep running.

Now that this is out of the way, we can go on to install Aiki by
pointing our browser to http://localhost/aiki, filling in the
information and smiling at the ‘Installation complete’ message.

Install Open Font Library
-------------------------

For this, just follow Christopher’s instructions. Read below for some of
our notes.

We only succeeded in importing the **.sql files** as root. An .sql file
can be ‘imported’ into a database by running

    mysql -u aiki -p aiki < commands.sql

In order to install **Fontaine**, [download
it](http://fontaine.svn.sourceforge.net/viewvc/fontaine/trunk/?view=tar),
unpack it into a directory, cd to it and run

    yum install cmake gcc-c++ freetype-devel graphviz graphviz-devel
    cd trunk
    cmake .
    make

Now copy the bin/fontaine file to
/assets/extensions/fontlibrary/scripts/, and go on with the
installation.

Hopefully, this will have you running a full-fledged Open Font Library
on your system. If you find any glitch during this process, let us know
in the comments.

 

(for our reference, we dumped here the notes we've been taking during
our quest to have OFLB running locally.)

    On the Aiki documentation, change MySQL command in order to ask 
    for the root password instead of typing it on the command line.
    http://www.aikiframework.org/wiki/Create_SQL_User
    Was:
    - mysql -v -u root -ppassword
    Should be:
    - mysql -v -u root -p
    s/-ppassword/-p/g

    Also, the step "Create Aiki database" should make clear that 
    you need to input the Aiki passwd, not root

    Debugging the dreaded 'Wrong site name' error while submitting the 
    Aiki installation form
    * 'Wrong site name' turns out to be the error message that pops up 
      if your Aiki SQL table is not created.
    * I replaced all instances of 'AllowOverride None' to 'All'. Not 
      sure if this is what I should have done. Still same error.
    * I had unpacked aiki in my user home directory, then logged in 
      as root and copied it to /var/www/html.
    * Somehow, I suspect this has to do with SELinux permissions. It 
      went away once I deleted the dir and unpacked the .tar.gz in 
      /var/www/html as root.

    * After putting data on the installer, i get a blank box.
    * After fiddling a bit, i got this error page, which was more 
      useful: 'Sorry, no permissions to create config.php, please 
      create it in /var/www/html/aiki with the following:'
    * (I can't put my finger as to what caused the blank box and 
      what made it disappear, but maybe it has to do with me 
      installing PHPMyAdmin to check the database, which pulled some 
      dependencies that might have helped with this.)

    * Now, trying to open 127.0.0.1/aiki, I get:
        Fatal Error: Wrong site name provided.
    * From what I understood, this error pops up if there's problems 
      with the database. The 'aiki' database is still empty, and from 
      skimming aiki.php it looks like it expects it to be an 
      aiki_sites table there.
    * Removed config file, changed dir ownership to 'apache:apache' 
      (was root:root) and opened aiki/index.php, filled details. 
      Same error.
    * Chmodded recursively the aiki/ dir. Still, I get the same no 
      permission error for creating config.php. Apache log says:
        [Fri Jul 22 12:32:24 2011] [error] [client 127.0.0.1] PHP 
        Warning:  fopen(config.php): failed to open stream: 
        Permission denied in /var/www/html/aiki/system/libraries/installer.php 
        on line 296, referer: http://127.0.0.1/aiki/
    * Here I removed the old aiki dir (since my chmodding probably 
      didn't do wonderful things) and created a new installation. 
      End up again with 'Wrong site name'. Restarted Apache. Same error.
    * The fopen error in the Apache log leads me to think that this 
      is a permissions issue. However, aiki/ is set to 777 (r/w access
      for everyone), and I can create files in there with my regular 
      user account.
    * About to give up, I went to /var/log/messages and grepped for 
      SELinux, as a last ditch check. And here:
        Jul 22 15:28:05 indra setroubleshoot: SELinux is preventing 
        /usr/sbin/httpd from write access on the directory aiki. For 
        complete SELinux messages. run sealert -l 
        0db385ec-53ea-488a-9c06-e7d7fe9cd4b3
    * So, I try to temporarily disable SELinux:
        echo 0 > /syslinux/enforce
    * After removing my manual config.php and filling in the install 
      form, success! I see the "Great!" screen, and I can now login 
      to my Aiki installation.
    * Editing /etc/sysconfig/selinux and changing 'SELINUX=enforcing' 
      to 'SELINUX=permissive' will make this change permanent. It's 
      probably overkill to recommend deactivating SELinux, but as 
      long as it works for me, it's good.

    Bumps while installing OFLB:
    - Couldn't run the .sql files using user aiki, only root. 
      (followed everything on the Aiki howto for SQL setup)
    - While importing oflb_aiki_widgets.sql, I get:
        ERROR 1062 (23000) at line 1: Duplicate entry '22' for key 
        'PRIMARY'
    - Aha, that suggestion to run 'DELETE FROM aiki_widgets WHERE 
      app_id = '0';' turned out to be key.

