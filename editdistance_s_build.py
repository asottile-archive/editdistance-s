from cffi import FFI

CDEF = '''\
unsigned int edit_distance(
    const wchar_t *, const size_t,
    const wchar_t *, const size_t
);
'''
SRC = '''\
#include "_editdistance.h"
'''

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(
    '_editdistance_s', SRC,
    sources=['_editdistance.cpp'],
    include_dirs=['.'],
)
