from numb3rs import validate

def test_valid_ip():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("172.16.254.1") == True

def test_invalid_ip():
    assert validate("256.256.256.256") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.999") == False
    assert validate("192.168@1.1") == False
    assert validate("192.168..1") == False
    assert validate("192.168.1.-1") == False
    assert validate("192.168.1.256") == False
    assert validate("275.3.6.28") == False
