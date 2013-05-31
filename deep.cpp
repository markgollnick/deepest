#include "builtin.hpp"
#include "os/__init__.hpp"
#include "stat.hpp"
#include "sys.hpp"
#include "os/path.hpp"
#include "deep.hpp"

namespace __deep__ {

str *const_0, *const_1, *const_10, *const_11, *const_12, *const_2, *const_3, *const_4, *const_5, *const_6, *const_7, *const_8, *const_9;


str *VERSION, *__name__, *deepest_path, *longest_file;
__ss_int breadth, max_depth, max_length, now_depth, now_length;



void *_get_depth(str *_, str *dirname, list<str *> *names) {
    /**
    Function called during `os.path.walk` directory traversal.
    
    `os.path.walk` is deprecated, but `os.walk` is not yet implemented in
    ShedSkin.
    
    @param dirname: The name of the directory currently being examined.
    @type  dirname: str
    @param names: The list of file names residing within the current directory.
    @type  names: list or iterable
    */
    
    breadth = (breadth+1);
    now_length = ___max(2, 0, max_length, len(dirname));
    now_depth = len(dirname->split(__os__::__path__::sep));
    now_depth = ___max(2, 0, max_depth, (now_depth-1));
    if ((max_length<now_length)) {
        max_length = now_length;
        longest_file = dirname;
    }
    if ((max_depth<now_depth)) {
        max_depth = now_depth;
        deepest_path = dirname;
    }
    print_update(breadth, max_length, max_depth);
    return NULL;
}

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
    print2(NULL,0,1, __modct(const_5, 1, longest_file));
    print2(NULL,0,1, __modct(const_6, 1, deepest_path));
    return NULL;
}

void *__ss_main() {
    /**
    Program entry.
    */
    str *path;
    __ss_bool __10, __9;

    path = const_7;
    if ((len(__sys__::argv)>1)) {
        path = (__sys__::argv)->__getfast__(1);
    }
    if ((__eq(path, const_8) or __eq(path, const_9))) {
        print2(NULL,0,1, __modct(const_10, 1, VERSION));
    }
    else {
        print_header();
        __os__::__path__::walk(path, _get_depth, const_4);
        print_footer();
    }
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
    const_7 = __char_cache[46];;
    const_8 = new str("--help");
    const_9 = new str("--version");
    const_10 = new str("\ndeep\nVersion %s\nWritten by Mark R. Gollnick <mark.r.gollnick@gmail.com> &#10013;\nBoost Software License, Version 1.0: boost.org/LICENSE_1_0.txt\nDetermines the maximum depth of the current (or a specified) directory tree.\n\nusage:\n\n    deep [dir]\n\noutput:\n\n    breadth of dirs examined    longest pathname    deepest directory\n                        1000                  55                    5\n\n    longest file: C:\\some\\really\\long\\filename_that_should_be_renamed.txt\n    deepest path: C:\\dwarves\\digging\\deep\\deeper\\deepest\\balrog.log\n");
    const_11 = new str("0.9, 2013-05-31");
    const_12 = new str("__main__");

    __name__ = new str("__main__");

    VERSION = const_11;
    breadth = 0;
    now_length = 0;
    now_depth = 0;
    max_length = 0;
    max_depth = 0;
    longest_file = const_4;
    deepest_path = const_4;
    if (__eq(__name__, const_12)) {
        __ss_main();
    }
}

} // module namespace

int main(int __ss_argc, char **__ss_argv) {
    __shedskin__::__init();
    __stat__::__init();
    __os__::__path__::__init();
    __os__::__init();
    __sys__::__init(__ss_argc, __ss_argv);
    __shedskin__::__start(__deep__::__init);
}
