Title: Generating outline fonts with 5 lines of code
Date: 2011-02-14 17:01
Author: manufactura
Category: Blogpost
Tags: hacks
Slug: generating-outline-fonts-with-5-lines-of-code
Lang: en

Contrary to popular belief, free software has its own gems
which easily outshine their proprietary counterparts. One of our
favourite examples of this is
[Fontforge](http://fontforge.sourceforge.net).

Though one might be misled by its peculiar user interface, Fontforge is
a very elegant and powerful tool for type design. However, we think the
real killer feature of Fontforge is its Python scripting interface. It
means you can write your own scripts calling on Fontforge operations,
dispensing with the GUI and allowing for some very interesting
batch-processing approaches. Plus, the Python bindings are exhaustively
[documented](http://fontforge.sourceforge.net/python.html).

[![](http://blog.manufacturaindependente.org/wp-content/uploads/2011/02/douar-outline-1024x640.png "douar-outline")](http://blog.manufacturaindependente.org/wp-content/uploads/2011/02/douar-outline.png)

The window on the left is the GNOME font previewer showing an outline
version of [VTF Foundry](http://www.vtf.fadebiaye.com/)'s
[Douar](http://www.fadebiaye.com/type/douar/) font, which is licensed
with the [Open Font License](http://scripts.sil.org/OFL), allowing us to
hack it without mercy.

The real kicker is that the font was generated using a 5-line script.

    import fontforge
    font = fontforge.open('douar.sfd')
    for glyph in font:
        font[glyph].stroke('circular',  30, 'square', 'bevel', ('cleanup',))
    font.generate('douar-new.ttf')

This outline effect can now be applied to any font file. Not bad!

