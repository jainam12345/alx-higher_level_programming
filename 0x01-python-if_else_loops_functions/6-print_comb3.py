#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i < j):
            print("{}{}".format(i,j), end='')
            if (i + 1 != 9):
                print(", ", end='')
            else:
                print('\n')
