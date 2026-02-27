#!/usr/bin/python3
"""
This module contains the MyList class which inherits from list.
"""


class MyList(list):
    """A class that inherits from list and provides additional methods."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
