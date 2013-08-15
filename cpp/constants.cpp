#include "builtin.hpp"
#include "constants.hpp"

namespace __constants__ {

str *const_0, *const_1;


str *DESCRIPTION, *VERSION, *__name__;



void __init() {
    const_0 = new str("1.1, 2013-08-15");
    const_1 = new str("\ndeep\nVersion %s\nWritten by Mark R. Gollnick <mark.r.gollnick@gmail.com> &#10013;\nBoost Software License, Version 1.0: boost.org/LICENSE_1_0.txt\nDetermines the maximum depth of the current (or a specified) directory tree.\n\nusage:\n\n    deep [dir]\n\noutput:\n\n    breadth of dirs examined    longest pathname    deepest directory\n                          12                  59                    7\n\n    longest file: c:\\workspace\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log\n    deepest path: c:\\workspace\\some\\really\\long\\directory\\chain\\here\n");

    __name__ = new str("constants");

    VERSION = const_0;
    DESCRIPTION = __modct(const_1, 1, VERSION);
}

} // module namespace

