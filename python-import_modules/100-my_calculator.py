#!usr/bin/python3

if __name__ == '__main__':
    import  sys
    from calculator_1 import  add, sub, mul, div

    operators = ['+', '-', '*', '/']
    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    list_args = sys.argv[1:]
    a = int(list_args[0])
    b = int(list_args[-1])
    for arg in list_args:
        if list_args[1] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if list_args[1] == '':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if list_args[1] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if list_args[1] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
