#include "builtin.hpp"
#include "globals.hpp"

namespace __globals__ {

str *const_0;


str *__name__, *deepest_path, *longest_file;
__ss_int breadth, max_depth, max_length, now_depth, now_length;
__ss_bool runas_program;



void __init() {
    const_0 = new str("");

    __name__ = new str("globals");

    breadth = 0;
    now_length = 0;
    now_depth = 0;
    max_length = 0;
    max_depth = 0;
    longest_file = const_0;
    deepest_path = const_0;
    runas_program = False;
}

} // module namespace

