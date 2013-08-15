#ifndef __PRINTER_HPP
#define __PRINTER_HPP

using namespace __shedskin__;
namespace __printer__ {

extern str *const_0, *const_1, *const_2, *const_3, *const_4, *const_5, *const_6;



extern str *__name__;


void __init();
void *print_header();
void *print_update(__ss_int breadth, __ss_int length, __ss_int depth);
void *print_footer();

} // module namespace
#endif
