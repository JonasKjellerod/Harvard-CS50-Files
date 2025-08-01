from bank import value

def test_value_lower():
    assert value('hello') == 0
    assert value('hi') == 20
    assert value('greetings') == 100

def test_value_upper():
    assert value('HELLO') == 0
    assert value('HI') == 20
    assert value('GREETINGS') == 100

def test_value_char():
    assert value('.-?+!') == 100
    assert value('1234') == 100
