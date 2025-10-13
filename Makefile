.PHONY: doc

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
DOC = doc
APIDOC = $(DOC)/api
UML = $(DOC)/uml

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	## Needs to be run as a module because I am using modules. Running "$(PYTHON) src/pig_dice_game.py" would cause an error stating that module src cannot be found
	$(PYTHON) -m src.pig_dice_game

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf $(DOC)
	rm -rf .pytest_cache
	rm -f .coverage

doc: $(VENV)/bin/activate
	. $(VENV)/bin/activate; \
	pdoc -html src -o $(APIDOC)

test: $(VENV)/bin/activate
	. $(VENV)/bin/activate; \
	pytest src

coverage: $(VENV)/bin/activate
	. $(VENV)/bin/activate; \
	pytest --cov=src src
	## coverage run -m pytest ....

uml: $(VENV)/bin/activate
	mkdir -p $(UML)
	. $(VENV)/bin/activate; \
	pyreverse -ASmy --ignore tests -o png -p "Python Game" -d $(UML) src

lint: $(VENV)/bin/activate
	. $(VENV)/bin/activate; \
	pylint --rcfile=.pylintrc src; \
	flake8 --config=.flake8 src

black: $(VENV)/bin/activate
	. $(VENV)/bin/activate; \
	black src

build: $(VENV)/bin/activate lint test uml doc
