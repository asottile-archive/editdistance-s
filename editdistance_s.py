import _editdistance_s

_lib = _editdistance_s.lib


def distance(s1: str, s2: str) -> int:
    return _lib.edit_distance(s1, len(s1), s2, len(s2))
