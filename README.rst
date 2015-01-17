deepest
=======

.. image:: https://travis-ci.org/markgollnick/deepest.svg?branch=master
    :target: https://travis-ci.org/markgollnick/deepest
    :alt: Build Status

.. image:: https://coveralls.io/repos/markgollnick/deepest/badge.svg?branch=master
    :target: https://coveralls.io/r/markgollnick/deepest?branch=master
    :alt: Coverage Status

.. image:: http://content.screencast.com/users/markgollnick/folders/Jing/media/ef41e433-1177-42fd-9b1b-783385c29044/deep.jpg
    :alt: Diavik Diamond Mine, Canada

..

    *“There are older and fouler things than Orcs in the deep places of the
    world.”*

    *— Gandalf, from “The Lord of the Rings: The Fellowship of the Ring”, by
    J.R.R. Tolkein*

**deepest** — A cross-platform (and cross-language) command-line utility used
to determine the maximum depth of the current (or a specified) directory tree.

Available in both Python and C++ flavors (via the `ShedSkin`_ libraries).

.. _ShedSkin: https://code.google.com/p/shedskin/


Rationale
---------

*   Needed a way to determine how close a project was getting to the
    8-subdirectory limit defined by ISO-9660.

*   Needed a way to determine how close to ``MAX_PATH`` directories were
    getting.

    *   ``MAX_PATH`` is defined as 260 characters on Windows: 3 for the drive
        (``C:\``), 1 for the terminating ``NULL`` character at the end, and 256
        for directories, back-slashes, filenames, and extensions in the middle.

*   “Yes, but… Why Python?”

    *   It’s faster for prototyping. (Bias… I’m just more familiar with it.)
    *   It gave me an excuse to try out `ShedSkin`_. :-)


Requirements
------------

* Python >= 2.6, 2.7, 3.2, 3.3, 3.4, possibly more…
* ShedSkin >= 0.9.3, 0.9.4 — *optional*
* g++ >= 4.6.2 or clang++ >= 3.2 — *optional*
* MinGW/MSYS (2012-04-26 catalog) — *optional*


Installation
------------

**Python (Users)**::

    pip install deepest

**Python (Developers)**::

    git clone git@github.com:markgollnick/deepest.git
    cd deepest
    python setup.py build install
    # Alternatively...
    make python
    pip install dist/deepest-*.tar.gz

**C++**:

1.  Download and install `ShedSkin`_ (`instructions`_).
2.  Run the following::

        ./3to2  # Make some minor adjustments for ShedSkin compatibility
        cd deepest  # This is the dir INSIDE the project's root dir
        shedskin deepest.py
        make
        # Alternatively, from the project's root dir...
        make cpp

.. _instructions: https://code.google.com/p/shedskin/wiki/docs#Installation


Usage
-----

**Python:**

Once installed, you can use it as a script…

::

    $ deepest .
    breadth of dirs examined    longest pathname    deepest directory
                          13                  58                    7

    longest file: ./workspace/dwarves/digging/deep/deeper/deepest/balrog.log
    deepest path: ./workspace/some/really/long/directory/chain/here

…or, you can use it as a library::

    >>> import deepest
    >>> deepest.get_depth('c:\\workspace')
    ('c:\\workspace\\some\\really\\long\\directory\\chain\\here', 7)
    >>> deepest.get_length('c:\\workspace')
    ('c:\\workspace\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log', 59)

**C++:**

Once compiled, it is a (notably faster) alternative to the Python script::

    $ deepest c:\\workspace
    breadth of dirs examined    longest pathname    deepest directory
                          13                  59                    7

    longest file: c:\workspace\dwarves\digging\deep\deeper\deepest\balrog.log
    deepest path: c:\workspace\some\really\long\directory\chain\here


Speed
-----

In a project containing well over 5000 directories with a max depth of 13, the
Python and C++ versions (compiled with clang-503.0.40) were pitted against each
other. Both versions were run three times each on a Late 2013 Mac Book Pro.

These are the averaged results::

    $ time deepest  # Python script
    ...
    real    0m0.423s
    user    0m0.244s
    sys     0m0.160s

    $ time deepest  # C++ binary
    ...
    real    0m0.169s
    user    0m0.063s
    sys     0m0.101s

In practical observation, using the compiled C++ version may gain you anywhere
from a 10% to a whopping 60% boost in speed. :-)


License
-------

Boost Software License, Version 1.0: <http://www.boost.org/LICENSE_1_0.txt>
