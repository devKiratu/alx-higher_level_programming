#!/usr/bin/python3
from sys import argv
import calculator_1 as c


def calculate():
    print("argv: {}".format(argv))
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in "+-/*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op == '+':
            print("{} + {} = {}".format(a, b, c.add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, c.sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, c.mul(a, b)))
        elif op == '/':
            print("{} / {} = {}".format(a, b, c.div(a, b)))


if __name__ == "__main__":
    calculate()
