"""Constants File."""


VERSION = 'v2.0.0, 2014-12-14'

DESCRIPTION = """
deepest
Version %s
Written by Mark R. Gollnick <mark.r.gollnick@gmail.com> &#10013;
Boost Software License, Version 1.0: boost.org/LICENSE_1_0.txt
Determines the maximum depth of the current (or a specified) directory tree.

usage:

    deepest [dir]

output:

    breadth of dirs examined    longest pathname    deepest directory
                          12                  59                    7

    longest file: c:\\workspace\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log
    deepest path: c:\\workspace\\some\\really\\long\\directory\\chain\\here
""" % VERSION  # NOQA
