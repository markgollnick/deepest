#! /usr/bin/env make -f

# Phony target (targets in this list can always be re-run, regardless of state)
.PHONY: \
		all \
		build-cpp \
		build-python \
		clean \
		compile-cpp \
		cpp \
		package-python \
		python \
		validate-readme

define HELP_TEXT
Select a target:

  make python  # (build-python, package-python)
  make cpp     # (compile-cpp, build-cpp)
  make clean   # (removes compiled C++/Python)

endef
export HELP_TEXT


# Default target

all:
	@echo "$$HELP_TEXT"


# Python targets

python: clean build-python package-python

build-python: validate-readme
	python setup.py build

package-python: validate-readme
	python setup.py sdist

validate-readme:
	python -m setup check -r -s


# C++ targets

cpp: compile-cpp build-cpp

compile-cpp:
	cd deepest; ../3to2 .
	cd deepest; shedskin deepest.py

build-cpp:
	cd deepest; make
	cd deepest; git checkout -- .


# Cleanup

clean:
	rm -rf build
	rm -rf dist
	rm -f deepest/Makefile
	rm -f deepest/deepest{,.exe}
	find . -iname "*.pyc" -print -exec rm -f \{\} \;
	find . -iname "*pp" -print -exec rm -f \{\} \;
	cd deepest; git checkout -- .
