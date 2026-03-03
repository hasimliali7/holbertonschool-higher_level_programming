#!/usr/bin/python3
"""
Bu modul JSON string-i Python obyektinə çevirən funksiyanı ehtiva edir.
"""
import json


def from_json_string(my_str):
    """
    JSON string ilə təmsil olunan Python obyektini qaytarır.

    Args:
        my_str (str): JSON formatında olan mətn.

    Returns:
        any: Python data strukturu (list, dict, str, int və s.).
    """
    return json.loads(my_str)
