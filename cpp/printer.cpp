#include "builtin.hpp"
#include "sys.hpp"
#include "printer.hpp"
#include "globals.hpp"

namespace __printer__ {

str *const_0, *const_1, *const_2, *const_3, *const_4, *const_5, *const_6;


str *__name__;



void *print_header() {
    /**
    Prints a table header to be displayed during directory traversal.
    */
    
    print2(NULL,0,1, const_0);
    print2(NULL,0,1, const_1);
    return NULL;
}

void *print_update(__ss_int breadth, __ss_int length, __ss_int depth) {
    /**
    Updates the results table with the new information.
    
    Will only work on consoles that support ANSI escape character sequences.
    Otherwise, will print a line-by-line series of updates. Workable, but ugly.
    
    @param breadth: The number of directories that have been examined.
    @type  breadth: int
    @param length: The current largest length of a path, in characters.
    @type  length: int
    @param depth: The current deepest level in a path, in subdirectories.
    @type  depth: int
    */
    __ss_int _, __3, __4, __5, __6, __7, __8;

    (__sys__::__ss_stdout)->write(const_2);

    FAST_FOR(_,0,(24-len(__str(breadth))),1,3,4)
        (__sys__::__ss_stdout)->write(const_3);
    END_FOR

    (__sys__::__ss_stdout)->write(__str(breadth));

    FAST_FOR(_,0,(20-len(__str(length))),1,5,6)
        (__sys__::__ss_stdout)->write(const_3);
    END_FOR

    (__sys__::__ss_stdout)->write(__str(length));

    FAST_FOR(_,0,(21-len(__str(depth))),1,7,8)
        (__sys__::__ss_stdout)->write(const_3);
    END_FOR

    (__sys__::__ss_stdout)->write(__str(depth));
    print2(NULL,0,1, const_4);
    return NULL;
}

void *print_footer() {
    /**
    Prints the footer for the results table, containing the longest path and
    deepest directory encountered.
    */
    
    print2(NULL,0,1, const_4);
    print2(NULL,0,1, __modct(const_5, 1, __globals__::longest_file));
    print2(NULL,0,1, __modct(const_6, 1, __globals__::deepest_path));
    return NULL;
}

void __init() {
    const_0 = new str("breadth of dirs examined    longest pathname    deepest directory");
    const_1 = new str("                       0                   0                    0");
    const_2 = new str("\033[#F");
    const_3 = __char_cache[32];;
    const_4 = new str("");
    const_5 = new str("longest file: %s");
    const_6 = new str("deepest path: %s");

    __name__ = new str("printer");

}

} // module namespace

