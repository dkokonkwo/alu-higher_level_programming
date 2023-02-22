#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    list_args = sys.argv[1:]
    if len(list_args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(list_args[0])
    b = int(list_args[2])
    if list_args[1] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif list_args[1] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif list_args[1] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif list_args[1] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
