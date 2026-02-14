#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Tuple-ları standart formaya (minimum 2 element) gətiririk
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # İlk iki elementi toplayıb yeni tuple qaytarırıq
    return (a[0] + b[0], a[1] + b[1])
