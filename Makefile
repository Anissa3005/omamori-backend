PY = python3
VENV = venv
BIN=$(VENV)/bin
ACTIVATE = $(BIN)/activate
ACTIVATE_CMD = . $(ACTIVATE)

# make it work on windows too
ifeq ($(OS), Windows_NT)
	BIN=$(VENV)/Scripts
	ACTIVATE = $(BIN)/activate
	PY=python
	ACTIVATE_CMD = call $(ACTIVATE)
endif

$(VENV): requirements.txt
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -r requirements.txt

.PHONY: createvenv install test runserver

createvenv:
	@echo 📁 Creating venv file...
	$(PY) -m venv $(VENV)

install:
	@echo ⚙️ Install packages...
	pip install -r requirements.txt

test: 
	@echo 🧪 Running tests... 🧪
	$(PY) manage.py test

runserver:
	@echo 🚀 Starting server... 🚀
	$(PY) manage.py runserver

