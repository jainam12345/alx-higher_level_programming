#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    list_len = len(my_list)
    if my_list:
        if idx < 0 or idx >= list_len:
            return my_list
        else:
            for i in range(len(my_list)):
                if i != idx:
                    new_list.append(my_list[i])
            return new_list
