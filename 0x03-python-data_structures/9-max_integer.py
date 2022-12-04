#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if (list_len == 0):
        return None
    else:
        max_val = my_list[0]
        for i in range(list_len):
            if (my_list[i] > max_val):
                max_val = my_list[i]
        return max_val
