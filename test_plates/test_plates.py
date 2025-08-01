from plates import is_valid


def test_c1():
    assert is_valid('1J') == False
    assert is_valid('11') == False
    assert is_valid('J1') == False
    assert is_valid('JJ') == True


def test_c2():
    assert is_valid('J') == False
    assert is_valid('JJ') == True
    assert is_valid('JJJJJJ') == True
    assert is_valid('JJJJJJJ') == False


def test_c3():
    assert is_valid('JJ') == True
    assert is_valid('JJ22') == True
    assert is_valid('JJ22JJ') == False

def test_c4():
    assert is_valid('JJ.') == False
    assert is_valid('JJ,') == False
    assert is_valid('JJ ') == False


def test_c5():
    assert is_valid('') == False


