from lib.make_diary import *

def test_make_diary_equal_to_5():
    actual = make_diary("here are the first five")
    expected = "here are the first five"
    assert actual == expected

def test_make_diary_greater_than_5():
    actual = make_diary("here are the first five words of this sentence")
    expected = "here are the first five ..."
    assert actual == expected

def test_make_diary_less_than_5():
    actual = make_diary("here are the")
    expected = "here are the"
    assert actual == expected