#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list == None:
        return None
    else:
        max_int = my_list[0]
        for n in my_list:
            if n > max_int:
                max_int = n
        return max_int
