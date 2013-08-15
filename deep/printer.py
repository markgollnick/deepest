import sys

import globals # Needed for ShedSkin


def print_header():
    """
    Prints a table header to be displayed during directory traversal.
    """
    print 'breadth of dirs examined    longest pathname    deepest directory'
    print '                       0                   0                    0'


def print_update(breadth, length, depth):
    """
    Updates the results table with the new information.

    Will only work on consoles that support ANSI escape character sequences.
    Otherwise, will print a line-by-line series of updates. Workable, but ugly.

    @param breadth: The number of directories that have been examined.
    @type  breadth: int
    @param length: The current largest length of a path, in characters.
    @type  length: int
    @param depth: The current deepest level in a path, in subdirectories.
    @type  depth: int
    """
    sys.stdout.write('\x1b[#F') # move the cursor back to the previous line
    for _ in range(24 - len(str(breadth))):
        sys.stdout.write(' ')
    sys.stdout.write(str(breadth))
    for _ in range(20 - len(str(length))):
        sys.stdout.write(' ')
    sys.stdout.write(str(length))
    for _ in range(21 - len(str(depth))):
        sys.stdout.write(' ')
    sys.stdout.write(str(depth))
    print '' # newline


def print_footer():
    """
    Prints the footer for the results table, containing the longest path and
    deepest directory encountered.
    """
    print ''
    print 'longest file: %s' % globals.longest_file
    print 'deepest path: %s' % globals.deepest_path
