def no_c(my_string):
    new_str = list(my_string)
    for ch in new_str:
        if ch == 'c' or ch == 'C':
            new_str.remove(ch)
    return "".join(new_str)
