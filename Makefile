PY = python3
VENV = venv
BIN=$(VENV)/bin
ACTIVATE = $(BIN)/activate

# make it work on windows too
ifeq ($(OS), Windows_NT)
	BIN=$(VENV)/Scripts
	ACTIVATE = $(BIN)/activate
	PY=python
	ACTIVATE_CMD = call $(ACTIVATE)
else
	# For Unix-like systems
	ACTIVATE_CMD = . $(ACTIVATE)
endif

$(VENV): requirements.txt
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -r requirements.txt

.PHONY: test
test: $(VENV)
	@echo "Running tests"
	@$(ACTIVATE_CMD) && $(PY) manage.py test

