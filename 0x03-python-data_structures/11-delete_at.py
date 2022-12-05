#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    if my_list:
        if idx < 0 or idx >= list_len:
            return my_list
        else:
            return [my_list[i] for i in range(list_len) if i != idx]
