#!/usr/bin/python3
"""
Modulw that loads, saves
"""
import os
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json'):
    obj = load('add_item.json')
else:
    obj = []
for i in range(1, len(sys.argv)):
    obj.append(sys.argv[i])

save(obj, 'add_item.json')
