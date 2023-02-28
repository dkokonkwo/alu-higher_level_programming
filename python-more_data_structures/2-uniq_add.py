#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
    add = 0
    for x in uniq_list:
        add += x
    return add
