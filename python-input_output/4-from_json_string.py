#!/usr/bin/python3
"""
Bu modul JSON string-i Python obyektinə çevirən funksiyanı ehtiva edir.
"""
import json


def from_json_string(my_str):
    """
    JSON string ilə təmsil olunan Python obyektini qaytarır.
    """
    return json.loads(my_str)
