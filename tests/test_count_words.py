from lib.count_words import *

def test_count_words():
    actual = count_words("here is a sentence to count")
    expected = 6

    assert actual == expected

def test_count_words_2():
    actual = count_words("here is a sentence to count with lots and lots of big words")
    expected = 13

    assert actual == expected