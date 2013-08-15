#include "builtin.hpp"
#include "stat.hpp"
#include "os/path.hpp"
#include "os/__init__.hpp"
#include "sys.hpp"
#include "printer.hpp"
#include "globals.hpp"
#include "traverser.hpp"

namespace __traverser__ {

str *const_0;

using __printer__::print_update;

str *__name__;



void *traversal_callback(str *_, str *dirname, list<str *> *files) {
    /**
    Function called during `os.path.walk` directory traversal.
    
    `os.path.walk` is deprecated, but `os.walk` is not yet implemented in
    ShedSkin.
    
    @param dirname: The name of the directory currently being examined.
    @type  dirname: str
    @param files: The list of file names residing within the current directory.
    @type  files: list or iterable
    */
    list<str *>::for_in_loop __12;
    list<str *> *__9;
    str *filename, *fullname;
    __ss_int __11;
    __iter<str *> *__10;

    fullname = const_0;
    __globals__::breadth = (__globals__::breadth+1);
    if (___bool(files)) {

        FOR_IN(filename,files,9,11,12)
            fullname = ((dirname)->__add__(__os__::__path__::sep))->__add__(filename);
            __globals__::now_length = ___max(2, 0, __globals__::max_length, len(fullname));
            if ((__globals__::max_length<__globals__::now_length)) {
                __globals__::max_length = __globals__::now_length;
                __globals__::longest_file = fullname;
            }
        END_FOR

    }
    else {
        __globals__::now_length = ___max(2, 0, __globals__::max_length, len(dirname));
        if ((__globals__::max_length<__globals__::now_length)) {
            __globals__::max_length = __globals__::now_length;
            __globals__::longest_file = dirname;
        }
    }
    __globals__::now_depth = len(dirname->split(__os__::sep));
    __globals__::now_depth = ___max(2, 0, __globals__::max_depth, (__globals__::now_depth-1));
    if ((__globals__::max_length<__globals__::now_length)) {
        __globals__::max_length = __globals__::now_length;
        __globals__::longest_file = dirname;
    }
    if ((__globals__::max_depth<__globals__::now_depth)) {
        __globals__::max_depth = __globals__::now_depth;
        __globals__::deepest_path = dirname;
    }
    if (__globals__::runas_program) {
        print_update(__globals__::breadth, __globals__::max_length, __globals__::max_depth);
    }
    return NULL;
}

void __init() {
    const_0 = new str("");

    __name__ = new str("traverser");

}

} // module namespace

