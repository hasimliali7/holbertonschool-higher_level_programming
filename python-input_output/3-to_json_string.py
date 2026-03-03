#!/usr/bin/python3
"""
Bu modul Python obyektini JSON string-ə çevirən funksiyanı ehtiva edir.
"""
import json


def to_json_string(my_obj):
    """
    Python obyektinin JSON təmsilini (string) qaytarır.
    """
    return json.dumps(my_obj)
