#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It checks if the inputs are integers or floats, casts them to integers,
and returns their sum.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, defaults to 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers, floats, or are NaN/Inf.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlanışı (Overflow qarşısını almaq üçün)
    if a != a or abs(a) > 1.7976931348623157e+308:
        raise TypeError("a must be an integer")
    if b != b or abs(b) > 1.7976931348623157e+308:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
