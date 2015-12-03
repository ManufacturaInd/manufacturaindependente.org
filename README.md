## Estrutura de ficheiros

Todo o conteúdo está no diretório `content`, que tem vários subdiretórios:

  * `portfolio-en`
  * `portfolio-pt`
  * `posts-en`
  * `posts-pt`
  * `talks-en`
  * `talks-pt`
  * `workshops-en`
  * `workshops-pt`
  * `pages` -- Páginas estáticas (about, about-pt, 404 e 500)
  * `private` -- Documentos privados para ser passados a outros; não são
    linkados no index, mas podem ser acedidos diretamente pelo URL. Todos os
    documentos lá dentro têm de ter a linha `Status: draft` no cabeçalho.
  * `files` -- Dump de ficheiros; são acessíveis em
    http://manufacturaindependente.org/files
  * `extra` -- Ficheiros estáticos para ser copiados para o server (htaccess). É
    preciso editar o campo EXTRA_FILE_METADATA no pelicanconf.py quando
    adicionarmos ficheiros aqui.

## Instalar todas as dependências

 * `sudo apt-get install python-dev` (para poder compilar o Pillow)

## Atualizar o site

Para re-gerar todo o site:

    make build

Para ver que ficheiros vão ser acrescentados, apagados ou atualizados no
servidor, antes de os enviar de vez para o site live:

    make rsync_upload_dry

Se tudo parecer ok, é hora de atualizar o site live!

    make rsync_upload

Os dois últimos comandos re-geram todo o site, por isso não é preciso fazer
`make html` antes.
