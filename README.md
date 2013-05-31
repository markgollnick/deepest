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
* g++ >= 4.6.2 — *optional*
* MinGW — *optional*


Installation
------------

**Python:**

* Proper Python packaging coming soon. For now, `python deep.py` works.

**C++:**

1. Download and install [ShedSkin][].
2. Edit `Makefile.shedskin` to match the paths on your system.
3. Run `make build`.


Usage
-----

    deep [dir]


Output
------

    breadth of dirs examined    longest pathname    deepest directory
                        1000                  55                    5

    longest file: C:\some\really\long\filename_that_should_be_renamed.txt
    deepest path: C:\dwarves\digging\deep\deeper\deepest\balrog.log


Limitations
-----------

Does not currently take filenames into account when calculating max pathname
length. Will be added later (hence version 0.9).


License
-------

Boost Software License, Version 1.0: <http://www.boost.org/LICENSE_1_0.txt>
