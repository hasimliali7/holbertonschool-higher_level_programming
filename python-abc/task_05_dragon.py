#!/usr/bin/python3
"""
This module demonstrates the use of Mixins to compose class behaviors.
"""


class SwimMixin:
    """Mixin to add swimming functionality."""
    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying functionality."""
    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits functionalities from multiple mixins."""
    def roar(self):
        """Prints a roaring message specific to the dragon."""
        print("The dragon roars!")
