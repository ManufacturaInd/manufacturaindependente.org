Title: Implied Spacing
Summary: Spacing text with colour
Date: 2012-02-24 00:33
Author: manufactura
Category: Post
Tags: hacks, lgru
Slug: implied-spacing
Lang: en

![](http://blog.manufacturaindependente.org/wp-content/uploads/2012/02/salt-post.png "Love like Salt with Implied Spacing")
Working with the
[Scribus](http://www.scribus.net/canvas/Scribus "Scribus") API we wrote
a script for something we named Implied Spacing.

The script removes all spaces between words and creates a gradient in
the letter colouring. The rule is, as a word gets closer to its end,
each letter gets progressively lighter.

It's quite short so here it is:

    :::python
    from scribus import *

    # change values here
    font = "Bevan Regular"
    fontsize = 10
    linespacing = 11
    defineColor("PunctColor", 0, 255, 255, 70)
    defineColor("TextColor", 200, 100, 0, 50)
    punct_chars = ".,?!\""

    # open the text we'll use
    txt = open('/home/rlafuente/proj/lgru/space/lovelikesalt.txt', 'r').read()
    txt = txt.replace('\n', ' ')
    # create text box
    textbox_name = createText(0, 0, 595, 840, "Text1")
    setText(txt, textbox_name)

    # set up textbox attributes
    selectObject(textbox_name)
    setFont(font, textbox_name)
    setFontSize(fontsize, textbox_name)
    setLineSpacing(linespacing, textbox_name)
    setTextColor("TextColor", textbox_name)

    def allindices(string, sub, listindex=None, offset=0):
        # find all indices of a specific string
        if not listindex:
            listindex = []
        i = string.find(sub, offset)
        while i >= 0:
            listindex.append(i)
            i = string.find(sub, i + 1)
        return listindex

    # get positions for all space characters
    txt = getAllText(textbox_name)
    spaceindexes = allindices(txt, " ")
    print spaceindexes
    # likewise for punctuation
    punctindexes = []
    for char in punct_chars: 
        idxs = allindices(txt, char)
        punctindexes.extend(allindices(txt, char))

    deselectAll()

    shade = 100
    for i in range(1, len(txt)):
        if i in spaceindexes:
            # space
            shade = 100
        elif i in punctindexes:
            # punctuation
            selectObject(textbox_name)
            selectText(i, 1)
            setTextColor("PunctColor")
        else:
            # not space
            if shade < 20:
                shade = 20
            selectObject(textbox_name)
            selectText(i, 1)
            setTextShade(shade)
            shade -= 20

    # now delete all spaces
    spaceindexes.reverse() 
    for i in spaceindexes:
        selectText(i, 1, textbox_name)
        deleteText() 

