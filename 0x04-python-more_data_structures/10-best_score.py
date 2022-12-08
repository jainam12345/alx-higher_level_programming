#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        max_key = ''
        for i in a_dictionary.keys():
            if a_dictionary[i] == max_value:
                max_key = i
                return max_key
    else:
        return None
