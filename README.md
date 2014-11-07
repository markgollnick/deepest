deep
====

[![Build Status](https://travis-ci.org/markgollnick/deep.svg?branch=master)](https://travis-ci.org/markgollnick/deep)
[![Coverage Status](https://img.shields.io/coveralls/markgollnick/deep.svg)](https://coveralls.io/r/markgollnick/deep?branch=master)

![Diavik Diamond Mine, Canada](http://content.screencast.com/users/markgollnick/folders/Jing/media/ef41e433-1177-42fd-9b1b-783385c29044/deep.jpg)

> *“There are older and fouler things than Orcs in the deep places of the
> world.”*
> 
> *— Gandalf, from “The Lord of the Rings: The Fellowship of the Ring”,
> by J.R.R. Tolkein*

***deep*** — A cross-platform (and cross-language) command-line utility written
to determine the maximum depth of the current (or a specified) directory tree.

Available in both Python and C++ flavors (via the [ShedSkin][] libraries).

[ShedSkin]: https://code.google.com/p/shedskin/


Rationale
---------

*   Needed a way to determine how close a project was getting to the
    8-subdirectory limit defined by ISO-9660.

*   Needed a way to determine how close to `MAX_PATH` directories were getting.
    *   `MAX_PATH` is defined as 260 characters on Windows: 3 for the drive
        (`C:\`), 1 for the terminating `NULL` character at the end, and 256 for
        the directories, back-slashes, filenames, and extensions in the middle.

*   “Yes, but… Why Python?”
    *   It’s faster for prototyping. (Bias… I’m just more familiar with it.)
    *   It gave me an excuse to try out [ShedSkin][]. :-)


Requirements
------------

* Python >= 2.6, 2.7, 3.2, 3.3, 3.4, possibly more…
* ShedSkin >= 0.9.3, 0.9.4 — *optional*
* g++ >= 4.6.2 or clang++ >= 3.2 — *optional*
* MinGW/MSYS (2012-04-26 catalog) — *optional*


Installation
------------

**Python (Users):**

    pip install git+ssh://git@github.com/markgollnick/deep@v1.3.0#egg=deep-1.3.0

**Python (Developers):**

    git clone git@github.com:markgollnick/deep.git
    cd deep
    python setup.py build install
    # Alternatively...
    make python
    pip install dist/deep-1.3.0.tar.gz

**C++:**

1.  Download and install [ShedSkin][] ([instructions][]).
2.  Run the following:

        cd deep  # this is the dir INSIDE the project's root dir...
        shedskin deep.py
        make
        # Alternatively, from the project's root dir...
        make cpp

[instructions]: https://code.google.com/p/shedskin/wiki/docs#Installation


Usage
-----

**Python:**

Once installed, you can use it as a script…

    $ deep .
    breadth of dirs examined    longest pathname    deepest directory
                          13                  58                    7

    longest file: ./workspace/dwarves/digging/deep/deeper/deepest/balrog.log
    deepest path: ./workspace/some/really/long/directory/chain/here

…or, you can use it as a library:

    >>> import deep
    >>> deep.get_depth('c:\\workspace')
    ('c:\\workspace\\some\\really\\long\\directory\\chain\\here', 7)
    >>> deep.get_length('c:\\workspace')
    ('c:\\workspace\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log', 59)

**C++:**

Once compiled, it is a (notably faster) alternative to the Python script:

    $ deep c:\\workspace
    breadth of dirs examined    longest pathname    deepest directory
                          13                  59                    7

    longest file: c:\workspace\dwarves\digging\deep\deeper\deepest\balrog.log
    deepest path: c:\workspace\some\really\long\directory\chain\here


Speed
-----

In a project containing well over 5000 directories with a max depth of 13, the
Python and C++ versions (compiled with clang-503.0.40) were pitted against each
other. Both versions were run three times each on a Late 2013 Mac Book Pro.

These are the averaged results:

    $ time deep
    ...
    real    0m0.423s
    user    0m0.244s
    sys     0m0.160s

    $ time deep
    ...
    real    0m0.169s
    user    0m0.063s
    sys     0m0.101s

In practical observation, using the compiled C++ version may gain you anywhere
from a 10% to a whopping 60% boost in speed. :-)


License
-------

Boost Software License, Version 1.0: <http://www.boost.org/LICENSE_1_0.txt>
