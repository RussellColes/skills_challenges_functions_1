def reading_time(text, wpm):
    if type(wpm) == float or type(wpm) == int:
        wpm_integer = int(round(wpm))
        if type(text) == str:
            lst_words = text.split()
            return int(round(len(lst_words) / int(round(wpm)))) * 60
        else:
            raise Exception("You must input a string followed by an integer")            

    # wpm_int = int(round(wpm))
    # return wpm_int
    else:
        raise Exception("You must input a string followed by an integer")
    # else:
    #     lst_words = text.split()
    #     return int(round(len(lst_words) / int(round(wpm)))) * 60