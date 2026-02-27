#!/usr/bin/python3
"""
This module defines a BaseGeometry class with area and integer_validator.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
        - name is assumed to be a string.
        - value must be an integer, otherwise raise TypeError.
        - value must be > 0, otherwise raise ValueError.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
