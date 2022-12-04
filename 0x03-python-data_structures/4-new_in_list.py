#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    list_len = len(my_list)
    if (idx < 0 or idx >= list_len):
        return my_list
    else:
        for i in range(list_len):
            new_list.append(my_list[i])
        new_list[idx] = element
        return new_list
