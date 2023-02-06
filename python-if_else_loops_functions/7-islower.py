#!/usr/bin/python3
def islower(c: str) -> bool:
    letters = []
    for i in range(ord('a'), ord('z') + 1):
        letters.append(chr(i))
    if c in letters:
        return True
    else:
        return False
