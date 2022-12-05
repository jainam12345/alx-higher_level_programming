#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    if list_len > 0:
        i = list_len - 1
        while (i >= 0):
            print("{:d}".format(my_list[i]))
            i -= 1
