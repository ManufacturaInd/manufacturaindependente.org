Title: Adeus Dolly e Olá Libre Graphics 
Date: 2011-02-27 23:30
Author: ana
Category: Blogpost
Tags: hacks
Slug: bye-dolly-hello-libre-graphics

Há umas semanas atrás, durante um serão e entre leituras de feeds,
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
vamos voltar a dedicar-nos a isto mais à frente.
