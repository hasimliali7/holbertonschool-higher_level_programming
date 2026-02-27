#!/usr/bin/python3
"""
This module defines a VerboseList class that extends the built-in list class
to provide notifications on modifications.
"""


class VerboseList(list):
    """A list subclass that prints messages when items are added or removed."""

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification with the count."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item and prints a notification before removal."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a notification before removal."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
