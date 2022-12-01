#!/usr/bin/python3
import sys
arg_list = sys.argv
arg_len = len(arg_list)
if arg_len == 1:
    print("0 arguments.")
elif arg_len == 2:
    print("1 argument:")
    print("{}".format(arg_list[1]))
else:
    print("{} arguments:".format(arg_len - 1))
    for i in range(1, arg_len):
        print("{}: {}".format(i, arg_list[i]))
