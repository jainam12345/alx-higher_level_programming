#!/usr/bin/python3
0;276;0cimport random
number = random.randint(-10000, 10000)
l_digit = None
if number >= 0:
    l_digit = number % 10
else:
    l_digit = -1 * (abs(number) % 10)
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
elif l_digit < 6 and l_digit != 0:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
