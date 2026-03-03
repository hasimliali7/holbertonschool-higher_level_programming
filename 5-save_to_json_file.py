#!/usr/bin/python3
"""
Bu modul Python obyektini JSON formatında fayla yazan funksiyanı ehtiva edir.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Obyektin JSON təmsilini mətn faylına yazır.

    Args:
        my_obj: Fayla yazılacaq Python obyekti.
        filename (str): Faylın adı.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
