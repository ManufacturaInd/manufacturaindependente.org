PY?=python
PELICAN?=pelican
PELICANOPTS=
LOAD_VENV_CMD=. `pwd`/.env/bin/activate

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=dh
SSH_PORT=22
SSH_USER=rlaf
SSH_TARGET_DIR=/home/rlaf/www/manufacturaindependente.org

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make build                       (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo '                                                                       '

install:
	virtualenv .env --no-site-packages --distribute --prompt=\(manufactura\)
	$(LOAD_VENV_CMD); pip install -r requirements.txt

build:
	$(LOAD_VENV_CMD); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(LOAD_VENV_CMD); $(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(LOAD_VENV_CMD); pelican --listen
else
	$(LOAD_VENV_CMD); pelican --listen
endif

devserver:
ifdef PORT
	. `pwd`/.env/bin/activate; $(BASEDIR)/develop_server.sh restart $(PORT)
else
	. `pwd`/.env/bin/activate; $(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	. `pwd`/.env/bin/activate; $(LOAD_VENV_CMD); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

deploy: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dry-deploy: publish
	rsync -n -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload github
