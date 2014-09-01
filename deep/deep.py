"""Deep: determine the maximum depth of a directory tree."""

import os
import sys

import globals  # Needed for ShedSkin

from constants import DESCRIPTION
from printer import print_header, print_footer
from traverser import traversal_callback


def get_depth(dirname):
    """
    Function for obtaining the deepest directory below `dirname`.

    @param dirname: The name of the directory to examine.
    @type  dirname: str
    @return       : The deepest directory, and its depth.
    @rtype        : tuple
    """
    os.path.walk(dirname, traversal_callback, '')
    return (globals.deepest_path, globals.max_depth)


def get_length(dirname):
    """
    Function for obtaining the longest file/path name in `dirname`.

    @param dirname: The name of the directory to examine.
    @type  dirname: str
    @return       : The longest path, and the path length.
    @rtype        : tuple
    """
    os.path.walk(dirname, traversal_callback, '')
    return (globals.longest_file, globals.max_length)


def main():
    """Program entry."""
    globals.runas_program = True

    path = '.'

    if len(sys.argv) > 1:
        path = sys.argv[1]

    if path == "--help" or path == "--version" or path == "-h":
        print(DESCRIPTION)

    else:
        print_header()
        os.path.walk(path, traversal_callback, '')
        print_footer()


if __name__ == "__main__":
    main()
