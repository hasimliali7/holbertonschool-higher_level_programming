#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Orijinal siyahının surətini yaradırıq
    copy_list = my_list[:]
    
    # İndeks yoxlaması
    if idx < 0 or idx >= len(my_list):
        return copy_list
    
    # Surət üzərində dəyişiklik edirik
    copy_list[idx] = element
    return copy_list
