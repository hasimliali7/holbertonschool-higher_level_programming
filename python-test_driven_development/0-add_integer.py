#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The module ensures inputs are valid integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number, must be int or float.
        b: The second number, must be int or float.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float,
        or if they are NaN/Infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və ya Infinity (Sonsuzluq) yoxlanışı
    # NaN heç vaxt özünə bərabər deyil (a != a)
    # Infinity-nin mütləq dəyəri çox böyükdür
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
