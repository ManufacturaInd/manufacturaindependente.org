Title: fonts.txt
Summary: ASCII Art font design workshop at FCForum, Barcelona
Date: 2014-11-07 12:00
Author: manufactura
Category: Workshops
Tags: type
Slug: fontstxt
Lang: en

![Setting characters](http://media.manufacturaindependente.org/fontstxt-02.jpg "Setting characters")

We were invited to participate in [FCForum](http://lab.2014.fcforum.net/en/)
with a keynote and a type design workshop.

The **fonts.txt** workshop featured our usual double-purpose workshop approach: test
a system that we've been working on, as well as producing concrete results that
everyone can share and take home.

This time, our theme was **plaintext**: as part of our experiments in alternative
interfaces for type design, our challenge would be to design bitmap
fonts using simple text files. Reminiscent of ASCII art and the practice of
drawing with text characters, our pipeline again used the [Graphicore bitmap
font](http://lab.2014.fcforum.net/en/) library to convert the text files into
OpenType fonts.


The workshop
------------

Once again, we put our traditional font editor aside and propose a different
kind of workflow.  

The [Graphicore Bitmap Font
Format](http://graphicore.de/en/archive/2010-09-09_A-Brute-Font-Attack)
proposes a bitmap font representation that we particularly enjoy: each glyph is
described in a separate `.txt` file, containing a visual representation that
brings us back to ASCII art. For instance, here's an example of what you'd find
in a text file that describes a capital A:

    ...###...
    ..#...#..
    ..#...#..
    ..#####..
    ..#...#..
    ..#...#..
    .###.###.

The visual nature of this font format makes it ideal for getting anyone up to
speed with creating digital versions of bitmap typefaces. The fact that each
glyph lives in a separate file makes it possible to have teams working on the
same font.

We had a full house with more than enough people to form 3 teams who could work
on separate fonts. Each team was assigned a specific proportion for the
typeface they'd design:

* Team A: a typeface taller than it is wide (condensed)
* Team B: a typeface wider than it is tall (extended)
* Team C: a typeface with the same width and height

From there, the teams moved to quickly iterate through possible designs and make
fast decisions where to go next, with Ana and Ricardo serving as [benevolent
dictators](http://en.wikipedia.org/wiki/Benevolent_dictator_for_life) whenever
a complex decision needed to be taken -- otherwise there would be no way to end
up with a finished typeface in 4 hours!

![Sketching](http://media.manufacturaindependente.org/fontstxt-01.jpg "Sketching")
![Sketching 2](http://media.manufacturaindependente.org/fontstxt-09.jpg "Sketching 2")
![Sketching 3](http://media.manufacturaindependente.org/fontstxt-06.jpg "Sketching 3")

Stemming from the [X11
fonts](ihttps://packages.debian.org/sid/all/xfonts-base/filelist) style of
naming fonts after their proportion (`5x8` or `6x10`), we decided on using a
Catalan transliteration from the proportions of each team's font:

* 6 by 12 = **Sisperdotze**
* 7 by 10 = **Setperdeu**
* 7 by 7 = **Setperset**


![Digitising](http://media.manufacturaindependente.org/fontstxt-07.jpg "Digitising")
![Digitising Sisperdotze](http://media.manufacturaindependente.org/fontstxt-10.jpg "Digitising Sisperdotze")
![Digitising Setperset](http://media.manufacturaindependente.org/fontstxt-08.jpg "Digitising Setperset")
![Digitising in Notepad](http://media.manufacturaindependente.org/fontstxt-16.jpg "Digitising in Notepad")

The outcomes
------------

Work was fast and intense, and after some prodding and discussion each team
delivered their text files, which we then eagerly fed our set our scripts in order
to end up with TTF files. Our goal was to have *at least* the uppercase glyphs
covered, and we were delighted that each team was able to tackle figures as
well!

**Sisperdotze** is an elegant and thin sans-serif which stays close to the terminal
font aesthetic

![Sisperdotze](http://media.manufacturaindependente.org/fontstxt-03.jpg "Sisperdotze")

**Deuperset** has a blocky and (dare we say) retro look that brings us back to early
Atari-type TV consoles.

![Deuperset](http://media.manufacturaindependente.org/fontstxt-04.jpg "Deuperset")

**Setperset** is a daring proposal to put forward a serif design which stands out
from its play on a square frame.

![Setperset](http://media.manufacturaindependente.org/fontstxt-05.jpg "Setperset")

After digitising these designs and passing them through our script pipeline, we
now have beautiful outline versions that can be used in web sites or print
layouts.

<link rel="stylesheet" href="../theme/css/font-sampler.css">
<style>
    @font-face {
      font-family: 'Sisperdotze';
      src: url('http://media.manufacturaindependente.org/fonts/Sisperdotze/Sisperdotze-Regular.eot');
      src: url('http://media.manufacturaindependente.org/fonts/Sisperdotze/Sisperdotze-Regular.eot?#iefix') format('embedded-opentype'), 
           url('http://media.manufacturaindependente.org/fonts/Sisperdotze/Sisperdotze-Regular.woff') format('woff'), 
           url('http://media.manufacturaindependente.org/fonts/Sisperdotze/Sisperdotze-Regular.ttf')  format('truetype'),
           url('http://media.manufacturaindependente.org/fonts/Sisperdotze/Sisperdotze-Regular.svg#svgFontName') format('svg');
      font-weight: normal;
      font-style: normal;
    }
    @font-face {
      font-family: 'Deuperset';
      src: url('http://media.manufacturaindependente.org/fonts/Deuperset/Deuperset-Regular.eot');
      src: url('http://media.manufacturaindependente.org/fonts/Deuperset/Deuperset-Regular.eot?#iefix') format('embedded-opentype'), 
           url('http://media.manufacturaindependente.org/fonts/Deuperset/Deuperset-Regular.woff') format('woff'), 
           url('http://media.manufacturaindependente.org/fonts/Deuperset/Deuperset-Regular.ttf')  format('truetype'),
           url('http://media.manufacturaindependente.org/fonts/Deuperset/Deuperset-Regular.svg#svgFontName') format('svg');
      font-weight: normal;
      font-style: normal;
    }
    @font-face {
      font-family: 'Setperset';
      src: url('http://media.manufacturaindependente.org/fonts/Setperset/Setperset-Regular.eot');
      src: url('http://media.manufacturaindependente.org/fonts/Setperset/Setperset-Regular.eot?#iefix') format('embedded-opentype'), 
           url('http://media.manufacturaindependente.org/fonts/Setperset/Setperset-Regular.woff') format('woff'), 
           url('http://media.manufacturaindependente.org/fonts/Setperset/Setperset-Regular.ttf')  format('truetype'),
           url('http://media.manufacturaindependente.org/fonts/Setperset/Setperset-Regular.svg#svgFontName') format('svg');
      font-weight: normal;
      font-style: normal;
    }
</style>

<div id="tester">
    <input id="tester-box" type="text" placeholder="Test these lovely fonts!" />
</div>
<ul id="font-list">
    <li id="sisperdotze">
        <span class="sample" style="font-family: 'Sisperdotze'">The quick brown fox jumps over the lazy dog</span>
        <p class="details">
            <span class="name">Sisperdotze</span> by
            <span class="authors">Óscar Pereira, Irene Farré Márquez, Kira Riera Contijoch,
            Dario Trapasso, María Florencia Fernández, Maria Luisa Jimenez</span>
        </p>
    </li>
        <li id="deuperset">
        <span class="sample" style="font-family: 'Deuperset'">The quick brown fox jumps over the lazy dog</span>
        <p class="details">
            <span class="name">Deuperset</span> by
            <span class="authors">Alba Clemente, Sílvia Fabra, Nuría Fernández, Maitane González,
            Aurora Alonso and Adrià Valls</span>
        </p>
    </li>
        <li id="setperset">
        <span class="sample" style="font-family: 'Setperset'">The quick brown fox jumps over the lazy dog</span>
        <p class="details">
            <span class="name">Setperset</span> by
            <span class="authors">Oriol Gayán, Nelson Dieguez, Vanessa Pacheco, Irene Serrano</span>
        </p>
    </li>
</ul>

Now they're available at the [Open Font Library](http://openfontlibrary.org),
so check out, download, use and hack on them!


Acknowledgments
---------------

##### Image credits

  * [Carla Boserman](http://twitter.com/cboserman)
  * [Manufactura Independente](http://twitter.com/manufacturaind)

##### Workshop participants

  * *Sisperdotze*:
    - Kira Riera Contijoch
    - María Florencia Fernández
    - Maria Luisa Jimenez
    - Irene Farré Márquez
    - Óscar Pereira
    - Dario Trapasso

  * *Deuperset*:
    - Aurora Alonso
    - Alba Clemente
    - Sílvia Fabra
    - Nuría Fernández
    - Maitane González
    - Adrià Valls

  * *Setperset*:
    - Nelson Dieguez
    - Oriol Gayán
    - Vanessa Pacheco
    - Irene Serrano

##### Special thanks

  * the FCForum team for organising an energetic and deep-reaching event, and
    for highlighting the "open design" ecosystem; our <3 to [Jaron
    Rowan](http://twitter.com/sirjaron), [Carla
    Boserman](http://twitter.com/cboserman), [Jara
    Rocha](http://twitter.com/jararocha) and everyone involved in organising
    and supporting this one-of-a-kind event.
  * all the participants in the workshop, who did some excellent work in a
    particularly tight timeframe!

![Group photo](http://media.manufacturaindependente.org/fontstxt-12.jpg "Group photo")


<script src="../theme/js/jquery-1.11.1.min.js"></script>
<script src="../theme/js/modernizr-2.8.3-custom.min.js"></script>
<script src="../theme/js/font-sampler.js"></script>
