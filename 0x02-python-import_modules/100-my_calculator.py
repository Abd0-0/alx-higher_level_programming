#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    av = sys.argv
    ac = len(av) - 1
    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(av[1])
    b = int(av[3])
    op = av[2]
    if op == '+':
        print(f"{a} + {b} = {add(a,b)}")
    elif op == "-":
        print(f"{a} - {b} = {sub(a,b)}")
    elif op == '*':
        print(f"{a} * {b} = {mul(a,b)}")
    elif op == '/':
        print(f"{a} / {b} = {div(a,b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
