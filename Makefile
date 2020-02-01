PY?=python
PELICAN?=pelican
PELICANOPTS=
LOAD_VENV_CMD=. `pwd`/.env/bin/activate

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=opal5.opalstack.com
SSH_PORT=22
SSH_USER=manufactura
SSH_TARGET_DIR=/home/manufactura/apps/static-manufactura

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

install:
	virtualenv .env --no-site-packages --distribute
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
	$(LOAD_VENV_CMD); $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

deploy: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dry-deploy: publish
	rsync -n -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload github
