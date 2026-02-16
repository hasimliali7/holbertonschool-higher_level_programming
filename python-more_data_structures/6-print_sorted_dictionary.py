#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    # Açarları əlifba sırası ilə sıralayırıq
    sorted_keys = sorted(a_dictionary.keys())
    
    # Sıralanmış açarlar üzrə dövr qurub çap edirik
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
