Title: Goodbye Dolly, Hello Libre Graphics
Summary: A plugin for WordPress
Date: 2011-02-27 23:30
Author: manufactura
Category: Post
Tags: hacks
Slug: bye-dolly-hello-libre-graphics
Lang: en

Some weeks ago, during a feed-reading evening, I checked the
recipe blog that me and some friends share. We set it up so we could
easily share tips and new tricks among us.

I took the chance to visit the admin area, and noticed that Wordpress
and its plug-ins needed updating. As the process went through, I
couldn't help noticing the little bits of the "Hello Dolly" song that
keep showing up every time you visit a new admin page. It's one of those
little details that make me smile and find something meaningful in one
of the most popular blogging platforms available.

It seemed like a good idea to adapt this plug-in to our recipe blog,
replacing Hello Dolly by one of the songs that my friends and me listen
to together. In a few minutes, I was tweaking the plug-ins PHP file,
which can be found at "wp-content \> plugins \> hello.php". Changing it
was quite simple, only needing to replace the lyrics of one song with
another, and that part sits right in the beginning of the script. The
line breaks in the lyrics delimit each different quote. Then, a PHP
function randomly fetches one of the lines each time an admin page is
loaded. Finally, a bit of CSS was used to finetune the looks and
positioning of the quotes inside the admin interface.

After uploading my changes, I spent a few moments switching pages in
order to see what bits of the lyrics I got. I guess it will take some
time before the others notice the change, but I think it's going to be a
happy surprise.

A search for "Hello Dolly plugin" took me to an interesting
[article](http://weblogtoolscollection.com/archives/2010/12/20/is-hello-dolly-a-copyright-infringing-plug-in/)
where the issue of the song's usage rights was discussed. This plug-in
is part of the default Wordpress plug-in bundle, which is distributed
under the GPL license. The song, however, is encumbered by much more
restrictive copyright terms.

Not sure whether this use of the song fits under fair use, the article
author points us to an [alternative
version](http://core.trac.wordpress.org/attachment/ticket/15769/free_software.diff),
in which Hello Dolly was replaced by the [Free Software
Song](http://www.gnu.org/music/free-software-song.html).

This search also took me to the plug-in discussion pages on the
Wordpress site. It's fun to see that most comments ask why such a
useless plug-in is included in the Wordpress base install, as something
that has no meaning or use. Only one user made a feature request --
having a different song for each user — and asked for help to make it
happen.

[Here](http://manufacturaindependente.com/hello-libregraphics.zip) is
our version of this plug-in, which we did for our blog. We call it
"Hello Libre Graphics", since we used the [Libre Graphics Magazine
manifesto](http://libregraphicsmag.com/manifesto.html "Manifesto da Libre Graphics Magazine").
We have a few more ideas to try out with this plug-in, which we love,
and we'll be trying new recipes in the near future.
