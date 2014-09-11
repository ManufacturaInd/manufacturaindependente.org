Title: Uma primeira experiência de texto na web com várias cores
Date: 2011-02-07 17:01
Author: manufactura
Category: Blogpost
Tags: hacks
Slug: a-first-experiment-with-multicoloured-web-fonts
Lang: pt

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
funcione como desejado — é boa ideia consultar o style.css que temos
como ponto de partida.

Além disso, o texto é seleccionável (com algumas lacunas, ver abaixo).
Ter o texto como parte do documento torna possíveis algumas experiências
divertidas — como [tradução
automática](http://translate.google.com/translate?hl=en&sl=en&tl=eu&u=http%3A%2F%2Fmanufacturaindependente.com%2Fcolorfont%2F)!<a href="http://translate.google.com/translate?hl=en&amp;sl=en&amp;tl=eu&amp;u=http%3A%2F%2Fmanufacturaindependente.com%2Fcolorfont%2F">

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
cabeçalho — aparecem linhas duplicadas. Qualquer pessoa familiarizada
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
