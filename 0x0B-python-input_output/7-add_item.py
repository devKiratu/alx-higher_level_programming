#!/usr/bin/python3
"""This script adds all arguments to a Python list,
and saves them to a file 'add_item.json'
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except Exception:
    items = []
    save_to_json_file(items, filename)
for i in range(1, len(argv)):
    items.append(argv[i])
save_to_json_file(items, filename)
