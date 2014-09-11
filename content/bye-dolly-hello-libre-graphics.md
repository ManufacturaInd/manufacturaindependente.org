Title: Goodbye Dolly, Hello Libre Graphics
Date: 2011-02-27 23:30
Author: ana
Category: Blogpost
Tags: hacks
Slug: bye-dolly-hello-libre-graphics

<!--:en-->Some weeks ago, during a feed-reading evening, I checked the
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
having a different song for each user -- and asked for help to make it
happen.

[Here](http://manufacturaindependente.com/hello-libregraphics.zip) is
our version of this plug-in, which we did for our blog. We call it
"Hello Libre Graphics", since we used the [Libre Graphics Magazine
manifesto](http://libregraphicsmag.com/manifesto.html "Manifesto da Libre Graphics Magazine").
We have a few more ideas to try out with this plug-in, which we love,
and we'll be trying new recipes in the near future.<!--:--><!--:pt-->Há
umas semanas atrás, durante um serão e entre leituras de feeds,
espreitei o blog de receitas e outros truques, que partilho com algumas
amigas. Decidimos, há algum tempo, montá-lo para poder guardar e trocar
facilmente coisas entre nós.

Aproveitei a ocasião para visitar a parte de administração e reparei que
precisava de uma actualização da versão de Wordpress e dos plugins que
temos instalados. Enquanto o fazia, não pude deixar de reparar nos
pequenos trechos da letra da música "Hello Dolly" que vão sendo
carregados a cada mudança de página da administração. É um daqueles
pormenores que me fazem sorrir e encontrar algo coisa mais naquela é uma
das maiores e mais poderosas plataformas de blogging disponível
livremente.

Pareceu-me uma boa ideia adaptar o plugin ao nosso blog e substituir a
Hello Dolly por uma das músicas que costumamos ouvir quando estamos
juntas. Em poucos minutos tinha aberto o único documento PHP de que é
feito este plugin (localizado em "wp-content \> plugins \> hello.php"),
e estava a editá-lo. Foi mesmo simples porque basta substituir a letra
de uma música pela letra da outra, e isso está logo no início do script.
A quebra de linhas na letra indica os pedaços em que esta vai ficar
dividida. Depois há uma função que vai buscar, aleatoriamente, uma das
linhas da letra de cada vez que uma página da administração é carregada.
No final, um pedaço CSS serviu para configurar o aspecto e o
posicionamento da frase na página de administração.

Fiz upload da minha alteração e estive alguns instantes a trocar entre
páginas para ver o que me ia calhando da letra da nova música. Imagino
que vai demorar até alguém reparar nessa pequena alteração, mas quando
acontecer sei que vai ser uma boa surpresa.

Uma pesquisa por "Hello Dolly plugin" levou-me a um
[artigo](http://weblogtoolscollection.com/archives/2010/12/20/is-hello-dolly-a-copyright-infringing-plug-in/)
interessante onde se colocava a questão dos direitos do uso desta
música. Este plugin faz parte do pacote default Wordpress, que é
distribuído com uma licença GPL. A música, por sua vez, está sobre uma
licença de uso mais restritiva.

Sem certeza de que este uso encaixa nos termos do 'uso aceitável'
(tradução do termo anglofóno *fair use*), o autor do artigo menciona uma
[versão alternativa do
plugin](http://core.trac.wordpress.org/attachment/ticket/15769/free_software.diff),
em que o Hello Dolly foi substituído pela [Free Software
Song](http://www.gnu.org/music/free-software-song.html).

A mesma pesquisa levou-me às páginas de discussão sobre o plugin no site
do Wordpress. É engraçado ver que a maioria dos comentários de
utilizadores questiona o porquê de incluir um plugin tão *inútil* na
distribuição base de Wordpress. Uma coisa aparentemente sem qualquer uso
ou sentido. Só um utilizador partilha uma ideia para alterar o plugin --
poder ter uma música diferente para cada utilizador da administração --
e pede ajuda para a concretizar.

[Aqui](http://manufacturaindependente.com/hello-libregraphics.zip) fica
a nossa versão deste plugin, que fizemos para o nosso blog. Chamamos-lhe
Hello Libre Graphics, e usamos como texto base o [manifesto da revista
Libre
Graphics](http://libregraphicsmag.com/manifesto.html "Manifesto da Libre Graphics Magazine").
Temos mais algumas ideias para modificar este plugin, que adoramos, e
vamos voltar a dedicar-nos a isto mais à frente.<!--:-->

