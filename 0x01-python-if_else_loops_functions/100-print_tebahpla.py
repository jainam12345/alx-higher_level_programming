#!/usr/bin/python3
i = ord('z')
while(i > ord('a') - 1):
    print("{}".format(chr(i - 32) if i % 2 == 1 else chr(i)), end='')
    i = i - 1
