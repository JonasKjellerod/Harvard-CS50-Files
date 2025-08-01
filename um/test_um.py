from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3
    assert count("Um, um, UM") == 3
    assert count("um... um... um...") == 3

def test_no_um():
    assert count("hello, world") == 0
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_um_in_sentence():
    assert count("Um, I was thinking, um, maybe we could go, um, to the park.") == 3
    assert count("The word 'um' is often used as a filler.") == 1
    assert count("Um, the quick brown fox jumps over the lazy dog.") == 1
