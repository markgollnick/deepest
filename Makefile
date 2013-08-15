all: python cpp build-cpp

install: install-python

build-cpp:
	cd cpp; make -f Makefile.shedskin
	if [ ! -e "build" ]; then mkdir build; fi
	if [ -e "cpp/deep" ]; then mv cpp/deep build/; fi
	if [ -e "cpp/deep.exe" ]; then mv cpp/deep.exe build/; fi

clean:
	rm -rf cpp
	rm -rf build

cpp:
	cd deep; shedskin -mMakefile.shedskin deep.py
	if [ ! -e "cpp" ]; then mkdir cpp; fi
	mv deep/*pp cpp/
	mv deep/Makefile.shedskin cpp/

install-python:
	python setup.py build install

python:
	python setup.py build
