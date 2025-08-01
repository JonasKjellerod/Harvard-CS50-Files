from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert('1/1') == 100
    assert convert('1/2') == 50
    assert convert('1/3') == 33
    assert convert('0/2') == 0


def test_char():
    with pytest.raises(ValueError):
        convert('J/1')
def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

