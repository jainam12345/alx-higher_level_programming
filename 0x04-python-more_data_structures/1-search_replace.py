#!/usr/bin/python3
def search_replace(my_list, search, replace):
    fn = lambda x: replace if(x==search) else x
    new_list = list(map(fn, my_list))
    return new_list
