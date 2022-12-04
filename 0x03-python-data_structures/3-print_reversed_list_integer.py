#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    i = list_len - 1
    while (i >= 0 and my_list != None):
        print("{:d}".format(my_list[i]))
        i -= 1
