all install: cpp build
	echo DONE! Now simply copy the deep executable to a directory on your PATH.

build:
	make -f Makefile.shedskin

cpp:
	shedskin -mMakefile.shedskin deep.py

clean:
	rm -f *.exe *.o *pp *.shedskin
