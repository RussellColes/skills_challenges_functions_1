# Grammar Improver Function Design Recipe


## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def grammar_improver(string):
    """Looks for features within a string

    Parameters: (list all parameters and their types)
        string containing words and punctuation

    Returns: (state the return value and its type)
        True or False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence beginning with a capital letter and ending with one of .?!
It returns True
"""
grammar_improver("Hello World!") => True

"""
Given a different sentence beginning with a capital letter and ending with one of .?!
It returns True
"""
grammar_improver("Goodbye, my darlings!") => True

"""
Given no punctuation
It returns False
"""
grammar_improver("Hello world") => False

"""
Given lowercase initial letter
It returns False
"""
grammar_improver("hello world!") => False

"""
Given a no punctuation and lower case inital letter
It returns False
"""
grammar_improver("hello world") => False

"""
Given all uppercase
It returns False
"""
grammar_improver("HELLO WORLD!") => False

"""
Given an empty string
It returns an error message - "Please provide a string"
"""
grammar_improver("") => "Please provide a string"

"""
Given a non-string
It returns an error message - "Please provide a string"
"""
grammar_improver(10) => "Please provide a string"

"""
Given a None value
It returns an error message - "Please provide a string"
"""
grammar_improver(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
