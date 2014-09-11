Title: A first experiment with multicoloured web fonts
Date: 2011-02-07 17:01
Author: ricardo
Category: Blogpost
Tags: hacks
Slug: a-first-experiment-with-multicoloured-web-fonts

<!--:en-->

<!-- p, li { white-space: pre-wrap; } -->[![](http://blog.manufacturaindependente.org/wp-content/uploads/2011/02/Screenshot-300x111.png "Screenshot")](http://blog.manufacturaindependente.org/wp-content/uploads/2011/02/Screenshot.png)

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

First, do [check it
out](http://manufacturaindependente.com/colorfont/v1). (**UPDATE**: In
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
CSS in order to make it work -- be sure to check the CSS file we made as
a starting point.

Also, the text is actually selectable (with a couple of caveats -- see
below). Having the text as part of the document makes some fun
experiments possible -- try [translating
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
heading -- it returns repeated lines. Anyone familiar with semantic
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

<!--:--><!--:pt-->

[![](../wp-content/uploads/2011/02/Screenshot-300x111.png "Screenshot")](../wp-content/uploads/2011/02/Screenshot.png)

Em poucos dias, e depois de uma achega do [Dave
Crossland](http://understandingfonts.com/), que perguntou se haveria
hipóteses de criar texto com mais de uma cor que pudesse funcionar num
documento HTML, fizemos um pequeno hack para demonstrar que é possível.
Através de uma pequena biblioteca Javascript (ver mais abaixo para o
link de download) e umas alterações à fonte
[DIN](http://ospublish.constantvzw.org/foundry/osp-din/) criada pelos
[OSP](http://ospublish.constantvzw.org/), fizemos uma 'proof-of-concept'
que mostra fontes sobrepostas para chegar ao efeito desejado. Esta
experiência também tornou evidentes algumas limitações postas pelo
formato HTML; infelizmente, elas impedem o uso corrente desta técnica,
por razões que especificamos mais abaixo.

Primeiro, vale a pena [ver do que se
trata](http://manufacturaindependente.com/colorfont/).

<!--:--><!--more--><!--:pt-->

Isto funciona?
--------------

Funciona quase perfeitamente para os nossos modestos propósitos. O
objectivo era tornar o uso deste efeito o mais fácil possível e sem
poluir o HTML. Assim, tudo é resolvido com CSS e Javascript/JQuery, sem
ter de usar truques manhosos em HTML.

Para poder experimentar isto, só vais precisar de especificar o ficheiro
Javascript no cabeçalho do HTML. Depois, qualquer header (\<h1\>,
\<h2\>, etc.) com a classe 'colorfont' vai aparecer com o efeito de
sobreposição. Será talvez preciso editar o ficheiro CSS para que
funcione como desejado -- é boa ideia consultar o style.css que temos
como ponto de partida.

Além disso, o texto é seleccionável (com algumas lacunas, ver abaixo).
Ter o texto como parte do documento torna possíveis algumas experiências
divertidas -- como [tradução
automática](http://translate.google.com/translate?hl=en&sl=en&tl=eu&u=http%3A%2F%2Fmanufacturaindependente.com%2Fcolorfont%2F)!<a href="http://translate.google.com/translate?hl=en&amp;sl=en&amp;tl=eu&amp;u=http%3A%2F%2Fmanufacturaindependente.com%2Fcolorfont%2F">

</a>

Como é que é feito?
-------------------

O truque funciona em Javascript/JQuery, criando um segundo cabeçalho
sobreposto ao primeiro.

O código Javascript é bastante simples, procurando cabeçalhos com o
atributo 'colorfont', colocando-os dentro de um \<div\> e juntando um
\<span\> para o texto a sobrepôr. Desta forma, isto:

    <h1 class="colorfont">Hola mundo!</h1>

vai tornar-se:

    <div class="colorfont-container">
      <h1 class="colorfont">Hola mundo!</h1>
      <span class="colorfont-overlay">Hola mundo!</span>
    </div>

A folha de estilos CSS trata de definir os tipos de letras e cores
utilizados.

Existem poucas fontes feitas para este tipo de efeito. O [Gustavo
Ferreira](http://twitter.com/hipertipo) indicou uma [experiência feita
em 2009](http://afrojet.com/brutal) por [John
Skelton](http://afrojet.com/) que produz o mesmo efeito.

O que falta?
------------

Encontrámos uma limitação do HTML, que é a necessidade de declarar na
DOM *todos* os elementos de texto. Isto causa um problema semântico, já
que polui o documento com dados redundantes (neste caso, um \<span\>
adicional) para obter um efeito visual.

Tentámos dar a volta ao problema usando apenas CSS, mas isso fez
aparecer uma data de outras complicações, e perdia-se a possibilidade de
seleccionar texto. Infelizmente, não conseguimos encontrar uma forma
mais elegante de chegar a este efeito. Se souberes de alguma forma,
diz-nos nos comentários!

Este problema também se revela quando tentamos fazer corta-e-cola do
cabeçalho -- aparecem linhas duplicadas. Qualquer pessoa familiarizada
com a estrutura semântica de documentos HTML irá correctamente dizer que
isto não se faz (ter cabeçalhos repetidos para fins decorativos). Nós
concordamos, mas não deixamos de nos sentir algo impotentes e desejosos
de uma forma fácil e simples para conseguir efeitos complexos de texto
na web.

Finalmente, o efeito pode apenas ser aplicado em cabeçalhos (\<h1\>,
\<h2\>, etc). Chateia-nos nos comentários caso precises de mais.

Finally, the effect can only be applied on \<h1\> and \<h2\> headings.
Bug us in the comments if you need more.

Posso usar isto?
----------------

Claro! Vai buscar o
[colorfont.js](http://manufacturaindependente.com/colorfont/colorfont.js)
e inclui-a no documento HTML. Vê também o código fonte da nossa
[demo](http://manufacturaindependente.com/colorfont/) para ver como é
que tudo funciona. Caso seja confuso, os comentários deste post são o
melhor sítio para dar alguma luz no problema.

Temos também o código disponível num repositório no
[Gitorious](http://gitorious.org/mihacks/colorfont).

Qual é a licença?
-----------------

O colorfont.js está disponível segundo os termos da
[WTFPL](http://sam.zoy.org/wtfpl/).

</p>
<!--:-->

