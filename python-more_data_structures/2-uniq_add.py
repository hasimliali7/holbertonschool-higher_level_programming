#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)"""
    # Siyahını çoxluğa (set) çeviririk ki, təkrarlar silinsin
    unique_numbers = set(my_list)
    # Çoxluğun içindəki bütün elementləri toplayırıq
    return sum(unique_numbers)
