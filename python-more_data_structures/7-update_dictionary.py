#!/usr/bin/python3
def update_dictionary(a_dictionary, key: str, value) -> dict:
    if key in a_dictionary:
        a_dictionary.update({str(key): value})
    else:
        a_dictionary[key] = value
    return a_dictionary
