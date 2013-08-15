#include "builtin.hpp"
#include "stat.hpp"
#include "os/path.hpp"
#include "os/__init__.hpp"
#include "sys.hpp"
#include "printer.hpp"
#include "deep.hpp"
#include "constants.hpp"
#include "globals.hpp"
#include "traverser.hpp"

namespace __deep__ {

str *const_0, *const_1, *const_2, *const_3, *const_4, *const_5;

using __printer__::print_header;
using __printer__::print_footer;
using __traverser__::traversal_callback;

str *DESCRIPTION, *__name__;



void *__ss_main() {
    /**
    Program entry.
    */
    str *path;
    __ss_bool __13, __14, __15;

    __globals__::runas_program = True;
    path = const_0;
    if ((len(__sys__::argv)>1)) {
        path = (__sys__::argv)->__getfast__(1);
    }
    if ((__eq(path, const_1) or __eq(path, const_2) or __eq(path, const_3))) {
        print2(NULL,0,1, DESCRIPTION);
    }
    else {
        print_header();
        __os__::__path__::walk(path, traversal_callback, const_4);
        print_footer();
    }
    return NULL;
}

void __init() {
    const_0 = __char_cache[46];;
    const_1 = new str("--help");
    const_2 = new str("--version");
    const_3 = new str("-h");
    const_4 = new str("");
    const_5 = new str("__main__");

    __name__ = new str("__main__");

    DESCRIPTION = __constants__::DESCRIPTION;
    if (__eq(__name__, const_5)) {
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
    __globals__::__init();
    __constants__::__init();
    __printer__::__init();
    __traverser__::__init();
    __shedskin__::__start(__deep__::__init);
}
