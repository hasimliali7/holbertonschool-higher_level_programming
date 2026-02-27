#!/usr/bin/python3
"""
This module defines a Shape abstract class and its subclasses
Circle and Rectangle, demonstrating duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculates area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates perimeter."""
        pass


class Circle(Shape):
    """Circle class with radius."""

    def __init__(self, radius):
        """Initializes circle with radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class with width and height."""

    def __init__(self, width, height):
        """Initializes rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of a shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
