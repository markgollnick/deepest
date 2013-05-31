import os
import sys

VERSION = '0.9, 2013-05-31'

breadth = 0
now_length = 0
now_depth = 0
max_length = 0
max_depth = 0

longest_file = ''
deepest_path = ''


def _get_depth(_, dirname, names):
    """
    Function called during `os.path.walk` directory traversal.

    `os.path.walk` is deprecated, but `os.walk` is not yet implemented in
    ShedSkin.

    @param dirname: The name of the directory currently being examined.
    @type  dirname: str
    @param names: The list of file names residing within the current directory.
    @type  names: list or iterable
    """
    global breadth
    global now_length, now_depth, max_length, max_depth
    global longest_file, deepest_path

    breadth += 1

    now_length = max(max_length, len(dirname)) # TODO: Support file names also
    now_depth = len(dirname.split(os.path.sep))
    now_depth = max(max_depth, now_depth - 1)

    if max_length < now_length:
        max_length = now_length
        longest_file = dirname

    if max_depth < now_depth:
        max_depth = now_depth
        deepest_path = dirname

    print_update(breadth, max_length, max_depth)


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
    global longest_file, deepest_path
    print ''
    print 'longest file: %s' % longest_file
    print 'deepest path: %s' % deepest_path


def main():
    """
    Program entry.
    """
    path = '.'

    if len(sys.argv) > 1:
        path = sys.argv[1]

    if path == "--help" or path == "--version":
        print """
deep
Version %s
Written by Mark R. Gollnick <mark.r.gollnick@gmail.com> &#10013;
Determines the maximum depth of the current (or a specified) directory tree.

usage:

    deep [dir]

output:

    breadth of dirs examined    longest pathname    deepest directory
                        1000                  26                    2

    longest file: C:\\some\\really\\long\\filename_that_should_be_renamed.txt
    deepest path: C:\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log
""" % VERSION

    else:
        print_header()
        os.path.walk(path, _get_depth, '')
        print_footer()


if __name__ == "__main__":
    main()
