import editdistance_s


def test_same():
    assert editdistance_s.distance('hello', 'hello') == 0


def test_unicode():
    assert editdistance_s.distance('hell🙃', 'hell☃') == 1
