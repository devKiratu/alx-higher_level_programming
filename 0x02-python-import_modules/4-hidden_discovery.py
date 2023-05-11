#!/usr/bin/python3
import hidden_4 as h


def print_names():
    for f in dir(h):
        if not f.startswith("__"):
            print(f)


if __name__ == "__main__":
    print_names()
