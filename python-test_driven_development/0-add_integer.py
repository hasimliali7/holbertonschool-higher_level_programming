#!/usr/bin/python3
"""
Bu modul iki tam ədədi toplamaq üçün funksiya təqdim edir.
Burada add_integer funksiyası yerləşir.
"""


def add_integer(a, b=98):
    """İki tam və ya onluq ədədi toplayır.

    Arqumentlər:
        a: birinci ədəd (int və ya float)
        b: ikinci ədəd (int və ya float, default 98)

    Returns:
        İki ədədin cəmi (int)

    Raises:
        TypeError: Əgər a və ya b int/float deyilsə.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
