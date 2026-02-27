#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square using Rectangle."""

    def __init__(self, size):
        """Initializes the square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
