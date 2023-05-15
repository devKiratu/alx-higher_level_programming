#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
        a = b = 0
        if len(tuple_a) >= 2 and len(tuple_b) >= 2:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + tuple_b[1]
        else:
            list_a = list(tuple_a)
            list_b = list(tuple_b)
            while len(list_a) < 2:
                list_a.append(0)
            while len(list_b) < 2:
                list_b.append(0)
            a = list_a[0] + list_b[0]
            b = list_a[1] + list_b[1]
        return a, b
