#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list
    new_len = len(new_list)
    if (idx < 0 or idx > new_len):
        return new_list
    else:
        new_list[idx] = element
        return new_list
