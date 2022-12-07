#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_items = list(a_dictionary.items())
    dict_items.sort()
    sorted_dict = dict(dict_items)
    for i in sorted_dict:
        print("{}: {}".format(i, sorted_dict[i]))
