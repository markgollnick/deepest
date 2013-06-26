#ifndef __DEEP_HPP
#define __DEEP_HPP

using namespace __shedskin__;
namespace __deep__ {

extern str *const_0, *const_1, *const_10, *const_11, *const_12, *const_2, *const_3, *const_4, *const_5, *const_6, *const_7, *const_8, *const_9;


typedef void *(*lambda0)(str *, str *, list<str *> *);

extern __ss_int breadth, max_depth, max_length, now_depth, now_length;
extern str *VERSION, *__name__, *deepest_path, *longest_file;


void *_get_depth(str *_, str *dirname, list<str *> *files);
void *print_header();
void *print_update(__ss_int breadth, __ss_int length, __ss_int depth);
void *print_footer();
void *__ss_main();

} // module namespace
#endif
