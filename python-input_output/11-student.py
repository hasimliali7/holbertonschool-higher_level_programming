#!/usr/bin/python3
"""
Bu modul 'Student' klassını və onun atributlarını yeniləmə
 metodunu ehtiva edir.
"""


class Student:
    """Tələbə məlumatlarını təyin edən klass."""

    def __init__(self, first_name, last_name, age):
        """Student instansiyasını inistilizasiya edir."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Student instansiyasının lüğət təsvirini qaytarır.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Lüğətdəki açar/dəyər cütlükləri ilə bütün atributları əvəzləyir.

        Args:
            json (dict): Atribut adları və yeni dəyərlər lüğəti.
        """
        for key, value in json.items():
            setattr(self, key, value)
