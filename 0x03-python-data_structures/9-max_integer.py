#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = 0
    list_len = len(my_list)
    if (list_len == 0):
        return None
    else:
        for i in range(list_len):
            if (my_list[i] > max_val):
                max_val = my_list[i]
        return max_val
