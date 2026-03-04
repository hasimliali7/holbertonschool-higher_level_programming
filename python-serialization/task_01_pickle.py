#!/usr/bin/env python3
"""
Bu modul xüsusi obyektlərin 'pickle' modulu vasitəsilə 
serializasiyasını və deserializasiyasını təmin edir.
"""
import pickle


class CustomObject:
    """Xüsusi məlumatları saxlayan klass."""

    def __init__(self, name, age, is_student):
        """Obyekt atributlarını inistilizasiya edir."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarını tələb olunan formatda çap edir."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Mövcud obyekti binar formata çevirib fayla yazır.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Fayldan binar məlumatı oxuyur və obyekt instansiyasını qaytarır.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.PickleError, Exception):
            return None
