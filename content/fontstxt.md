Title: fonts.txt
Summary: ASCII Art font design workshop at FCForum, Barcelona
Date: 2014-11-07 12:00
Author: manufactura
Category: Workshops
Tags: type
Slug: fontstxt
Lang: en


We were invited to participate in FCForum with a keynote and a type design workshop.

This time, our theme was plaintext: as part of our experiments in alternative
interfaces for type design, this time our challenge would be to design bitmap
fonts using simple text files. Reminiscent of ASCII art and the practice of
drawing with text characters, our pipeline again used the Graphicore bitmap font
library to convert the text files into OpenType fonts.

The fonts.txt workshop featured our usual double-purpose workshop approach: test
a system that we've been working on, as well as producing concrete results that
everyone can share and take home.


The workshop
------------

Enough people for 3 groups, 3 fonts. Naming using the Catalan names for the
fonts (based on X11 practice of naming fonts after their proportions: 6x10, etc).

* 6 by 12 = Sis per dotze
* 7 by 10 = Set per deu
* 7 by 7 = Set per set

BFDL, quick decision making


The outcomes
------------

Uppercase and figures!

* Sisperdotze
* Setperdeu
* Setperset


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

<script src="../theme/js/jquery-1.11.1.min.js"></script>
<script src="../theme/js/modernizr-2.8.3-custom.min.js"></script>
<script src="../theme/js/font-sampler.js"></script>
