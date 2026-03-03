#!/usr/bin/python3
"""
Bu modul 'Student' klassını ehtiva edir.
"""


class Student:
    """Tələbə məlumatlarını təyin edən klass."""

    def __init__(self, first_name, last_name, age):
        """
        Student instansiyasını inistilizasiya edir.

        Args:
            first_name (str): Tələbənin adı.
            last_name (str): Tələbənin soyadı.
            age (int): Tələbənin yaşı.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Student instansiyasının lüğət təsvirini qaytarır.
        """
        return self.__dict__
