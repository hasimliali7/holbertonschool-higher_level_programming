#!/usr/bin/env python3
"""
Bu modul əsas JSON serializasiya və deserializasiya
 funksiyalarını ehtiva edir.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini JSON faylına çevirir və yadda saxlayır.

    Args:
        data (dict): Serializasiya olunacaq lüğət.
        filename (str): Çıxış faylının adı.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    JSON faylından məlumatı oxuyur və Python lüğətinə çevirir.

    Args:
        filename (str): Giriş JSON faylının adı.

    Returns:
        dict: Deserializasiya olunmuş lüğət.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
