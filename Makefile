all:
	@echo Select a target:
	@echo \ \ \ \ make python \(build-python, package-python\)
	@echo \ \ \ \ make cpp \ \ \ \(compile-cpp, build-cpp\)
	@echo \ \ \ \ make clean \ \(removes compiled C++/Python\)


# Python targets

python: build-python package-python

build-python:
	python setup.py build

package-python:
	python setup.py sdist


# C++ targets

cpp: compile-cpp build-cpp

compile-cpp:
	cd deep; shedskin deep.py

build-cpp:
	cd deep; make


# Cleanup

clean:
	rm -rf build
	rm -rf dist
	rm -f deep/Makefile
	rm -f deep/deep{,.exe}
	find . -iname "*.pyc" -print -exec rm -f \{\} \;
	find . -iname "*pp" -print -exec rm -f \{\} \;
