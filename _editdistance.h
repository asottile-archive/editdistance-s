#ifndef ___EDITDISTANCE__H__
#define ___EDITDISTANCE__H__

#include <stdint.h>
#include <wchar.h>

#ifdef __cplusplus
extern "C" {
#endif

unsigned int edit_distance(const wchar_t *a, const size_t asize, const wchar_t *b, const size_t bsize);

#ifdef __cplusplus
}
#endif

#endif
