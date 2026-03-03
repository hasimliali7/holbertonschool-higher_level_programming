#!/usr/bin/python3
"""
Bu skript bütün arqumentləri Python siyahısına əlavə edir
 və onları JSON faylına saxlayır.
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Əgər fayl varsa, mövcud siyahını yüklə, yoxdursa boş siyahı yarat
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Terminaldan gələn arqumentləri siyahıya əlavə et (skriptin adından başqa)
items.extend(sys.argv[1:])

# Yenilənmiş siyahını fayla saxla
save_to_json_file(items, filename)
