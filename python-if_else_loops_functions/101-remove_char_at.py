#!/usr/bin/python3
def remove_char_at(str, n) -> str:
    if n > len(str) or n < 0:
        return str
    else:
        return (str.replace(str[n], ''))
