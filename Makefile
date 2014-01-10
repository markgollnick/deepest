SSINCLUDE=c:\\shedskin\\include
SSLIB=c:\\shedskin\\lib


all:
	@echo Select a target:
	@echo \ \ \ \ make python \(build-python, install-python\)
	@echo \ \ \ \ make cpp \ \ \ \(compile-cpp, build-cpp\)
	@echo \ \ \ \ make clean \ \(removes compiled C++/Python\)
	@echo 
	@echo Note for C++ builders:
	@echo \ \ \ \ You need to open ./Makefile and set the
	@echo \ \ \ \ SSINCLUDE and SSLIB variables to point to
	@echo \ \ \ \ your installation of Shedskin.


# Python targets

python: build-python install-python

build-python:
	python setup.py build

install-python:
	python setup.py install


# C++ targets
cpp: compile-cpp build-cpp

compile-cpp:
	cd deep; shedskin -mMakefile.shedskin deep.py
	if [ ! -e "cpp" ]; then mkdir cpp; fi
	mv deep/*pp cpp/
	mv deep/Makefile.shedskin cpp/Makefile.edit
	@cat cpp/Makefile.edit | sed 's/deep\([\/]\)deep./deep\1cpp\1/g' > cpp/Makefile.shedskin
	@rm -f cpp/Makefile.edit

build-cpp:
	cd cpp; export CPPFLAGS="-I$(SSINCLUDE)"; export LDFLAGS="-L$(SSLIB)"; make -f Makefile.shedskin
	if [ ! -e "build" ]; then mkdir build; fi
	if [ -e "cpp/deep" ]; then mv cpp/deep build/; fi
	if [ -e "cpp/deep.exe" ]; then mv cpp/deep.exe build/; fi


# Cleanup

clean:
	rm -rf cpp
	rm -rf build
