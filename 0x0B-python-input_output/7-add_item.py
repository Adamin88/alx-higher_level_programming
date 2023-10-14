#!/usr/bin/python3
"""
Adding all arguments to a Python list and saving them to a file.
"""

import os.path
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

my_file = 'add_item.json'
if (os.path.isfile(my_file)):
    my_obj = load_from_json_file(my_file)
else:
    my_obj = []
my_obj.extend(sys.argv[1:])
save_to_json_file(my_obj, my_file)
