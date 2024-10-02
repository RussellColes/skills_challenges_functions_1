from lib.grammar_improver import *
import pytest

def test_grammar_improver_correct():
    actual = grammar_improver("Hello World!")
    expected = True
    assert actual == expected

def test_grammar_improver_correct_2():
    actual = grammar_improver("Goodbye, my darlings!")
    expected = True
    assert actual == expected

def test_grammar_improver_no_punctuation():
    actual = grammar_improver("Hello world")
    expected = False
    assert actual == expected

def test_grammar_improver_lowercase_initial_letter():
    actual = grammar_improver("goodbye, my darlings!")
    expected = False
    assert actual == expected

def test_grammar_improver_lowercase_initial_letter_no_punctuation():
    actual = grammar_improver("goodbye, my darlings")
    expected = False
    assert actual == expected

def test_grammar_improver_all_uppercase():
    actual = grammar_improver("HELLO WORLD")
    expected = False
    assert actual == expected

def test_grammar_improver_empty_string():
    with pytest.raises(Exception) as e:
        grammar_improver("")
    error_message = str(e.value)
    assert error_message == "You must input a string"


def test_grammar_improver_none():
    with pytest.raises(Exception) as e:
        grammar_improver(None)
    error_message = str(e.value)
    assert error_message == "You must input a string"