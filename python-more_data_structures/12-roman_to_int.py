#!/usr/bin/python3:
def roman_to_int(roman_string):
    list_of_num = []
    roman_dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if isinstance(roman_string, str):
        for letter in roman_string:
            if letter in roman_dictionary:
                list_of_num.append(roman_dictionary[letter])

        them_changes = []
        for x in list_of_num:
            if them_changes and x > them_changes[-1]:
                them_changes[-1] = -them_changes[-1]
                them_changes.append(x)
            else:
                them_changes.append(x)
        return sum(them_changes)
    elif roman_string is None:
        return 0
    else:
        return 0
