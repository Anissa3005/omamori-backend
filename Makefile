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
	$(BIN)/pip install -r requirements.txt

.PHONY: test runserver
test: $(VENV)
	@echo 🧪 Running tests... 🧪
	@$(ACTIVATE_CMD) && $(PY) manage.py test

runserver: $(VENV)
	@echo 🚀 Starting server... 🚀
	@$(ACTIVATE_CMD) && $(PY) manage.py runserver

