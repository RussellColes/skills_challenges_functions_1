def make_diary(string):
    first_five = string.split()
    if len(first_five) <= 5:
        first_five_string = " ".join(first_five[0:5])
    else:    
        first_five_words = " ".join(first_five[0:5])
        first_five_string = f"{first_five_words} ..."
    return first_five_string