def grammar_improver(sentence):
    if type(sentence) == str and len(sentence) != 0:
        punctuation = [".", "?", "!"]
        if sentence[0].isupper() == True and sentence[-1] in punctuation:
            return True
        else:
            return False
    else:
        raise Exception("You must input a string")