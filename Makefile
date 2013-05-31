all:
	make cpp
	make build

cpp: deep.py
	shedskin -mMakefile.shedskin deep.py

build: deep.cpp deep.hpp Makefile.shedskin
	make -f Makefile.shedskin

clean:
	rm -f *.exe *.o *pp *.shedskin
