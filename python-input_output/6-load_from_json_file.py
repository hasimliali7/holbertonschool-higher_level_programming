#!/usr/bin/python3
"""
Bu modul JSON faylından Python obyektini yükləyən funksiyanı ehtiva edir.
"""
import json


def load_from_json_file(filename):
    """
    JSON faylından (Object) Python data strukturunu yaradır.

    Args:
        filename (str): Oxunacaq faylın adı.

    Returns:
        any: JSON-dan çevrilmiş Python obyekti.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
