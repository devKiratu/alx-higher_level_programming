#!/usr/bin/python3
"""Solution to the N queens puzzle problem"""


from sys import argv
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    num = int(argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if num < 4:
    print("N must be at least 4")
    exit(1)
print([])
