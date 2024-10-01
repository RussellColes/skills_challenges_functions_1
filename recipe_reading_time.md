# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature


_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(mixed_words):
    """Calculates an estimate of reading time for a text

    Parameters: ()
        a string containing words (the text): (e.g. "hello WORLD")
        an integer representing the number of words per minute that the user can read

    Returns: (state the return value and its type)
        an integer representing the number of seconds it will take to read a text

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
Given a string and an integer
It returns an integer
"""
reading_time("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus scelerisque nisi nec ligula cursus, nec luctus libero ultricies. Nulla ac orci nisi. Duis tincidunt eros vel metus congue, vel vehicula mauris lobortis. Praesent vel odio id orci posuere sollicitudin. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean condimentum lorem vitae bibendum efficitur. Cras venenatis lectus ut lacus malesuada, at ultricies augue gravida.

Suspendisse potenti. Vestibulum nec felis sit amet nisl tincidunt feugiat a vitae libero. Ut porttitor suscipit turpis, sed vulputate ipsum pulvinar sit amet. Curabitur in gravida libero, in congue sapien. Maecenas scelerisque urna orci, ut aliquet turpis dignissim ac. Mauris tempus, tortor at accumsan ullamcorper, turpis lorem finibus dolor, vel aliquam orci nulla ac nisl. Nunc sit amet magna gravida, dapibus ante sit amet, bibendum augue.

Integer suscipit justo quis lorem laoreet, nec ultricies orci scelerisque. Donec luctus vehicula metus, sit amet maximus ligula facilisis et. Fusce blandit mi vel enim vulputate, ac dapibus mi fermentum. Pellentesque tincidunt enim non nibh luctus, nec gravida nunc fermentum. Nam volutpat euismod sapien, non rutrum ante malesuada id.""", 200) 
=> [60]

"""
Given a string and a float
It returns an integer
"""
reading_time("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus scelerisque nisi nec ligula cursus, nec luctus libero ultricies. Nulla ac orci nisi. Duis tincidunt eros vel metus congue, vel vehicula mauris lobortis. Praesent vel odio id orci posuere sollicitudin. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean condimentum lorem vitae bibendum efficitur. Cras venenatis lectus ut lacus malesuada, at ultricies augue gravida.

Suspendisse potenti. Vestibulum nec felis sit amet nisl tincidunt feugiat a vitae libero. Ut porttitor suscipit turpis, sed vulputate ipsum pulvinar sit amet. Curabitur in gravida libero, in congue sapien. Maecenas scelerisque urna orci, ut aliquet turpis dignissim ac. Mauris tempus, tortor at accumsan ullamcorper, turpis lorem finibus dolor, vel aliquam orci nulla ac nisl. Nunc sit amet magna gravida, dapibus ante sit amet, bibendum augue.

Integer suscipit justo quis lorem laoreet, nec ultricies orci scelerisque. Donec luctus vehicula metus, sit amet maximus ligula facilisis et. Fusce blandit mi vel enim vulputate, ac dapibus mi fermentum. Pellentesque tincidunt enim non nibh luctus, nec gravida nunc fermentum. Nam volutpat euismod sapien, non rutrum ante malesuada id.""", 99.5) 
=> 120

"""
Given a string and a string
It returns an error message
"""
reading_time("hello world", "hello world") => Error Message: "You must input a string followed by an integer"

"""
Given an integer and a string
It returns an error message
"""
reading_time(20, "hello world") => Error Message: "You must input a string followed by an integer"

"""
Given an integer and an integer
It returns an error message
"""
reading_time(300, 40) => Error Message: "You must input a string followed by an integer"

"""
Given None in either input
It returns an error message
"""
reading_time("hello WoRLD", None) => Error Message: "You must input a string followed by an integer"

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
reading_time("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
reading_time("") => []

"""
Given a None value
It throws an error
"""
reading_time(None) throws an error
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
