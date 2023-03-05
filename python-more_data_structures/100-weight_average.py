#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denominator = 0
        for x in my_list:
            numerator += x[0] * x[1]
            denominator += x[1]
        average = numerator / denominator
        return average
    else:
        return 0
