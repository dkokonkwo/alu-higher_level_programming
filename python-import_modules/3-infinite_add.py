#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    total = 0
    list_int = sys.argv[1:]
    for arg in list_int:
        total += int(arg)
    print(total)
