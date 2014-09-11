Title: A first experiment with multicoloured web fonts
Date: 2011-02-07 17:01
Author: manufactura
Category: Blogpost
Tags: hacks
Slug: a-first-experiment-with-multicoloured-web-fonts
Lang: en

[![](http://blog.manufacturaindependente.org/wp-content/uploads/2011/02/Screenshot-300x111.png "Screenshot")](http://blog.manufacturaindependente.org/wp-content/uploads/2011/02/Screenshot.png)

We made a little hack in a couple of days after a poke by [Dave
Crossland](http://understandingfonts.com/), who asked how hard it would
be to create multi-colored text that could work in an HTML document.
Through a tiny Javascript library (see below for download link) and a
tweak of [OSP](http://ospublish.constantvzw.org)'s [DIN
typeface](http://ospublish.constantvzw.org/foundry/osp-din/), we did a
proof-of-concept page that showcases overlaying fonts to achieve the
desired effect. It also shows through some limitations that HTML forced
on us, preventing this from being a technique that could be widely used
in the web.

First, do [check it out](http://manufacturaindependente.com/colorfont/v1). (**UPDATE**: In
the meantime, we fixed some rough edges, and created a [git
repository](https://gitorious.org/manufacturaindhacks/colorfont) for
this.)

Does it work?
-------------

It mostly works for our modest text-wrangling purposes! The goal was to
make the use of this effect as straightforward as possible and without
cluttering the HTML; as it is, most of the action is taken care of with
CSS and Javascript, without having to use "special" HTML tricks.

In order to use this, you only need to specify the Javascript file in
your HTML header. From there, any \<h1\> tag with the 'colorfont' class
will be styled with the overlay effect. It's also up to you to edit the
CSS in order to make it work — be sure to check the CSS file we made as
a starting point.

Also, the text is actually selectable (with a couple of caveats — see
below). Having the text as part of the document makes some fun
experiments possible — try [translating
it](http://translate.google.com/translate?hl=en&sl=en&tl=eu&u=http%3A%2F%2Fmanufacturaindependente.com%2Fcolorfont%2F)!

How is this done?
-----------------

The trick is done with Javascript, creating a second header right on top
of the first one.

The JS is pretty simple, looking for headings with the 'colorfont'
attribute and appending another identical heading with the 'colorfont2'
attribute. In this way, this:

    <h1 class="colorfont">Hola mundo!</h1>

will become:

    <div class="colorfont-container">
      <h1 class="colorfont">Hola mundo!</span>
      <span class="colorfont-overlay">Hola mundo!</span>
    </div>

The CSS file takes care of defining the typefaces and colors used for
this effect.

There aren't many fonts around designed to be used for the purpose of
creating typographic overlays. [Gustavo
Ferreira](http://twitter.com/hipertipo) pointed us to a [2009
experiment](http://afrojet.com/brutal) by [John
Skelton](http://afrojet.com/) which achieves the same effect.

What's missing?
---------------

There's a limitation of HTML that we ran into, which is that any extra
text element *must* be explicitly declared in the DOM. This is a
semantics problem, since it litters the document with redundant data (in
this case, an extra header) in order to achieve a visual effect.

We did try working around this issue by trying to get this effect
through CSS, but a slew of other issues popped up, and we lost the
ability to select text with that approach. Sadly, we couldn't find a
cleaner way to accomplish this effect. If you can shed some light on
this, let us know in the comments!

This shortcoming also reveals itself once you try to copy and paste the
heading — it returns repeated lines. Anyone familiar with semantic
structure of HTML documents will correctly point this as a no-no (having
duplicate headers just for stylistic effect). We agree, but can't help
feeling a bit powerless and longing for an easy and elegant solution for
complex, multi-colored text effects on the web.

Finally, the effect can only be applied on \<h1\> and \<h2\> headings.
Bug us in the comments if you need more.

Can i use it?
-------------

Sure! Get the
[colorfont.js](http://manufacturaindependente.com/colorfont/colorfont.js)
file and include it inside your document. Check the source of our
[demo](http://manufacturaindependente.com/colorfont/) in order to get a
feel of how things work. If you're stumped, leave a comment and we'll
try to get you going.

What's the license?
-------------------

colorfont.js is available under the [WTFPL](http://sam.zoy.org/wtfpl/).
