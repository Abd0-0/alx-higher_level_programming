#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_str = [ch for ch in my_string if ch not in "Cc"]
        return "".join(new_str)
