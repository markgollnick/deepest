deep
====

![Diavik Diamond Mine, Canada](http://content.screencast.com/users/markgollnick/folders/Jing/media/ef41e433-1177-42fd-9b1b-783385c29044/deep.jpg)

> *“There are older and fouler things than Orcs in the deep places of the
> world.”*
> 
> *— Gandalf, from “The Lord of the Rings: The Fellowship of the Ring”,
> by J.R.R. Tolkein*

***deep*** — A command-line utility written to determine the maximum depth of
the current (or a specified) directory tree.

Available in both Python and C++ flavors (via the [ShedSkin][] libraries).

[ShedSkin]: https://code.google.com/p/shedskin/


Rationale
---------

* Needed a way to determine how close a project was getting to the
  8-subdirectory limit defined by ISO-9660.
* Needed a way to determine how close to `MAX_PATH` directories were getting.
    * `MAX_PATH` is defined as 260 characters on Windows: 3 for the drive (e.g.
      `C:\`), 1 for the terminating `NULL` character at the end, and 256 for
      the directories, back-slashes, filenames, and extensions in the middle.

* “Yes, but… Why Python?”
    * It’s faster to write, for me.
    * It gave me an excuse to try out [ShedSkin][]. :-)


Requirements
------------

* Python >= 2.6
* ShedSkin >= 0.9.3 — *optional*
* g++ >= 4.6.2 or clang++ >= 3.2 — *optional*
* MinGW — *optional*


Installation
------------

**Python:**

    python setup.py build install

**C++:**

1. Download and install [ShedSkin][].
2. Edit the `Makefile` and change paths to match those on your system.
3. Run `make cpp`.


Usage
-----

**Python:**

With Python, you can use it as a program…

    $ python -m deep.deep c:\\workspace
    breadth of dirs examined    longest pathname    deepest directory
                          12                  59                    7

    longest file: c:\workspace\dwarves\digging\deep\deeper\deepest\balrog.log
    deepest path: c:\workspace\some\really\long\directory\chain\here

…or, you can use it as a library:

    >>> import deep
    >>> deep.get_depth('c:\\workspace')
    ('c:\\workspace\\some\\really\\long\\directory\\chain\\here', 7)
    >>> deep.get_length('c:\\workspace')
    ('c:\\workspace\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log', 59)

**C++:**

    $ deep c:\\workspace
    breadth of dirs examined    longest pathname    deepest directory
                          12                  59                    7

    longest file: c:\workspace\dwarves\digging\deep\deeper\deepest\balrog.log
    deepest path: c:\workspace\some\really\long\directory\chain\here


Speed
-----

In a project containing over 6000 directories with a max depth of 14, the
Python and C++ versions (g++-4.6.2 compiled) were pitted against one another.
Both versions were run three times each on a Windows 7 x64 machine (though in
both cases the programs were run in 32-bit mode) with an Intel Core i7 CPU.

These are the averaged results:

    $ time python -m deep.deep ...
    ...
    real    0m31.571s
    user    0m0.010s
    sys     0m0.015s

    $ time deep.exe ...
    ...
    real    0m28.047s
    user    0m0.000s
    sys     0m0.015s

Thus, using the C++ version may gain you about a 10% speed boost. :-)


License
-------

Boost Software License, Version 1.0: <http://www.boost.org/LICENSE_1_0.txt>
