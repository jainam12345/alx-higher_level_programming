#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    else:
        return [True if my_list[i] % 2 == 0 else False for i in my_list]
