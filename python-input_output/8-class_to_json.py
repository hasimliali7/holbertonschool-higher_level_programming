#!/usr/bin/python3
"""
Bu modul bir Class obyektini JSON serializasiyası üçün
 lüğət (dictionary) strukturuna çevirən funksiyanı ehtiva edir.
"""


def class_to_json(obj):
    """
    Obyektin lüğət təsvirini qaytarır.

    Args:
        obj: Bir Class-ın instansiyası (obyekti).

    Returns:
        dict: Obyektin atributlarını saxlayan lüğət.
    """
    return obj.__dict__
