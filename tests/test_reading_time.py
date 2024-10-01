import pytest
from lib.reading_time import *

def test_reading_time_correct_input():
    actual = reading_time("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus scelerisque nisi nec ligula cursus, nec luctus libero ultricies. Nulla ac orci nisi. Duis tincidunt eros vel metus congue, vel vehicula mauris lobortis. Praesent vel odio id orci posuere sollicitudin. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean condimentum lorem vitae bibendum efficitur. Cras venenatis lectus ut lacus malesuada, at ultricies augue gravida.
Suspendisse potenti. Vestibulum nec felis sit amet nisl tincidunt feugiat a vitae libero. Ut porttitor suscipit turpis, sed vulputate ipsum pulvinar sit amet. Curabitur in gravida libero, in congue sapien. Maecenas scelerisque urna orci, ut aliquet turpis dignissim ac. Mauris tempus, tortor at accumsan ullamcorper, turpis lorem finibus dolor, vel aliquam orci nulla ac nisl. Nunc sit amet magna gravida, dapibus ante sit amet, bibendum augue.
Integer suscipit justo quis lorem laoreet, nec ultricies orci scelerisque. Donec luctus vehicula metus, sit amet maximus ligula facilisis et. Fusce blandit mi vel enim vulputate, ac dapibus mi fermentum. Pellentesque tincidunt enim non nibh luctus, nec gravida nunc fermentum. Nam volutpat euismod sapien, non rutrum ante malesuada id.""", 200) 
    expected = 60

    assert actual == expected


def test_reading_time_coreect_input_2():
    actual = reading_time("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus scelerisque nisi nec ligula cursus, nec luctus libero ultricies. Nulla ac orci nisi. Duis tincidunt eros vel metus congue, vel vehicula mauris lobortis. Praesent vel odio id orci posuere sollicitudin. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean condimentum lorem vitae bibendum efficitur. Cras venenatis lectus ut lacus malesuada, at ultricies augue gravida.
Suspendisse potenti. Vestibulum nec felis sit amet nisl tincidunt feugiat a vitae libero. Ut porttitor suscipit turpis, sed vulputate ipsum pulvinar sit amet. Curabitur in gravida libero, in congue sapien. Maecenas scelerisque urna orci, ut aliquet turpis dignissim ac. Mauris tempus, tortor at accumsan ullamcorper, turpis lorem finibus dolor, vel aliquam orci nulla ac nisl. Nunc sit amet magna gravida, dapibus ante sit amet, bibendum augue.
Integer suscipit justo quis lorem laoreet, nec ultricies orci scelerisque. Donec luctus vehicula metus, sit amet maximus ligula facilisis et. Fusce blandit mi vel enim vulputate, ac dapibus mi fermentum. Pellentesque tincidunt enim non nibh luctus, nec gravida nunc fermentum. Nam volutpat euismod sapien, non rutrum ante malesuada id.""", 99.5) 
    expected = 120

    assert actual == expected

def test_reading_time_string_string():
    with pytest.raises(Exception) as e:
        reading_time("word1", "word2")
    error_message = str(e.value)
    assert error_message == "You must input a string followed by an integer"

def test_reading_time_num_num():
    with pytest.raises(Exception) as e:
        reading_time(200, 20)
    error_message = str(e.value)
    assert error_message == "You must input a string followed by an integer"

def test_reading_time_num_none():
    with pytest.raises(Exception) as e:
        reading_time(200, None)
    error_message = str(e.value)
    assert error_message == "You must input a string followed by an integer"

def test_reading_time_none_num():
    with pytest.raises(Exception) as e:
        reading_time(None, 200)
    error_message = str(e.value)
    assert error_message == "You must input a string followed by an integer"