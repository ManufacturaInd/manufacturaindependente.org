Title: OFLB: Interface widgets
Date: 2011-08-08 17:01
Author: manufactura
Status: draft
Category: Post
Tags: oflb
Slug: oflb-interface-widgets
Lang: en

While refining our catalogue and font views, we realised there were two
features that we had to implement:

-   a **colour picker** for setting the previews' foreground and
    background colour, handy to see the font in its intended context,
    and
-   a **slider** for altering the preview text size.

There are quite a few JavaScript-based colour widgets around, and for
now we're trying out [Stefan Petre](http://eyecon.ro)'s
[Colorpicker](http://eyecon.ro/colorpicker/). It provides an intuitive
and quick interface for choosing a colour, and on top of that it allows
you to fine-tune a colour, and even specify it through its hex code.

For the slider, we went with [JQuery UI](http://jqueryui.com)'s stock
slider, which is more than enough for our purposes.

After hooking up a couple of callbacks, our interface for HTML
font-preview is already working — now, on to finish the styling and
placement of the widget elements.

[![Screenshot-5.png](http://media.manufacturaindependente.org/Screenshot-5.png "Screenshot-5.png")](http://media.manufacturaindependente.org/Screenshot-5.png)

