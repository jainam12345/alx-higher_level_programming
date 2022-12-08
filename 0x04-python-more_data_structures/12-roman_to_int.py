#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    else:
        roman = {'I': 1,
                 "V": 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        num_eq = []
        total = 0
        for i in roman_string:
            num_eq.append(roman[i])
        list_len = len(num_eq)
        for i in range(list_len):
            if i != list_len - 1 and num_eq[i] < num_eq[i+1]:
                total -= num_eq[i]
            elif i != list_len - 1 and num_eq[i] >= num_eq[i+1]:
                total += num_eq[i]
            else:
                total += num_eq[i]
        return total
