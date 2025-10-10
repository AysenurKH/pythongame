# Python Game

## About this project

### Game

This is a Python implementation of the dice game "Pig". 

---

## How to run

This project comes with a Makefile which should handle all necessary setup for you, and it allows you to generate documentation, uml diagrams, run tests, and more.
Make needs to installed, and should probably be run from a UNIX terminal (Mac, Linux, or with tools like WSL in Windows)

Install Make and Graphviz on your computer. These are needed and are not installed automatically or by default.

It's not necessary to manually install any other dependencies, as this is handled automatically by the Makefile.

### List of Make targets

`make run` 

Runs the game.

`make build` 

Refreshes the dependencies in the virtual environment, runs the linter, runs the tests, and finally outputs docs and uml.

`make clean` 

Deletes all dependencies and output directories that are created via the other make targets.

`make doc`

Creates documentation .html files.

`make lint` 

Runs the linter. Checks syntax, naming, docstring formatting, etc.

`make uml` 

Creates classes diagram and packages diagram.

`make test`

Runs the full test suite.

`make coverage`
 
Displays the full test coverage report.

---

## Technical details for developers

### Make

You can install make on Windows with `winget install ezwinports.make` or by other means, but you still cannot run the other UNIX comands like `rm -rf`.
For this reason, I recommend using a WSL terminal on Windows. 

We are using a virtual environment in python, and this is where dependencies are installed, but this virtual environment is activated in the `$(VENV)/bin/activate` 
make target. If I then want to use one of the installed dependencies in a different make target, like `make lint` which uses flake8, 
it is not enough to say that the `lint` target depends on `$(VENV)/bin/activate`. It just ensures that `$(VENV)/bin/activate` is called before `lint`, 
but since every make target (and indeed every line within each target) is run in a separate terminal process, we will run into an issue: 
When a make target depends on `$(VENV)/bin/activate`, it means that we activates the virtual environment in one terminal, 
immediately close the terminal, and then try to use flake8 in a new terminal, causing the flake8 command to fail because we are no longer in the virtual environment, and the 
flake8 package cannot be found. For this reason, I needed to manually activate the virtual environment in these make targets, and combine the individual lines with ;\\
to ensure that all lines are sent together as a single command to the terminal. 

Somehow it is possible to run pdoc without without first activating the virtual environment, if it is passed to the python interpreter as a module (`python -m pdoc`).
 I am not sure why this works. 

### UML

Pylint already comes with the "pyreverse" library which is able to output a couple different formats.
There's PUML and Mermaid, which are natively supported and can be rendered with different external tools, but in order to directly output an image format like .png,
 the software Graphviz needs to be installed. Pyreverse will then output a .gv (graphviz) file, which is sent to Graphviz. 

https://pylint.readthedocs.io/en/latest/additional_tools/pyreverse/configuration.html#output
https://pylint.readthedocs.io/en/latest/additional_tools/pyreverse/index.html#output-formats

There is a python package with the name "graphviz", but it doesn't seem to work in my case.

Additionally, pyreverse is not able to create the output directory if it doesn't already exists. For this reason, the `uml` make target creates the folder first
before running pyreverse.

### Documentation

I'm using pdoc for generating .html documentation from docstrings. Pdoc is very quick and easy to set up, and it ran perfectly straight out of the box.

Sphinx seemed very complex, and I struggled to understand how to set it up, so I have not used Sphinx.

### Graphviz installation instructions

As mentioned above, Graphviz must be installed **on your system, not as a dependency via pip**.

#### Windows
If running `make` through WSL on Windows, install it with `sudo apt install graphviz` inside of your WSL terminal. 
This installs Graphviz in your Linux virtual machine.

If you don't use WSL, install Graphviz directly on your Windows machine via https://www.graphviz.org/download/

### Test coverage

There are a few ways to get test coverage reports. You can either use Coverage.py, or the pytest-cov plugin for pytest.

I just picked the pytest-cov plugin because I already had pytest. Not sure if Coverage.py is any better.

### Pyreverse flags

I'm using -ASmy which is shorthand for -A -S -m[y]. It does the following:

* --all-ancestors, -A
  * show all ancestors off all classes in "projects" (default: None)
* --all-associated, -S
  * show recursively all associated off all associated classes (default: None)
* --module-names -m (y or n)
  * include module name in representation of classes (default: None)

### Modules

I wanted to split my project into different folders, but this messes with a lot of my dependencies and installed packages. 

Normal folders are considered "Namespace packages", and these are not traversed recursively by some of my dependencies. To fix this, I added a 
__init__.py file in each folder, which converts them into "modules". 

### Configuration file

It's possible to have a single configuration file (tox.ini, setup.cfg) which is split up into sections. The different dependencies all share this
configuration file, and the different sections in the file configure different dependencies. 

I chose to not do it this way, because it feels simpler and more understandable to have separate configuration files for each dependency.

### Linting

I use `flake8` and `pylint` for linting. 

#### Pylint

Pylint returns a [bit-encoded error code](https://pylint.pycqa.org/en/latest/user_guide/usage/run.html#exit-codes). This error code is then printed by make, 
resulting in an output like `make: *** [Makefile:36: lint] Error 4`. This looks like an error in the Makefile, but it's not. Error 4 indicates a warning. 

If both a warning and a conventional message is issued, it would return error 20 (4 + 16).

Pylint is configured via the .pylintrc configuration file, as per the `--rcfile` flag when invoking pylint. It can be left empty to use the default configuration. 
For demonstration purposes, I just copy pasted a configuration file from the internet, and made some changes, but it can of course be further customized.

#### Flake8

(TODO: Don't really know why we are using both Flake8 and Pylint, and if Flake8 does anything by itself without extensions?)

Flake8 is a linter that supports various extensions that check different things. I am using flake8-docstrings to check docstrings, which is installed in the virtual environment.

Additionally, the linting options can be configured with a .flake8 file in the project root.

Flake8 is smart enough that it can auto-detect the .flake8 configuration file, and it checks all files in the projects by default, but for good measure I have manually 
selected the .flake8 file location and src directory in the call to flake8 in the Makefile.

Flake8 uses the concept of "error codes". Each error has a specific error code associated with it. For example, error code `D404` is returned when a
docstring starts with the word "this". For the sake of demonstration, I have excluded this specific error code in the .flake8 configuration file.

### Virtual environment & dependencies

I'm using a requirements.txt file to define exactly which dependencies my application needs.

In order to not permanently clutter my (or your) computer with python packages, and in order to avoid package version conflicts, I am using
a virtual environment. The purpose of this virtual environment is that all packages my game needs are installed in a temporary
location while running the game, and afterwards they can deleted. They will not interfere with other Python applications. 

Another benefit is that I have full control over which dependencies my application is using, and exactly which versions, as it's not possible to access 
dependencies installed globally from a virtual environment.
This means that the list of dependencies in requirements.txt is all that I'm using when running my application, so I can be fairly confident that
if I send my project to somebody else, it will work there as well.

If I need to install, uninstall or change the version of dependencies, I can easily just update the requirements.txt file, 
delete the `venv` directory and re-generate it. This is handled automatically with the Makefile, because the various targets depend on the
`$(VENV)/bin/activate` command, which in turn depends on the requirements.txt file, so the virtual environment is only regenerated when the requirements.txt file has been changed.

#### Type hints (TODO: ??, how to enforce? Write something here)