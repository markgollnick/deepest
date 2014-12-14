"""Logic for traversing the filesystem."""

import os

from . import globals  # Needed for ShedSkin

from .printer import print_update


def traversal_callback(_, dirname, files):
    """
    Function called during `os.path.walk` directory traversal.

    `os.path.walk` is deprecated, but `os.walk` is not yet implemented in
    ShedSkin.

    @param dirname: The name of the directory currently being examined.
    @type dirname: str
    @param files: The list of file names residing within the current directory.
    @type files: list or iterable
    """
    fullname = ''

    # "Breadth" is the total number of directories that have been examined.
    globals.breadth += 1

    # "Length" is the longest path name encountered during the traversal.
    if files:
        for filename in files:
            fullname = dirname + os.path.sep + filename
            globals.now_length = max(globals.max_length, len(fullname))
            if globals.max_length < globals.now_length:
                globals.max_length = globals.now_length
                globals.longest_file = fullname
    else:  # No files in this directory; check the name of the directory itself
        globals.now_length = max(globals.max_length, len(dirname))
        if globals.max_length < globals.now_length:
            globals.max_length = globals.now_length
            globals.longest_file = dirname

    # "Depth" is the largest subdirectory chain encountered during traversal.
    globals.now_depth = len(dirname.split(os.sep))
    globals.now_depth = max(globals.max_depth, globals.now_depth - 1)

    if globals.max_depth < globals.now_depth:
        globals.max_depth = globals.now_depth
        globals.deepest_path = dirname

    if globals.runas_program:
        print_update(globals.breadth, globals.max_length, globals.max_depth)
