#ifndef __TRAVERSER_HPP
#define __TRAVERSER_HPP

using namespace __shedskin__;
namespace __traverser__ {

extern str *const_0;


typedef void *(*lambda0)(str *, str *, list<str *> *);

extern str *__name__;


void __init();
void *traversal_callback(str *_, str *dirname, list<str *> *files);

} // module namespace
#endif
