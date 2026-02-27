#!/usr/bin/python3
"""
This module defines a CountedIterator class that keeps track
of the number of items iterated over.
"""


class CountedIterator:
    """An iterator wrapper that counts the number of items fetched."""

    def __init__(self, iterable):
        """Initializes the iterator and the counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.count

    def __next__(self):
        """Increments the counter and returns the next item."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
