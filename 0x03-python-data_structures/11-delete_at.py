#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if my_list:
        for i in my_list:
            if i != idx:
                new_list.append(i)
    return new_list
