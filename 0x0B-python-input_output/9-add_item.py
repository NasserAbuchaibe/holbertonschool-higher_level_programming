#!/usr/bin/python3
"""[summary]    """
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    MyJsonList = load_from_json_file("add_item.json")
except:
    MyJsonList = []

for x in argv[1:]:
    MyJsonList.append(x)

save_to_json_file(MyJsonList, "add_item.json")
