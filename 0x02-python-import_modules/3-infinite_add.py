#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv)
    sum_t = 0
    if arg_len == 1:
        print(int(0))
    elif arg_len == 2:
        print(int(argv[1]))
    else:
        for i in range(1, arg_len):
            sum_t += int(argv[i])
        print(sum_t)
