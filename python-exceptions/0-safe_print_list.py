#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index, value in enumerate(my_list):
            if index < x:
                print(value, end='')
        print()
        if x <= (index + 1):
            return x
        else:
            return index + 1
    except:
        print("There was an error somewhere!")
