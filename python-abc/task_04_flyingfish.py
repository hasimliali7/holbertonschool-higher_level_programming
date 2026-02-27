#!/usr/bin/python3
"""
This module explores multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Parent class representing a fish."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message."""
        print("The fish lives in water")


class Bird:
    """Parent class representing a bird."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Subclass representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Overrides fly method from Bird."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides swim method from Fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method from both parents."""
        print("The flying fish lives both in water and the sky!")
