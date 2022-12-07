#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def f(x):
        if x == search:
            return replace
        else:
            return x
    new_list = list(map(f, my_list))
    return new_list
