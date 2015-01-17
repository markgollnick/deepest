"""Printer for running on the command-line, and not as a library."""

import sys

from os import linesep

from . import globals  # Needed for ShedSkin


def print_header():
    """
    Print a table header to be displayed during directory traversal.

    The header consists of the number of directories traversed, the length of
    the longest pathname encountered, and the depth of the deepest directory
    encountered thus far.
    """
    txt = 'breadth of dirs examined    longest pathname    deepest directory'
    sys.stdout.write(txt + linesep)


def print_update(breadth, length, depth):
    """
    Update the results table with new information.

    Will only work on consoles that support ANSI escape character sequences.
    Otherwise, will print a line-by-line series of updates. Workable, but ugly.

    @param breadth: The number of directories that have been examined.
    @type breadth: int
    @param length: The current largest length of a path, in characters.
    @type length: int
    @param depth: The current deepest level in a path, in subdirectories.
    @type depth: int
    """
    sys.stdout.write('\r')  # Restore cursor position
    for _ in range(24 - len(str(breadth))):
        sys.stdout.write(' ')
    sys.stdout.write(str(breadth))
    for _ in range(20 - len(str(length))):
        sys.stdout.write(' ')
    sys.stdout.write(str(length))
    for _ in range(21 - len(str(depth))):
        sys.stdout.write(' ')
    sys.stdout.write(str(depth))


def print_footer():
    """
    Print the footer for the results table.

    The footer contains the longest path and the deepest directory encountered.
    """
    sys.stdout.write(linesep + linesep)
    sys.stdout.write('longest file: %s' % globals.longest_file + linesep)
    sys.stdout.write('deepest path: %s' % globals.deepest_path + linesep)
